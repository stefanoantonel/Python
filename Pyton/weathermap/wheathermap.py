
import requests
import json
import sys
import argparser

URL="http://api.openweathermap.org/data/2.5/weather?q="

class Weather():
	def get_json(self,ciudad):
		r=requests.get(URL+ciudad)
		return r.content
	
	def print_weather(self, ciudad, unidad):
		
		j = self.get_json(ciudad)
		r = json.loads(j)
		temperatura = r["main"]["temp"] #pongo el texto jason y lo guardo en el resultado y me lo tranforma a un diccionario 
		#temperatura viene en K
		unidad = unidad.lower()
		
		if (unidad == "celsius" or unidad == "c"):
			temperatura = temperatura -273.15
		elif (unidad == "fahrenheit" or unidad == "f"):
			temperatura = temperatura * (9/5) - 459.67
			
		return str(temperatura)

def main():
	city="London"
	if(len(sys.argv))<1:
	#	city=argv[1]
		parser= argparser.ArgsParser()
		parser.get_city(sys.argv)

	print str(sys.argv)
	map=Weather()
	#map.get_json("Cordoba")
	print (map.get_json(city)) #esto devuelve el JSON como texto, por eso puedo poner print
	print "-----------------------------"
	print map.print_weather(city)
	return 0

if __name__ == '__main__':
	main()

