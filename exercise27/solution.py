import images

def es13(fimm,fimm1):
    img=images.load(fimm)
    ins=set()
    for r in range(len(img)):
        for c in range(len(img[0])):
            ins.add(img[r][c])
    ls_tuple=list(ins)
    ls_tuple=sorted(ls_tuple)
    N = len(ls_tuple)
    ls_fin=[]
    for ind in range(0,N,50):
        ls_fin.append(ls_tuple[ind:ind+50])
    for r in range(len(img)):
        for c in range(len(img[0])):
            for el in ls_fin:
                if img[r][c] in el:
                    img[r][c]=el[0]
    images.save(img,fimm1)
    return len(ls_fin) 
