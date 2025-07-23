from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_price(coin_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[coin_id]['usd'] if coin_id in data else None

@app.route('/')
def index():
    btc_price = get_price('bitcoin')
    eth_price = get_price('ethereum')
    return f"<h1>Crypto Prices</h1><p>Bitcoin (BTC): ${btc_price}</p><p>Ethereum (ETH): ${eth_price}</p>"

if __name__ == '__main__':
    app.run(debug=True)
