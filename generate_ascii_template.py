from PIL import ImageFont
import string

# use a bitmap font
font = ImageFont.truetype('Silkscreen/slkscr.ttf', 12)


def char_to_ascii(char_input):
    mask = font.getmask(char_input)
    width = font.getsize(char_input)[0]

    pixels = ""
    i = 0
    for pixel in mask:
        if pixel < 200:
            pixels += '0'
            i += 1
        else:
            pixels += '1'
            i += 1
        if i % width == 0:
            pixels += '\n'
    return pixels


if __name__ == '__main__':
    for char in string.ascii_letters:
        with open(f'characters/{char}.txt', 'w') as f:
            f.write(char_to_ascii(char))
