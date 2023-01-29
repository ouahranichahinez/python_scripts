import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "HEY !",
            message = "IT WILL BE ALLRIGHT, JUST SMILE.. <3",
            timeout = 15
        )
        time.sleep(5000)
