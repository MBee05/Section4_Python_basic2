#function, to use it have to call it


def say_hello():
    print('helllooooooo')
    
say_hello()





picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#to repeat the pattern several the we have to paste the code many times while we can do it in short way with function



def show_tree():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print('')
        
show_tree()
show_tree()
show_tree()