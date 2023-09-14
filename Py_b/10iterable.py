# iterable is an object or a collection that can be iterated over again, list, dictionary, tuple, set, string

# iterate(action)-> one by one to check each item in the collection
 

# for item4 in (1,2,3,4,5):
#     for x in ['a', 'b', 'c']:
#         print(item4, x)
        
        
#dict has 3 methods

user = {
    'name': 'mass',
    'age': 50,
    'can_swim' : False
}       

# for i in user.items(): 
#     print(i) #output: key + value
    

    
    
# for i in user.values(): 
#     print(i) #print the values
    
    
# for i in user.keys(): 
#     print(i) # print the keys
    
    
# for i in user.items(): 
#     key, value = i;
#     print(key, value)
    


for key, value in user.items():
    print(key, value)