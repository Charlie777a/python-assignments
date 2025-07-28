def factorial(x):
    if x<2:
        return 1
    return x*(factorial(x-1))

x=int(input("enter the number: "))
ans=factorial(x)
print("the factorial is :",ans)