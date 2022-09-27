import mido
state = False
# set light state to off by default

with mido.open_input() as inport:
    for msg in inport:
        if msg.type == 'note_on':
            if state == False:
                print('light on')
                state = True
            else:
                pass
        if msg.type == 'note_off':
            if state == True:
                print('light off')
                state = False
            if state == False:
                pass
