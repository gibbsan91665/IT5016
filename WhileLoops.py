# WhileLoops.py
#
is_running = True

while is_running:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer, so exit loop - reset is_running
        is_running = False
    else:
        print("Sorry that is the wrong answer.... "
              "Try again!\n")

x = input("Press any key to exit.")
'''
# assertion test case 1
answer = love then loop executes
# assertion test case 2
answer = 42 results in Correct! Well done!
'''
