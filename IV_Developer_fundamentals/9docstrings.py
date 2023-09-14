# def test (a):
#     print(a)
    
# test('!!!!!!!!!!!!!')



#we can use docstrings

def test (a):
    '''
    info: this func tests and prints param a   
    '''          ##to add comment and definition to your function, help you coworker
    print(a)
    
#test('!!!!!!!!!!!!!')
#test()# refers to which func it belongs

#help(test)# to find out what the func does

#magic method
#print(test.__doc__) 