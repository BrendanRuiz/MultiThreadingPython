from threading import *
from time import sleep 

class SomeClass(Thread): 
	#need to use run() from the threading class
	def run(self):
		for i in range(5):
			print('thread 1 running')
			#go to sleep for a second to simulate a large function 
			#being run 
			sleep(1)

class SomeOtherClass(Thread): 
	def run(self):
		for i in range(5):
			print('thread 2 running')
			sleep(1)

thread1 = SomeClass()
thread2 = SomeOtherClass()

thread1.start()
#place a gap between the two calls to alternate
sleep(0.2)
thread2.start()

#tell main thread to wait for the first two threads to join
thread1.join()
thread2.join()


print('now running main thread')