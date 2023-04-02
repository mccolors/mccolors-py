#!/usr/bin/python3

from .mc import codes


def mcreplace(text, reset_all=True):
    """
    Allows you to replace the color codes
    with their respective colors.

    :param text: Text
    :param reset_all: Boolean value that decides whether to reset the text color at the end.
    :return: Colored text
    """

    for code in codes.items():
        text = text.replace(f'&{code[0]}', code[1]
                  ).replace(f'§{code[0]}', code[1])

    if reset_all:
        return(f'{text}\033[0m')
    
    else:
        return(text)
