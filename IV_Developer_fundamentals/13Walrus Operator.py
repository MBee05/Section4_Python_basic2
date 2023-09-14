#walrus operator -> :=

a = 'helloooooooooooooo'
# if (len(a) > 10):
#     print(f"too long {len(a)} elements")  # using len *2
    
    
# if ((n := len(a))> 10):
#     print(f"too long {n} elements")   # avoid repeatition



while ((n := len(a)) > 1):
    print(n)    
    a=a[:-1]
print(a)