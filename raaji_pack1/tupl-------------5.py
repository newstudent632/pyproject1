tup = ('love','self','me')
tup = ();
tup = (25,);
tup1 = ('R','S','RS','SR')
tup2 = (1,2,3,4)
tup3 = ('amma','mummy','mom','ambha')
print(tup1[0])
print(tup1[1:2])
print(tup2[3])
print(tup2[0:2])
print(tup3[3])
print(tup3)
print(tup2)
print(tup1,tup2,tup3)
#packing
R = ('kalyan','chakravarthy','kalyanchakravarthy')
print(R)
#unpacking
(hero,super,star) = R
print(hero)
print(star,super)
print(hero,super)
#comparing tuples
#case1
a = (1,2)
b = (2,2)
if(a>b):print("a is bigger")
eles: print("b is bigger")
#case2
xy = (-1/2,5/2)
yz = (-2/2,5/2)
if(xy>yz):print("a is bigger")
eles: print("b is bigger")
#using tuples as key in dictionaries                     0nn
a ={'y':200,'z':200}
print(a)
#slicing of tuple
x = ("raaju","raaji","vijaya","kalyan",)
print(x[1:2])
