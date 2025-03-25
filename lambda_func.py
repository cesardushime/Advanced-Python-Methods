# lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
# The expression is executed and the result is returned.

from functools import reduce

double = lambda x: x * 2
add = lambda x, y: x + y
max_val = lambda x, y: x if x > y else y
min_val = lambda x, y: x if x < y else y
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0

age_check = lambda age: "Adult" if age >= 18 else "Child"

print(age_check(20)) # Adult
print(age_check(15)) # Child
print(double(5)) # 10
print(add(5, 10)) # 15
print(max_val(5, 10)) # 10
print(min_val(5, 10)) # 5
print(full_name("John", "Doe")) # John Doe
print(is_even(10)) # True
print(is_odd(10)) # False

# filter() function is used to filter the give iterable (list, tuple, set, etc.)
# with the help of a function that tests each element in the iterale to be true or not.
# Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers) # [2, 4, 6, 8, 10]

# map() function is used to apply a given function to all the items in an input_list.
# Syntax: map(function, iterable)

# squaring all evens in the list
squared_numbers = list(map(lambda x: x ** 2, even_numbers))

# reduce() function is used to apply a function to the elements of an iterable in a rolling computation. It performs a pair-wise operation on the elements of the iterable.
# The reduce() function is defined in the functools module.
# Syntax: reduce(function, iterable)

sum = reduce(lambda x, y: x + y, squared_numbers)
print(sum) # 220, sum of all squared even numbers in the list