def fact (n):
    if n == 1:
        return 1
    return fact(n - 1) * n

result = fact(5)
print(result)



'''

def fact (n):
    if 5 == 1:
        return 1
    return fact(24) * 5  -->  20 play -->  120
    
    if n=4 == 1:
        return 1
    return fact(6) * 4   --> 12  play --> 24 
    
    if n=3 == 1
        return 1
    return fact(2) * 3   --> 6 play --> 6
    
    if n=2 == 1
        return 1
    return fact(1) * 2   -->  2 play --> 2
    
    if n=1 == 1
        return 1
    
fact(5)

'''

