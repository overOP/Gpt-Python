def greet_all(greeting, *names):
    for name in names:
        print(greeting, name)

greet_all("Hi", "Pradeep", "Roshani")


def wish(*me):
    for mee in me:
        print("Hello", mee)

wish("Pradeep", "Roshani")


def show_profill(**info):
    for key,value in info.items():
        print(key ,"=", value)

show_profill(name = "pradeep", age= 24)


pi = 3.14
def area_of_circlr(r):
    return pi * r * r
r = int(input("Enter the area of circle: "))

print(area_of_circlr(r))

def total(a,b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    mod = a % b
    return add, sub, mult, div, mod
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

a,s,m,d,mo = total(a,b)
print("Total= ",a,"Sub= ",s,"Mult= ",m,"div= ",d,"Mod= ",mo)

def biggest(a,b):
    if a > b:
        return a
    else:
        return b
    
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

big = biggest(a,b)
print("big number = ", big)