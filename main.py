import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def cargar_imagen():
    Tk().withdraw()
    filename = askopenfilename()
    return filename
