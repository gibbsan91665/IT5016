# WaveLengths.py
# If elif Statements
print("Welcome to wavelength to colour converter\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you entered in nanometres is ", wave_length,"\n")
print("The colour for this wavelength is...", end="")

if wave_length > 750:
    print ("The wavelength entered is higher than the visible spectrum! This is infrared.")
elif wave_length >= 620:
    print ("Red")
elif wave_length >= 590:
    print("Orange")
elif wave_length >= 570:
    print("Yellow")
elif wave_length >= 495:
    print("Green")
elif wave_length >= 450:
    print("Blue")
elif wave_length >= 380:
    print("Violet")
else:
    print("Indeterminate, :-(, the number entered is outside the visible spectrum!")

# test case assertion 1
'''
wave_length = 385
colour is Violet
'''
