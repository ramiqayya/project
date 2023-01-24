import os
import sys
import requests
import urllib.parse
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Stonks App')
root.iconbitmap('./stonks_icon.ico')


row1 = 3
emsg = 0
frame = LabelFrame(root, text='Stonks App', padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

stonk_img = Image.open("stonks_img.jpg")

resized_image = stonk_img.resize((400, 205), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
img_label = Label(frame, image=new_image)
img_label.grid(row=0, column=0, columnspan=3)


api_key = 'RZCZQLZF3628BWEB'

# font = Font(family="Helvetica", size=20, weight="bold")
# label.config(font=font)


def main():

    font = ('Times', 12)

    symbol = Entry(frame, font=font, width=20, borderwidth=5)
    symbol.grid(row=1, column=0, padx=20, pady=20)
    symbol.insert(0, 'Stock Symbol')

    print(symbol)

    global sos
    global son

    sos = 0
    son = 0

    button = Button(frame, text='Get price', font=font, padx=30,
                    pady=5, command=lambda: get_price(symbol.get()))

    button.grid(row=1, column=1, padx=20, pady=20)

    sellb = Button(frame, text='Calculate', font=font,
                   padx=30, pady=5, command=sell)
    sellb.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    # clearb = Button(root, text='Clear', padx='30', pady='5', command=clear_all)
    # clearb.grid(row=1, column=3, padx=20, pady=20)

    # print(lookup('AAPL'))

    # print(stock_name('AAPL'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()


def sell():

    global frame2
    top = Toplevel()
    top.iconbitmap('./stonks_icon.ico')
    global font
    font = ('Times', 12)

    frame2 = LabelFrame(top, text='Stonks App',
                        padx=10, pady=10)
    frame2.grid(row=0, column=0, padx=10, pady=10)
    stock_symbol = Label(frame2, text='Stock Symbol',
                         font=font, padx=5, pady=5)
    stock_symbol.grid(row=0, column=0, columnspan=2)
    symbolE = Entry(frame2, font=font, width=20, borderwidth=5)
    symbolE.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
    stock_amount = Label(frame2, text='Amount', font=font, padx=5, pady=5)
    stock_amount.grid(row=0, column=2, columnspan=2)
    amountE = Entry(frame2, font=font, width=20, borderwidth=5)
    amountE.grid(row=1, column=2, columnspan=2, padx=20, pady=20)
    # check for name and price

    calc_btn = Button(frame2, text='Calculate', font=font, padx=30,
                      pady=5, command=lambda: calc_price(symbolE.get(), amountE.get()))
    # print(calc_btn)

    calc_btn.grid(row=2, column=0, columnspan=4, padx=20, pady=20)


def calc_price(sym, amount):
    global frame2
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
        total = multiply(float(priceE), float(amount))
    except (KeyError, IndexError, ValueError):
        error_message('Error!', 'Error! 404 Stock not found!')

    if son == 0:

        s_name = Label(frame2)
        s_name.grid(row=3, column=0)
        s_name2 = Label(frame2)
        s_name2.grid(row=4, column=0)

        s_amount = Label(frame2)
        s_amount.grid(row=3, column=1)
        s_amount2 = Label(frame2)
        s_amount2.grid(row=4, column=1)

        unit_price = Label(frame2)
        unit_price.grid(row=3, column=2)
        unit_label = Label(frame2)
        unit_label.grid(row=4, column=2)

        tot_val = Label(frame2)
        tot_val.grid(row=3, column=3)
        tot_label = Label(frame2)
        tot_label.grid(row=4, column=3)

    s_name.grid_forget()
    s_name2.grid_forget()
    s_amount.grid_forget()
    s_amount2.grid_forget()
    unit_price.grid_forget()
    unit_label.grid_forget()
    tot_val.grid_forget()
    tot_label.grid_forget()

    global font
    font = ('Times', 12, 'bold')

    s_name = Label(frame2, text='Stock name', font=font,
                   relief=RIDGE, padx=10, pady=10)
    s_name.grid(row=3, column=0, padx=20, pady=20, sticky=NSEW)
    s_name2 = Label(frame2, text=nameE, font=font,
                    relief=RIDGE, padx=10, pady=10)
    s_name2.grid(row=4, column=0, padx=20, pady=20, sticky=NSEW)

    s_amount = Label(frame2, text='Stock amount', font=font,
                     relief=RIDGE, padx=10, pady=10)
    s_amount.grid(row=3, column=1, padx=20, pady=20, sticky=NSEW)
    s_amount2 = Label(frame2, text=amount, font=font,
                      relief=RIDGE, padx=10, pady=10)
    s_amount2.grid(row=4, column=1, padx=20, pady=20, sticky=NSEW)

    unit_price = Label(frame2, text='Unit price', font=font,
                       relief=RIDGE, padx=10, pady=10)
    unit_price.grid(row=3, column=2, padx=20, pady=20, sticky=NSEW)
    unit_label = Label(
        frame2, text=f"${float(priceE):,.2f}", font=font, relief=RIDGE, padx=10, pady=10)
    unit_label.grid(row=4, column=2, padx=20, pady=20, sticky=NSEW)

    tot_val = Label(frame2, text='Total Value', font=font,
                    relief=RIDGE, padx=10, pady=10)
    tot_val.grid(row=3, column=3, padx=20, pady=20, sticky=NSEW)
    tot_label = Label(
        frame2, text=f"${total:,.2f}", font=font, relief=RIDGE, padx=10, pady=10)
    tot_label.grid(row=4, column=3, padx=20, pady=20, sticky=NSEW)
    son = 1


def multiply(x, y):
    return x*y


def sum_num(x, y):
    return x+y


def get_price(sym):
    font = ('Times', 12, 'bold')
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

        name = Label(frame, text=name, font=font, padx=5, pady=5,
                     bg='#94ff57', bd=1, relief=SUNKEN)
        name.grid(row=row1, column=0)
        price = Label(frame, text=' $'+price, font=font, padx=5, pady=5,
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
