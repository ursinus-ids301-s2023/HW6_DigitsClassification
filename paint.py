import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import scipy.stats
from skimage.transform import resize
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
from digits import *

digits = load_mnist_digits()

def classify():
    """
    Resize the image that the user drew to 28x28
    and call the classification code from digits.py
    to classify it
    """
    I = np.array(digit_image) # The image that we drew
    I = I[:, :, 0]
    dim = digits[0][0].shape[0]
    I = resize(I, (dim, dim), anti_aliasing=True)
    print(classify_digit(I, digits, 10))
    root.destroy()

def paint(event):
    """
    Paint on the PIL canvas and the Tkinter canvas in parallel
    Draw canvas will be saved, while Tkinter canvas shows
    the user what they are drawing
    """
    bs = 10
    x1, y1 = (event.x - bs), (event.y - bs)
    x2, y2 = (event.x + bs), (event.y + bs)
    canvas.create_oval(x1, y1, x2, y2, fill="black")
    draw.ellipse([x1, y1, x2, y2], fill="#000000")


if __name__ == '__main__':
    width = 200  # canvas width
    height = 200 # canvas height
    root = Tk()
    # create a tkinter canvas to draw on
    canvas = Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    # Create a PIL image and a drawer object
    digit_image = PIL.Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(digit_image)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.bind("<B1-Motion>", paint)

    # add a button to save the image
    button=Button(text="classify",command=classify)
    button.pack()

    root.mainloop()