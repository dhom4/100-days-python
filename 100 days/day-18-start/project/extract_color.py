import colorgram

colors = colorgram.extract("i.png", 30)
# first_color = color[0]
# print(first_color.rgb)

new_rgb_color = []

# for color in colors:
#     new_color.append(color.rgb)

for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new_color = (r,g,b)
    new_rgb_color.append(new_color)

# print(new_rgb_color)