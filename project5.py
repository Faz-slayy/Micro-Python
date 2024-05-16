import machine
import time

# Set up the soil moisture sensor
moisture_sensor = machine.ADC(machine.Pin(26))

# Set up the relay
relay = machine.Pin(15, machine.Pin.OUT)

# Set the threshold moisture level
threshold = 400

while True:
    # Read the moisture level from the sensor
    moisture_level = moisture_sensor.read_u16()

    # If the moisture level is below the threshold, turn on the relay
    if moisture_level < threshold:
        relay.on()
    else:
        relay.off()

    # Wait for 1 second before the next reading
    time.sleep(1)