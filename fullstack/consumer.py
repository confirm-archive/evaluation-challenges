# Finish me!

from PIL import Image

# Core logic

input = Image.open("jason.jpg")
output = input.resize((64, 64), Image.BICUBIC)
output.save("jason.png", "png")