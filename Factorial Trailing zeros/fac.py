
def trailingZeroes(n):
    
    result = 0
    #base cases
    if n < 5:
        return result
    else:
        i = 5
        while(i <= n):
            result += n/i
            i *= 5
    return result


print trailingZeroes(24)
print trailingZeroes(25)
