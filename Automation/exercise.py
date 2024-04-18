from collections import deque
from tkinter import Button
import keyboard
import pyautogui as auto


# Find Position
# print(auto.position())  #(1582, 79)

# Click
# auto.click(1582, 79, clicks=1, button='left', duration=0, interval=0)

# Double Click
# auto.doubleClick(50, 50, button='left', duration=0, interval=0)

# Move Mouse
# auto.move(50, 50, 1)

# Move To
# auto.moveTo(50, 50, 1)

# Drag (specify)
# auto.drag(50, 50, duration=1)

# Drag To
# auto.dragTo(50, 50, duration=1)

# Use Various Keys
# Copy
# auto.hotkey('ctrl', 'c')

# Write
# auto.typewrite("Hello World")

# Click Enter Key
# auto.typewrite(["enter"])
# auto.press('enter')

# Display Mouse Position
# auto.displayMousePosition()
# (1684, 65)

# Mouse Info
# auto.mouseInfo()
# (83, 83, 83)

# while keyboard.is_pressed('q') == False:
#     if auto.pixel(1190, 385)[0] == 83:
#         auto.typewrite(['space'])

# ScreenShot
# auto.screenshot('c:\\users\Yousef Sayed\desktop\Hi.png')

# dis = 100
# while dis > 0:
#     auto.drag(dis, -dis, duration=0.5)
#     dis -= 5
#     auto.drag(-dis, -dis, duration=0.5)
#     dis -= 5
#     auto.drag(-dis, dis, duration=0.5)
#     dis -= 5
#     auto.drag(dis, dis, duration=0.5)
#     dis -= 5

# Press
# auto.press(['H', 'i'])

# Keys
# print(auto.KEYBOARD_KEYS)

# To Know The Key
# print(auto.isValidKey('cntlr'))

# Is Shift
# print(auto.isShiftCharacter('A'))
# print(auto.isShiftCharacter('a'))

# auto.hotkey('ctrl', 't')

# Dino
# while True:
#     x = auto.position()
#     p = auto.pixel(x[0], x[1])
#     if (p[0] == p[1]) and (p[1] == p[2]) and (p[2] == 83):
#         auto.hotkey('up')

# auto.typewrite('print("Hello World")')

# Alert
# auto.alert(
#     'Mission Complete',
#     title='Alert', 
#     button='Accept', Return Accept
#     timeout=2000
#     # icon='Path of Image',
#     )

# Confirm
# auto.confirm(
#     'Hello World',
#     title= 'Hi',
#     buttons=('Accept', 'No'), # Return What I Choose
# )

# Counter
# auto.countdown(20)

# Prompt
# auto.prompt(
    # 'Write Anything',
    # default='Type Here',
    #title
    #timeout
    # )

# Password
# auto.password(
#     text='Password',
#     default='Password',
#     title='Login',
#     mask='#'
# )

# auto.write('Hello World', interval=0.2)

# auto.click('Hi.png')

# auto.moveTo(50, 50, duration=1)
# auto.move(50, 50, duration=1)

# auto.displayMousePosition()