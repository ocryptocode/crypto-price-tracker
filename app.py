from flask import Flask, jsonify, send_from_directory
import requests
from dotenv import load_dotenv
from config import get_config

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__, static_folder='static')
app.config.from_object(get_config())  # Load configuration from config.py


@app.route('/api/prices', methods=['GET'])
def get_prices():
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
		'X-CMC_PRO_API_KEY': app.config['COINMARKETCAP_API_KEY'],
		'Accepts': 'application/json'
	}
	params = {
		'symbol': 'BTC,ETH,XRP'
	}
	try:
		response = requests.get(url, headers=headers, params=params)
		response.raise_for_status()
		data = response.json()
		return jsonify(data['data'])
	except requests.RequestException:
		app.logger.error('Error fetching data: {e}')
		return jsonify({'error': 'Error fetching data'}), 500


@app.route('/')
def serve_frontend():
	return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
	app.run(debug=True, port=5001)
