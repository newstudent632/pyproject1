Dict = { 'Raaji': 25, 'Jeevna':23 }
print(Dict['Jeevna'])
#dictionary elements
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
print (Dict['Tirumalesh'])

#copy data fields into variables
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
Boys = {'Tirumalesh':22}
Girls = {'Raaji': 18,'jeevana':12,'Nikila':25}

StudentX = Boys.copy()
StduentY = Girls.copy()
print(StudentX)
print(StduentY)
#Update data fields into dictionary
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
Dict.update({"Rangaswamy":49})
Dict.update({"Lakshmi":45})
print(Dict)

#Delete data fields into dictionary
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
del Dict["Nikila"]
print(Dict)

#Items display from dictiory
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
Dict.update({"Rangaswamy":49})
print(Dict.items())

#check exitsng record
Dict = {'Raaji': 18,'jeevana':12,'Tirumalesh':22,'Nikila':25}
Boys = {'Tirumalesh':22}
Girls = {'Raaji': 18,'jeevana':12,'Nikila':25}
for key in Girls.keys():
    if key in Dict.keys():
        print (True)
    else:
        print (False)

#sorting in dictionry
Dict = {'Tirumalesh':22,'Raaji': 18,'Jeevana':12,'Nikila':25}
Boys = {'Tirumalesh':22}
Girls = {'Raaji': 18,'jeevana':12,'Nikila':25}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
#length for dictionry
Dict = {'Tirumalesh':22,'Raaji': 18,'Jeevana':12,'Nikila':25, 'Ranga':49}
print("Length : %d" % len (Dict))
print("variable Type: %s" %type (Dict))

#compare dictionary
Boys = {'Tirumalesh':22}
Girls = {'Raaji': 18,'jeevana':12,'Nikila':25}
print(Girls, Boys)
#string in dictonry
Dict = {'Tirumalesh':22,'Raaji': 18,'Jeevana':12,'Nikila':25, 'Ranga':49}

print("variable Type: %s" %str (Dict))

#merge dictionir
Boys = {'Tirumalesh':22}
Girls = {'Raaji': 18,'jeevana':12,'Nikila':25}
Boys.update(Girls)

print(Boys)