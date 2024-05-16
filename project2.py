from machine import Pin
import time
import _thread
import dht

# FAN
fan = Pin(32, Pin.OUT)
fan.off()

# DHT11
d = dht.DHT11(Pin(23))
t = 0
h = 0

def check_temp():
    print('Check Temp Starting...')
    global t
    global h
    while True:
        try:
            d.measure()
            time.sleep(2)
            t = d.temperature()
            h = d.humidity()
            temp = 'Temp: {:.0f} C'.format(t)
            humid = 'Humidity: {:.0f} %'.format(h)
            print('DHT11:', t, h)
            time.sleep(5)
        except:
            pass


# RUN
global fan_status
fan_status = 'OFF'

def show_lcd():
    while True:
        try:
            temp = 'Temp: {:.0f} C'.format(t)
            humid = 'Humidity: {:.0f} %'.format(h)
            fan_s = 'FAN : {:}'.format(fan_status)
            lcd.clear()
            lcd.putstr(fan_s)
            time.sleep(2)
            lcd.clear()
            lcd.putstr(temp)
            lcd.move_to(0,1)
            lcd.putstr(humid)
            time.sleep(2)
        except:
            pass

def auto_fan():
    global fan_status
    while True:
        if t > 30:
            time.sleep(1)
            fan.on()
            fan_status = 'ON (AUTO)'
            time.sleep(10)    # TURN ON FAN 10 sec
            fan.off()
            fan_status = 'OFF (AUTO)'
            time.sleep(10)
        else:
            pass

_thread.start_new_thread(check_temp,())
_thread.start_new_thread(auto_fan,())