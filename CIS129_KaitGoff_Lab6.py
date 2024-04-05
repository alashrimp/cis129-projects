# Kaitlynn Goff
# 31 March 2024 
# CIS129 Lab 6
# This code is a Hot Dog Cookout Calculator 

#Import library 
import math

#Define variables 
hot_Dogs = 10 # number of hot dogs in a package 
Buns = 8 # number of buns in a package

#Input from user 
print("Enter the number of people attending the cookout",":")
num_of_people = int(input()) # number of people attending cookout
print("Enter the number of hot dogs for each person:")
hotdogs_per_person = int(input()) # number of hot dogs per person
total_Hotdogs = num_of_people * hotdogs_per_person

#Calculating hot dogs needed
min_Dogs = math.ceil(total_Hotdogs / hot_Dogs)
dogs_Left = (hot_Dogs - total_Hotdogs % hot_Dogs) % hot_Dogs # left over hot dogs

#Calculating hot dog buns needed 
min_Dogs = math.ceil(total_Hotdogs / hot_Dogs) # minimum hotdogs needed 
buns_Left = (Buns - total_Hotdogs % Buns) % Buns # left over hot dog buns
min_Buns = math.ceil(total_Hotdogs / Buns)

print("Minimum packages of hot dogs needed: ", min_Dogs)
print("Minimum packages of hot dogs buns needed: ", min_Buns)
print("Hot dogs left over: ", dogs_Left)
print("Hot dog buns left over: ", buns_Left)
