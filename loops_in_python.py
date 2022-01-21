from math import sqrt
# import_demo=__import__("import demo")
# my_list = [1, 2, 3, 4, 5]
# for i in my_list:
#     print(i)
# print("outside the loop")
#
# for i in range(1, 5, 1):
#     print(i)
#     if i == 3:
#         break
# else:
#     print("for loop is executed successfully")
# print("while loop")
# i = 0
# while i <= 5:
#     print(i)
#     i = i + 1
# else:
#     print("while loop's else block")
#
#
# def empty_function():
#     pass

# varargs :- variable number of arguments as tuple or list
# kwargs:- collection of arguments in key value pair


def variable_arguments(*params1, **params):
    # print("variable1 :",variable1)
    # print("variable2 :",variable2)
    print("params1 :",params1[0][0])
    print("params1 :",params1[1])
    print("params2 :",params)


# lambda_exp=lambda x:x*x
# print(lambda_exp(10))
# import_demo.square()
# empty_function()
my_tuple = (1, 2, 3,4,5,6,7)
my_dict = {"Language1": "Python", "Language2": "Java",1:"value1"}
variable_arguments(my_tuple,my_dict,key1="value1")

# print(sqrt(1331))