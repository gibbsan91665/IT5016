# MorseCode.py
# Creating a morse encoder

morse = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
"0" : "-----",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"." : ".-.-.-",
"," : "--..--"
}

word = input('\nPlease enter a string:').upper()
morseString = ''

for char in word:
  morseString += morse[char]
  morseString += ' '

print('\nThe MorseCode for ', word, 'is :')
print(morseString)

# Test Case Assertion
# Assertion 1: input and output should be
# Please enter a string:hellothere
# The MorseCode for HELLOTHERE is :
# .... . .-.. .-.. --- - .... . .-. .
