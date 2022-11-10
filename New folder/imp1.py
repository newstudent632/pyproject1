f1 = open('py1.txt','r')
str1 = 'my name is raani'
f2 = open('py2.txt','a')

for i in f1:
    f2.write(i)
f2.close()
f2 = open('py2.txt','r')
print(f2.read())

