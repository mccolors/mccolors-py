#!/usr/bin/python3

from .mc import codes


def mcwrite(text, reset_all=True):
    """
    Allows you to write with colors in 
    the terminal using the color codes

    :param text: Text
    :param reset_all: Boolean value that decides whether to reset the text color at the end.
    """

    for code in codes.items():
        text = text.replace(f'&{code[0]}', code[1]
                  ).replace(f'§{code[0]}', code[1])

    if reset_all:
        print(f'{text}\033[0m')
    
    else:
        print(text)
