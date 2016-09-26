#!/usr/bin/python

import threading
import time 

#Code 1 
'''
thread = []

def worker():
	print "Thead fn working"
	return

#for i in range(5):
	#t=threading.Thread(target=worker)
	#thread.append(t)
	#t.start()		

''''THreading is initialed using function start()''''

#Adding Argument in fn call 

def threadl(num):
	print "Arg thread fn wrkng"+num
	return

for i in range(5):
	t=threading.Thread(target=threadl , args=(i))
	thread.append(t)
	t.start()
'''


#Code 2 - Naming thread

def worker():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(3)
	print threading.currentThread().getName(), 'Exiting'

def service():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(4)
	print threading.currentThread().getName(), 'Exiting'

for i in range(5):
	ser = threading.Thread(name='process' , target=service)
	wor = threading.Thread(name='worker', target=worker)
	wor2 = threading.Thread(target=worker)
#Using wor2 gives 'Thread-1' in the name thread column in the output
	ser.start()
	wor2.start()
	wor.start()

