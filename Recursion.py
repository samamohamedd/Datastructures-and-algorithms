#using recrsion:
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
#using loops:
def factorial2(num):
    i = num 
    fact = 1
    while i > 1:
        fact = fact * i
        i -= 1
    return fact     

print (factorial(6)) 
print (factorial2(6)) 