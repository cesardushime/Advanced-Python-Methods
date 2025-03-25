# Aggregate elements from two or more iterables, creating a pair of elements at the same index.
# The zip() function returns an iterator of tuples based on the iterable objects.
# If the passed iterables are of different lengths, the iterator stops as soon as the shortest iterable is exhausted.
# Syntax: zip(iter1, iter2, iter3, ...)

usernames = ['john', 'jane', 'doe']
passwords = ['password', 'password123', 'password456']

# zip the usernames and passwords
users = zip(usernames, passwords) # zip objects are iterable.

for user in users:
    print(user)