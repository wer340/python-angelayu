from PIL.Image import Image
import colorgram
colors=colorgram.extract("Image/colorgram.jpg",22)
color_rgb=[]
for color in colors:
    r=color.rgb.r    
    g=color.rgb.g
    b=color.rgb.b
    tuple_color=(r,g,b) 
    color_rgb.append(tuple_color)
print(color_rgb)