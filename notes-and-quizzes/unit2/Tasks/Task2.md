# Task 2

## Prompt
To build the circuit below using Arduino and create the program in Python to control the LED.

## System Diagram
![](/Assets/Task2_SysD.jpg)


## Code Structure(Forever) 
```.py
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
```

## Code Structure(User Input) 
```.py
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
```

## Evidence
![](/Assets/Task2_Evidence.jpeg)
*Fig.2* **Photo of the build**
As we can see in Figure 2, it shows a arduino on the left of the photo

## Video

[Click here for the video](https://drive.google.com/file/d/1f_uqRTZztHHKePOmN2UyAHlGDSkFtJRf/view?usp=share_link)

*Video.1* **Video of the first program**

[Click here for the video](https://drive.google.com/file/d/1pvcRx-9zHo7RyiVTpqROfeByRSnRg2VE/view?usp=share_link)

*Video.2* **Video of the second program**

## Citations

[1] Pinzon, Ruben. “System Diagram Binary Counter.” System Diagram Binary Counter: Google Slides, 8 Nov. 2022, docs.google.com/presentation/d/1sgshVux_DLBBhZKoKJrq9l79a9B_2aTzmdnAtdFDHhc/edit#slide=id.p.






