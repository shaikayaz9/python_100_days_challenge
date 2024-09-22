import time
from plyer import notification

def drink_water_reminder():
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink water!",
            timeout=10  # Notification stays for 10 seconds
        )
        time.sleep(60*60)  # Remind every hour 

if __name__ == "__main__":
    drink_water_reminder()