import cv2
import numpy as np


def filter(image, upix, lpix):
    h = image.shape[0]
    w = image.shape[1]
    for i in range(h):
        for j in range(w):
            if image[j, i] > upix:
                image[j, i] = 200
            elif image[j, i] < lpix:
                image[j, i] = 0
    return image
def main():
    path = '../cat.jpg'
    img = cv2.imread(path, 0)
    img1 = cv2.imread(path, 0)
    filtered = filter(img, 100, 100)
    cv2.imshow('original', img1)
    cv2.imshow('filtered', filtered)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
