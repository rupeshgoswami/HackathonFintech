import praw
import cryptocompare
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import defaultdict
import datetime
import matplotlib.pyplot as plt
import numpy as np

#Reddit API credentials
client_id = 'oOGNbmuTE37cTOqv9fEXvA'
client_secret = 'Zd0Pw5JD5al-HgRhj1jHjdL6yp0Jmg'
user_agent = 'script:crypto_sentiment_analysis:v1.0 (by /u/yourusername)'

#Initialize Reddit API client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

#Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def fetch_posts(subreddits, period='month', limit=20):
    """Fetch posts from specified subreddits over a specified period."""
    all_posts = []
    for subreddit in subreddits:
        print(f"Fetching posts from /r/{subreddit}...")
        posts = reddit.subreddit(subreddit).top(time_filter=period, limit=limit)
        for post in posts:
            all_posts.append((post.title + " " + post.selftext, post.created_utc))
        print(f"Completed fetching posts from /r/{subreddit}.")
    return all_posts

def filter_posts_by_date(posts, days_ago):
    """Filter posts to a specific day, `days_ago` days from today."""
    target_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    start_of_day = datetime.datetime(target_date.year, target_date.month, target_date.day)
    end_of_day = start_of_day + datetime.timedelta(days=1)
    return [post for post in posts if start_of_day.timestamp() <= post[1] < end_of_day.timestamp()]

def analyze_sentiments(posts, keyword):
    """Analyze sentiments of fetched posts."""
    sentiment_sum = 0
    count = 0
    for post, _ in posts:
        if keyword in post.lower():
            sentiment = sia.polarity_scores(post)
            sentiment_sum += sentiment['compound']
            count += 1
    return sentiment_sum / count if count else 0  #Return average sentiment

def fetch_crypto_prices(dates, crypto):
    """Fetch cryptocurrency prices for given dates."""
    prices = {}
    for date in dates:
        historical = cryptocompare.get_historical_price_day(crypto, currency='USD', toTs=date)
        if historical:
            prices[date.strftime("%Y-%m-%d")] = historical[0]['close']
    return prices

def analyze_and_plot(subreddits, crypto, keyword):
    all_posts = fetch_posts(subreddits, period='month')

    daily_sentiments = {}
    for i in range(14):
        filtered_posts = filter_posts_by_date(all_posts, days_ago=i)
        daily_sentiments[i] = analyze_sentiments(filtered_posts, keyword)

    dates = [datetime.datetime.now() - datetime.timedelta(days=day) for day in range(13, -1, -1)]
    scores = [daily_sentiments[day] for day in range(13, -1, -1)]
    crypto_prices = fetch_crypto_prices(dates, crypto)

    days = np.arange(len(dates))
    sentiment_scores = np.array(scores)
    price_values = np.array([crypto_prices.get(date.strftime("%Y-%m-%d"), None) for date in dates])

    #Polynomial fit of 5th degree
    sentiment_fit = np.poly1d(np.polyfit(days, sentiment_scores, 5))
    price_fit = np.poly1d(np.polyfit(days, price_values, 5))

    #Graph sentiment and crypto prices with polynomial fit
    fig, ax1 = plt.subplots(figsize=(10, 5))
    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sentiment Score', color=color)
    ax1.plot([date.day for date in dates], sentiment_scores, 'o', color=color)
    ax1.plot([date.day for date in dates], sentiment_fit(days), color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  #instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel(f'{crypto} Price (USD)', color=color)
    ax2.plot([date.day for date in dates], price_values, 'o', color=color)
    ax2.plot([date.day for date in dates], price_fit(days), color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title(f'{crypto} Sentiment and Price Trend with 5th Degree Polynomial Regression')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    #Analyzing the trend direction to provide a buy, hold, or sell signal
    sentiment_derivative = sentiment_fit.deriv()
    recent_trend = sentiment_derivative(days[-1])  #Evaluate the derivative at the most recent day

    if recent_trend > 0:
        print(f"The recent trend in sentiment for {crypto} is increasing, suggesting a potential BUY signal.")
    elif recent_trend < 0:
        print(f"The recent trend in sentiment for {crypto} is decreasing, suggesting a potential SELL signal.")
    else:
        print(f"The recent trend in sentiment for {crypto} is stable, suggesting to HOLD.")

def main():
    subreddits = ['CryptoCurrency', 'Bitcoin', 'ethereum', 'Ripple', 'Litecoin', 
                  'Cardano', 'CryptoMarkets', 'CryptoCurrencies', 'altcoin', 'InvestingCrypto']

    print("Analyzing Bitcoin...")
    analyze_and_plot(subreddits, 'BTC', 'bitcoin')

    print("Analyzing Ethereum...")
    analyze_and_plot(subreddits, 'ETH', 'ethereum')

if __name__ == "__main__":
    main()
