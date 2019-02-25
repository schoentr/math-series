""" 
 Overview of both Fibonacci Sequence and Lucas Sequence
"""
def fibonacci(value):
    """
    Accepts a number and returns the value of that number in the Fibonacci Sequence
    """
    fib_list = [0, 1]
    if value > 2:
        for i in range(2, value):
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[value - 1]
    
def lucas(value):
    """
    Accepts a number and returns the value of that number in the Lucas Sequence
    """
    lucas_list = [2, 1]
    if value > 2:
        for i in range(2, value):
            lucas_list.append(lucas_list[i - 2] + lucas_list[i - 1])
    return lucas_list[value - 1]

def sum_series(value, start=0, second=1):
    """
    Accepts a threesnumber and returns the value of that number Sequence
    """
    sum_list = []
    sum_list.append(start)
    sum_list.append(second)
    if value > 2:
        for i in range(2, value):
            sum_list.append(sum_list[i - 2] + sum_list[i - 1])
    return sum_list[value - 1]