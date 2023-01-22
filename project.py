import os
import requests
import urllib.parse


# Replace YOUR_API_KEY with your actual API key
api_key = 'RZCZQLZF3628BWEB'

# Define the endpoint for the real-time stock market data


# Send the GET request to the endpoint


def main():
    # Print the JSON data returned by the API

    print(lookup('AAPL'))

    print(stock_name('AAPL'))


def lookup(x):
    endpoint = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
        x+'&apikey='+api_key

    response = requests.get(endpoint)
    return response.json()


def stock_name(m):
    endpoint = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={m}&apikey={api_key}'


# Send the GET request to the endpoint
    response = requests.get(endpoint)

# Parse the JSON data returned by the API
    return response.json()['bestMatches'][0]['2. name']

#['bestMatches'][0]['2. name']


if __name__ == "__main__":
    main()
