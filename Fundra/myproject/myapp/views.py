from django.shortcuts import render
from myapp.models import SentimentData

def home(request):
    return render(request, 'myapp/index.html')

def crypto_sentiment(request):
    btc_data = SentimentData.objects.filter(crypto='BTC').latest('date')
    eth_data = SentimentData.objects.filter(crypto='ETH').latest('date')

    context = {
        'btc_graph': btc_data.graph,
        'btc_recommendation': btc_data.recommendation,
        'eth_graph': eth_data.graph,
        'eth_recommendation': eth_data.recommendation,
    }

    return render(request, 'myapp/crypto_sentiment.html', context)
