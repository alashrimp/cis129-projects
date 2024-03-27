# Author : Kaitlynn G. 
# Lab 3 in CIS129 course at PCC
# Short 'My Coffee Shop' simulator program 

Coffee_cost = 5.00
Muffin_cost = 4.00
Tax_rate = 0.06

print("Welcome to Kait's Coffee Shop!")

# Get user input

Coffee = int(input("How many coffees would you like?"))

Muffin = int(input("How many muffins would you like?"))

# Calculate Subtotal

Subtotal = int(Coffee * Coffee_cost) + int(Muffin *Muffin_cost)
print("Subtotal:$",Subtotal)

Taxamount = Tax_rate * (int(Coffee) + int(Muffin))
print("Tax amount:$",Taxamount) 

Totalamount = Taxamount + Subtotal
print("Grand total:$",Totalamount)

subtotal = (int(Coffee) + int(Muffin)) * Tax_rate

grandtotal = subtotal + Taxamount 

print("Thank you for coming, we hope to see you again soon!")
