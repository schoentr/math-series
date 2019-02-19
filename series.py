def fibSeq(value):
    fib_list = [0, 1]
    if value > 2:
        for i in range(2, value):
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[value - 1]
    
def lucas(value):
    lucas_list = [2, 1]
    if value > 2:
        for i in range(2, value):
            lucas_list.append(lucas_list[i - 2] + lucas_list[i - 1])
    return lucas_list[value-1]