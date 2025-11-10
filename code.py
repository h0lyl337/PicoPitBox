import rotaryio
import time
import board
import usb_hid
import digitalio
import analogio
from adafruit_hid.keyboard import  Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from hid_gamepad import Gamepad
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import board
print(dir(board))


gamepad = Gamepad(usb_hid.devices)

encoder = rotaryio.IncrementalEncoder(board.GP14, board.GP15)

encoder_2 = rotaryio.IncrementalEncoder(board.GP11, board.GP10)

last_position = None

last_position_2 = None

m = Mouse(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

ax = analogio.AnalogIn(board.A0)
ay = analogio.AnalogIn(board.A1)

def map_range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

MAX_position = 10
MIN_POSITION = 1

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

### FUNCTOINALITIES ARE KEYBOARD , GAMEPAD, MOUSE_UP_DOWN, MOUSE_LEST_RIGHT, MOUSE_CLICK, MOUSEWHEEL ###

_BUTTON_1_FUNCTIONALITY = "GAMEPAD"
_BUTTON_2_FUNCTIONALITY = "GAMEPAD"
_BUTTON_3_FUNCTIONALITY = "GAMEPAD"
_BUTTON_4_FUNCTIONALITY = "GAMEPAD"
_BUTTON_5_FUNCTIONALITY = "GAMEPAD"
_BUTTON_6_FUNCTIONALITY = "GAMEPAD"
_BUTTON_7_FUNCTIONALITY = "GAMEPAD"
_BUTTON_8_FUNCTIONALITY = "GAMEPAD"
_BUTTON_9_FUNCTIONALITY = "GAMEPAD"


### ROTARY FUNCTIONALITIES ARE NUMKEYS, MOUSE_UP_DOWN , MOUSE_LEST_RIGHT, VOL_UP_DOWN ###


_BUTTON_1_PRESS = 1
_BUTTON_2_PRESS = 2
_BUTTON_3_PRESS = 3
_BUTTON_4_PRESS = 4
_BUTTON_5_PRESS = 5
_BUTTON_6_PRESS = 6
_BUTTON_7_PRESS = 7
_BUTTON_8_PRESS = 8
_BUTTON_9_PRESS = 9

_BUTTON_1_KEYPRESS = Keycode.G
_BUTTON_2_KEYPRESS = Keycode.TWO
_BUTTON_3_KEYPRESS = Keycode.ONE
_BUTTON_4_KEYPRESS = Keycode.X
_BUTTON_5_KEYPRESS = Keycode.ONE
_BUTTON_6_KEYPRESS = Keycode.ONE
_BUTTON_7_KEYPRESS = Keycode.ONE
_BUTTON_8_KEYPRESS = Keycode.ONE
_BUTTON_9_KEYPRESS = Keycode.W

#  PIN SETUP #

### ENCODER_1 BUTTON ###

rotary_button = digitalio.DigitalInOut(board.GP12)
rotary_button.direction = digitalio.Direction.INPUT
rotary_button.pull = digitalio.Pull.UP

### ENCODER_2 BUTTON ###

rotary_button_2 = digitalio.DigitalInOut(board.GP28)
rotary_button_2.direction = digitalio.Direction.INPUT
rotary_button_2.pull = digitalio.Pull.UP

### BUTTON_1 ###

button_1 = digitalio.DigitalInOut(board.GP0)
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.UP

### BUTTON_2 ###
button_2 = digitalio.DigitalInOut(board.GP2)
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.UP

### BUTTON_3 ###

button_3 = digitalio.DigitalInOut(board.GP3)
button_3.direction = digitalio.Direction.INPUT
button_3.pull = digitalio.Pull.UP

### BUTTON_4 ###

button_4 = digitalio.DigitalInOut(board.GP4)
button_4.direction = digitalio.Direction.INPUT
button_4.pull = digitalio.Pull.UP

### BUTTON_5 ###

button_5 = digitalio.DigitalInOut(board.GP5)
button_5.direction = digitalio.Direction.INPUT
button_5.pull = digitalio.Pull.UP

### BUTTON_6 ###

button_6 = digitalio.DigitalInOut(board.GP6)
button_6.direction = digitalio.Direction.INPUT
button_6.pull = digitalio.Pull.UP

### BUTTON_7 ###

button_7 = digitalio.DigitalInOut(board.GP7)
button_7.direction = digitalio.Direction.INPUT
button_7.pull = digitalio.Pull.UP

### BUTTON_8 ###

button_8 = digitalio.DigitalInOut(board.GP8)
button_8.direction = digitalio.Direction.INPUT
button_8.pull = digitalio.Pull.UP

### BUTTON_9 ###

button_9 = digitalio.DigitalInOut(board.GP9)
button_9.direction = digitalio.Direction.INPUT
button_9.pull = digitalio.Pull.UP


global _LEFT_ROTARY_FUNCTIONALITY
global _LEFT_ROTARY_FUNCTIONALITY_ORIGINAL
global _LEFT_ROTARY_FUNCTIONALITY_TOGGLE

_LEFT_ROTARY_FUNCTIONALITY = "VOL_UP_DOWN"
_LEFT_ROTARY_FUNCTIONALITY_TOGGLE = "NUMKEYS"
_LEFT_ROTARY_FUNCTIONALITY_ORIGINAL = _LEFT_ROTARY_FUNCTIONALITY

global _RIGHT_ROTARY_FUNCTIONALITY
global _RIGHT_ROTARY_FUNCTIONALITY_ORIGINAL
global _RIGHT_ROTARY_FUNCTIONALITY_TOGGLE

_RIGHT_ROTARY_FUNCTIONALITY = "NUMKEYS"
_RIGHT_ROTARY_FUNCTIONALITY_TOGGLE = "NUMKEYS"
_RIGHT_ROTARY_FUNCTIONALITY_ORIGINAL = _RIGHT_ROTARY_FUNCTIONALITY

### MAIN LOOP ###

while True:
    position = encoder.position

    position_2 = encoder_2.position

    kbd = Keyboard(usb_hid.devices)

    # Read analog values from the analog pins
    x_value = ax.value
    y_value = ay.value

    #print(y_value)
    gamepad.move_joysticks(
        x=map_range(ax.value, 0, 65535, -127, 127),
        y=map_range(ay.value, 0, 65535, -127, 127),
    )



    ### GAMEPAD BUTTON_1 PRESS ###


    if _BUTTON_1_FUNCTIONALITY == "GAMEPAD":
        while button_1.value == False:
            gamepad.press_buttons(_BUTTON_1_PRESS)
        gamepad.release_buttons(_BUTTON_1_PRESS)

    if _BUTTON_1_FUNCTIONALITY == "KEYBOARD":
        while button_1.value == False:
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_1_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_1_KEYPRESS)

#################

    while button_2.value == False:
        if _BUTTON_2_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_2_PRESS)
        gamepad.release_buttons(_BUTTON_2_PRESS)

        if _BUTTON_2_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_2_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_2_KEYPRESS)

#################

    while button_3.value == False:
        if _BUTTON_3_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_3_PRESS)
        gamepad.release_buttons(_BUTTON_3_PRESS)

        if _BUTTON_3_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_3_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_3_KEYPRESS)

#################

    while button_4.value == False:
        if _BUTTON_4_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_4_PRESS)
        gamepad.release_buttons(_BUTTON_4_PRESS)

        if _BUTTON_4_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_4_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_4_KEYPRESS)

#################

    while button_5.value == False:
        if _BUTTON_5_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_5_PRESS)
        gamepad.release_buttons(_BUTTON_5_PRESS)

        if _BUTTON_5_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_5_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_5_KEYPRESS)

#################

    while button_6.value == False:
        if _BUTTON_6_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_6_PRESS)
        gamepad.release_buttons(_BUTTON_6_PRESS)

        if _BUTTON_6_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_6_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_6_KEYPRESS)

#################

    while button_7.value == False:
        if _BUTTON_7_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_7_PRESS)
        gamepad.release_buttons(_BUTTON_7_PRESS)

        if _BUTTON_7_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_7_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_7_KEYPRESS)

#################

    while button_8.value == False:
        if _BUTTON_8_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_8_PRESS)
        gamepad.release_buttons(_BUTTON_8_PRESS)

        if _BUTTON_8_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_8_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_8_KEYPRESS)

#################

    while button_9.value == False:
        if _BUTTON_9_FUNCTIONALITY == "GAMEPAD":
            gamepad.press_buttons(_BUTTON_9_PRESS)
        gamepad.release_buttons(_BUTTON_9_PRESS)

        if _BUTTON_9_FUNCTIONALITY == "KEYBOARD":
            kbd = Keyboard(usb_hid.devices)
            kbd.press(_BUTTON_9_KEYPRESS)
            time.sleep(0.5)
        kbd.release(_BUTTON_9_KEYPRESS)

#################


    ### ROTORY 1 BUTTON PRESS ###
    if rotary_button.value == False:
        global _LEFT_ROTARY_FUNCTIONALITY
        global _LEFT_ROTARY_FUNCTIONALITY_ORIGINAL
        global _LEFT_ROTARY_FUNCTIONALITY_TOGGLE

        if _LEFT_ROTARY_FUNCTIONALITY == _LEFT_ROTARY_FUNCTIONALITY_ORIGINAL:
            _LEFT_ROTARY_FUNCTIONALITY = _LEFT_ROTARY_FUNCTIONALITY_TOGGLE
        else:
            _LEFT_ROTARY_FUNCTIONALITY = _LEFT_ROTARY_FUNCTIONALITY_ORIGINAL

        time.sleep(.5)
        print(_LEFT_ROTARY_FUNCTIONALITY)

    ### ROTORY 2 BUTTON PRESS ###

    if rotary_button_2.value == False:
        global _RIGHT_ROTARY_FUNCTIONALITY
        global _RIGHT_ROTARY_FUNCTIONALITY_ORIGINAL
        global _RIGHT_ROTARY_FUNCTIONALITY_TOGGLE

        if _RIGHT_ROTARY_FUNCTIONALITY == _RIGHT_ROTARY_FUNCTIONALITY_ORIGINAL:
            _RIGHT_ROTARY_FUNCTIONALITY = _RIGHT_ROTARY_FUNCTIONALITY_TOGGLE
        else:
            _RIGHT_ROTARY_FUNCTIONALITY = _RIGHT_ROTARY_FUNCTIONALITY_ORIGINAL

        time.sleep(.5)
        print(_RIGHT_ROTARY_FUNCTIONALITY)


    if _LEFT_ROTARY_FUNCTIONALITY == "NUMKEYS":

        if last_position is None or position != last_position:
            print(position)
            led.value = True
            if position < 0 :
                encoder.position = 1
            if position >= 10:
                encoder.position = 10

            if position == 1:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.ONE)
                                time.sleep(0.09)
                                kbd.release(Keycode.ONE)
                                led.value = False

            if position == 2:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.TWO)
                                time.sleep(0.09)
                                kbd.release(Keycode.TWO)
                                led.value = False

            if position == 3:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.THREE)
                                time.sleep(0.09)
                                kbd.release(Keycode.THREE)
                                led.value = False

            if position == 4:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.FOUR)
                                time.sleep(0.09)
                                kbd.release(Keycode.FOUR)
                                led.value = False

            if position == 5:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.FIVE)
                                time.sleep(0.09)
                                kbd.release(Keycode.FIVE)
                                led.value = False

            if position == 6:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.SIX)
                                time.sleep(0.09)
                                kbd.release(Keycode.SIX)
                                led.value = False

            if position == 7:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.SEVEN)
                                time.sleep(0.09)
                                kbd.release(Keycode.SEVEN)
                                led.value = False

            if position == 8:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.EIGHT)
                                time.sleep(0.09)
                                kbd.release(Keycode.EIGHT)
                                led.value = False

            if position == 9:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.NINE)
                                time.sleep(0.09)
                                kbd.release(Keycode.NINE)
                                led.value = False

            if position == 10:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.ZERO)
                                time.sleep(0.09)
                                kbd.release(Keycode.ZERO)
                                led.value = False

    if _LEFT_ROTARY_FUNCTIONALITY == "MOUSE_UP_DOWN":
        if last_position is None or position != last_position:
            print(position_2)

            if position < 0:
                encoder.position = 0
                m.move(0, 25, 0)

            if position > 1:
                encoder.position = 1
                m.move(0, -25, 0)

    if _LEFT_ROTARY_FUNCTIONALITY == "MOUSE_LEFT_RIGHT":
        if last_position is None or position != last_position:
            print(position_2)

            if position < 0:
                encoder.position = 0
                m.move(-25, 0, 0)

            if position > 1:
                encoder.position = 1
                m.move(25, 0, 0)



    if _LEFT_ROTARY_FUNCTIONALITY == "VOL_UP_DOWN":
            if position < 0:
                encoder.position = 0
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)

            if position >1:
                encoder.position = 1
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)

    if _LEFT_ROTARY_FUNCTIONALITY == "MOUSEWHEEL":
        if last_position is None or position != last_position:
            print(position_2)

            if position < 0:
                encoder.position = 0
                m.move(25, 0, 1)

            if position > 1:
                encoder.position = 1
                m.move(-25, 0, -1)


########################################################################

    if _RIGHT_ROTARY_FUNCTIONALITY == "NUMKEYS":

        if last_position_2 is None or position != last_position_2:
            print(position)

            led.value = True
            if position_2 < 0 :
                encoder_2.position = 1
            if position_2 >= 10:
                encoder_2.position = 10


            if position_2 == 1:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                time.sleep(0.09)
                                kbd.release(Keycode.ONE)
                                led.value = False

            if position_2 == 2:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.TWO)
                                time.sleep(0.09)
                                kbd.release(Keycode.TWO)
                                led.value = False

            if position_2 == 3:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.THREE)
                                time.sleep(0.09)
                                kbd.release(Keycode.THREE)
                                led.value = False

            if position_2 == 4:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.FOUR)
                                time.sleep(0.09)
                                kbd.release(Keycode.FOUR)
                                led.value = False

            if position_2 == 5:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.FIVE)
                                time.sleep(0.09)
                                kbd.release(Keycode.FIVE)
                                led.value = False

            if position_2 == 6:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.SIX)
                                time.sleep(0.09)
                                kbd.release(Keycode.SIX)
                                led.value = False

            if position_2 == 7:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.SEVEN)
                                time.sleep(0.09)
                                kbd.release(Keycode.SEVEN)
                                led.value = False

            if position_2 == 8:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.EIGHT)
                                time.sleep(0.09)
                                kbd.release(Keycode.EIGHT)
                                led.value = False

            if position_2 == 9:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.NINE)
                                time.sleep(0.09)
                                kbd.release(Keycode.NINE)
                                led.value = False

            if position_2 == 10:
                                # Initialize Keyboard
                                kbd = Keyboard(usb_hid.devices)
                                # Press and release CapsLock.
                                kbd.press(Keycode.ZERO)
                                time.sleep(0.09)
                                kbd.release(Keycode.ZERO)
                                led.value = False

    if _RIGHT_ROTARY_FUNCTIONALITY == "MOUSE_UP_DOWN":
        if last_position_2 is None or position_2 != last_position_2:
            print(position_2)

            if position_2 < 0:
                encoder_2.position = 0
                m.move(0, 25, 0)

            if position_2 > 1:
                encoder_2.position = 1
                m.move(0, -25, 0)


    if _RIGHT_ROTARY_FUNCTIONALITY == "VOL_UP_DOWN":
            if position_2 < 0:
                encoder_2.position = 0
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)

            if position >1:
                encoder.position = 1
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)

    if _RIGHT_ROTARY_FUNCTIONALITY == "MOUSEWHEEL":
        if last_position is None or position != last_position:
            print(position_2)

            if position_2 < 0:
                encoder_2.position = 0
                m.move(25, 0, 1)

    if _RIGHT_ROTARY_FUNCTIONALITY == "MOUSE_LEFT_RIGHT":
            if position_2 > 1:
                encoder_2.position = 1
                m.move(-25, 0, -1)



    last_position = position
    last_position_2 = position_2
