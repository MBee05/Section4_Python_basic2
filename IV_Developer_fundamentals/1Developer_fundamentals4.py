#Python has auto-format
#code clean
#readability
#predictability
#DRY- do  not repeat


picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# iterate over picture
# if -> print ''
# if -> print "*"


#original code

for row in picture:
  for pixel in row:
    if pixel == 0:
      print(' ', end=' ')
    else:
      print('*', end=' ')
  print('')
   
   


#simpler
for row in picture:
  for pixel in row:
    if (pixel):    #pixel bit confusing so, we can remove the brackets           
      print('*', end=' ')
    else:
      print(' ', end=' ')
  print('')
   
   
   
   
#another way
fill = '*'
empty= ' '
   
for row in picture:
  for pixel in row:
    if (pixel):         
      print(fill, end=' ')
    else:
      print(empty, end=' ')
  print('')
   
   
   