def wish(*names):
    for name in names:
        print("Hello", name)

wish("Pradeep", "Over")

pi = 3.14
def area_of_circle(r):
    return pi * r *r 
r = int(input("Enter the radius of circle: "))
print("Area of circle is: ", area_of_circle(r))

def calculete(a, b):
    total = a + b
    diff = a - b
    prod = a * b
    div = a / b
    mod = a % b
    return total, diff, prod, div, mod
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
s,d,p,q,m = calculete(a,b)
print("Total= ",s,"Diff= ",d,"Prod= ",p,"Div= ",q,"Mod= ",m)
