# Paulo Drefahl

# I decided to go with this library because it gets the image and bases the pattern on it.
from PIL import Image, ImageDraw, ImageFont

def generate_letter(letter):
    size = 20
    image1 = Image.new('L', (40, 40), color=255) # define image settings
    draw_image = ImageDraw.Draw(image1)  # here its blank
    font = ImageFont.load_default()

    draw_image.text((size // 2, size // 2), letter, font=font, fill=0) #here I am drawing with the font os your specific OS
    # I observed that the font default is different between MAC and Windows but it works in both if you use default.

    pixels = image1.load() # this variable is for the coordinates
    rows = []

    # building our pattern for that specific letter
    for y in range(image1.height):
        row = ""
        for x in range(image1.width):
            if pixels[x, y] < 128:
                row += letter
            else:
                row += " "
        if row.strip():
            rows.append(row)
    return rows


# This is just iterating through the input and executing the function we created before
def print_name_with_letters(name):
    name = name.upper() # needs to be uppercase
    letters = [generate_letter(letter) for letter in name] # here we are getting the patterns for the used letters
    max_rows = max(len(l) for l in letters)

    # I am adding this to be able to display horizontally
    for row_index in range(max_rows):
        line = ""
        for l in letters:
            if row_index < len(l):
                line += l[row_index]
            else:
                line += " " * len(l[0])  # in case we need more space I added this
            line += " "
        print(line)


name = input("Enter your name: ")
print_name_with_letters(name)
# The final result is good, however I wanted to space a bit less the letters
# but the library to get the images has some restrictions with sizes
# #and it glitches a bit if I try to go smaller
