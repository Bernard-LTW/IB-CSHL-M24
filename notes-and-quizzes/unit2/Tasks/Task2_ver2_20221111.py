# 2022-11-11 Task2 Part2
#Updated 2022-11-15

# Create a program where it is a game of ten questions
# The user will be asked to press YES or NO on the arduino
# If the answer is correct, the LED will blink for five seconds

import time
import pyfirmata
from pyfirmata import Arduino
# Create a question bank of 10 yes/no questions and answers
question_bank = [
    ["Is our teacher Dr Ruben?", "yes"],
    ["Is PyCharm a programming language?", "no"],
    ["Is Python a programming language?", "yes"],
    ["Do we have a quiz every class?", "yes"],
    ["Is 11 in binary 1011?", "yes"],
    ["Is 3 in binary 11?", "yes"],
    ["Have we tried programming in Swift yet?", "no"],
    ["Do we use github to submit school work?", "yes"],
    ["Is snakify a lot of work?", "yes"],
    ["Is Dr Ruben a genius?", "yes"],
    ["Do you like Computer Science?", "yes"]
]



board = Arduino('/dev/cu.usbserial-110')
print("Board is ready")

it = pyfirmata.util.Iterator(board)
it.start()

buttonA = board.digital[9]
buttonA.mode = pyfirmata.INPUT
button_stateA = False

buttonB = board.digital[5]
buttonB.mode = pyfirmata.INPUT
button_stateB = False

LED = board.digital[2]
LED.write(0)
for i in question_bank:
    print(i[0])
    print("Waiting for the button to be pressed")
    while not button_stateA and not button_stateB:
        time.sleep(0.1)

        button_stateA = buttonA.read()
        button_stateB = buttonB.read()
        #print(button_stateA, button_stateB)
    print("Button is pressed.")
    if button_stateA:
        if i[1] == "yes":
            print("Correct!")
            for j in range(5):
                LED.write(1)
                time.sleep(1)
                LED.write(0)
                time.sleep(1)
        else:
            print("Incorrect!")
    elif button_stateB:
        if i[1] == "no":
            print("Correct!")
            for j in range(5):
                LED.write(1)
                time.sleep(1)
                LED.write(0)
                time.sleep(1)
        else:
            print("Incorrect!")
    button_stateA = False
    button_stateB = False

print("Done")
exit()
