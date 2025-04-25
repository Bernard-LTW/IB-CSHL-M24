# 2022-11-08 Task 2

# Binary counter to LEDs on Arduinos
from my_lib import validate_1_to_n_input
import time
from pyfirmata import Arduino

board = Arduino('/dev/cu.usbserial-10')
print("Board is ready")

while True:
    i = validate_1_to_n_input(input("Enter a number: "), 7)
    board.digital[12].write(0)
    board.digital[5].write(0)
    board.digital[9].write(0)
    board.digital[12].write(i // 4)
    board.digital[5].write((i % 4) // 2)
    board.digital[9].write(i % 2)
    time.sleep(1)
