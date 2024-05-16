from machine import Pin, ADC
import time

# Initialize the MQ-2 sensor on GPIO pin 26
mq2 = ADC(Pin(26))

# Calibration values for MQ-2 sensor (These values may vary depending on the sensor and environment)
Ro = 10.0  # resistance in clean air
Rl = 1.0   # resistance in gas

def get_gas_resistance(adc_value):
    return (1023 / adc_value - 1) * (Ro / 10)

def get_gas_ppm(gas_resistance):
    return (gas_resistance / Rl) * 100

while True:
    # Read the analog value from the MQ-2 sensor
    adc_value = mq2.read_u16()

    # Calculate gas resistance
    gas_resistance = get_gas_resistance(adc_value)

    # Calculate gas ppm
    gas_ppm = get_gas_ppm(gas_resistance)

    # Print the equivalent ppm values for various gases
    print("Smoke: {:.1f} ppm - LPG: {:.1f} ppm - Methane: {:.1f} ppm - Hydrogen: {:.1f} ppm".format(
        gas_ppm, gas_ppm * 0.5, gas_ppm * 1.5, gas_ppm * 2.0))

    # Wait for 1 second before the next reading
    time.sleep(1)