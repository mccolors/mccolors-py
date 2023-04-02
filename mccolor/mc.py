#!/usr/bin/python3

from .ansi import Foreground, Util

codes = {
    '0': Foreground.BLACK,
    '1': Foreground.BLUE,
    '2': Foreground.GREEN,
    '3': Foreground.CYAN,
    '4': Foreground.RED,
    '5': Foreground.MAGENTA,
    '6': Foreground.YELLOW,
    '7': Foreground.LIGHTBLACK_EX,
    '8': Util.DIM + Foreground.LIGHTBLACK_EX,
    '9': Foreground.LIGHTBLUE_EX,
    'a': Foreground.LIGHTGREEN_EX,
    'b': Foreground.LIGHTCYAN_EX,
    'c': Foreground.LIGHTRED_EX,
    'd': Util.BOLD + Foreground.LIGHTMAGENTA_EX,
    'e': Foreground.LIGHTYELLOW_EX,
    'f': Foreground.WHITE,
    'k': Util.OBFUSCATED,
    'l': Util.BOLD,
    'm': Util.STRIKETHROUGH,
    'n': Util.UNDERLINE,
    'o': Util.ITALIC,
    'r': Util.RESET_ALL,
    'x': ''
}