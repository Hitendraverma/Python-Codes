#!/usr/bin/python

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

def worker():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Exting')

def service():
	logging.debug('Starting')
	time.sleep(3)
	logging.debug('Exiting')

for i in range(3):
	ser = threading.Thread(name='process' , target=service)
	ser.setDeamon(True)
	wor = threading.Thread(name='work' , target=worker)
	wor2 = threading.Thread(target=worker)

	ser.start()
	wor2.start()
	wor.start()




