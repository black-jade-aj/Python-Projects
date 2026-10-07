import time
import winsound

seconds = int(input("Enter the time in seconds: "))
print(f"Alarm set for {seconds} seconds.")
time.sleep(seconds)
winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms    