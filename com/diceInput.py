'''
Created on Jun 9, 2017

@author: moni
'''

from pymongo import MongoClient
from tkinter import Button, Tk, Label
import random

Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["Dice"]   

class colorOrSwitch():
    def __init__(self):
        self.doubleTable()
    def doubleTable(self):
        label =  Label(root, text = "Chose then Click 15 times ", justify ="center")
        label.pack()
        button1 = Button(root, text="Color Dice", width ="20", command = self.r)
        button1.pack()
        button2 = Button(root, text="Orginal Dice", width ="20", command = self.s)
        button2.pack()
        
    def s (self):
        try:
            import com.fireboxtraining.OrdinaryDice as D
        except AttributeError as a:
            print("Restart and try again")
            
        
    def r(self):
        import  com.colorDice    
    def random_generator(self):
        result = random.randint(1, 6)
        d = self.faceDie(result)
        strinG = ""
        strinG += str(result)
        return d
    
    
root = Tk()

c= colorOrSwitch()

root.mainloop()




