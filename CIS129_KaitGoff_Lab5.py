# Kaitlynn Goff
# 30 March 2024 
# Lab 5 
# This code will calculate number of bottles collected by a store for 7 days

# Defining variables 

total_Bottles = 0
today_bottles = 0
total_payout = 0
keepGoing = 'y' 
counter = 1
num_of_days = 7
price_per_bottle = .10

#Calculating number of bottles for 7 days

while (keepGoing == 'y'):
    counter = 1 #initializing back to first day in week
    while (counter <= num_of_days): 
        print("Enter number of bottles returned for day", counter,":")
        today_bottles = int(input())
        total_Bottles = today_bottles + total_Bottles
        total_payout = price_per_bottle * total_Bottles
        counter += 1  
    print("The total number of bottles collected is:", total_Bottles)
    print("The total paid out is:", total_payout)
    print("Do you want to enter another week's worth of data?")
    keepGoing = input("Enter y or n:")
