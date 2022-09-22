def is_square(n):   
    
    x = n**0.5
    if type(x) == complex:
        return False
    
    elif int(x)*int(x) == n and x>=0:
        return True
    else:
        return False
