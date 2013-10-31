#jfjf
import sys
try:
	import pygtk
	pygtk.require("2.0")
except:
	print "no tengo pygtk 2.0"
	sys.exit(1)
	
try:
	import gtk
	import gtk.glade
except:
	print "no hay librerias"

class GladeEjemploWindow:
	def __init__(self):
		#~ self.gladeFile="ejemplo1.glade"
		self.gladeFile="u.glade"
		self.builder=gtk.Builder() #es el que usa para parsear el archivo .glade
		self.builder.add_from_file(self.gladeFile)
	
		window=self.builder.get_object("MainWindow") ##tiene que ser el mismo que pusimos en la UI
		window.show_all()
		
	def onbtnClicked(self,btn): #recibo con el boton que me mando el glade
		print "se apreto el boton"
		nombre=self.builder.get_object("nombreEntry").get_text()
		carrera=self.builder.get_object("carreraEntry").get_text()
		resultado=self.builder.get_object("resultado")
		text="Nombre: "+ nombre + " Carrera: "+ carrera
		resultado.set_text(text)
		
if __name__ == "__main__":
	gew=GladeEjemploWindow()	#glade ejemplo windowd
	gtk.main()
	sys.exit(0)
	
