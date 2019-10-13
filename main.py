from time import sleep
from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
delay = 0.009 * pow(2, 0.062854 * random.uniform(35, 55))


def controlKeyboard():
    for char in "":
        
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(float(delay))
        print(char)
        print(delay)

sleep(2); controlKeyboard()
    
