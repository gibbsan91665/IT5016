# WhileBreak.py
#

number_of_tries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer, so exit loop using break
        break
    else:
        print("Sorry that is the wrong answer.... "
              "Try again!\n")
        number_of_tries -= 1

    # check number of tries and break if none left
    if number_of_tries == 0:
        print("You have run out of goes. Sorry.")
        break

x = input("Press any key to exit.")
'''
# assertion test case 1
answer = 42 results in Correct! Well done!
# assertion test case 2
answers 1,2 then 3 results in You have run out of goes. Sorry.
'''
