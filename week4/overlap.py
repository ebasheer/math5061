import point2d_methods as p2

def overlap(A_tl, A_br, B_tl, B_br):
    return not ( A_br.isleftof(B_tl) or A_tl.isrightof(B_br) or 
                 A_br.isabove(B_tl) or A_tl.isbelow(B_br)) 

if __name__ == '__main__':
    A_tl = p2.Point2D(input('Top-Left of A: '))
    A_br = p2.Point2D(input('Bottom-Right of A: '))
    B_tl = p2.Point2D(input('Top-Left of B: '))
    B_br = p2.Point2D(input('Bottom-Right of A: '))

    if overlap(A_tl, A_br, B_tl, B_br):
        print('Rectangles overlap')
    else:
        print('No Overlap')
