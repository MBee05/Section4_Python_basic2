
#Exercise: check for duplicate in list
some_list = ['a','c','b','d','m','n','n','b']
new_list = []

# for i in some_list:
#     if i not in new_list:
#         new_list.append(i)
#         print(new_list)
        
        
        

# remove all db duplicate
# new_list1 = set(some_list)        
# print(new_list1)



# list the duplicate item
# dup = {x for x in some_list if some_list.count(x) > 1}
# print(dup)


for value in some_list:
    if some_list.count(value)>1:
        if value not in new_list:
            new_list.append(value)
print(new_list)
    