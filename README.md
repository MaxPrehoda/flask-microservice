# flask-microservice
CS 361 Stock Market Price Microservice

Base URL: maxpreh.pythonanywhere.com

This random username microservice is deployed to Python Anywhere! You will need to make HTTP requests to receive data from the microservice.

# Recieving Data

maxpreh.pythonanywhere.com/<symbol>

Data will be sent from the server in JSON format

# GET /<symbol>

'''Status: 200
{
    "market_price": int
}'''
