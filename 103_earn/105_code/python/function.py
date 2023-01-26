# normal functions

def factorial(n):
    if n < 0:
        return -1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# for i in range(-3, 7):
    # print(factorial(i))

# function with default arguments

def sum(first, second=0):
    return first+second


# print(sum(3, 4), sum(5))

# function with variable number of arguments
def variable(name, *details):
    print(name, details)
    print(type(details))  # its a tuple


def variables(name, **details):
    print(name, details)
    print(type(details))  # its a dict


# variables("asrar", age=3, years=7)

# named arguments:
print(sum(first=3, second=7))
