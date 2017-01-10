#phthano
#Deletes any image smaller than 640x480

import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
img_dir = filedialog.askdirectory()
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    with Image.open(filepath) as im:
        x, y = im.size
    totalsize = x*y
    if totalsize < 307201:
        os.remove(filepath)