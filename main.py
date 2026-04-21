from utils.sensor import read_sensors
import time
import csv
import os

os.makedirs("data", exist_ok=True)

TEMP_LIMIT = 30
HUM_LIMIT = 70
LIGHT_LIMIT = 300

with open("data/logs.csv", "a", newline="") as file:
    writer = csv.writer(file)

    while True:
        temp, hum, light = read_sensors()

        print(f"Temp: {temp}°C | Humidity: {hum}% | Light: {light}")
        writer.writerow([temp, hum, light])

        if temp > TEMP_LIMIT:
            print("⚠️ High Temperature Alert!")
        if hum > HUM_LIMIT:
            print("⚠️ High Humidity Alert!")
        if light < LIGHT_LIMIT:
            print("⚠️ Low Light Detected!")

        print("-" * 40)
        time.sleep(2)
