'''
Created on Jun 11, 2017

@author: moni
'''
import random

import com.fireboxtraining.ColorChart as cfc
from tkinter import Button, Toplevel, Tk
import tkinter

count  = 0
diceList = [0,0,0,0,0,0]

class colorDice(tkinter.Button):
    
    
    def __init__(self):
        
        self.button = None
        self.g()
        self.count=0
        
    
    def random_generatorForColor(self):
        result = random.randint(0, 478)
        f = cfc.c.COLORS[result]
        return str(f)   
    def random_generator(self):
        result = random.randint(1, 6)
        self.numberCounter(result)
        strinG = ""
        strinG += str(result)
        return strinG
    def g(self):
        global count
        if(self.button == None):
            
            result = self.random_generator()
            cResult = self.random_generatorForColor()
            self.button =  Button(root, text = "" + result, bg =""+cResult, height = 3  , width = 10, command = self.g)
            self.button.pack()
            count+=1
            
        if(count%15==0 and count !=0 ):
            import com.fireboxtraining.mom as M
            print("gjhghgui")
            M.start(diceList)
            
        else:
            result = self.random_generator()
            cResult = self.random_generatorForColor()
            self.button.destroy()
            self.button =  Button(root, text = "" + result, bg =""+cResult , height = 3  , width = 10, command = self.g)
            self.button.pack()
            count+=1
        if(count%15==0 and count !=0 ):
            import com.fireboxtraining.mom as M
            print("gjhghgui")
            M.start(diceList)
            
    def numberCounter(self, result):
            if result == 1:
                diceList[0]+=1
            elif result == 2:
                diceList [1]+=1
            elif result == 3:
                diceList[2]+=1
            elif result == 4:
                diceList[3]+=1
            elif result == 5:
                diceList[4]+=1
            else:
                diceList[5]+=1
                      
root = Toplevel()

cd = colorDice()


root.mainloop()
        
        
        
    
    
    
    