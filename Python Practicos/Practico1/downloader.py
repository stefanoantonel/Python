
import json
import re
import requests
import urllib2
import os

class Downloader():
	def downloadFile(self, filePath):
		fileName = filePath.split('/')[-1]
		
		try:
			u = urllib2.urlopen(filePath)
			print "Descargado: "+filePath
		except:
			print "No se pudo descargar " + filePath
			return False
		directory="./download/"
		if not os.path.exists(directory):
			os.makedirs(directory)
		completeName = os.path.abspath(directory+fileName)
		f = open(completeName, 'wb')
		blockSz = 28192
		while True:
			buffer = u.read(blockSz)
			if not buffer:
				break
			f.write(buffer)
		f.close()
		return True
		
	def downloadAll(self, url, ext):
		#~ pass
		url2= url.split('/')[0:-1]
		url2 = "/".join(url2)
		print  url2
		r=requests.get(url)
		cont=r.content
		#~ regExp=r"a href=\".*?\""
		regExp=r"a href=\".*?"+ext+"\""
		#~ regExp="\"http://www.*?"+ext+"\""
		matches =re.findall(regExp,cont)
		for i in matches:
			
			# i: a href="/complex/complex.html"
			fi=i.find("\"") #posicion de la primera comilla
			sin= i[fi+1:-1] # desde la posicion 8 hasta la penultima [1:3] desde el 1 hasta el 3 sin contar el 3
			#osea la url completa
			if( sin.startswith("/")):
				t= url2+sin
				self.downloadFile(t)
			elif (sin.startswith("h")):
				self.downloadFile(sin)
			elif(sin.startswith("www.")):
				#~ print "wwwwwww"
				t= "http://"+sin
				
				#~ print t
				self.downloadFile(t)
			elif(sin.startswith("..")):
				url3= url2.split('/')[0:-1]
				url3 = "/".join(url3)
				sin=sin[2:]
				t= url3+sin
				print "t: " + t
				self.downloadFile(t)
			else:
				#~ print "otros"
				t= url2+"/"+sin
				self.downloadFile(t)
			
			

		return len(matches)

def main():
	
	return 0

if __name__ == '__main__':
	main()

