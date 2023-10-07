import os
import time
from random import random

tab_ = "\t\t\t\t\t"  # global variable


def get_formatted_time():
    return time.strftime("%-I:%M %p")


def typing_animation(duration=2, num_dots=3):
    for _ in range(num_dots):
        print(f"{tab_}Typing" + "." * (_ + 1), end="\r")
        time.sleep(duration)
    print(" " * (num_dots + 7), end="\r")


def random_sleep():
    time.sleep(random.randint(1, 2))


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
