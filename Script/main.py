import threading
from os.path import basename, dirname
from tkinter import BOTH, DISABLED, NORMAL, TOP, Menu, Tk, X
from tkinter.filedialog import askopenfilename

from pdf2image import convert_from_path

from ExtractFrame import ExtractFrame
from OpenPDFFrame import OpenPDFFrame

root = Tk()
root.title('PDF to Image')
root.resizable(False, False)

def open_file(event=None):
  global frame_open_pdf
  frame_open_pdf.button_open_pdf.configure(state=DISABLED)
  filepath = askopenfilename(filetypes=[('PDF File', '*.pdf')])
  if not filepath:
    frame_open_pdf.button_open_pdf.configure(state=NORMAL)
    return

  frame_open_pdf.FILENAME = basename(filepath)
  frame_open_pdf.PATH = dirname(filepath)
  frame_open_pdf.progress_opening_pdf.pack(side=TOP, expand=True, fill=X, padx=4, pady=8)
  threading.Thread(target=load_pdf, args=(filepath,)).start()

def load_pdf(filepath):
  global frame_open_pdf, root
  frame_open_pdf.progress_opening_pdf.start()
  pdf = convert_from_path(filepath)
  frame_open_pdf.LIST_IMAGE.extend(pdf)
  frame_open_pdf.progress_opening_pdf.stop()
  frame_open_pdf.pack_forget()
  frame_extract_pdf = ExtractFrame(root, padx=4, pady=8)
  filename = frame_open_pdf.FILENAME.split('.')
  del filename[-1]
  filename = '.'.join(filename)
  frame_extract_pdf.save(f'{frame_open_pdf.PATH}/{filename}', frame_open_pdf.LIST_IMAGE)
  frame_extract_pdf.pack()
  

frame_open_pdf = OpenPDFFrame(root)
frame_open_pdf.button_open_pdf.bind('<Button-1>', open_file)

frame_open_pdf.pack(side=TOP, fill=BOTH, expand=True)

menu = Menu(root)
fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open File', command=open_file)
fileMenu.add_command(label='Exit', command=root.quit)

root.config(menu=menu)
root.mainloop()
