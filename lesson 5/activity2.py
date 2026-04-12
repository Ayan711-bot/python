actual_cost=int(input("Enter thr actual price of the product"))
sale_amt=int(input("Enter the sale amount of the product"))
if sale_amt > actual_cost:
    amt=sale_amt-actual_cost
    print("profit of about",amt)
else: 
    print("Tou are in loss")