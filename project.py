import os
import sys
import requests
import urllib.parse
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Stonks App')
row1 = 3
emsg = 0
frame = LabelFrame(root, text='Stonks App', padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

myLabel = Label(frame, text='Stonks')
myLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
api_key = 'RZCZQLZF3628BWEB'


def main():
    # adding a frame

    # Print the JSON data returned by the API
    symbol = Entry(frame, width=20, borderwidth=5)
    symbol.grid(row=1, column=0, padx=20, pady=20)
    symbol.insert(0, 'Inser stock symbol')

    print(symbol)

    global sos
    global son

    sos = 0
    son = 0

    button = Button(frame, text='Get price', padx=30,
                    pady=5, command=lambda: get_price(symbol.get()))

    button.grid(row=1, column=1, padx=20, pady=20)

    sellb = Button(frame, text='Calculate', padx=30, pady=5, command=sell)
    sellb.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    # clearb = Button(root, text='Clear', padx='30', pady='5', command=clear_all)
    # clearb.grid(row=1, column=3, padx=20, pady=20)

    # print(lookup('AAPL'))

    # print(stock_name('AAPL'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()


def sell():
    global top
    top = Toplevel()
    stock_symbol = Label(top, text='Stock Symbol', padx=5, pady=5)
    stock_symbol.grid(row=0, column=0, columnspan=2)
    symbolE = Entry(top, width=20, borderwidth=5)
    symbolE.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    stock_amount = Label(top, text='Amount', padx=5, pady=5)
    stock_amount.grid(row=0, column=2, columnspan=2)
    amountE = Entry(top, width=20, borderwidth=5)
    amountE.grid(row=1, column=2, columnspan=2, padx=20, pady=20)
    # check for name and price

    calc_btn = Button(top, text='Get price', padx=30,
                      pady=5, command=lambda: calc_price(symbolE.get(), amountE.get()))
    print(calc_btn)

    calc_btn.grid(row=2, column=0, columnspan=2, padx=20, pady=20)


def calc_price(sym, amount):
    global top
    global son

    global s_name
    global s_name2
    global s_amount
    global s_amount2
    global unit_price
    global unit_label
    global tot_val
    global tot_label

    try:

        nameE = stock_name(sym)
        priceE = lookup(sym)['Global Quote']['05. price']
        total = float(priceE)*float(amount)
    except (KeyError, IndexError, ValueError):
        error_message('Error!', 'Error! 404 Stock not found!')

    if son == 0:

        s_name = Label(top)
        s_name.grid(row=3, column=0)
        s_name2 = Label(top)
        s_name2.grid(row=4, column=0)

        s_amount = Label(top)
        s_amount.grid(row=3, column=1)
        s_amount2 = Label(top)
        s_amount2.grid(row=4, column=1)

        unit_price = Label(top)
        unit_price.grid(row=3, column=2)
        unit_label = Label(top)
        unit_label.grid(row=4, column=2)

        tot_val = Label(top)
        tot_val.grid(row=3, column=3)
        tot_label = Label(top)
        tot_label.grid(row=4, column=3)

    s_name.grid_forget()
    s_name2.grid_forget()
    s_amount.grid_forget()
    s_amount2.grid_forget()
    unit_price.grid_forget()
    unit_label.grid_forget()
    tot_val.grid_forget()
    tot_label.grid_forget()

    s_name = Label(top, text='Stock name', padx=10, pady=10)
    s_name.grid(row=3, column=0, padx=20, pady=20)
    s_name2 = Label(top, text=nameE, padx=10, pady=10)
    s_name2.grid(row=4, column=0, padx=20, pady=20)

    s_amount = Label(top, text='Stock amount', padx=10, pady=10)
    s_amount.grid(row=3, column=1, padx=20, pady=20)
    s_amount2 = Label(top, text=amount, padx=10, pady=10)
    s_amount2.grid(row=4, column=1, padx=20, pady=20)

    unit_price = Label(top, text='Unit price', padx=10, pady=10)
    unit_price.grid(row=3, column=2, padx=20, pady=20)
    unit_label = Label(
        top, text=f"${float(priceE):,.2f}", padx=10, pady=10)
    unit_label.grid(row=4, column=2, padx=20, pady=20)

    tot_val = Label(top, text='Total Value', padx=10, pady=10)
    tot_val.grid(row=3, column=3, padx=20, pady=20)
    tot_label = Label(top, text=f"${total:,.2f}", padx=10, pady=10)
    tot_label.grid(row=4, column=3, padx=20, pady=20)
    son = 1


def get_price(sym):
    try:

        global row1
        global name
        global price
        row1 = 3
        global sos
        global error
        global emsg

        if sos == 0:

            name = Label(frame)
            name.grid(row=row1, column=0)
            price = Label(frame)
            price.grid(row=row1, column=0)

        # print(emsg)

        name.grid_forget()
        price.grid_forget()

        name = stock_name(sym)
        price = lookup(sym)['Global Quote']['05. price']

        name = Label(frame, text=name, padx=5, pady=5,
                     bg='#94ff57', bd=1, relief=SUNKEN)
        name.grid(row=row1, column=0)
        price = Label(frame, text=' $'+price, padx=5, pady=5,
                      bg='#94ff57', bd=1, relief=SUNKEN)
        price.grid(row=row1, column=1)
        sos = 1
        # row1 += 1
        # clear.lift()
    except KeyError:
        error_message('Error!', 'Error! 404 Stock not found!')


# def clear_all():
#     # global name
#     # global price
#     name.delete(0, END)
#     price.delete(0, END)


def lookup(x):
    try:
        endpoint = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
            x+'&apikey='+api_key

        response = requests.get(endpoint)
        return response.json()
    except (KeyError, IndexError):
        error_message('Error!', 'Error! 404 Stock not found!')


def stock_name(m):
    try:
        endpoint = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={m}&apikey={api_key}'

    # Send the GET request to the endpoint
        response = requests.get(endpoint)

    # Parse the JSON data returned by the API
        return response.json()['bestMatches'][0]['2. name']
    except (KeyError, IndexError):
        error_message('Error!', 'Error! 404 Stock not found!')


def error_message(title, message):
    global row1
    global error
    global emsg
    # error = Label(frame, text=message, bg='red')
    # error.grid(row=row1, column=0, columnspan=2)
    # button_quit = Button(frame, text="Exit", command=root.quit)
    # button_quit.grid(row=4, column=0, columnspan=2)
    # emsg = 1
    global sos
    sos = 0
    something = messagebox.showerror(title, message)
    # print(something)
    if something == 'ok':
        root.quit()
        sys.exit()


if __name__ == "__main__":
    main()
