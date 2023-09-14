# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False
    
# print(is_even(50))



#how clean up this code

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:      #we can remove the elif bcz we only check if it is an even num
#         return False
    
# print(is_even(50))


#shorten
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
    
# print(is_even(50))


#even shorter
def is_even(num):
    return num % 2 == 0
      
print(is_even(50))