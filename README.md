# ShareMyFile

Description:
Our project allows multiple clients to connect to a server and send files of any type (including images) through that server to each other.

Modules:
	Receive Module:
		Allows a client to receive files from the server
	Send Module:
		Allows a client to send files to the server

Explanation:
	1) Connection is established between clients and server
	2) The sender sends a file to the Server and this is stored in the server's socket
		. The file is read line by line and sent 500 packets at a time
		.The server upon receiving these packets writes to a new file
	3) Similarly, the server sends the file to the receiver
	4) The connection is closed

IMPORTANT:
Read setup.txt for setting up the application.

Contributors:

Sharath Menon
Shailesh Sridhar
Shailendra Hegde
