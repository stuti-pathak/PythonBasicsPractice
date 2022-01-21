def divide():
    a = 5
    b = 0
    try:
        if b == 0:
            raise ZeroDivisionError("divide by zero exception")
        # else:
        #     raise ValueError("value error is raised")
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
