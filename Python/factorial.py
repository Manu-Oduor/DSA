def factorial (num):
    res= 1
    for i in range(2,num+1):
        res*=i
    
    return res

num =5
print("the factorial for", num ,"is",factorial(5))


def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(6))