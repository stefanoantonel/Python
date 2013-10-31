#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygtk
import gtk,gobject
import gtk.glade

class GladeEjemploWindow:
	def __init__(self):
		self.lista=[]
		mylist = [("1", "4", "2"),("1", "2", "2")]
		mylist.sort()
		
		self.left=gtk.TreeView()
		self.gladeFile = "practico2.glade"
		self.builder = gtk.Builder() 
		self.builder.add_from_file(self.gladeFile) 
		handlers={
			"buttonClicked": self.onbtnClicked,
		}
		self.builder.connect_signals(handlers)
		self.tree= self.builder.get_object("tablaContactos")
		self.model=gtk.TreeStore(gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING)
		
		cella = gtk.CellRendererText()
		col1=gtk.TreeViewColumn("Apellido ",cella)
		col1.add_attribute(cella,"text",0)
		
		
		celln = gtk.CellRendererText()
		col2=gtk.TreeViewColumn("Nombre ",celln)
		col2.add_attribute(celln,"text",1)
		
		cellt = gtk.CellRendererText()
		col3=gtk.TreeViewColumn("Telefono ",cellt)
		col3.add_attribute(cellt,"text",2)
		
		col2.set_sort_column_id(1)
		
		self.tree.append_column(col1)
		self.tree.append_column(col2)
		self.tree.append_column(col3)

		self.tree.set_model(self.model)
		
		self.window = self.builder.get_object("MainWindow")  
		self.window.show_all()
		
	def errorCartel(self,widget,mnj):
		print "error"
		md = gtk.MessageDialog(widget, 
				gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
				gtk.BUTTONS_CLOSE, mnj)
		md.run()
		md.destroy()
		
	def onbtnClicked(self, btn):
		print "btn"
		apellido=self.builder.get_object("txtApellido").get_text()
		nombre=self.builder.get_object("txtNombre").get_text()
		telefono=self.builder.get_object("txtTelefono").get_text()
		print apellido
		if apellido == "" or nombre == "" or telefono == "":
			self.errorCartel(self.window,"FALTA COMPLETAR DATOS")
		else:
			person = apellido,nombre,telefono
			self.lista.append(person)
			print self.lista
			self.lista.sort()
			self.model=gtk.TreeStore(gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING)
			for per in self.lista:
				self.model.append(None,per)
			self.tree.set_model(self.model)
if __name__ == "__main__":  #unicamente tiene nombre main si la ejecuto, si la importo no
	gew = GladeEjemploWindow()
	gtk.main()
	
	
