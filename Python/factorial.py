def factorial (num):
    res= 1
    for i in range(2,num+1):
        res*=i
    
    return res

num =5
print("the factorial for", num ,"is",factorial(5))