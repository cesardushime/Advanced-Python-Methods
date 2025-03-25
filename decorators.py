# A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# Allows you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
# Decorators can be used to check for permissions, modify or track the arguments passed to a function, log the calls to a function, etc.

def add_sprinkles(func):
    def wrapper(): # wrapper function that adds sprinkles to the icecream
        func()
        print("You also got sprinkles 🎉")
    return wrapper

def add_cherry(func):
    def wrapper(): # wrapper function that adds cherry to the icecream
        func()
        print("And some cherries 🍒")
    return wrapper

@add_sprinkles # decorator that adds sprinkles to the icecream
@add_cherry # decorator that adds cherry to the icecream
# The order of the decorators matters. The decorator that is defined first is the one that is executed last.
def get_icecream():
    print("Here is your icecream🍨")

get_icecream()