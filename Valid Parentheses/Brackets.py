def isValid(s):
    check = {'(':')','{':'}','[':']'}
    brackets = list(s)
    current = []
    result = 0
    for i in brackets:
        if check.has_key(i):
            current.append(i)
        elif len(current) != 0:
            if i != check[current.pop()]:
                return False
        else:
            return False
        
    return True
    


print isValid("[")        