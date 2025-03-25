# lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
# The expression is executed and the result is returned.


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
