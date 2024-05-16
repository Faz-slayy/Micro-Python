import machine
import utime
import dht

try:
    # Initialize a DHT11 object on GPIO pin 16
    dht11 = dht.DHT11(machine.Pin(16))

    # Initialize an ADC object on GPIO pin 26 for the MQ2 sensor
    mq2_AO = machine.ADC(14)

    # Initialize an ADC object on GPIO pin 27 for the light sensor
    light_AO = machine.ADC(27)

    while True:
        try:
            # Read the temperature and humidity from the DHT11 sensor
           dht11.measure()
           temp = dht11.temperature()
            hum = dht11.humidity()

            # Read the analog value from the MQ2 sensor
            mq2_value = mq2_AO.read_u16()

            #Read the analog value from the light sensor
           light_value = light_AO.read_u16()

          #Print the sensor readings
          print("Temperature: {:.1f}°C, Humidity: {}%, Gas: {}, Light: {}".format(temp, hum, mq2_value, light_value))
           
        except Exception as e:
            print("Error reading from sensors: ", e)

        # Wait for 2 seconds before taking the next reading
        utime.sleep(2)

except Exception as e:
    print("Error initializing sensors: ", e)
