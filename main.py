# This is a sample Python script.
import re
import sys
import os

foo_bar = __import__("import demo")
# from my_manual_package.add import add_numbers
from my_manual_package.add import multiply

# from foo_bar import my_file
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(a):
    """
    This is first function to print hello
    :param a:
    :return:
    """
    name = 12
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, there "+a,name)
    print(f"Hi, there {a} {name}")  # Press Ctrl+F8 to toggle the breakpoint. format string


# ctrl+alt+l

if __name__ == '__main__':
    print_hi("Python")
    # print(print_hi.__doc__)

    # c=foo_bar.square()
    # print(dir(list)) # to get all the functions supported by it or defined in it
    # print(dir(__builtins__)) # get builtin functions and data types
    # d=multiply(12,13)
    # print(d)
    # name=input("enter name")
    # print(name)
    # load_dotenv()
    # print(os.getenv('ADMIN'))
