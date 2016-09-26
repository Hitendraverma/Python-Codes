#!/usr/bin/python

mylist=[1,23,4,4,5,5,5,4,7,7,78,9,9,]
print"len func () gives no of char:" , len(mylist)
print"max gives max no. : " , max(mylist)
print"min gives min no. : " , min(mylist)
print"Count() gives repeated char no : " , mylist.count(7)
print"append() in list , only one char at a time : " , mylist.append(80)
print(mylist)

#Insert elemnt in list 

print"Insert() a element : " 
mylist.insert(5,500)
print(mylist)
mylist.reverse()
print"Reverse : " , mylist
mylist.remove(500)
print"Remove 500 " , mylist
mylist.sort()
print"sort list", mylist
