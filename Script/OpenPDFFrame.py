from time import sleep
from tkinter import Tk, Frame, Label, Button, TOP, BOTH, DISABLED, NORMAL, X
from tkinter.messagebox import showwarning
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk

class OpenPDFFrame(Frame):
  PATH = ''
  LIST_IMAGE = []
  FILENAME = ''
  
  def __init__(self, root, background='#003545', **kwargs):
    Frame.__init__(self, master=root, **kwargs)
    self.frame_open_pdf = Frame(self, background=background, padx=8, pady=4)

    img = Image.open('./Script/image/book.png')
    self.img_book_file = ImageTk.PhotoImage(img)
    self.lbl_book = Label(self.frame_open_pdf, image=self.img_book_file, background='#003545')
    self.button_open_pdf = Button(self.frame_open_pdf, text = 'Buka PDF', background='#3B2C85', foreground='#fff', activebackground='#283149', padx=25, pady=4,)
    self.lbl_book.pack(side=TOP, fill=BOTH, expand=True)
    self.button_open_pdf.pack(side=TOP, fill=BOTH, expand=True)
    self.frame_open_pdf.pack(side=TOP, expand=True, fill=BOTH)
    self.progress_opening_pdf = Progressbar(self.frame_open_pdf, orient='horizontal', mode='indeterminate', )


if __name__ == '__main__':
  root = Tk()
  root.title('PDF to Image')
  root.resizable(False, False)

  frame_open_book = OpenPDFFrame(root)
  frame_open_book.pack(side=TOP, fill=BOTH, expand=True)

  root.mainloop()