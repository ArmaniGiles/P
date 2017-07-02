'''
Created on May 29, 2017

@author: moni
'''
from tkinter import ttk, Tk, Button, Frame, Label
import tkinter 
import random
from builtins import str, None


from pymongo import MongoClient
Client  = MongoClient()
db        = Client["miniProjects"]
collection = db ["Dice"]


 
class Dice():
    
    count =0
    dic = {}
    dic["1"] = 1
    dic["2"] = 2
    dic["3"] = 3
    dic["4"] = 4
    dic["5"] = 5
    def __init__(self):
        self.hello = "hello"
        self.greatButton =Button()
        """self.go()"""
        self.go2()
        self.random_generator2()
        self.count =0
        self.button =  Button()
        
        self.number =0
    def random_generator2(self):
        result= random.randint(0, 100)
        strinG = ""
        strinG += str(result)
        """ print( strinG)"""
        return strinG
    def go(self):
            
            if(self.count==0):
                self.button = Button(root, text = self.random_generator2() , command =self.go)
                self.button.pack()
                self.count+=1
            elif(self.count==1):
                self.button.pack_forget()
                self.number+=1
                if(self.greatButton !=None and self.number>1):
                    self.greatButton.pack_forget() 
                    self.greatButton = Button(root, text = self.random_generator2() , command =self.go)
                    self.greatButton.pack()
            
                
            
            """elif self.count > 0:
            if(self.button != None):
                self.button.pack_forget()"""
            """Question command = self.go()  vs  command self.go """
    def go2(self):
                    self.greatButton.pack_forget() 
                    self.greatButton = Button(root, text = self.random_generator2() , command =self.go2)
                    self.greatButton.pack()
  
    def random_generator(self):
        result= random.randint(0,5)
        strinG = ""
        strinG += str(result)
        return  strinG
           

root = None
"""root= Tk()"""

""""c = Dice()
root.mainloop()"""
            