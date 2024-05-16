from machine import Pin, ADC
import utime
from dht import DHT11

# Initialize sensors and pins
light_sensor = ADC(Pin(26))
smoke_sensor = ADC(Pin(27))
fan_pin = Pin(2, Pin.OUT)
led_pin = Pin(1, Pin.OUT)
dht11 = DHT11(Pin(14))

# Control the fan based on smoke sensor value
def control_fan(value):
    if value > 2000:  # Adjust this threshold based on your needs
        fan_pin.value(1)  # Turn on the fan
    else:
        fan_pin.value(0)  # Turn off the fan

# Control the LED based on light sensor value
def control_led(value):
    if value > 3000:  # Adjust this threshold based on your needs
        led_pin.value(1)  # Turn on the LED
    else:
        led_pin.value(0)  # Turn off the LED

# Control the exhaust fan based on the temperature read by the DHT11 sensor
def control_exhaust_fan(temp):
    if temp > 25:  # Adjust this threshold based on your needs
        exhaust_fan_pin.value(1)  # Turn on the exhaust fan
    else:
        exhaust_fan_pin.value(0)  # Turn off the exhaust fan

# Main loop
while True:
    light_value = light_sensor.read_u16()
    smoke_value = smoke_sensor.read_u16()
    control_fan(smoke_value)
    control_led(light_value)
    dht11.measure()
    control_exhaust_fan(dht11.temperature())
    utime.sleep_ms(200)