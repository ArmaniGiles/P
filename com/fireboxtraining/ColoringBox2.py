'''
Created on May 22, 2017

@author: moni
'''
from tkinter import Frame, Button, Label, ttk as tik, Tk
import tkinter


class CB2():
    def __init__(self):
        self.red_Button()
        self.blue_Button()
        self.yellow_Button()
        self.white_Button()
    def red_Button(self):
            style =  tik.Style()
            button1  = Button( fox,text="red", command=red_Action)
            button1.grid(row=0, column=0)
     
    def blue_Button(self):
            style =  tik.Style()
            button  = Button(fox, text="blue",command=blue_Action)
            button.grid(row=0, column=1)
           
    def yellow_Button(self):
            style =  tik.Style()
           
            button  = Button(fox, text="yellow",command=yellow_Action).grid(row=1, column=0)
            
    def white_Button(self):
            style =  tik.Style()

            button  = Button(fox, text="white",command=white_Action).grid(row=1, column=1)
            
    

""" Ac Class that excutes the Button commands"""       
class red_Action():
    def __init__(self):
        self.red()
        self.method()
    def method(self):
        return "red" 
    def red(self):
        print("This is red") 
     
class blue_Action():
    def __init__(self):
        self.blue()
        self.method()
    def method(self):
        return "blue"
    def blue(self):
        print("This is blue") 
class yellow_Action():
    def __init__(self):
        self.yellow()
        self.method()
    def method(self):
        return "yellow"
    def yellow(self):
        print("This is yellow") 
class white_Action():
    def __init__(self):
        self.white()
        self.method()
    def method(self):
        return "white"
    def white(self):
        print("This is white")          
R = red_Action()
B = blue_Action()
Y = yellow_Action()
W= white_Action()


from pymongo import MongoClient

class MDB():
    def __init__(self):
        print("asd")


Client = MongoClient()

db = Client["Library"]
collection =  db["Books"]
book ={}
book ["year"] = 2015
book ["Author"] = R.method()
book ["Cake"] = B.method()
book["zoey"] = Y.method()
book["wjo"] = W.method()

collection.insert(book)

print(book)
Client = MongoClient()
db1 = Client["myJobs"]

collection = db1["sofware"]

job = {}
job ["Job_Title"] = "Sofware Tester"
job ["Location"] = "Delware County"
job ["Company"] = " Targets"
job ["Applied"] = "5/28/2017"
job ["Communte"] = "Driviing, an half an hour"
job ["Other"] = " "

collection.insert(job)


db2 = Client["Music"]

collection =  db2["song"]

music = {}

music["Song"] = "Two Steps From Hell"

music["Genere"] = "Theater"

music ["Artist"] ="Thomas"

collection.insert(music)





  
fox =None
"""fox = Tk()  
"""
root = None 
"""root=Tk()"""

q = CB2()
root.mainloop()
