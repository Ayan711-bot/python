a='codingal'
print(a[::-1])

string = input("Please enter your owm string:")

string2 = ('')
for i in string:
    string2 = i + string2
print("\nThe Original String =",string)
print("The reversed string =", string2)