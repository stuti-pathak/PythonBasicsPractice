import unittest
import pytest

from class_implementation import UserDetails
from contact_exception import ContactCustomException


class TestUserDetails(unittest.TestCase):
    def test_user_first_name(self):
        try:
            param=("alex","Thomson")
            # type(input1) == str
            user=UserDetails(param)
        except ContactCustomException as exception:
            self.assertEqual("Name must be of at least 3 characters",exception.message)
            # self.assertEqual(True,1<3)
            # self.assertTrue(1<3)

    def test_user_with_valid_details(self):
        param=("Alex","Thomson")
        user=UserDetails(param)
        self.assertEqual("Alex",user.first_name)
