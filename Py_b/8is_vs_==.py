# is  checks strictly if the location in the memory is the same thing that you are looking for

# ==  checks only the values

print(True == 1) # true   boolean = 1 & 0
print(True is 1) # false bcz True is not 1
print(True is True)# true


print('' == 1)  #False
print('1' == '1') # true bcz of the same type that are in same location


print([] == [])  #True
print([] is [])  # False, every time, I created a list, its added in  memory(location), whenever i create a new list it creates in another location, so these are 2 different lists

print(10 == 10.0)   #true 


print([1,2,3] is [1,2,3]) #false eventhough bcz created in new location (same for set, tuple and dict)


a = [1,2,3]
b = [1,2,3]
print(a is b) #false bcz created in different location but if do the following

print(a == b) # true bcz checks only the values
