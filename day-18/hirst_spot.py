from PIL.Image import Image
import colorgram
colors=colorgram.extract("Image/colorgram.jpg",22)
color_rgb=[]
for color in colors:
    color_rgb.append(color.rgb)
print(color_rgb)