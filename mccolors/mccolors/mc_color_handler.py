from .mc import minecraft_colors, minecraft_formatting


def mcwrite(text, reset_all=True):
    """
    Allows you to write with colors in 
    the terminal using the color codes

    :param text: Text
    :param reset_all: Boolean value that decides whether to reset the text color at the end.
    """

    for code, color_code in minecraft_colors.items():
        text = text.replace(f'&{code}', f'&r{color_code}'
                    ).replace(f'§{code}', f'&r{color_code}')

    for code, format_code in minecraft_formatting.items():
        text = text.replace(f'&{code}', format_code
                    ).replace(f'§{code}', format_code)

    if reset_all:
        text += '\033[0m'

    print(text)
    return text


def mcreplace(text, reset_all=True):
    """
    Allows you to replace the color codes
    with their respective colors.

    :param text: Text
    :param reset_all: Boolean value that decides whether to reset the text color at the end.
    :return: Colored text
    """

    for code, color_code in minecraft_colors.items():
        if f'&{code}' in text or f'§{code}' in text:
            text = text.replace(f'&{code}', f'&r{color_code}'
                        ).replace(f'§{code}', f'&r{color_code}')

    for code, format_code in minecraft_formatting.items():
        if f'&{code}' in text or f'§{code}' in text:
            text = text.replace(f'&{code}', format_code
                        ).replace(f'§{code}', format_code)

    if reset_all:
        text += '\033[0m'

    return text


def mcremove(text):
    """
    Allows you to remove color codes from a text.

    :param text: Text
    :return: Clean text
    """

    for code in minecraft_colors.keys():
        text = text.replace(f'&{code}', ''
                  ).replace(f'§{code}', '')

    for code in minecraft_formatting.keys():
        text = text.replace(f'&{code}', ''
                  ).replace(f'§{code}', '')
    
    return text
