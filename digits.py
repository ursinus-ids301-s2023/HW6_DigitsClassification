import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import scipy.stats

def load_mnist_digits():
    """
    Load in all of the MNIST digits and put them into a big array

    Parameters
    ----------
    list(10) of list of ndarray(28, 28)
        All of the MNIST digits
    """
    # Load in all digits
    res = 28
    digits = []
    for i in range(10):
        digits.append([])
        I = skimage.io.imread("Digits/{}.png".format(i))/255.0
        row = 0
        col = 0
        while row < I.shape[0]:
            col = 0
            while col < I.shape[1]:
                img = I[row:row+res, col:col+res]
                if np.sum(img) > 0:
                    digits[i].append(img)
                col += res
            row += res
    return digits

if __name__ == '__main__':
    digits = load_mnist_digits()
    i = 4
    ex = 302
    plt.imshow(digits[i][ex], cmap='gray')
    plt.xlabel("Pixel Column")
    plt.ylabel("Pixel Row")
    plt.colorbar()
    plt.show()