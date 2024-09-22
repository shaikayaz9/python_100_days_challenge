import time
from plyer import notification

def drink_water_reminder():
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to stay hydrated! Drink a glass of water.",
            timeout=10
        )
        time.sleep(60*60)  # Remind every hour

if __name__ == "__main__":
    drink_water_reminder()