import datetime as dt
#import pandas as pd
#print("Hello, World! and Dogs")


list =[
    ['dog','brown','Touser'],
    ['donkey','brown','Toofus'],
    ['cat','brown','Typhus'],
    ['dog','black','Touser'],
]
#df = pd.DataFrame(list)

def showlist():
    txt= ""
    for item in list:
        txt=str(item)
    #print(txt)
    Element("lists").write(txt)
#showlist() 
