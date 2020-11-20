from enum import Enum
class Factorial_type(Enum):
    ITERATIVE = 1
    RECURSIVE = 2

def factorial_of_recursive(n: int):
    if(n<0):
        return -1
    if( n==0):
        return 1
    return n * factorial_of_recursive(n-1)

def factorial_of_iterative(n: int):
    if(n<0):
        return -1
    if( n==0):
        return 1

    result = 1
    i=2
    while i<=n:
        result = result*i
        i=i+1 
    return result

def factorial_of(n:int, mode: Factorial_type):
    return (factorial_of_iterative(n) ) if (mode ==Factorial_type.ITERATIVE) else factorial_of_recursive(n)