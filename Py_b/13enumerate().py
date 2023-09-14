#enumerate takes an  iterable object and gives you an index counter the item of that index



# for i,char in enumerate ('hello'):
#     print(i, char)



#list
# for i,char in enumerate ([1,2,3]):
#     print(i, char)


#tuple
# for i,char in enumerate ((1,2,3)):
#     print(i, char)    



for i,char in enumerate (list(range(100))):
    #print(i, char)
    

    if char == 50:
        print(f"index of 50 is:{i}")