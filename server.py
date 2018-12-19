import socket
import time

#from _thread import *
from thread import start_new_thread
import threading 

print_lock = threading.Lock() 

def main():

	# creating a socket to listen for incoming connections
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# binding hostname and port number to socket
	# server.bind((socket.gethostname(), 8888))
	server.bind(('',8801))
	# dont bind on the localhost
	# listening for connections
	server.listen(1)
	while True:
		# accepting connection from client
		server_client, addr = server.accept()
		print "Connected to client"		
 
		choice=int(server_client.recv(1024))
		if choice==1:
			print_lock.acquire()
			f=open('/home/flame-alchemist/Pictures/Wallpapers/socket.jpg','w')			#'''CHANGE THE PATH NAME ACCORDINGLY''' 
			size=server_client.recv(1024)
			print "SIZE OF FILE RECEIVED = "+size
			size=int(size)
			i=1
			while i<=size:
				if (i+500)>size:
					data=server_client.recv(500+size-i)
					print i
				else:
					data=server_client.recv(500)
					print i	
				f.write(data)
				i=i+500
			print_lock.release()
			#break
			

		else:
			print_lock.acquire()
			f=open('/home/flame-alchemist/Pictures/Wallpapers/socket.jpg','r') 			#'''CHANGE THE PATH NAME ACCORDINGLY''' 
			data=f.read()
			size=len(data)
			print "SIZE OF FILE SENT = "+str(size)
			server_client.send(str(size))
			time.sleep(5)
			server_client.send(data)
			print_lock.release()
			break
		#break
	f.close()
	server_client.close()
	server.close()
	print "end"

if __name__=='__main__':
	main()

