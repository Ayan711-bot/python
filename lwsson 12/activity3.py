num = input("Enter number:")

if len(num) >= 4:
    mid = len(num)//2
    prod = int(num[mid]) * int(num[mid-1])
    print("Product =",prod)
else:
    print("Enter at least 4-digit number")
