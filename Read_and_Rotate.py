"""
Adarsh Patel

Image Manipulation Library

Functions for reading a given PGM image and obtaining the relevant data in the form of a namedTuple

Includes functions that allow simple manipulation of the image geometrically i.e Vertical, Horizontal reflections

Python script v1
"""

import numpy as np
import sys
from collections import namedtuple

# the only relevant file type is P2
FILETYPE = 'P2'

# structure for storing the data of a PGM file
PGMFile = namedtuple('PGMFile', 'max_shade, data')

"""
This function receives the name of a PGM file and returns the data in
the form of a PGMFile.
"""


def read_image(filename):
    with open(filename) as imagefile:
        # list to hold integer entries in the file
        entries = []

        firstword = True
        for line in imagefile:
            words = line.split()
            worditer = iter(words)
            comment = False
            endline = False
            while not comment and not endline:
                try:
                    word = next(worditer)
                    if not word.startswith('#'):
                        if not firstword:
                            # an entry that is not part of a comment and is not
                            # the first word is an integer
                            entries.append(int(word))
                        else:
                            # the first word that is not a comment is the file type
                            assert word == FILETYPE, f"The only supported file type is P2."
                            firstword = False
                    else:
                        # this is a comment; drop the rest of the line
                        comment = True
                except StopIteration:
                    endline = True

    num_cols = entries[0]  # number of columns in the image
    num_rows = entries[1]  # number of rows in the image
    max_shade = entries[2]  # maximum pixel value

    # all remaining integers are pixel values
    # arrange them in a numpy array using dimensions read from the header
    data = np.reshape(np.array(entries[3:]), (num_rows, num_cols))

    return PGMFile(max_shade, data)


"""
This function receives a file name and a PGMFile, and writes
a PGM file with the given data.

The pixel data must be in a NumPy array whose dimensions are the 
number of rows and number of columns in the image.  

"""


def write_image(filename, image):
    # read the dimensions of the image from the shape of the pixel data array
    num_rows, num_cols = image.data.shape

    # create the file header
    header = f"{FILETYPE}\n{num_cols} {num_rows}\n{image.max_shade}"

    # entries in the pixel data array are written to the file as integers
    np.savetxt(filename, image.data, fmt="%d", comments='', header=header)

    return


"""
mirror_lr

Reflects an image left to right
"""


def mirror_lr(image):
    newdata = np.fliplr(image.data)
    return PGMFile(image.max_shade, newdata)


"""
mirror_ud

Reflects an image top to bottom
"""


def mirror_ud(image):
    newdata = np.flipud(image.data)
    return PGMFile(image.max_shade, newdata)


"""
invert_black_white

Inverts black and white
"""


def invert_black_white(image):
    newdata = image.max_shade - image.data
    return PGMFile(image.max_shade, newdata)


"""
Brightens by the % passed in as parameter alongside the image namedTuple
One possible interpretation:  the value of each pixel is increased by 10%,
then rounded to the nearest integer.  Then any values that exceed the max
shade are set to the max shade.
"""


def brighten(image, percentageBrightness):
    # magic number given in assignment
    percentage = percentageBrightness

    newdata = image.data + image.data * percentage / 100

    # round to nearest integer, then clip values below at 0
    # and above at the max pixel value
    newdata = np.clip(np.rint(newdata), 0, image.max_shade)

    return PGMFile(image.max_shade, newdata)


if len(sys.argv) > 1:

    filename = sys.argv[1]
    image = read_image(filename)

    basename = filename[:filename.rfind('.')]

    image_lr = mirror_lr(image)
    filename_lr = basename + '-1-lr.pgm'
    write_image(filename_lr, image_lr)

    image_ud = mirror_ud(image)
    filename_ud = basename + '-2-ud.pgm'
    write_image(filename_ud, image_ud)

    image_inv = invert_black_white(image)
    filename_inv = basename + '-3-inv.pgm'
    write_image(filename_inv, image_inv)

    image_bright = brighten(image)
    filename_bright = basename + '-4-bright.pgm'
    write_image(filename_bright, image_bright)

else:
    print("Please enter a file name.")