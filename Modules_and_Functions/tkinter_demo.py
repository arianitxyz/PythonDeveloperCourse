try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x640")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='top', fill=tkinter.X, expand=True)

button1 = tkinter.Button(mainWindow, text="Button1")
button1.pack(side='left', anchor='n')
mainWindow.mainloop()
