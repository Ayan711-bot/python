a=[1,2,3]
b=[1,2,3]
c=a
print(a is b)
print(a is c)
print(b is c)
print(id(a))
print(id(b))
print(id(c))
x=5
if type(x) is int:
    print("No is integer")
else:
    print("It is not an integer")