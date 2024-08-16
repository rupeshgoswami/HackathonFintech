# HackathonFintech
Hackathonfintech repository
---

# FinTech Hackathon Project

Welcome to our FinTech startup project! This repository contains all the code and resources for our innovative financial technology solution developed during the hackathon Fundra.

# Demo Video of Fundra
youtube link - https://www.youtube.com/watch?v=HCqiCPlLGhc
Google Drive link - https://drive.google.com/file/d/10cIwAmo53pk-wLJbBecT8l9t6PUG3nzi/view?usp=drive_link
Live Server Access of cross border payment functionality - https://easypey.streamlit.app/

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Our project aims to revolutionize the way people manage their finances through cutting-edge technology. We provide a user-friendly platform that simplifies financial transactions, budgeting, and investment management.

## Features

- **Secure Transactions**: Ensure safe and encrypted financial transactions.
- **Budgeting Tools**: Easy-to-use tools for managing personal and business budgets.
- **Investment Tracking**: Monitor and analyze investment portfolios in real-time.
- **Financial Insights**: Gain insights with data analytics and predictive models.

## Tech Stack

- **Frontend**: React, HTML, CSS, JavaScript
- **Backend**: Node.js, Express
- **Database**: MongoDB
- **Authentication**: JWT, OAuth
- **Hosting**: AWS, Heroku
- **APIs**: Plaid API for banking data, Alpha Vantage for financial market data

## Setup

To run this project locally, follow these steps:

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/fintech-startup.git
    cd fintech-startup
    ```

2. **Install dependencies**
    ```bash
    npm install
    ```

3. **Set up environment variables**
    Create a `.env` file in the root directory and add the following variables:
    ```plaintext
    MONGODB_URI=your_mongodb_connection_string
    JWT_SECRET=your_jwt_secret
    PLAID_CLIENT_ID=your_plaid_client_id
    PLAID_SECRET=your_plaid_secret
    ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    ```

4. **Run the development server**
    ```bash
    npm run dev
    ```

5. **Open the application in your browser**
    Navigate to `http://localhost:3000` to see the application in action.

## Usage

After setting up the project, you can start using it by following these steps:

1. **Register/Login**: Create a new account or log in with your existing credentials.
2. **Link Bank Accounts**: Use the Plaid integration to securely link your bank accounts.
3. **Manage Budget**: Set up your budget and track your spending.
4. **Track Investments**: Monitor your investment portfolios and get real-time updates.
5. **Get Insights**: Use the analytics dashboard to gain financial insights and make informed decisions.

## Contributing

We welcome contributions from the community. To contribute, please follow these steps:

1. **Fork the repository**
2. **Create a new branch**
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**
4. **Commit your changes**
    ```bash
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Create a pull request**

Please make sure your code follows our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
