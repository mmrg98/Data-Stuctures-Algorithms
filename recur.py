def rec(lst):
    result=0
    for i in lst:
        if type(i)==int:
            result=result+i
        else:
            result+=rec(i)
    return result
numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]
print(rec(numbers))