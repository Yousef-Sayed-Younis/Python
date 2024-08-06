import random
import time
# help me show the snake on the screen and read the inputs of user
import curses

# Screen
s = curses.initscr()
curses.curs_set(0)
time.sleep(100)

# Screen width
sh, sw = s.getmaxyx()

# Window in my screen
w = curses.newwin(sh, sw, 0, 0)

# Make window ready to have inputs from user
w.keypad(1)

# Refresh the window every 100 ms
w.timeout(100)

# Save the initail position of snake in the middle and making the deviviton int 
# snk_x = sw//4
# snk_y = sh//2

# # Make the Snake
# snake = [
#     [snk_y, snk_x],
#     [snk_y, snk_x-1],
#     [snk_y, snk_x-2],
# ]

# # Make the food
# food = [sh//2, sw//2]

# # Make the food apears on the screen 
# w.addch(food[0], food[1], curses.ACS_PI)

# # Make the initial direction of the snake to the right
# key = curses.KEY_RIGHT

# # Make the direction of the snake
# while True:
# # get the input of direction
#     next_key = w.getch
#     key = key if next_key == -1 else next_key

# # Make the border of the screen 
#     if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[1: ]:
#         # Close the screen
#         curses.endwin()
#         quit()
    
#     # Make the head of the snake
#     new_head = [snake[0][0], snake[0][1]]

#     # Make the direction of the head of the snake
#     if key == curses.KEY_DOWN:
#         new_head[0] += 1
#     if key == curses.KEY_UP:
#         new_head[0] -= 1
#     if key == curses.KEY_RIGHT:
#         new_head[0] -= 1
#     if key == curses.KEY_LEFT:
#         new_head[0] += 1

#     snake.insert(0, new_head)

#     # See if the snake eat the food or not
#     if snake[0] == food:
#         food = None
#         # make the food apears in any place when its eated
#         while food is None:
#             nf = [
#                 random.randint(1, sh-1),
#                 random.randint(1, sw-1),
#             ]
#             # make the food not apear in the snake
#             food = nf if nf not in snake else None
#         # Make the food apear on the screen
#         w.addch(food[0], food[1], curses.ACS_PI)
#     else:
#         tail = snake.pop()
#         w.addch(tail[0], tail[1], ' ')

#     # Make the snake bigger
#     w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOAR)
