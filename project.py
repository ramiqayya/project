import os
import requests
import urllib.parse
from tkinter import *

root = Tk()

myLabel = Label(root, text='Stonks')
myLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
api_key = 'RZCZQLZF3628BWEB'


def main():
    # Print the JSON data returned by the API
    symbol = Entry(root, width=20, borderwidth=5)
    symbol.grid(row=1, column=0, padx=20, pady=20)
    symbol.insert(0, 'Inser stock symbol')

    print(symbol)

    button = Button(root, text='get price', padx='30',
                    pady='5', command=lambda: get_price(symbol.get()))

    button.grid(row=1, column=1, padx=20, pady=20)

    # print(lookup('AAPL'))

    # print(stock_name('AAPL'))

    root.mainloop()


def get_price(sym):
    try:
        name = stock_name(sym)
        price = lookup(sym)['Global Quote']['05. price']
        price_label = Label(root, text=name+': $'+price)
        price_label.grid(row=3, column=0, columnspan=2)
    except KeyError:
        return '404 price not found!'


def lookup(x):
    try:
        endpoint = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
            x+'&apikey='+api_key

        response = requests.get(endpoint)
        return response.json()
    except KeyError:
        return 'Cannot find stonk!'


def stock_name(m):
    try:
        endpoint = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={m}&apikey={api_key}'

    # Send the GET request to the endpoint
        response = requests.get(endpoint)

    # Parse the JSON data returned by the API
        return response.json()['bestMatches'][0]['2. name']
    except KeyError:
        return '404 not found'


if __name__ == "__main__":
    main()
