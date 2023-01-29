import json
import datetime as dt
import time
from plyer import notification


with open("schedule.json") as s:
    data = json.load(s)

# current day in string
current_day = dt.datetime.today().strftime("%A")


# takes string time and converts to time object
def time_convert(t):
    t = t + ":00"
    return dt.datetime.strptime(t, "%X").time()


# finds time remaining until a specified time (t)
def wait_time(t):
    current_time = dt.datetime.now().time()
    target_time = time_convert(t)
    td1 = dt.timedelta(hours=current_time.hour, minutes=current_time.minute, seconds=current_time.second)
    td2 = dt.timedelta(hours=target_time.hour, minutes=target_time.minute, seconds=target_time.second)
    return (td2 - td1).total_seconds() - 300.00


def send_notification(message):
    notification.notify(
        title='Online Classes',
        message=message,
        app_icon=None,
        timeout=10,  # seconds
    )


for a, b in data[current_day].items():
    wait = wait_time(a)
    if wait < 0.00:
        continue
    else:
        text1 = f"{b} begins in 5 minutes at {a}."
        text2 = f"{b} has started."

        print("alarm at: " + a, end=", ")
        print("time to wait in seconds:  " + str(wait))

        time.sleep(wait)
        send_notification(text1)

        time.sleep(300)
        send_notification(text2)
