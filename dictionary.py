capita_Dic= {'India':'delhi', 'Canada': 'Ottawa'}
print(capita_Dic)

"""This is a doc to fetch doc"""
for k in capita_Dic:
    print(k)
    print(capita_Dic[k])

capita_Dic['India'] = 'Mumbai'
print(capita_Dic)

#print(dictionary.__doc__)
import Assignemnt
 
print( repr(capita_Dic))
print( str(capita_Dic))

#set operations
print("Set operatins")
aset= {'abcd', 'bcd','dec'}
bset={'abcd', 'cda', 'doc'}
print(aset)
aset.add('GEY')
print(aset | bset)
print('abcd' in aset)

#Frozenset
print("Frozenset")
frSet= frozenset({"Orange","Banana","Kela"})
frSet2= frozenset({"Orange2","Banana2","Kela2"})
#print(frSet+frSet2)
frSet = [1,2,3,4]
print(frSet)

from collections import Counter

a = "Sitaramans"
print(a)
counterA= Counter(a)
print(counterA)
