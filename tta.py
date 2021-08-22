from PIL import ImageFont


def letter_to_ascii(letter):
    retval = ""
    with open(f'characters/{letter}.txt', 'r') as f:
        for line in f:
            retval += line.replace('0', ' ').replace('1', letter)
    return retval


def word_to_ascii(phrase, font, font_size, kerning):
    font = ImageFont.truetype(font, font_size)
    height = font.getsize('a')[1]

    retval = ""
    for row in range(height):
        for letter in phrase:
            width = font.getsize(letter)[0]
            height = font.getsize(letter)[1]
            mask = [x for x in font.getmask(letter)]

            bitmap = [mask[r*width:r*width + width] for r in range(height)]

            row_bitmap = bitmap[row]
            if len(row_bitmap) == 0:
                retval += width * ' '
            for pixel in row_bitmap:
                if pixel < 100:
                    retval += ' '
                else:
                    retval += str(letter)
            retval += kerning * ' '
        retval = retval.rstrip()
        retval += '\n'
    return retval.rstrip()


if __name__ == '__main__':
    print(word_to_ascii(
        phrase='hey there!', 
        font='slkscr.ttf', 
        font_size=12,
        kerning=5,
    ))
