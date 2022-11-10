dict = {'xy':1,'yz':2,'zx':3}
print(dict)
dict = {'raaju':200,'raaji':100}
print(dict['raaju'])
#dictionary elements
dict = {'A':100,'B':200,'C':300,'D':400}
print(dict['A'])
print(dict['D'])
#copy data fields into variadle
dict = {'raam':30,'pradeep':30,'raaji':24,'raaju':24}
boys = {'raam':30,'pradeep':30,'raaju':24}
girl = {'raaji'}
studentX = girl.copy()
studentY = boys.copy()
print(studentX)
print(studentY)
#updata data field into dictionary
dict = {'R':1,'S':2,'L':3,'V':4,'T':5}
dict.update({'love':500})
print(dict)
dict.update({'self':600})
print(dict)
dict.update({'believe':700})
#delete data field into dictionary
dict = {'raju':589,'raaji':1600,}
del dict['raaji']
print(dict)
#item display from dictionary
dict = {'A':1,'B':2,'C':3,'D':4}
dict.update({'M':5})
print(dict.items())
