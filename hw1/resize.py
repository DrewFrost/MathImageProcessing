import cv2
import numpy as np
PATH = '../lion'
IMG = cv2.imread((PATH+'.jpg'), 0)
H = IMG.shape[0]
W = IMG.shape[1]
X = 2


def bigger():
    """
    resize picture x times bigger
    """
    big_h = int(W * X)
    big_w = int(H * X)
    big_img = np.zeros((big_w, big_h, 3), np.uint8)
    for j in range(big_h):
        for i in range(big_w):
            big_img[i, j] = IMG[i // X][j // X]
    return big_img


def pixel(block):
    """
    resize pixel blocks
    """
    pix = 0
    itr = 0
    for rows in block:
        for val in rows:
            pix += val
            itr += 1
    return pix / itr


def smaller():
    """
    resize image x times smaller
    """
    sm_w = (W//X)
    sm_h = (H//X)
    sm_img = np.zeros((sm_h, sm_w, 3), np.uint8)
    size = 1*X
    for j in range(sm_w):
        for i in range(sm_h):
            block = IMG[i * size:(i * size + size), j * size:(j * size + size)]
            res = pixel(block)
            sm_img[i, j] = res
    return sm_img
def main():
    BIG = bigger()
    SML = smaller()
    cv2.imshow("original", IMG)
    cv2.imshow("big", BIG)
    cv2.imwrite((PATH+'big.jpg'), BIG)
    cv2.imshow("small", SML)
    cv2.imwrite((PATH+'small.jpg'), SML)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
