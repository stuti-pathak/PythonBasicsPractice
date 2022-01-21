# In this section, you learned that:
# A list comprehension is an expression that creates a list by iterating over another container.
# A basic list comprehension:

temp=[i*2 for i in [1, 5, 10]]
print(temp)

#  List comprehension with if condition:
temp=[i*2 for i in [1, -2, 10] if i>0]
print(temp)

#  List comprehension with an if and else condition:
temp=[i*2 if i>0 else 0 for i in [1, -2, 10]]
print(temp)