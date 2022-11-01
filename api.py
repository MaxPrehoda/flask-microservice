from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
@app.route("/")
def hello_world():
    symbol = 'AAPL'

    r = requests.get(f'https://finance.yahoo.com/quote/{symbol}')
    print(r)
    if str(r) == "<Response [404]>":
        print('bad symbol, got 404')
    to_be_parsed = str(r.text)[r.text.find(f'data-symbol="{symbol}" data-test="qsp-price" data-field="regularMarketPrice"'):r.text.find('" active="">')]
    regular_market_price = float(to_be_parsed[to_be_parsed.find('value="')+7:])
    print(regular_market_price)
    return f'<p>Hello, Hobs! The price of {symbol} is {regular_market_price} </p>'

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        print(json)
        symbol = json['symbol']
        r = requests.get(f'https://finance.yahoo.com/quote/{symbol}')
        if str(r) == "<Response [404]>":
            print('bad symbol, got 404')
        to_be_parsed = str(r.text)[r.text.find(f'data-symbol="{symbol}" data-test="qsp-price" data-field="regularMarketPrice"'):r.text.find('" active="">')]
        regular_market_price = float(to_be_parsed[to_be_parsed.find('value="')+7:])
        return str(regular_market_price)
    else:
        return 'Content-Type not supported!'