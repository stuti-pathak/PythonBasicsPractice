import pytest
# from _pytest._code import ExceptionInfo

from contact_exception import ContactCustomException
from class_implementation import UserDetails


class TestContactDetails:

    @pytest.fixture()
    def user(self):
        param = ("Peter", "Thomson")
        user = UserDetails(param)
        return user

    @pytest.fixture()
    def user_details(self,request):
        param = ("Peter", "Thomson")
        user = UserDetails(request.param)
        return user

    def test_user_first_name_with_invalid_details(self, user):
        # param = ("Peter", "Thomson")
        # user = UserDetails(param)
        # ex= ExceptionInfo()
        with pytest.raises(ContactCustomException) as exception:
            user.first_name = "alex"
        assert user.first_name != "alex"
        assert exception.value.message == "Name must be of at least 3 characters"

    @pytest.mark.parametrize("actual,expected", [("", "Please enter valid name")])
    def test_user_last_name_with_given_inputs(self, user, actual, expected):
        with pytest.raises(ContactCustomException) as exception:
            user.last_name = actual
        assert exception.value.message == expected
    #
    # @pytest.mark.parametrize("user_details",[["Peter", "Thomson"]],indirect=True)
    # def test_check_parameter_pass_to_fixture(self,user_details):
    #     assert user_details.first_name=="Peter"


