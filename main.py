def close10(x, y):
    if abs (x - 10) < abs(y - 10):
        return x
    elif x == y:
        return 0
   
    else:
        return y
    
    
print (close10(9, 9))

