'''
Created on May 29, 2017

@author: moni
'''

from tkinter import  Button as But , PhotoImage, Toplevel
import tkinter
import random

diceList = [0,0,0,0,0,0]

count  = 0
class diceListe(tkinter.Toplevel):
    
    def __init__(self):
        self.greatButton = But()
        self.random_generator()
        self.go()
        self.photo = PhotoImage()
        self.count = 0
    def random_generator(self):
        result = random.randint(1, 6)
        d = self.faceDie(result)
        strinG = ""
        strinG += str(result)
        return d
    def random_generatorForColor(self):
        result = random.randint(0, 478)
        return result
    def faceDie(self, face):
        if(face==1):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice1150x150.png")
            diceList[0] +=1
            return self.photo
        elif(face==2):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice2150x150.png")
            diceList[1] +=1
            return self.photo
        elif(face==3):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice3150x150.png")
            diceList[2] +=1
            return self.photo
        elif(face==4):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice4150x150.png")
            diceList[3] +=1
            return self.photo
        elif(face==5):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice5150x150.png")
            diceList[4] +=1
            return self.photo
        else:
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice6150x150.png")
            diceList[5] +=1
            return self.photo
        
    def go(self):
        global count
        """check this out  http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter"""
        count+=1
        self.greatButton.pack_forget() 
        self.greatButton = But(root, image=self.random_generator(),
                command =self.go,height = 150   , width = 150 )
        self.greatButton.pack()
        if(count%15==0 and count !=0 ):
            import com.fireboxtraining.mom as M
            print("gjhghgui")
            M.start(diceList)
            
            
"""print(help(diceListe))"""

root  = Toplevel() 
c = diceListe()
print(id(c.go()))
root.mainloop() 



            