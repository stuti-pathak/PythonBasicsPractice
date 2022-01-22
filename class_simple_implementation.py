from contact_exception import ContactCustomException
import re
from my_manual_package.add import add_numbers

# class method, static method and instance method


class UserDetails:
    """
    class represents the user details
    """
    name="Python"  # class variable

    def __init__(self, *params):
        """

        :param params:
        """
        print("Constructor called")
        print(params[0])
        self.first_name = params[0][0]
        self.last_name = params[0][1]

    @classmethod
    def get_name(cls):
        return cls.name

    @staticmethod
    def get_age(age):
        return age

    def get_first_name(self):
        """
        get the first name attribute
        :return: fisrt name of the user
        """
        print("getter called")
        print(self.name)
        return self.first_name

    def set_first_name(self, value):
        print("setter called")
        if value is None:
            raise ContactCustomException("Please enter valid name")
        if re.fullmatch("^[A-Z]{1}[a-z]{2,}$", value):
            self.first_name = value
        else:
            raise ContactCustomException("Name must be of at least 3 characters")

    # @property
    # def last_name(self):
    #     return self.last_name_
    #
    # @last_name.setter
    # def last_name(self, value):
    #     if value is None or value is "":
    #         raise ContactCustomException("Please enter valid name")
    #     if re.fullmatch("^[A-Z]{1}[a-z]{2,}$", value):
    #         self.last_name_ = value
    #     else:
    #         raise ContactCustomException("Name must be of at least 3 characters")

    def __str__(self):
        print("__str__() called")
        return self.first_name + " " + self.last_name


user1 = UserDetails(["Draco", "Malfoy"])
print(user1)
try:
    user1.set_first_name(None)
except Exception as exp:
    print(exp.__str__())
# print(user1.get_first_name())
# print(user1.get_age(12))
# print(UserDetails.get_name())
name=input("enter the name")
print(type(int(name)))
# print(user1.first_name)
# user1.first_name="Ammy"
# print(user1.first_name)
# print(user1)
# user1.__str__()
# try:
#     user1.first_name = "joE"
# except ContactCustomException as exception:
#     print(exception.__str__())

# print(UserDetails.__doc__)
# print(UserDetails.first_name.__doc__)
