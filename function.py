def num(n):
    print(n)
n=input("enter the num:")
print(n)
num(n)

print("Factorial series:")

def fact(n):
    i=1
    f=1
    while(i<=n):
        f=f+f*i
        i=i+1
        return f
n=input("enter the num:")
x=fact(n)
print(n)
