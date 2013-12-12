import socket
import sys

class Client ():
	
	def getArgumentos(self,ip,puerto):
		self.ip=ip
		self.puerto=puerto
	
	def conectar(self):
		msg="Conectar"
		print "entro"
		ip="100.100.142.115"
		sock = socket.socket(socket.AF_INET, # Internet
							 socket.SOCK_DGRAM) # UDP
		sock.sendto(msg, (self.ip, self.puerto))
		
		while True:
			data, ip =sock.recvfrom(1024)
			if(ip[0]==self.ip):
				print data

def main():
	c= Client()
	arg= sys.argv
	c.getArgumentos(arg[1],int(arg[2]))
	c.conectar()
	return 0;
	
if __name__=='__main__':
	main()
