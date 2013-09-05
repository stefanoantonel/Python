#!/usr/bin/env python

import pygtk
import gtk
import wheathermap

class WeatherForm(gtk.Window):

    def destroy(self, wdw):
	""" Cuando este metodo es llamado, abortara el lazo principal (gtk.main)
	    y terminara completamente la ejecucion (control vuelve a la terminal
	    o al sistema operativo segun como se llamo al programa.
	"""
	gtk.main_quit()
        
    def __init__(self):
	""" En el constructor, haremos la composicion del dialogo de ingreso
	    de datos. Al final, se ejecuta a gtk.main(), por lo que el constructor
	    no vuelva al llamador hasta que destrye.
	"""
        gtk.Window.__init__(self)
        
        # Antes de todo, conectaremos un metodo para abortar el lazo principal
        # El metodo lo definimos mas abajo en la misma clase
        self.connect("destroy", self.destroy)
        
        vbox1 = gtk.VBox()
        self.add(vbox1)
        
        l = gtk.Label("A label - Aqui ira el menu...")
        vbox1.pack_start(l)
        
        # VBox para organizar el area de trabajo
        vbox_work = gtk.VBox()
        vbox1.pack_start(vbox_work)
        
        # En la parte superior, un Table para poner los campos de edicion
        tbl = gtk.Table()
        vbox_work.pack_start(tbl)
        
        # Las dos etiquetas de la izquierda:
        l = gtk.Label("Ciudad:")
        tbl.attach(l, 0, 1, 0, 1, xoptions = gtk.FILL, yoptions = gtk.FILL)
        l = gtk.Label("Campo a interrogar:")
        tbl.attach(l, 0, 1, 1, 2, xoptions = gtk.FILL, yoptions = gtk.FILL)
        l = gtk.Label("Temperatura:")
        tbl.attach(l, 0, 1, 2, 3, xoptions = gtk.FILL, yoptions = gtk.FILL)
        self.l = gtk.Label() ## es donde voy a setear la temp que e vino
        tbl.attach(self.l, 0, 2, 2, 3, xoptions = gtk.FILL, yoptions = gtk.FILL)
        
        # Los dos campos de ingreso de datos:
        self.entry_city = gtk.Entry() # le tengo que poner self para que este disponible para toda la clase
        tbl.attach(self.entry_city,  1, 2, 0, 1, xoptions = gtk.FILL, yoptions = gtk.FILL)
        self.entry_field = gtk.Entry()
        tbl.attach(self.entry_field, 1, 2, 1, 2, xoptions = gtk.FILL, yoptions = gtk.FILL)
        
        # El boton de busqueda
        btn = gtk.Button("Buscar")
        btn.set_tooltip_text("Oprimir para activar la busqueda")
        btn.set_size_request(90, -1)
        btn.connect("clicked", self.search)
        tbl.attach(btn, 2, 3, 0, 2, xoptions = gtk.FILL, yoptions = gtk.FILL)
        
        self.show_all()
        gtk.main()
		
    def search(self, btn):
		lugar=self.entry_city.get_text()
		unidad=self.entry_field.get_text()
		print lugar
		print unidad
		w=wheathermap.Weather()
		temp=w.print_weather(lugar, unidad)
		print "Boton cliqueado"
		
		self.l.set_text(temp)
	
        
        
def main():
    w = WeatherForm()
    
 
main()
