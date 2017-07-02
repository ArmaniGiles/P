'''
Created on May 21, 2017
I keep poping two windows

@author: moni
'''



from tkinter import ttk as tik, Tk as tk, ttk, Button, RIGHT, BOTH, RAISED
import tkinter 
from tkinter.ttk import Label
from tkinter.ttk import Button

class ColorGrid(Button):
    style  = ttk.Style()
    style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'red'), ('active', 'blue')])
    def __init__(self):
        """tkinter.Button.__init__(self, parent)  """ 
       
        self.startB()
    def startB(self):  
        button1 = Button(root,text="what", style="C.TButton")
        print("Enter")  
        button1.pack()
      
    def row(self):
        print("ROX")

    """  def buttonPushed(self):"""
        


root = None
"""root = tk()

app = ColorGrid()
root.mainloop()"""

    

