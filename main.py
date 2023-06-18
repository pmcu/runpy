import pandas as pd
list =[
    ['dog','brown','Touser'],
    ['donkey','brown','Toofus'],
    ['cat','brown','Typhus'],
    ['dog','black','Touser'],
]
'''
for item in list:
    print(item)
'''

mydataset = {
'cars': ["BMW","Volvo","Ford"],
'passings': [3,7,2]
    }
myvar = pd.DataFrame(mydatset)
print(myvar)

