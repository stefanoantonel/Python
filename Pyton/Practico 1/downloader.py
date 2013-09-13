
import json
import re
import requests
import urllib2

class Downloader():
	def downloadFile(self, filePath):
		fileName = filePath.split('/')[-1]
		
		try:
			u = urllib2.urlopen(filePath)
			print "Descargado: "+filePath
		except:
			print "No se pudo descargar " + filePath
			return False
		f = open(fileName, 'wb')
		blockSz = 8192
		while True:
			buffer = u.read(blockSz)
			if not buffer:
				break
			f.write(buffer)
		f.close()
		return True
		
	def downloadAll(self, url, ext):
		#~ pass
		
		r=requests.get(url)
		cont=r.content
		#~ regExp=r"a href=\".*?\""
		regExp=r"a href=\".*?"+ext+"\""
		#~ regExp="\"http://www.*?"+ext+"\""
		matches =re.findall(regExp,cont)
		for 
			
			d=Downloader()
			fi=i.find("\"")
			
			sin= i[fi+1:-1]
			
			if( sin.startswith("/")):
				#~ print "/////"
				t= url+sin
				d.downloadFile(t)
			elif (sin.startswith("h")):
				#~ print "httttttt"
				d.downloadFile(sin)
			elif(sin.startswith("www.")):
				#~ print "wwwwwww"
				t= "http://"+sin
				
				#~ print t
				d.downloadFile(t)
			else:
				#~ print "otros"
				t= url+"/"+sin
				d.downloadFile(t)
			
			

		return len(matches)

def main():
	
	return 0

if __name__ == '__main__':
	main()

