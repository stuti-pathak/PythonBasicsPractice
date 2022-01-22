def divide():
    a = 5
    b = 4
    try:
        # c=a/b
        if b == 0:
            raise ZeroDivisionError("give proper value othre than 0")
        else:
            raise ValueError("value error is raised")
    except ValueError as value_error:
        print(value_error.__str__())
    except ZeroDivisionError as exc:
        print(exc.__str__())
    except Exception as exp:
        print(exp.__str__())
    finally:
        print("try executed successfully")


print("calling the divide function")
divide()
