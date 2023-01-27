import schedule
import time

def remainder():
    print("Remainder: Don't forget to do your task!")

schedule.every().day.at("09:00").do(remainder)

while True:
    schedule.run_pending()
    time.sleep(1)
