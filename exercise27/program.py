
'''
Design a function ex13(fimm1,fimm2) such that,
    - it receives as argument path names of two .PNG files ('fimm1'
      and 'fimm2')
    - it reads and modifies the image stored in 'fimm1' and then saves
      the new image into 'fimm2' file
    - it returns the number of DIFFERENT colors present in the
      modified image.
    The color of each pixel of the original image is modified with the
    following procedure:
    - the tuples of the DIFFERENT colors in the first image are
      ordered in ascending order
    - the ordered sequence of tuples is, then, divided into ordered
      groups of 50 (if the total number of tuples is not a multiple of
      50, then the last group will have less than 50 elements)
    - all the colors in a given group will be modified with the first
      color of the group.
    This implies that the pixels with colors belonging to the same
    group will alll have the same color, corresponding to the first
    color of the group.

    Example: the function should transform the image of Foto2.png into
    the image of RisFoto2.png and return the value 4.

    To load and save the image in PNG files, use the load and save
    functions of the images.py library.
'''
import images


def ex13(fimm1, fimm2):
    img = images.load(fimm1)
    h = len(img)
    w = len(img[0])
    t_set = set()
    chunks = []
    colormap = dict()
    for y in range(h):
        for x in range(w):
            t_set.add(img[y][x])
    t_unique = sorted(list(t_set))

    for tp in range(0, len(t_unique), 50):
        chunks.append(t_unique[tp: tp+50])

    for chunk in chunks:
        first = chunk[0]
        for col in chunk:
            colormap[col] = first

    for i, row in enumerate(img):
        for j, pix in enumerate(row):
            img[i][j] = colormap[pix]

    images.save(img, fimm2)
    return len(chunks)


if __name__ == '__main__':
    print(ex13('Foto2.png', 'testFoto2.png'))
