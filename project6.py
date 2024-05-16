import machine
import time

# Set up the light sensor
light_sensor = machine.ADC(machine.Pin(26))

# Set up the LED
led = machine.Pin(15, machine.Pin.OUT)

while True:
    # Read the light level from the sensor
    light_level = light_sensor.read_u16()

    # If the light level is below a threshold, turn on the LED
    if light_level < 10000:
        led.on()
    else:
        led.off()

    # Wait for 1 second before the next reading
    time.sleep(1)