import random

def read_sensors():
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 90)
    light = random.randint(100, 500)
    return temperature, humidity, light
