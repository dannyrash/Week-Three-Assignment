_author_ = "danny.rash"

# CIS-125
# English to Pig Latin Translator
#
# Takes an English word and translates it to Pig Latin

# Declare Magic Numbers and Constants

vowels = "aeiou"

# LOOPCOUNTER = 2
# name = Danny

# Write program code here

# Input
# Retrieve English word for translation

word = input('Enter an English word to translate: ')

# Output
# Process and print Pig Latin translation

if word[0] in vowels :
    print (word + "yay")
else :
    print (word.upper()[1] + word[2:] + word.lower()[0] + "ay")
    
# Case fix: I used the 'upper' and 'lower' commands to fix the case issue