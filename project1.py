from machine import Pin
from time import sleep



led = Pin(14, Pin.OUT)    # 22 number in is Output
push_button = Pin(13, Pin.IN)  # 23 number pin is input

while True:
  
  logic_state = push_button.value()
  if logic_state == True:     # if pressed the push_button
      led.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led.value(0)             # led will turn OFF