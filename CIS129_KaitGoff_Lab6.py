# Kaitlynn Goff
# 31 March 2024 
# CIS129 Lab 6
# This code is a Hot Dog Cookout Calculator 

import math

def gettotal_Hotdogs():
    print("Enter the number of people attending the cookout",":")
    num_of_people = int(input())
    print("Enter the number of hot dogs for each person:")
    hotdogs_per_person = int(input())
    total_Hotdogs =  num_of_people *  hotdogs_per_person
    return total_Hotdogs 

def showresults(total_Hotdogs):
    hot_Dogs = 10
    Buns = 8 
    
    min_Dogs = math.ceil(total_Hotdogs / hot_Dogs)
    dogs_Left = (hot_Dogs - total_Hotdogs % hot_Dogs) % hot_Dogs # left over hot dogs
    
    min_Buns = math.ceil(total_Hotdogs / Buns)
    buns_Left = (Buns - total_Hotdogs % Buns) % Buns # left over hot dog buns

    print("Minimum packages of hot dogs needed: ", min_Dogs)
    print("Minimum packages of hot dogs buns needed: ", min_Buns)
    print("Hot dogs left over: ", dogs_Left)
    print("Hot dog buns left over: ", buns_Left)
    
total_Hotdogs = gettotal_Hotdogs()
showresults(total_Hotdogs)
