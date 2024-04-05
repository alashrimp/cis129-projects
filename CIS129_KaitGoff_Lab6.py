# Kaitlynn Goff
# 31 March 2024 
# CIS129 Lab 6
# This code is a Hot Dog Cookout Calculator 

#Define variables 

hot_Dogs = 10 # number of hot dogs in a package 
Buns = 8 # number of buns in a package
dogs_Left = 0 # left over hot dogs
min_Dogs = 0 # minimum hotdogs needed 
buns_Left = 0 # left over hot dog buns
num_of_people = 0 # number of people attending cookout 
dogs_per_person = 0 # number of hot dogs per person
import math

#Input from user 

print("Enter the number of people attending the cookout",":")
num_of_people = input(int())
print("Enter the number of hot dogs for each person:")
dogs_per_person = input(int())
total_Hotdogs = num_of_people * dogs_per_person

#Calculating hot dogs needed
min_Dogs = math.ceil(total_Hotdogs / hot_Dogs)
dogs_Left = (hot_Dogs - total_Hotdogs % hot_Dogs) % hot_Dogs

#Calculating hot dog buns needed 
min_Dogs = math.ceil(total / hot_Dogs)
buns_Left = (Buns - total % Buns) % Buns
min_Buns = math.ceil(total / Buns)


total = num_of_people * total_hotdogs

print("Total number of hot dogs needed:")
input(int())
total_hotdogs = number_of_people * dog_per_person


print("Minimum packages of hot dogs needed: ", min_Dogs)
print("Minimum packages of hot dogs buns needed: ", min_Buns)
print("Hot dogs left over: ", dogs_Left)
print("Hot dog buns left over: ", buns_Left)

#Import Library
import math 

#Defining Variables

hot_Dogs = 10 # number of hot dogs in a package 
Buns = 8 # number of buns in a package
keepGoing = 'y'
counter = 0

#Input from user 

def total_Hotdogs():
    print("Enter the number of people attending the cookout", ":")
    num_of_people = input(int())
    print("How many hot dogs would you like?", counter, ":") 
    hot_dog_request = input(int())
    total_Hotdogs = num_of_people * hot_dog_request
    return total_Hotdogs 

min_Dogs = math.ceil(total_Hotdogs / hot_Dogs)
dogs_Left = (hot_Dogs - total_Hotdogs % hot_Dogs) % hot_Dogs
min_Dogs = math.ceil(total_Hotdogs / hot_Dogs)
buns_Left = (Buns - total_Hotdogs % Buns) % Buns
min_Buns = math.ceil(total / Buns)
    
print("Minimum packages of hot dogs needed: ", min_Dogs)
print("Minimum packages of hot dogs buns needed: ", min_Buns)
print("Hot dogs left over: ", dogs_Left)
print("Hot dog buns left over: ", buns_Left)


