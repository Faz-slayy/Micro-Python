import machine
import utime

# Initialize an ADC object on GPIO pin 26 for the MQ2 sensor
mq2_AO = machine.ADC(14)

# Initialize a digital output on GPIO pin 15 for the relay
relay = machine.Pin(15, machine.Pin.OUT)

# Set the relay to an initial state of off
relay.value(0)

while True:
    # Read the analog value from the MQ2 sensor
    value = mq2_AO.read_u16()

    # If the gas concentration is above a certain threshold, turn on the relay
    if value > 3000:  # adjust this value based on your sensor's output
        relay.value(1)
        print("Gas detected! Relay turned on.")
    else:
        relay.value(0)
        print("No gas detected. Relay turned off.")

    # Wait for 200 milliseconds before taking the next reading
    utime.sleep_ms(200)