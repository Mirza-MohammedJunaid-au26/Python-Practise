# print the string in reverse order using Recursion

def rev(st,l):
    if l == 0:
        return st[0]
    else:
        print(st[l],end="")
        return rev(st,l-1)

inp = input("Enter :")
print(rev(inp,len(inp)-1))


# program to find x raise to y using Recursion

def pow(b,p):
    
    if p == 1:
        return b
    
    else:
        return b * pow(b,p-1)

inp1 = int(input("Enter Number :"))
inp2 = int(input("Enter Power :"))
print(pow(inp1,inp2))


# Find Factorial using Recursion

def factorial(f):
    
    if f == 1:
        return 1
    
    else:
        return f * factorial(f-1)

inp3 = int(input("Enter :"))
print(factorial(inp3))


# GCD of two Numbers 

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
inp4 = int(input("Enter 1st Num :"))
inp5 = int(input("Enter 2nd Num :"))
print(gcd(inp4,inp5))


# Fibonachhi Series

def fib(i):
    
    if i == 1:
        return 0
    elif i == 2:
        return 1
    
    return i+fib(i-1)

inp6 = int(input("Enter :"))
print(fib(inp6))