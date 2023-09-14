

# c = 10
# def confusion(b):  # parameter is a local param
#     print(b)
#     c = 90

# confusion(300)



# total = 0
# def count():
#     global total #global is a way to access a global variable
#     total += 1
#     return total
# print(count())



#
total = 0
def count(total):
    total += 1
    return total


print(count(count(count(total))))