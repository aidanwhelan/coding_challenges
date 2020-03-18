# car_cdr.py
#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
#   and last element of that pair. For example, car(cons(3, 4)) returns 3, and
#   cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.
#
# Mar 10 2020
# Aidan Whelan

# Provided Functions
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Debugging
result = cons(1,2)
print(result)
print(result(f))

# Solution
def car(cons_out):
    x,y = cons_out(f)
    return(x)

def cdr(cons_out):
    x,y = cons_out(f)
    return(y)

# Testing
car(cons(3,4))
cdr(cons(3,4))
