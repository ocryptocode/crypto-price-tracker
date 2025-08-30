# Crypto Price Tracker

A platform that tracks all of crypto prices in real time.

This is the next coinmarketcap.

## Features

- Fetches latest prices for cryptocurrencies (BTC, ETH, XRP) from CoinMarketCap.
- Provides a basic frontend to display fetched data.

## Prerequisites

Before running the application, make sure you have:

- Python 3 installed
- API key from CoinMarketCap (stored in a .env file, see below)

## Setup

1. Clone the repository:
   
    git clone https://github.com/ocryptocode/crypto-price-tracker
   
    cd <repository-directory>

3. Install dependencies:

    pip install -r requirements.txt

4. Set up environment variables:

Create a .env file in the root directory and add your CoinMarketCap API key:

COINMARKETCAP_API_KEY=your_api_key_here

## Running the Application
To run the application, use the following command:

python app.py

The application will start on http://localhost:5001/.

## API Endpoint
/api/prices: Fetches latest cryptocurrency prices from CoinMarketCap.
Frontend
The frontend is served from the static directory and can be accessed at http://localhost:5001/.

## Troubleshooting
If you encounter issues fetching data, check your API key and ensure the Flask server is running correctly.

## Contributing
Feel free to contribute by submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
 
