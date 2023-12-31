from mccolors import mcwrite, mcreplace, mcremove

# Example of writing text with Minecraft colors
print("Example of writing text with Minecraft colors:")
mcwrite('&4Hello &rWorld!', reset_all=True)
print()

# Example of replacing color codes
print("Example of replacing color codes:")
text_to_replace = '&6Formatted &ctext &athat &3shines!'
formatted_text = mcreplace(text_to_replace)
print(f"Original text: {text_to_replace}")
print(f"Formatted text: {formatted_text}")
print()

# Example of removing color codes
print("Example of removing color codes:")
text_to_clean = '&eClean &7this &ftext.'
clean_text = mcremove(text_to_clean)
print(f"Original text: {text_to_clean}")
print(f"Clean text: {clean_text}")
