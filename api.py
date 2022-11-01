from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
@app.route("/<symbol>")
def hello_world(symbol):
    r = requests.get('https://finance.yahoo.com/quote/%s' % symbol)
    print(r)
    if str(r) == "<Response [404]>":
        return jsonify({'error': 'bad symbol'})
    to_be_parsed = str(r.text)[r.text.find(f'data-symbol="{symbol}" data-test="qsp-price" data-field="regularMarketPrice"'):r.text.find('" active="">')]
    regular_market_price = float(to_be_parsed[to_be_parsed.find('value="')+7:])
    print(regular_market_price)
    return jsonify({'market_price': regular_market_price})