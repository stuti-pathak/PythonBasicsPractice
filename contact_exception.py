class ContactCustomException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# obj=ContactCustomException("hfhfhfhf")
# print(obj)