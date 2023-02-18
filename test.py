# import math; import os; os.system("cls"); r = float(input("Enter the raidus of the circle: ")); print(f"The area of the circle with radius {r} is {math.pi*r*r}")
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def my_function(x, y):
    return x + y

my_function(3, 4)
