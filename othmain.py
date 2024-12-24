from math import *

def cos_series(x,terms):
    result = 0
    for n in range(terms):
        result += (-1**n)*((x**(2*n))/factorial((2*n)))
    return result

def shin_series(x,terms):
    result = 0
    for n in range(terms):
        result += (x**(2*n*1))/(factorial(2*n))
    return result

def log_nat(x,terms):
    result=0
    for n in range(x,terms):
        result += ((-1)**(n+1))*(((x**n)/n))
    return result


