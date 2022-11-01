# flask-microservice
##CS 361 Stock Market Price Microservice

Base URL: maxpreh.pythonanywhere.com

This microservice is deployed to Python Anywhere! You will need to make HTTP requests to receive data from the microservice. The main functionality of the backend of this api relies on using network results to scrape market data from Yahoo Finance.

Due to this there are some limits which I plan to add proxies to circumvent. Currently requests are limited to under ~2500 a day and ~1000 an hour

# Recieving Data

maxpreh.pythonanywhere.com/symbol

Data will be sent from the server in JSON format

# GET /symbol


{
    "market_price": int
}
