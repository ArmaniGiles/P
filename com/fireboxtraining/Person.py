from tkinter import Tk, ttk as td, Frame, messagebox
"""import tkinter"""




class Gogo(Tk):
    
    def __init__(self):
        td.Button.__init__(self)
        print("My Call Back")
        label1 = td.Label(root, text ="Hot")
       
        def jo ():
            print("you got RED")
            return "red"
        def jor ():
            print("you got BLUE")
        def jor2 ():
            print("you got YELLOW")
        def jor3 ():
            print("you got BLACK")
        def jor4 ():
            print("you got WHITE")
        def jor5 ():
            print("you got ABSENT")
            
        style = td.Style()
        style.map("A.TButton", foreground=[('pressed', 'red'), ('active', 'red')], background=[('pressed', '!disabled', 'red'), ('active', 'red')])
        style.map("B.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        style.map("D.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        style.map("E.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        style.map("F.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        style.map("Z.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        button1  = td.Button(root, text="Red", command =jo , style ="A.TButton").grid(row=0, column=0)
      
        button2  = td.Button(root, text="Blue", command =jor, style ="F.TButton").grid(row=1, column=0)
        
        button3  = td.Button(root, text="Yellow", command =jor2, style ="B.TButton").grid(row=0, column=1)
        
        button4  = td.Button(root, text="Black", command =jor3, style ="C.TButton").grid(row=1, column=1)
        
        button5  = td.Button(root, text="White", command =jor4, style ="D.TButton").grid(row=2, column=0)
        
        button6  = td.Button(root, text="Absent", command =jor5, style ="E.TButton").grid(row=2, column=1)
        """messagebox.showerror(title="Big Error", message= "ahaha")"""
        """ self.initUI()"""
        self.mainloop()
    def initUI(self):
         button0  = td.Button(self, text="Red", command =jow , style ="Z.TButton").grid(row=0, column=0)   
         def jow (self):
                    print("you got RED")
                    return "red"
   
        

from pymongo import MongoClient
root = None
"""root Tk()"""

Q = Gogo()
 
Client = MongoClient()
db = Client["Library"]
collection = db["Books"]
book ={}
book ["year"] = 2015
book ["Author"] = "Mahesh"


collection.insert(book)

print(book)





