import os
import requests
import urllib.parse
from tkinter import *

root = Tk()
root.title('Stonks App')
row1 = 3
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

    clearb = Button(root, text='Clear', padx='30', pady='5', command=clear_all)
    clearb.grid(row=1, column=3, padx=20, pady=20)

    # print(lookup('AAPL'))

    # print(stock_name('AAPL'))

    root.mainloop()


def get_price(sym):
    try:

        global row1

        name = stock_name(sym)
        price = lookup(sym)['Global Quote']['05. price']

        name = Label(root, text=name, bg='#94ff57')
        name.grid(row=row1, column=0)
        price = Label(root, text=' $'+price, bg='#94ff57')
        price.grid(row=row1, column=1)
        row1 += 1
        # clear.lift()
    except KeyError:
        error = Label(root, text='Error! 404 price not found!', bg='red')
        error.grid(row=row1, column=0, columnspan=2)
        row1 += 1


def clear_all():
    global name
    global price
    name.delete(0, END)
    price.delete(0, END)


def lookup(x):
    try:
        endpoint = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
            x+'&apikey='+api_key

        response = requests.get(endpoint)
        return response.json()
    except (KeyError, IndexError):
        global row1

        error = Label(root, text='Error! 404 Stock not found!', bg='red')
        error.grid(row=row1, column=0, columnspan=2)
        row1 += 1


def stock_name(m):
    try:
        endpoint = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={m}&apikey={api_key}'

    # Send the GET request to the endpoint
        response = requests.get(endpoint)

    # Parse the JSON data returned by the API
        return response.json()['bestMatches'][0]['2. name']
    except (KeyError, IndexError):
        global row1
        error = Label(root, text='Error! 404 Stock not found!', bg='red')
        error.grid(row=row1, column=0, columnspan=2)
        row1 += 1


if __name__ == "__main__":
    main()
