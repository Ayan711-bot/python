print("Enter Marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science:"))
physics = int(input("physics: "))

sum = math+english+science+physics
print("sum of math,english,science anf ohysics =", sum)
perc = (sum/400)*100
print(perc)
