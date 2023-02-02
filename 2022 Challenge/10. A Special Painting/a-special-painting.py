import os
from PIL import Image

filename = "a-special-painting.png"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with Image.open(filepath) as f:
    pixels = f.load()
    width, height = f.size

temp = ""
for i in range(height):
    for j in range(width):
        r, _, _ = pixels[j, i]
        temp += (format(int(f"{r:02x}", 16), '0>8b')[-1])
        if len(temp) == 8:
            if temp == "00000000":
                exit()
            print(int(temp, 2).to_bytes(int(temp, 2).bit_length()+7//8, "big").decode(), end="") # Answer: cake
            temp = ""