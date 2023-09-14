# def highest_even(li):
#     even=[]
    
#     for item in li:
#         if item % 2 ==0:
#             even.append(item)
#             return max(even)
       
# print(highest_even([10,2,9,4,5,8,3])) # output: 10



# def highest_even(li):
#     even=[]
#     for item in li:
#         if item % 2 ==0:
#             even.append(item)
#         return max(even)
       
# print(highest_even([10,2,9,4,5,8,3,2])) # output:10





# def highest_even(*args):
#     highest = 0
#     for item in args:
#         if item > highest:
#             if item % 2 == 0:
#                 highest = item
#                 return highest

# print(highest_even(10,69,60,20,12,33,54,54,53,45,21,23,11,56))



# def highest_even(num):
#     even=[]
#     for item in num:
#             if item % 2 == 0 and item > even:
#                 even=item
#                 return even
#     print(highest_even([10,69,60,20,12,33]))


def highest_even(num):
    maxi = 0
    for item in num:
        if item % 2 == 0:
            if item > maxi:
                maxi = item
                return maxi
print(highest_even([15,69,60,20,12,33]))



# def highest_even(list):
#     list.sort()
#     list.reverse()
#     for item in list:
#         return item if item % 2 == 0 else None

# print(highest_even([1,2,10,4,5]))


