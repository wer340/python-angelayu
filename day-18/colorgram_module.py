from PIL.Image import Image
import colorgram_module
colors=colorgram_module.extract("Image/colorgram.jpg",22)

for color in colors:
    r=color.rgb.r    
    g=color.rgb.g
    b=color.rgb.b
    tuple_color=(r,g,b) 
    color_rgb.append(tuple_color)
print(color_rgb)