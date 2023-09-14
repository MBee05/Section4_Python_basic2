#*args and **kwargs

#*args
# def super_func(*args): #*args means it can takes any numbers of positional arguments
#     print(*args) #1 2 3 4 5
#     return sum(args)

# super_func(1,2,3,4,5) # like these num




# def super_func(*args): #*args means it can takes any numbers of positional arguments
#     print(args) # tuple(1, 2, 3, 4, 5)
#     return sum(args)

# print(super_func(1,2,3,4,5))


##########################################

#**kwargs
# def super_func(*args, **kwargs): #**kwargs can take keyword
#     print(kwargs)
#     return sum(args)

# print(super_func(1,2,3,4,5, num1=5, num2=10))




# def super_func(*args, **kwargs): 
#     total = 0
#     print(kwargs)
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total

# print(super_func(1,2,3,4,5, num1=5, num2=10))


# Rule: params, *args, default parameters, **kwargs

#parameters of name
# def super_func( name,*args, **kwargs): 
    
    
# default parameters 
def super_func(name, *args, i='hi', **kwargs): # we usually one of them
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Andy',1,2,3,4,5, num1=5, num2=10))