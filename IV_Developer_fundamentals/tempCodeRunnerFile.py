
def highest_even(list):
    list.sort()
    list.reverse()
    for item in list:
        return item if item % 2 == 0 else None

print(highest_even([1,2,10,4,5]))
