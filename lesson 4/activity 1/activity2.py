Amount = int(input("Please enter amount for withdraw :"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 riyal", note_1)
print("notes of 50 riyal" , note_2)
print("notes of 10 riyal", note_3)