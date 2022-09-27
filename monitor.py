import mido # MIDI library
import asyncio # Required for kasa library
from kasa import SmartPlug # Smart Plug Control
from blinkt import set_pixel, set_brightness, show, clear # Blinkt LED board controller

plug = SmartPlug("127.0.0.1")

state = False
# set light state to off by default

with mido.open_input() as inport:
    # No filtering is done on the MIDI input, because the only MIDI signal being sent to this input is the output of the Logic recording light.
    for msg in inport:
        if msg.type == 'note_on':
            if state == False: # Checks light is off before triggering on signal
                asyncio.run(plug.turn_on) # Turn plug on
                print('light on')
                for i in range(8):
                    set_pixel(i,255,0,0) # Set 8 pixels of LED board to red
                state = True
            else:
                pass
        if msg.type == 'note_off':
            if state == True: # Checks light is off before triggering off signal
                asyncio.run(plug.turn_off)
                print('light off')
                for i in range(8):
                    set_pixel(i,255,255,255) # Set 8 pixels of LED board to white
                state = False
            if state == False:
                pass