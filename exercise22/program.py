
import images

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


def es42(fImageIn, fcolors, fImageOut):

    # Insert here your code

    image = images.load(fImageIn) #loading image
    
#the image is a list of tuples I think, the tuples are rgb
    l = len(image) 
    w = len(image[0])
    count = 0  
    colori = {} #dictionary key (tuple) : value (tuple), the key being the pixel color to change into the tuple value
    with open(fcolors, encoding='utf') as f:#open the file in which we have the colors
        for line in f: #for loop lines of the file
            r, g, b, R, G, B = map(int, line.split()) #mapping the 6 values in every line into ints
            colori[(r, g, b )] = R, G, B #assigning key-value pairs
    
    for y in range(l): #outer loop going through
        for x in range(w): #nested loop
            c = image[y][x] #every pixel
            if c in colori: #if the rgb of c is in the palette of colors to change
                image[y][x] = colori[c] #you change into the ones  R G B of the file
                count += 1 #increment by 1
    images.save(image, fImageOut) #save the output image
    print(image)


if __name__ == '__main__':
    es42('scacchiera.png', 'fcolori2.txt', 'out1.png')






'''
    Load an image from a file specified by fImageIn.

    Determine the dimensions of the image: l represents the number of rows,
    and w represents the number of columns.

    Initialize a variable count to keep track 
    of how many color replacements have been made.

    Create an empty dictionary called colori t
    hat will be used to map certain pixel colors to replacement colors.

    Open a file specified by fcolors and read its contents line by line.

    For each line in the file, the code extracts six integer values 
    (presumably representing RGB values and their corresponding replacement RGB values) 
    and stores them in variables r, g, b, R, G, and B.

    It then creates a key-value pair in the colori dictionary, 
    where the key is a tuple (r, g, b) representing the original pixel color, 
    and the value is a tuple (R, G, B) representing the replacement color.

    After populating the colori dictionary with color mappings, 
    the code enters two nested for loops to iterate over each pixel in the image.

    For each pixel at position (y, x), it checks if the color c 
    (represented as a tuple) exists as a key in the colori dictionary.

    If c is found in colori, it replaces the pixel's color with the corresponding replacement color from the dictionary, 
    and increments the count variable by 1.

    Finally, the modified image is saved to a file specified by fImageOut, 
    and the modified image is printed.

This code essentially allows you to specify a mapping of original pixel colors 
to replacement pixel colors and apply those replacements to the input image. 
The count variable keeps track of how many replacements were made.

'''