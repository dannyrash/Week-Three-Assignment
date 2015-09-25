_author_ = "danny.rash"

# CIS-125
# Star Wars Name Maker
#
# Uses a combination of your first name, last name, mother's maiden name, and town you were born in to create your Star Wars name

# Declare Magic numbers and constants

# LOOPCOUNTER = 2
# name = Danny

# Write program code here

print("Find out your Star Wars name!")

# Input
# Retrieve data for generation
firstname = input('Please enter your first name: ')
lastname = input('Please enter your last name: ')
maidenname = input('Please enter your mothers maiden name: ')
town = input('Please enter the name of the town in which you were born: ')

# Output
# Process and print generated Star Wars name
print("Your Star Wars name is " + lastname.capitalize()[0:3]+firstname.lower()[0:2], maidenname.capitalize()[0:2]+town.lower()[0:3] + "!")