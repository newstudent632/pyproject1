for i in range(10,90+1):
    flag= 0
    for k in range(4,i):
        if (i%k==0):
            flag = 1
            break

    if(flag==0):
         print(i,k)
print("..................")

string = ("gtl","mtl","ntl")
for i in string:
    for m in i:
         if m !="t":
            print(m)

#num = (10-100)
for i in range(10-100):
    for m in range(10-20):
         print(i,m)
