
import argparser
import wheathermap
import sys
import pygtk
import gtk

def main():
	
	
#	if(len(sys.argv))<1:
	#	city=argv[1]
		parser= argparser.ArgsParser()
		parser.get_city(sys.argv)

	print str(sys.argv)
	map=wheathermap.Weather()
	#print (map.get_json(city)) #esto devuelve el JSON como texto, por eso puedo poner print
	print "-----------------------------"
	print map.print_weather(city)
	return 0

if __name__ == '__main__':
	main()

