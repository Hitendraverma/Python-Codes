#!/usr/bin/python

import time
import calendar #calender in python

print(calendar.month(2015,12))

#print calender of full year ... calender.calender( year , day width ,each week occupy no. line , width btwn months )

print(calendar.calendar(2016 , 2 , 1 , 10))

time.sleep(3)
#leap year 

print"Check leap 2008 : " , calender.isleap(2008)


time.sleep(4)

print"time.time() : " , time.time()
print"time.localtime(time.time()) : " , time.localtime(time.time())
print"time.asctime() : " , time.asctime()
#make time function 
mytuple=(1923,4,2,14,23,12,0,0,0)
time.mktime(mytuple)
print"mktime localtime : " , time.localtime(time.mktime(mytuple))

#sleep method in python 


