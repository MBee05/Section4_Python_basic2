#while condition: do something loop

#i = 0 
# while i < 50:
#     print(i) # infinite loop
#     break 
    


# i = 0 
# while i < 50:
#     print(i) # infinite loop
#     break 
    
    
i = 0 
while i < 50:
    print(i)
    i += 1 #do it 50 times or i +=1
    
else:   #if we add a break statement b4 this else block win't work
    print('done with all the work')
    
    
    
#why should we use while loop and for loop, it depends on the problem in a for loop

my_list = [1,2,3]
for item in my_list:
    print(item)  #its much simpler 
                    #if you now how many times then have to use for loop 
    
    
    
i=0
while i < len(my_list[i]):
    print(i)
    i +=1             # gives the same answer so which one  to use
    
#while loop are very flexible, we can do more than 3 times if we dont know then use while loop    

    
while True:
    input('say something:')
    break    #without break it will continue until you end it



while True:
    response= input ('say something:')
    if (response == 'bye'):
        break



