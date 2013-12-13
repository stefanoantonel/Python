

import argsparser
import sys
import downloader
import pygtk
import gtk


class mainn():
	def __init__(self,url,ext):
		
		#~ parser = argsparser.ArgsParser()
		#~ args = sys.argv #toma los argumentos de la consola
		if (url.startswith("www.")):
			url="http://"+ url
		if(not ext.startswith(".")):
			ext="."+ext
	
		
		if (url == "" or ext == ""):
			print "Debe informar url y extension con --url= y --ext= ."
			
		contentDownl = downloader.Downloader()
		count = contentDownl.downloadAll(url, ext)
		print "Se han descargado " + str(count) + " archivos con extension "\
		 + ext + " de la url \"" + url + "\""
		
	
	
class inputt(gtk.Window):
	
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_size_request(300, 150)
		self.connect("destroy", self.destroy)
		vbox=gtk.VBox()
		l=gtk.Label("New Downloader Manager")
		
		self.urlE=gtk.Entry()
		self.urlE.set_text("Ingrese URL")
		self.extE=gtk.Entry()
		self.extE.set_text("Ingrese Extension")
		
		btn=gtk.Button("Descargar")
		btn.connect("clicked",self.ok)
		
		vbox.add(l)
		vbox.add(self.urlE)
		vbox.add(self.extE)
		vbox.add(btn)
		self.add(vbox)
		
		self.show_all()
		gtk.main()
		
	def ok(self,event):
		ma=mainn(self.urlE.get_text(),self.extE.get_text())
		
		
if __name__ == '__main__':
	inp=inputt()
	#~ main()

