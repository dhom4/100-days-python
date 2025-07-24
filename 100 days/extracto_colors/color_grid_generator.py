import colorgram
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import os

def get_contrast_text_color(rgb):
    r, g, b = rgb
    brightness = r * 0.299 + g * 0.587 + b * 0.114
    return (0, 0, 0) if brightness > 160 else (255, 255, 255)

def main():
    # GUI file picker
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images", "*.jpg *.png *.jpeg")])
    if not file_path:
        print("No file selected.")
        return

    try:
        color_count = int(input("How many colors to extract? (e.g., 12): "))
        squares_per_row = int(input("How many squares per row? (e.g., 4): "))
    except ValueError:
        print("Invalid number.")
        return

    print("Extracting colors...")
    colors = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colorgram.extract(file_path, color_count)]

    # Grid layout
    square_size = 80  # Increased size for readable text
    rows = (len(colors) + squares_per_row - 1) // squares_per_row
    img_width = squares_per_row * square_size
    img_height = rows * square_size

    img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

    # Draw squares with hex labels
    for i, color in enumerate(colors):
        row = i // squares_per_row
        col = i % squares_per_row
        x0 = col * square_size
        y0 = row * square_size
        x1 = x0 + square_size
        y1 = y0 + square_size

        draw.rectangle([x0, y0, x1, y1], fill=color)

        # Hex text
        hex_code = '#%02x%02x%02x' % color
        text_color = get_contrast_text_color(color)
        # Get bounding box of the text
        text_bbox = draw.textbbox((0, 0), hex_code, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        text_x = x0 + (square_size - text_width) // 2
        text_y = y0 + (square_size - text_height) // 2
        draw.text((text_x, text_y), hex_code, fill=text_color, font=font)

    # Save in same folder
    image_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = os.path.dirname(file_path)
    output_path = os.path.join(output_folder, f"{image_name}_color_grid.png")
    img.save(output_path)

    print(f"Color grid saved to: {output_path}")
    img.show()

if __name__ == "__main__":
    main()
