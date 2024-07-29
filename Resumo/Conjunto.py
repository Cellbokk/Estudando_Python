ex1 = {2,2,1,2,1}

print(ex1)

ex2 = {j for j in range(10)}
print(ex2)

ex2.add(2)
ex2.add(50)
ex2.add(100)

print(ex2)

# Converter uma lista em um conjunto
ages = [10, 5, 4, 5, 2, 1, 5]

set_of_ages = set(ages)
print(set_of_ages)

# Converter um conjunto em uma lista
list_of_ages = list(set_of_ages)
print(list_of_ages)

# Converter um conjunto em uma tupla
tuple_of_ages = tuple(list_of_ages)
print(tuple_of_ages)

