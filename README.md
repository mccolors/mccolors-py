# MCColors

MCColors is a Python module that allows you to handle Minecraft-style color codes in your terminal text output.

## Installation

You can install MCColors using pip:

```bash
pip install mccolors
```

## Usage

```python
from MCColors import mcwrite, mcreplace, mcremove

# Writing text with Minecraft color codes
mcwrite('&4Hello &rWorld!', reset_all=True)

# Replacing Minecraft color codes with their respective colors
formatted_text = mcreplace('&6Formatted &ctext &athat &3shines!')

# Removing Minecraft color codes from text
clean_text = mcremove('&eClean &7this &ftext.')
```

## Functions

### `mcwrite(text, reset_all=True)`
Allows writing text with Minecraft color codes in the terminal.

### `mcreplace(text, reset_all=True)`
Replaces Minecraft color codes in the text with their respective colors.

### `mcremove(text)`
Removes Minecraft color codes from the text, leaving clean text.

## Parameters

- `text`: The input text containing Minecraft color codes.
- `reset_all`: A boolean value that decides whether to reset the text color at the end (default: True).

## Contributions and Issues

Contributions and suggestions are welcome! If you encounter any issues or want to contribute, please open an issue or pull request on [GitHub](https://github.com/wrrulos/mccolors).

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
