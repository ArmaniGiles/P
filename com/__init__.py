


"""Frame, Button, Tk, ttk, PhotoImage"""
from  tkinter import ttk, Tk, Frame, Label,messagebox
import tkinter

"""from PhotoImage import *

import Image

"""


"""print(dir(PhotoImage))"""


class Sas(Tk):
    
    def __init__(self):
        """ print("1st self type : "+ type(self))"""
        Frame.__init__(self) 
        label1 = Label(root, text="Hello Tkinter!")
        label1.pack()
        label2 =Label(root,text ="Hello Python")
        label2.pack()
        def helloCallBack():
            messagebox.showinfo( "Hello Python", "Hello World")
        def callback():
            print("Call Back")
        """ w2 = Label(root, 
           justify="RIGHT",
           padx = 10, 
           text="explanation").pack(side="left")"""
        style   = ttk.Style()
        style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        colored_btn = ttk.Button(text="Test", style="C.TButton").pack()
        
        style.map("A.TButton", foreground=[('pressed', 'white'), ('active', 'white')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        colored_btn = ttk.Button(text="ing", style="A.TButton", command=helloCallBack).pack()
    



"""style = ttk.Style()"""

if __name__ == '__main__':
 
    root = None
    root =Tk() 
    root.mainloop()

"""
app = Sas()
app.mainloop()


root.mainloop()"""




