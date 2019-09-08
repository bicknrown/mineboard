#################################################################
#           midi keyboard to HID keyboard emulator              #
#           Authors: Adam Russell, Nick Brown                   #
#           github: https://github.com/bicknrown/mineboard      #
#################################################################

import pygame.midi

piano_list = []  # creates list for midi input (49)
for i in range(49):
    i = 36 + i
    piano_list.append(i)


def letter_range(start, stop="{", step=1):  # creates list of keyboard letters
    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)


type_list = list(letter_range("a", "z"))  # also creates list of keyboard letters
type_list.append('z')
print(type_list)


def readInput(input_device):  # read midi device input
    while True:
        if input_device.poll():
            event = input_device.read(1)
            print(event)


if __name__ == '__main__':  # also reads midi device input
    pygame.midi.init()
    my_input = pygame.midi.Input(1)
    readInput(my_input)
