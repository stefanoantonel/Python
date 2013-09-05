

import argsparser
import sys
import downloader

def main():
	parser = argsparser.ArgsParser()
	args = sys.argv
	
	url = parser.get_url(args)
	ext = parser.get_ext(args)

	
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

