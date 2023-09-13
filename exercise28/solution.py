import images


def ex4(fimm, fimm1, h1, w1):
    new_image = []                             # initializing a list for the new image
    image = images.load(fimm)        # loading the original image
    original_height = len(image)             # original image height
    original_width = len(image[0])         # original image width
    countColor = {}
    for _ in range(original_height*h1):             # preparing the image by inserting instead of each pixel, a 0
        row = []
        for _ in range(original_width*w1):
            row.append(0)
        new_image.append(row)
    for x in range(original_height):
        for y in range(original_width):
            pixel_color = image[x][y]
            new_image = drawRect(new_image, x*h1, y*w1, h1, w1, pixel_color)   # drawing the rectangle in new_image
            if pixel_color in countColor:                                             # update the color dictionary
                countColor[pixel_color] += 1
            else:
                countColor[pixel_color] = 1
    images.save(new_image, fimm1)                                                        # save the new image in fimm1
    maxColor = max(countColor.values())                                                   # taking the number of times more that a color appears
    listColor = sorted(list(filter(lambda x: countColor[x] == maxColor, countColor)))     # deleting all colors that do not appear the maximum number of times and order the obtained list
    return listColor[0]                                                                   # returning the color with maximum value

def drawRect(img, x, y, h, w, c):
    '''the function draws a rectangle in the img image
    with top left vertex in (x, y), height h and width w,
    color c'''
    for i in range(x, x+h):
        for j in range(y, y+w):
            img[i][j] = c
    return img

