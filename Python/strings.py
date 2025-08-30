s = 'gfg'
print(s[1])
print(s + s[2])

# Reverse a string through Slicing
def revstring(n):
    ans = n[::-1] #reads the string from end to start
    return ans
print(revstring("wenesday"))