import pygtk
import gtk

class miVentana(gtk.Window):
	
	def terminar(self, event):
		gtk.main_quit()
		
	def __init__(self):
		gtk.Window.__init__(self)
		self.connect("destroy",self.terminar) 
		#cuando presione el boton de X de la ventana me termina 
		hb=gtk.HBox() 
		#es una caja horiontal que me divide la ventana en 2 
		self.add(hb)
		
		#~ vamos a crear el treeview que se conecta con una base de datos, gtk tiene una base de datos chiquita.
		self.left=gtk.TreeView()
		hb.pack_start(self.left)
		
		self.right=gtk.TreeView()
		hb.pack_start(self.right)
		
		self.show_all()
		
		
	def l_columnas (self,cols): 
		#vamos a pasarle a esta funcion una lista con los nombres de la colmna que queremos hacer.
		types=(str,)*len(cols) 
		#multiplicamos la tupla (,) por lo que me pasa por parametro.
		print types
		self.left_store=gtk.ListStore(*types) 	
		#el ListStore es para hacer columnas para la base de datos.
		# el * remieve los parentesis de la tupla.
		
		for i in range(len(cols)):
		#me genera 0,1,2
			render=gtk.CellRendererText()
			#es el que sabe dibujar y que entiende los tamanos de las celdas y se comunica con el dueno de la celda
			#si tenemos que hcer algo ams
			col=gtk.TreeViewColumn(cols[i],render, text=i)
			#que el texto lo busque en el campo i de la BD
			self.left.append_column(col)
		
		self.left.set_model(self.left_store)

		
	def l_agregar_fila(self,person):
		#~ iter=self.left_store.append(person)
		#~ self.left_store.set(iter, 1,"Cambiado")
		self.left_store.append(person)
	
	def r_columnas (self,cols): 
		#vamos a pasarle a esta funcion una lista con los nombres de la colmna que queremos hacer.
		types=(str,)*len(cols) 
		#multiplicamos la tupla (,) por lo que me pasa por parametro.
		print types
		self.right_store=gtk.TreeStore(*types) 	
		#el ListStore es para hacer columnas para la base de datos.
		# el * remieve los parentesis de la tupla.
		
		for i in range(len(cols)):
		#me genera 0,1,2
			render=gtk.CellRendererText()
			#es el que sabe dibujar y que entiende los tamanos de las celdas y se comunica con el dueno de la celda
			#si tenemos que hcer algo ams
			col=gtk.TreeViewColumn(cols[i],render, text=i)
			#que el texto lo busque en el campo i de la BD
			self.right.append_column(col)
		
		self.right.set_model(self.right_store)
		
		
	def run(self):
		gtk.main() #esto es para que corraa  
		
	

def main():
	miv=miVentana()
	miv.l_columnas(("Fecha","Tarea","Responsable"))
	
	for person in [	["2013/09/05","Clases","John"],
					["2013/09/05","Practico","Fede"]]:
						#el for itera sobre toda la tupla de una, no cada elemento
						miv.l_agregar_fila(person)
	#le pasamos una tupla.
	miv.r_columnas(("Archivo","Fecha"))
	miv.run()
	return 0

if __name__ == '__main__':
	main()

