import random


# for i in range(10, 21,2):
#     if i == 16:
#         break
#     else:
#         print(i)
# else:
#     print("loop is ended successfully")
#
# a = 45
# b = 50
# if a > b:
#     print("a is greater")
# elif a < b:
#     print("b is greater")
#     print("")
# else:
#     print("a is equal to b")
# print("outside if else")
#
# i=0
# while i<3:
#     print(i)
#     break
#     i+=1
# else:
#     print("while loop ended successfully")

# kwargs and varags

#
# def square(number):
#     return number * number
#
#
# def empty_function():
#     pass
#
#
# print(square(49))
# print(empty_function())

# lambda arguments/parameters:expression
# lambda num:num*num


lambda_expression = lambda number1,number2,number3,string:str(number1 * number2*number3)+" "+string
print(lambda_expression(50,40,30,"concatenated"))
# a=10
# b=10.8
# c="string"
# print(type(a),type(b),type(c))
# print(type(square))
# print(dir(str))

