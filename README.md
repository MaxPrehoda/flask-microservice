# flask-microservice
CS 361 Stock Market Price Microservice

Base URL: maxpreh.pythonanywhere.com

This microservice is deployed to Python Anywhere! You will need to make HTTP requests to receive data from the microservice. The main functionality is using network results to scrape market data from Yahoo Finance.

# Recieving Data

maxpreh.pythonanywhere.com/symbol

Data will be sent from the server in JSON format

# GET /symbol

'''Status: 200
{
    "market_price": int
}'''
