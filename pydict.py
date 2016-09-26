#!/usr/bin/python

mydict={1994:"Pulp fiction", 1997:"seven", 1999:"Blood"}
print"My dic ",len(mydict)
print"Dictionary keys", mydict.keys()
print"Dictionary values",mydict.values()

newdict={1972:"God father",1980:"Range bull"}
mydict.update(newdict)
print"Update dictiony func() add new dict to old : " , mydict
mydict.clear()
print"this is clear func()" , mydict
