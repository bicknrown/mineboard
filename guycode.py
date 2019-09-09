#################################################################
#           midi keyboard to HID keyboard emulator              #
#           Authors: Adam Russell, Nick Brown                   #
#           github: https://github.com/bicknrown/mineboard      #
#################################################################

import pygame.midi
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()
piano_list = []  # creates list for midi input (49)
for i in range(49):
    i = 36 + i
    piano_list.append(i)  # piano input list
number_list = []
for i in range(10):
    i = i
    number_list.append(str(i))


def letter_range(start, stop="{", step=1):  # creates list of keyboard letters
    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)


z_list = ['z']

add_list = [',', '.', '/', ';', "'", '[', ']', '-', Key.space, Key.shift_l, Key.esc, Key.ctrl, Key.enter]

type_list = list(letter_range("a", "z")) + z_list + number_list + add_list  # also creates list of keyboard letters


def readInput(input_device):  # read midi device input
    while True:
        if input_device.poll():
            event = input_device.read(1)
            if event[0][0][2] != 0:
                keyboard.press(type_list[piano_list.index(event[0][0][1])])
            if event[0][0][2] == 0:
                keyboard.release(type_list[piano_list.index(event[0][0][1])])


if __name__ == '__main__':  # also reads midi device input
    pygame.midi.init()
    my_input = pygame.midi.Input(1)
    readInput(my_input)
