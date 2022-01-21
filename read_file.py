import csv
import pandas as pd
#  1 way
# my_file=open("fruits.txt")
# print(my_file.read())
# my_file.seek(0)
# content=my_file.read()
# print(content)
# my_file.close()
#  my_file.read() error is given
#  2 way using with which will automatically call the close() for you to close the file
# with open("fruits.txt","r") as my_file:
#     content=my_file.read()
# print(content)
# #
# # # to write to a file
# with open("vegetables.txt","w") as my_file:
#     my_file.write("Carrot")
# #
# #  to append on to the file, a to open file in append mode and + to open it for updating so while appending you can read
# #  the file as well
with open("vegetables.txt","a+") as my_file:
    my_file.write("Onion")
    # my_file.seek(0)  # to take cursur back at start of file
    # content=my_file.read()

# print(content)

# with open("user_details.csv") as my_file:
#     user_details=csv.reader(my_file,delimiter=",")
#     # header=next(user_details)
#     # print(header)
#     for row in user_details:
#         print('--'.join(row))

# dataframe=pd.read_csv("user_details.csv")
# # print(dataframe)
# print(dataframe.head(1))
# print("Number of rows:- ",dataframe.shape[0])


sniffer = csv.Sniffer()
dialect = sniffer.sniff('quarter:dime:nickel:penny')
print(dialect.delimiter)