import matplotlib.pyplot as plt
from pymongo import MongoClient
import random
import string

Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["Dice"] 
book={}
book["author"]  = "Armani"
book["text"] = "The magic of thinking Big"
book["tags"] = ["mongodb", "python", "pymongo"]

collection.insert(book)
"""print(book)"""
h ="sdf"
 
cursor =collection.find()
print(cursor)



import datetime
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id )


color1 = "" 
color2 = ""
color3 = ""
color4 = ""
color5 = ""
color6 = ""


h = []
count =0
def start(ok):
    
    
    
    print("hello World")
    # Data to plot
    labels = 'ONE', 'TWO','THREE','FOUR','FIVE','SIX'
    colors = random_generatorForColor()
    #colors =['0','.1','.2','.3','.4','.5']
    print(colors)
    for  s in colors:
        print(s)
        print("sdfdsfweerwqtvwytttttttvbr")
    #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'grey', 'violet']
    explode = (0.1, 0, 0, 0,0,0)  # explode 1st slice
    
    # Plot
    #try:
    plt.pie(ok, explode=explode, labels=labels, colors=None,
                autopct='%1.1f%%', shadow=True, startangle=140)
    #except ValueError as d :
        #start(ok)
        
    plt.axis('equal')
    plt.show()
    





def random_generatorForColor():
    global h
    global count
    import com.fireboxtraining.ColorChart as C
    result = random.randint(0, 478)
    
    if( "blue" not in C.c.COLORS[result] ):
        random_generatorForColor()
    #Prevent Copies of the same color of the Chart
    elif( C.c.COLORS[result] in h ):
        random_generatorForColor()
    else:
        h.append(''.join(C.c.COLORS[result].split()));
    if(count == 6):
        return  h
    else:
        count+=1
        random_generatorForColor()
        
        

