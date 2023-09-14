# scope- what are the variables do I have access to?
#1- start with local scope
#2- is there parent local scope?
#3-global 
#4- built in python function

def outer():
    x= ('local')
    def inner():
        nonlocal x  # takes the parent variable if take it out will print outer: local
        x="nonlocal"
        print("inner:", x)
        
    inner()
    print("outer:", x)
outer()


#Why do we need scope?

