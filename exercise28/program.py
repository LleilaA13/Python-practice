import images


def ex4(fimm1, fimm2, h1, w1):
    '''Design a function ex4(fimm1,fimm2) such that:
    - it receives as arguments two filenames 'fimm1' and 'fimm2',
      where 'fimm1' is a file with an .PNG image, and two integers
      'h1' and 'w1', both greater than zero;
    - it reads the image in 'fimm1' and creates a new image that
      saves as a PNG image in the 'fimm2' file;
    - it returns a tuple with the color that appears most often in the
      original image and, in case of tie, the one that precedes the
      others in ascending order.
    The new image has h1 times the height of the original image and w1
    times the width of the original image. Each pixel of the original
    image corresponds in the new image to a rectangle of pixels with
    the same color and with height h1 and width w1.

    To load and save the image in PNG files, use the load and save
    functions of the images.py library.

    '''
    # write here your code
    img = images.load(fimm1)
    h = len(img)
    w = len(img[0])
    height = h * h1
    width = w * w1

    img_flat = [col for row in img for col in row]

    colors = set(img_flat)

    freq = {col: img_flat.count(col) for col in colors}

    most_freq = max(
        list((k, v) for k, v in freq.items()), key=lambda tup: (tup[1], tup[0])
    )[0]

    new_img = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    for i, row in enumerate(img):
        for j, _ in enumerate(row):
            for v in range(h1):
                for u in range(w1):
                    new_img[i * h1 + v][j * w1 + u] = img[i][j]

    images.save(new_img, fimm2)

    return most_freq


if __name__ == '__main__':
    ex4('cubo.png', 'test8_1.png', 2, 2)
