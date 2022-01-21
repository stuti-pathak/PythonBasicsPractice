# From tuple to list:
data = (1, 2, 3)
print(list(data))

# From list to tuple:
data = [1, 2, 3]
print(tuple(data))

# From list to dictionary:
data = [["name", "John"], ["surname", "smith"]]
print(dict(data))
{'name': 'John', 'surname': 'smith'}
# Note that the original data type needs to have the data structured in a way that can be understood by the new data
# type For example, the following would not work:
data = [1, 2, 3]
print(dict(data))  # will give TypeError: cannot convert dictionary update sequence element 0 to a sequence
