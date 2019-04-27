from socket import *
import threading

class ClientThread(threading.Thread):
	def __init__(self, connect, address):
		threading.Thread.__init__(self)
		self.connectionSocket = connect
		self.addr = address
	def run(self):
		while True:
			try:
				message = connectionSocket.recv(1024)
				if not message:
					break
				filename = message.split()[1]
				print filename
				f = open(filename[1:])
				outputdata = f.read() 
				print "outputdata:", outputdata

				first_header = "HTTP/1.1 200 OK"
				header_info = {
					"Content-Length": len(outputdata),
					"Keep-Alive": "timeout=10, max=100",
					"Connection": "Keep-Alive",
					"Content-Type": "text/html"
				}
				
				following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
				print "following_header:", following_header
				connectionSocket.send("%s\r\n%s\r\n\r\n" %(first_header, following_header))

				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i])
			except IOError:
				f = open('error.html')
				outputdata = f.read()
				print "outputdata:", outputdata

				first_header = "HTTP/1.1 404 Not Found"
				header_info = {
					"Content-Length": len(outputdata),
					"Content-Type": "text/html"
				}
				following_header = "\r\n".join("%s:%s" % (
					item, header_info[item]) for item in header_info)
				print "following_header:", following_header
				connectionSocket.send("%s\r\n%s\r\n\r\n" % (first_header, following_header))
				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i])

if __name__ == '__main__':
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverPort = 3000
	serverSocket.bind(('',serverPort))
	serverSocket.listen(5)
	threads=[]

	while True:
		print 'Server is up and running on port %d' %serverPort
		connectionSocket, addr = serverSocket.accept()
		print "addr:\n", addr
		client_thread = ClientThread(connectionSocket, addr)
		client_thread.setDaemon(True)
		client_thread.start()
		threads.append(client_thread)

	for thread in threads:
		thread.join()
	serverSocket.close()
