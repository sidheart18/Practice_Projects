import datetime
import time

print("\n--- Reminder / Alarm Program ---")
alarm = input("Enter time in HH:MM format (24hr): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm:
        print("\nAlarm Time! Reminder Alert!")
        break
    time.sleep(1)
