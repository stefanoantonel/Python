#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_win.py


import pygtk
import gtk
import gtksourceview2 as gtksv
import preferences as pref
import editor_mgr
import os.path as osp
from preferences import *

pref_fn = osp.expanduser("~/.aula.config")

class about_window(gtk.MessageDialog):
	def __init__(self, event):
		gtk.MessageDialog.__init__(self, flags = gtk.DIALOG_MODAL, 
										 buttons = gtk.BUTTONS_OK, 
										 message_format = "(c) John Coppens")
										 
		
		self.show_all()
		if self.run():
			self.destroy()
		
		
class barraHerramientas(gtk.MenuBar):
	def __init__(self):
		self.params = dict()            # Empty dictionary for the parameters
		#~ self.pref_fn = fname
		gtk.MenuBar.__init__(self)
		
	   
	def get(self, cat, key):
		try:
			return self.params[cat][key][2]     # Return real value if it exists
		except:
			return self.params[cat][key][1]     # Return default value
			
	def add_items(self, items):
		
		for i in items.keys():
			menuVertical = gtk.Menu()
			fileitem = gtk.MenuItem(i)
			fileitem.set_submenu(menuVertical)
			subItems= items[i]
			for sItem in sorted(subItems.keys()):
				if(sItem ==""):
					subItem= gtk.SeparatorMenuItem()
				else:
					subItem= gtk.MenuItem(sItem)
					subItem.connect("activate",subItems[sItem])
				menuVertical.append(subItem)
			self.append(fileitem)
	


class main_menu(gtk.MenuBar):
	def __init__(self):
		gtk.MenuBar.__init__(self)
		
		
		fileitem = gtk.MenuItem("_File")
		filemenu = gtk.Menu()
		fileitem.set_submenu(filemenu)
		
		fopen = gtk.MenuItem("_Open")
		fsave = gtk.MenuItem("_Save")
		fquit = gtk.MenuItem("_Quit")
		filemenu.append(fopen)
		filemenu.append(fsave)
		filemenu.append(gtk.SeparatorMenuItem())
		filemenu.append(fquit)
		fquit.connect("activate", gtk.main_quit)
		
		helpitem = gtk.MenuItem("_Help")
		helpmenu = gtk.Menu()
		helpitem.set_submenu(helpmenu)
		
		habout = gtk.MenuItem("_About")
		habout.connect("activate", about_window)
		helpmenu.append(habout)
		
		self.append(fileitem)
		self.append(helpitem)
		
 
class main_window(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.connect("destroy", self.destroy)
		
		self.preferences = pref.preferences(pref_fn)
		 
		# subdivisor para menu y resto
		vb = gtk.VBox() #contenedor de TODO
		self.add(vb)
		#itemBarra={"_File",{{"_Save",self.save},{"", None},{"_Quit", self.destroy}}}
		
		itemBarra={"_File":	{
							"_Save": self.save,
							"": None,
							"_Quit": self.destroy,
							"_New": self.new,
							"_Open": self.openn
							},
					"_Edit":{
							"_Copy": self.copy,
							"_Cut": self.cut,
							"_Paste": self.paste
							},
			
					"_Help": {"_About": about_window}
					}
		
		barra = barraHerramientas()
		barra.add_items(itemBarra)
		vb.pack_start(barra, expand = False) 
		
		# subdivisor para editor/archivos
		self.hp = gtk.HPaned() 
		
		#~ vb.pack_start(hp, expand = False)
		vb.add(self.hp)
		
		l = gtk.Label("Espacio panel izquierdo")
		f1 = gtk.Frame()
		f1.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		f1.add(l)
		#~ hp.add1(f1)
		self.hp.add(f1)
		
		self.f2 = gtk.Frame()
		self.f2.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		self.ed_mgr = editor_mgr.editor_manager() # el notebook contenedor de pages(editors)
		
		# al notebook le agrega las paginas
		editor=self.ed_mgr.add_editor("Incial")
		self.editorActual=editor
		
		self.f2.add(self.ed_mgr) #agrega el notebook al paned
		self.hp.add(self.f2)
		self.show_all()
		
	def destroy(self, event):
		gtk.main_quit()
		
		
	def copy(self, event):
		buff=self.editor.get_buffer()
		buff.copy_clipboard(gtk.Clipboard())
	
	def cut(self, event):
		buff = self.editor.get_buffer()
		editable = self.editor.get_editable()
		buff.cut_clipboard(gtk.Clipboard(), editable)
		
	def paste(self, event):
		buff = self.editor.get_buffer()
		editable = self.editor.get_editable()
		pos = buff.get_iter_at_mark(buff.get_insert())
		buff.paste_clipboard(gtk.Clipboard(), pos, editable)
		
	def save(self,event):
		filename = None
		chooser = gtk.FileChooserDialog("Save File...", None,gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		
		response = chooser.run()
		if response == gtk.RESPONSE_OK: 
			filename = chooser.get_filename()
			chooser.destroy()
		buff = self.editorActual.get_buffer() #obtengo buffer del actual 
		startIter = buff.get_start_iter()
		endIter = buff.get_end_iter()
		text= self.editorActual.get_buffer().get_text(startIter,endIter)
		print ("texto nuevo:"+str(text))
		openfile = open(filename,"w")
		openfile.write(text)
		openfile.close() 
		
		#cambio el nombre del tab con el guardado recien
		arrayPath=filename.split("/")
		
		#~ print (arrayPath[-1])
		
		fileNameSaved = filename.split("/")[-1]
		self.ed_mgr.set_title(fileNameSaved)
		
	def new(self,event):
		self.editor3=self.ed_mgr.add_editor("NUEVO")
		self.f2.add(self.editor3)
		self.hp.add(self.f2)
		self.show_all()
		
	def run(self):
		gtk.main()
		
	def openn(self,event):
		chooser = gtk.FileChooserDialog("Open File...", None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		response = chooser.run()
		if response == gtk.RESPONSE_OK: 
			filename = chooser.get_filename()
			chooser.destroy()
		openfile = open(filename,"r")
		textOpen=openfile.read() #saco el contenido del file
		openfile.close()
		#agregar la tab 
		filename=filename.split("/")[-1]
		editorNew=self.ed_mgr.add_editor(filename)
		editorNew.get_buffer().set_text(textOpen)
		self.editorActual=editorNew
		
		self.show_all()
		

def main():
	w = main_window()
	w.run()
		
	return 0

if __name__ == '__main__':
	main()
