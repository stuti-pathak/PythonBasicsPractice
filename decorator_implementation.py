# def my_decorator(func): # func=say_whee()
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func() # inner function
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# say_whee()

# simple decorator without using the @ decorator thing
# say_whee=my_decorator(say_whee)
# say_whee()
# first_name=property(first_name)
# first_name()
# hello=my_decorator(say_whee)
# print(type(hello))
# hello()

################################################

#
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        print("Something is happening after the function is called.")
        func()
    return wrapper

#
@my_decorator
def say_whee():
    print("Whee!")
#
#
# # calling decorator using @ thing
say_whee()