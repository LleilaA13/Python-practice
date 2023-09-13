import images

def es42(fImageIn, fcolors, fImageOut):
    img = images.load(fImageIn)
    h = len(img)
    w = len(img[0])
    count = 0
    palette = {}
    with open(fcolors) as f:
        for line in f:
            r, g, b, R, G, B = map(int, line.split())
            palette[(r, g, b)] = R, G, B
    for y in range(h):
        for x in range(w):
            c = img[y][x]
            if c in palette:
                img[y][x] = palette[c]
                count += 1
    images.save(img, fImageOut)
    return count



'''
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




'''