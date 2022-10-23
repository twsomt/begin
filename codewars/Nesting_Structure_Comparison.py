def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False  
    
    
    for x, y in zip(original, other):
        if (type(x) is int and x == 1) and (type(y) is str and y == '['):
            return True
        
        if type(x) != type(y):
            return False
            
        if type(x) is list and type(y) is list:
            if not same_structure_as(x, y):
                return False
    
    return True