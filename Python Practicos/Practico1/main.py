

import argsparser
import sys
import downloader

def main():
	parser = argsparser.ArgsParser()
	args = sys.argv #toma los argumentos de la consola
	
	#~ url = parser.get_url(args)
	#url= "http://my.e-photovault.com/app/wl/?id=h&filename=India"
	#~ url="http://www.sosmath.com"
	#~ url="http://www.sosmath.com"
	url="http://www.sosmath.com/tables/tables.html"
	#~ ext = parser.get_ext(args)
	ext= ".php"
	
	if (url == "" or ext == ""):
		print "Debe informar url y extension con --url= y --ext= ."
		return 1

	contentDownl = downloader.Downloader()
	count = contentDownl.downloadAll(url, ext)
	print "Se han descargado " + str(count) + " archivos con extension "\
	 + ext + " de la url \"" + url + "\""
	
	return 0

if __name__ == '__main__':
	main()

