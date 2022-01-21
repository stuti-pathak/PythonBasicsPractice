# int, float, complex, str, tuple, list, dictionary, set,boolean
# complex_number=2+5j
# print(type(complex_number))
# print(isinstance(complex_number,complex))
my_tuple = (1, 2, "str")
print(my_tuple)
# print(type(my_tuple))
# print(isinstance(my_tuple,tuple))
# print(my_tuple[1])
# my_tuple[1] = 3
# print(dir(tuple))
# my_tuple=my_tuple+(3,4)
# print(my_tuple)
empty_tuple = tuple()
# print(empty_tuple)
# my_list = list()
# print(my_list)
# my_list = [3, 4, 5.89]
# print(my_list)
# my_list[0] = 2
# my_list[1] = 3
# print(my_list)
# #
# my_list.extend([12, 'list', 'list', 90.898])
# print(my_list)
# print(len(my_list))
# my_list.append([12, 'list'])
# print(my_list)
# print(len(my_list))
# print(len(my_list))
# print(my_list[6])
# print(my_list.index('list'))
# print("index acessing ", my_list[-2])
# # print(my_list.count('list'))
# print(my_list[::-1])
# #
# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     "Language": "Python"
# }
# print("dictionary ", my_dict)
# print(my_dict.get('key1'))
# print(my_dict.values())
# my_dict.update({"Update":"value"})
# print(my_dict)
# # set
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for key, value in phone_numbers.items():
#     print("{} has as phone number {}".format(key, value))

# list comprehension and dictionary comprehension
my_list = [1, 3, 67, 24, 36, 90, 13]
# a="ggdgd"
# b=114141 # variable b has value which object of int type
# c=5.7
# print(type(c))

output_list = list()
#
#
# def even_numbers():
#     for x in my_list:
#         if x % 2 == 0:
#             output_list.append(x)
#
# even_numbers()
# print("using function", output_list)
# # output_list = [x for x in my_list if x % 2 == 0]
# contact_list=[contact for contact in address_list if contact.city=="Mumbai"]
# output_list=[x*2 for x in my_list]
# print("list comprehension", output_list)
# if-else implementation in list comprehension
# temps = [221, 234, 567, -9999, 613]
# print(temps)
# temp2 = [item if item != -9999 else 0 for item in temps]
# # print(temp2)
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(dict1)
# double_dict1 = {k:v*2 for (k,v) in dict1.items()}
# print(double_dict1)
# lambda a,b,c : operation1
# filter,map,reduce
# filter
from functools import reduce

my_list = [1, 3, 67, 24, 36, 90, 13]
# filter syntax:- filter(function,iterator)
# larger_elements = filter((lambda number: number > 20), my_list)
# print(tuple(larger_elements))
# # first_name
# contacts=filter((lambda contact:contact.getFirstName==first_name),contact_list)
# if contacts is None

# map
# map syntax:- map(function,iterable[s])
# square_number_list = map((lambda number: number * number), my_list)
# # print("original list",my_list)
# print("map implementation",list(square_number_list))

# reduce
# reduce syntax :- reduce(function,iterator,initial_point)

# def even_number(number)
# reduce(even_number(number),my_list)


# def calculate_sum(sum,number):
#     sum+=number
#     return sum


# sum=reduce(calculate_sum,my_list)
# sum=reduce((lambda total,number: total+number),my_list,100)
# print(sum)
#
#
# def even_number(number):
#     return number%2==0
#
#
# even_list=filter(even_number,my_list)
# print(list(even_list))
