# def say_hello(name, emoji):
#     print(f'helllooooooo {name}{emoji}')
#say_hello()
    
    
            #positional argument require to be at the place, has to follow the parameters
#say_hello('andy','--')
#say_hello('sam','--')
#say_hello('lian','--')






#keyword arguments
#say_hello(emoji=' ', name= 'bibi') # but that made practise to change the order of the arguments better to follow the parameters



#default parameters
def say_hello(name='sam ram', emoji='---'):
    print(f'helllooooooo {name}{emoji}')
say_hello()