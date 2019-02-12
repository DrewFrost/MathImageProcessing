import numpy as np
import matplotlib.pyplot as plt
import cv2


def apply(img, kernel):
    h, w = img.shape[:2]
    new_img = np.zeros(img.shape)
    for i in range(1, h-1):
        for j in range(1, w-1):
            entry = img[i-1:i+2, j-1:j+2]
            value = np.sum(entry*kernel)  
            new_img[i, j] = value
    return new_img


def gaussian(size, sigma):
    gauss = np.zeros((size, size))
    size = size//2
    for i in range(-size, size+1):
        for j in range(-size, size+1):
            x = 2 * np.pi * (sigma ** 2)
            g = np.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))
            gauss[i + size, j + size] = (1/x)*g
    return gauss


def main():
    path = '../tiger.jpg'
    img = cv2.imread(path, 0)
    kernel1 = np.array([
                [0, 1, 0],
                [1, 2, 1],
                [0, 1, 0]])
    k1 = apply(img, kernel1)
    gauss = gaussian(3, 1.5)
    convo = apply(img, gauss)
    plt.figure('original')
    plt.imshow(img, cmap='gray')
    plt.figure('1/6')
    plt.imshow(k1, cmap='gray')
    plt.figure('gaussian')
    plt.imshow(convo, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
