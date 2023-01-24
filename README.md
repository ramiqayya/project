# STONKS
#### Video Demo: [Youtube Video Link](https://youtu.be/WxfggFjyjpc)

#### Description
In Stonks project I used the python library Tkinter to make a simple program with GUI for querying and calculating stocks and shares.

#### files
* The main program is in project.py so it can be executed using by typing **python project.py**
* I used also test_project.py to test some functions as per requested. it can be executed using the command **pytest test_project.py** 
* In requirements.txt all the dependencies are listed for this Python project

#### project.py
In project.py I used the library Tkinter to make a graphical user interface.
There are 9 functions in project.py: main, sell, calc_price, multiply, sum_num, get_price, lookup, stock_name, and error_message functions.
##### main
Is the main function in the project from which all other functions can be executed as needed.
##### calc_price 
This function will calculate the total value for a specific number of shares and display it on the GUI window with help of the other functions
##### multiply
This simple function takes two numbers and returns the multiplication result this is used to multiply the number of the shares with each share price
##### sum_num
This function takes two numbers and returns the summation
##### get_price 
This function is used to get the price of a given stock symbol and returns the price of that stock from the API
##### lookup
This function gives us all details from a given stock symbol using API
#### stock_name
This function used to search for the full name of a company for a given stock symbol 
#### error_message
This function will handle all the error messages if any error is raised from the previous functions