import socket
import time
import sys
from thread import start_new_thread
import threading 
#creating socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print_lock = threading.Lock() 

# connecting to server
print "Connecting to server"
client.connect(('192.168.0.70', 8801))							#'''SET THE IP ADDRESS ACCORDING TO THE SERVER SYSTEM'''
choice=int(input("Enter 1-To SEND 2-To RECEIVE\n"))
client.send(str(choice))
if choice==1:
	#sending data
	print "\t\t---------SENDER---------"
	print_lock.acquire()	
	path=input("Enter the path of file to be transferred\n")			#'''CHANGE THE PATH NAME ACCORDINGLY''' 
	f=open(path,'r')
	data=f.read()
	size=len(data)
	print "SIZE OF FILE SENT = "+str(size)
	client.send(str(size))
	time.sleep(5)
	client.send(data)
	f.close()
	print_lock.release()
elif choice==2:
	#receiving data
	print "\t\t---------RECEIVER---------"
	print_lock.acquire()	
	f=open('/home/flame-alchemist/Pictures/Wallpapers/gohan1.jpg','w')		#'''#CHANGE THE PATH NAME ACCORDINGLY'''
	size=client.recv(1024)
	print "SIZE OF FILE RECEIVED = "+size
	size=int(size)
	i=1
	while i<=size:
		if (i+500)>size:
			data=client.recv(500+size-i)
			print i
		else:
			data=client.recv(5000)
			print i	
		f.write(data)
		i=i+50
	f.close()
	print_lock.release()
else:
	print "INVALID CHOICE"

sys.stdout.flush()
#closing connection
client.close()
