import re
from tkinter.constants import NONE
from PIL.ImageOps import grayscale
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateOnScreen(
    "C:/Users/Yousef Sayed/Desktop/Coding/Python/Bot/Whatsapp/smile_attachment.png", grayscale=True,  confidence=.5)

x = position1[0]
y = position1[1]


def get_message():  # Get Message
    global x, y

    position = pt.locateOnScreen(
        "C:/Users/Yousef Sayed/Desktop/Coding/Python/Bot/Whatsapp/smile_attachment.png", grayscale=True, confidence=.5)
    x = position[0]
    y = position[1]

    pt.moveTo(x, y)  # duration = 0.05 For Mac Users
    pt.moveTo(x + 90, y - 80)
    pt.tripleClick()

    # To Copy
    # pt.rightClick()
    # pt.moveRel(-10, -150)
    # pt.click()

    pt.hotkey("ctrl", "c")
    message = pyperclip.paste()
    print("Message Received: " + message)

    return message


def post_response(message):  # Posts
    global x, y

    position = pt.locateOnScreen(
        "C:/Users/Yousef Sayed/Desktop/Coding/Python/Bot/Whatsapp/smile_attachment.png", grayscale=True, confidence=.5)
    x = position[0]
    y = position[1]

    pt.moveTo(x + 200, y + 20)
    pt.click()
    pt.typewrite(message)
    # pt.hotkey("ctrl", "v")

    # pt.typewrite("/n")  # Work Only with English


def process_response(message):  # Process Response
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't Ask Me Any Questions!"
    else:
        if random_no == 0:
            return "That's Cool!"
        elif random_no == 1:
            return "Remember To Subscribe!"
        else:
            return "I Want To Eat Something."


def check_new_messages():
    x1 = x + 70
    y1 = y - 70
    pt.moveTo(x1, y1)

    while True:
        try:
            position = pt.locateOnScreen(
                "C:/Users/Yousef Sayed/Desktop/Coding/Python/Bot/Whatsapp/green_dot.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No New Messages")

        if pt.pixelMatchesColor(int(x1), int(y1), (255, 255, 255), tolerance=10):
            print("is white")
            process_message = process_response(get_message())
            post_response(process_message)

        else:
            print("No New Messages Yet...")

        sleep(5)

check_new_messages()
