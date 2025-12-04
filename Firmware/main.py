import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

class ShiftLock:
    def __init__(self):
        self.active = False

    def toggle(self):
        self.active = not self.active
        if self.active:
            return [Press(KC.LSHIFT)]
        else:
            return [Release(KC.LSHIFT)]


shift_lock = ShiftLock()

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
        ),

        KC.MACRO(lambda: shift_lock.toggle()),

        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            KC.MACRO("code\n"),
        ),

        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            KC.MACRO("https://www.google.com"),
        ),

        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.C),
            Release(KC.LCTRL),
        ),

        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.V),
            Release(KC.LCTRL),
        ),
    ]
]

if __name__ == '__main__':
    keyboard.go()