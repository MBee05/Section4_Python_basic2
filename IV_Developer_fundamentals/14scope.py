# scope- what are the variables do I have access to?
#scope Rules
# if True:
#     x = 10

# def some_func():
#     total =100
#     print(total)





# a = 1

# def confusion():
#     a = 5
#     return a
# print(a)
# print(confusion())
    


#1- start with local scope
#2- is there parent local scope?
#3-global 
#4- built in python function



#parent
b = 1
def parent():
    b=10
    def confusion1():
        return b
    return confusion1()

print(parent())
print(b)



#global
# b = 1
# def parent():
#     def confusion1():
#         return b
#     return confusion1()

# print(parent())
# print(b)


#built in python function

c = 1
def parent1():
    def confusion2():
        return sum          #sum is a buitl in function
    return confusion2()

print(parent1())
print(c)