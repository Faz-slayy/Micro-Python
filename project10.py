import machine
import time
import os
import dht
import sdcard

# Initialize the DHT11 sensor
d = dht.DHT11(machine.Pin(14))

# Initialize the light sensor
light_sensor = machine.ADC(26)

# Initialize the MQ-2 sensor
mq2 = machine.ADC(27)

# Initialize the SD card
spi = machine.SPI(1, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))
sd = sdcard.SDCard(spi, machine.Pin(4))
os.mount(sd, '/sd')

# Continuously log sensor data
while True:
    try:
        # Read the DHT11 sensor
        d.measure()
        temp = d.temperature()
        hum = d.humidity()

        # Read the light sensor
        light_value = light_sensor.read_u16()

        # Read the MQ-2 sensor
        mq2_value = mq2.read_u16()

        # Log the sensor data
        with open('/sd/log.txt', 'a') as f:
            f.write('{},{},{},{},{}\n'.format(time.time(), temp, hum, light_value, mq2_value))

    except Exception as e:
        print('An error occurred: {}'.format(e))

    # Wait for 1 second before the next reading
    time.sleep(1)

