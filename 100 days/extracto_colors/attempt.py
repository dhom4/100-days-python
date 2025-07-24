import colorgram
from PIL import Image, ImageDraw

image = colorgram.extract("i.jpg", 12)
colors = []
for color in image:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors.append(new_color)

# Parameters
square_size = 50  # Size of each square in pixels
squares_per_row = 4  # Number of squares per row

# Calculate image size
num_colors = len(colors)
rows = (num_colors + squares_per_row - 1) // squares_per_row
img_width = squares_per_row * square_size
img_height = rows * square_size

# Create a blank image
img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw the squares
for i, color in enumerate(colors):
    row = i // squares_per_row
    col = i % squares_per_row
    x0 = col * square_size
    y0 = row * square_size
    x1 = x0 + square_size
    y1 = y0 + square_size
    draw.rectangle([x0, y0, x1, y1], fill=color, outline=(255, 255, 255))

# Save or show the result
img.save("color_squares.png")
img.show()
