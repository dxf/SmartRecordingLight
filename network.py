from pymidi import server
import asyncio # Required for kasa library
from kasa import SmartPlug # Smart Plug Control
from blinkt import set_pixel, set_brightness, show, clear # Blinkt LED board controller


# plug = SmartPlug("127.0.0.1")

class MIDIHandler(server.Handler):
    def on_peer_connected(self, peer):
        print('Peer connected: {}'.format(peer))

    def on_peer_disconnected(self, peer):
        print('Peer disconnected: {}'.format(peer))

    def on_midi_commands(self, peer, command_list):
        for command in command_list:
            if command.command == 'note_on':
                key = command.params.key
                velocity = command.params.velocity
                if velocity == 127:
                    #asyncio.run(plug.turn_on) # Turn plug on
                    print('light on')
                    clear()
                    set_brightness(0.2) # way too bright
                    for i in range(8):
                        set_pixel(i,255,0,0) # Set 8 pixels of LED board to red
                    show()
                if velocity == 0:
                    #asyncio.run(plug.turn_off)
                    print('light off')
                    clear()
                    set_brightness(0.2) # way too bright
                    for i in range(8):
                        set_pixel(i,255,255,255) # Set 8 pixels of LED board to white
                    show()
rxServer = server.Server([('0.0.0.0', 5051)])
rxServer.add_handler(MIDIHandler())
rxServer.serve_forever()