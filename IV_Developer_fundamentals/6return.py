#return
#function has always to return something
#1 can return something 
#2 or a function doesnt return anything but modify something


# def sum(num1, num2):
#     return num1 + num2

# print(sum(4,5))




# def sum(num1, num2):
#     print('hiii')   #return 'hiii'
#     num1 + num2

# print(sum(4,5))

#should do one thing really well.
#should return something

# def sum(num1, num2):
#      return num1 + num2
 
# ##total = sum(10,5) #so 15 in memory
# print(sum(10,sum(10,5)))


# def sum(num1, num2):
#     def another_func(num1, num2):
#      return num1 + num2
#     return another_func
 
# total =sum(10, 20)
# print(total(10,20))




# def sum(num1, num2):
#     def another_func(num1, num2):
#      return num1 + num2
#     return another_func(num1, num2)
 
# total =sum(10, 20)
# print(total)



# def sum(num1, num2):
#     def another_func(n1, n2):
#      return n1 + n2
#     return another_func(num1, num2)
 
# total =sum(10, 20)
# print(total)



def sum(num1, num2):
    def another_func(n1, n2):
     return n1 + n2
    return another_func(num1, num2)
    return 5
    print('hello')
 
total =sum(10, 20)
print(total)