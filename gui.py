import threading, os
from ExtractFrame import ExtractFrame
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from tkinter.messagebox import showerror
from tkinter.ttk import Progressbar, Style
from pdf2image import convert_from_path
from PIL import Image, ImageTk

root = Tk(baseName="Extract PDF")
root.title('PDF to Image')
root.iconbitmap()
root.resizable(False, False)

file_pdf = ""

process_open_book = None

def __open_file__(filepath):
  global file_pdf, progress
  progress.start()
  file_pdf = convert_from_path(filepath)
  progress.stop()
  frame_loading.pack_forget()
  frame_extract = ExtractFrame(root, padx=4, pady=8)
  basename = os.path.basename(filepath)
  basename = basename.split(".")
  del basename[-1]
  basename = ".".join(basename)
  file_dir = f"{os.path.dirname(filepath)}/{basename}"
  frame_extract.save(file_dir, file_pdf)
  frame_extract.pack()
  

def open_file():
  global progress, frame_loading, process_open_book
  file = askopenfilename(filetypes=[("PDF File", "*.pdf")])
  if not file:
    return

  try:
    frame_open_book.pack_forget()
    frame_loading.pack(side=TOP, expand=True, fill=BOTH)
    threading.Thread(target=__open_file__, args=(file,)).start()
  except Exception as e:
    showerror("Error", str(e))


frame_open_book = Frame(root, padx=14, pady=8, background='#003545')
img = ImageTk.PhotoImage(Image.open('./book.png'))
lbl_book = Label(frame_open_book, image=img, background='#003545')
lbl_book.pack(side=TOP, fill=BOTH, expand=True)
button_open = Button(frame_open_book, text = 'Buka PDF', background='#3B2C85', foreground='#fff', activebackground='#283149', padx=25, pady=4, command=open_file)
button_open.pack(side=BOTTOM, fill=X, expand=True)

frame_loading = Frame(root, padx=14, pady=8, background='#003545')
progress = Progressbar(frame_loading, orient='horizontal', mode='indeterminate', length=250)
progress.pack(fill=X, expand=True, side=TOP)

frame_open_book.pack(side=TOP, fill=BOTH, expand=True)
root.mainloop()