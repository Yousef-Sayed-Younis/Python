from plyer import notification
import time

title = 'Your Assistant'
message = 'Hey Yousef, Take A Break \u2764\ufe0f'

while True:
    time.sleep(1200)
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Yousef Sayed\Downloads\Dapino-Girl-In-A-Bunny-Suit-Girl-bunny-share.ico",
        timeout = 10, 
    )