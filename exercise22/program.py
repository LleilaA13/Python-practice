
import images

def es42(fImageIn, fcolors, fImageOut):
    '''Design and implement the function es42(fImageIn, fcolors,
    fImageOut) that changes the color of some pixels in an image read
    from a PNG image file, fImageIn, and then save the modified image in a
    new PNG image, fImageOut.

    The function also returns the number of pixels of the image whose
    colors have been changed.  The colors to modify are specified by
    the text file fcolors: the fcolors file has as many lines as the
    number of colors to modify.  Each line of fcolors contains 6
    integers with values between 0 and 255.  Every pixel of the color
    with the first three integers as color components should be
    changed with the color with the second three integers as color
    components.  For example if a line contains the sequence
    0 0 0 255 255 255, it indicates that in the image all pixels of
    black color (i.e. color (0,0,0)) must become of white color (i.e.
    color (255,255,255)).

    NOTE: every pixel should possibly change color only once, namely
    color replacement should happen only once for each pixel.

    :param fImageIn: name of the PNG file containing the image to edit
    :param fcolors: name of the text file in which to find the colors to modify
    :param fImageOut: name of the PNG file in which to save the modified image
    :return: number of modified pixels
    '''
    # Insert here your code



