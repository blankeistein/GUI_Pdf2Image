import re, os
import threading
from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
from pdf2image import convert_from_path

class ExtractFrame(Frame):
  
  RE_NUMERIC = re.compile('^[0-9]*$')
  ASPECT_RATIO = (16, 9)
  SIZE = (0, 0)
  TARGET_SIZE = (0, 0)
  LIST_IMAGE = []
  PATH = "./"

  def __init__(self, root, background='#003545', **kwargs):
    Frame.__init__(self, master=root, background=background, **kwargs)
    self.lock = True
    self.LBL_SIZE = StringVar(self, value="Ukuran : 0x0")
    self.btn_extract = Button(self, text='Extract Image', background='#3B2C85', activebackground='#2C2828', foreground='#fff', command= lambda: threading.Thread(target=self.__extract_image__).start())
    self.progress_extract = Progressbar(self, orient="horizontal", mode="determinate", length=300)
    
    self.percent = Scale(self, from_=1, to=100, orient=HORIZONTAL, length=300, command=self.__handler_scale__, showvalue=0)
    self.percent.set(100)

    self.lbl_size = Label(self, textvariable=self.LBL_SIZE)
    self.percent.grid(row=1, column=1, columnspan=2)
    self.lbl_size.grid(row=0, column=1, columnspan=2, sticky=W)
    self.btn_extract.grid(row=2, column=1, columnspan=2, padx=4, pady=8)

  def __handler_scale__(self, event):
    width = int(self.SIZE[0] * int(event) / 100)
    height = int(self.SIZE[1] * int(event) / 100)
    self.LBL_SIZE.set(f"Ukuran : {width}x{height}")
    self.TARGET_SIZE = (width, height)

  def __extract_image__(self, ):
    self.btn_extract.configure(state='disabled')
    self.progress_extract.grid(row=3, column=1, columnspan=2)
    if not os.path.isdir(self.PATH):
      os.mkdir(self.PATH)

    number = 1
    if len(self.LIST_IMAGE) != 0:
      for img in self.LIST_IMAGE:
        img.resize(self.TARGET_SIZE).save(f"{self.PATH}/{number}.jpg", "JPEG")
        self.progress_extract['value'] = int((number/len(self.LIST_IMAGE)) * 100)
        number += 1
    else:
      print("Buku Kosong")

    self.progress_extract.grid_forget()
    self.btn_extract.configure(state='normal')

  def save(self, path, list_image):
    self.PATH = path
    self.LIST_IMAGE = list_image
    self.SIZE = list_image[0].size
    self.TARGET_SIZE = list_image[0].size
    self.LBL_SIZE.set(f"Ukuran : {list_image[0].size[0]}x{list_image[0].size[1]}")
        

if __name__ == "__main__":
  root = Tk()
  root.title("Extract Image")
  frame_book = ExtractFrame(root, padx=8, pady=4, background='#003545')
  frame_book.pack(side=TOP, expand=True, fill=BOTH)

  root.mainloop()