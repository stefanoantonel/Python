#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
		vb = gtk.VBox()
		self.add(vb)
		#itemBarra={"_File",{{"_Save",self.save},{"", None},{"_Quit", self.destroy}}}
		
		itemBarra={"_File": {
			"_Save": self.save,
			"": None,
			"_Quit": self.destroy},
		"_Edit": {"_Copy": self.copy,
			"_Cut": self.cut,
			"_Paste": self.paste},
			#~ "": None,
			#~ "_Preferences": "edit_pref"},
		"_Help": {"_About": about_window}}
		
		barra = barraHerramientas()
		
		barra.add_items(itemBarra)
		vb.pack_start(barra, expand = False)
		
		# subdivisor para editor/archivos
		hp = gtk.HPaned()
		vb.pack_start(hp, expand = False)
		
		l = gtk.Label("Espacio panel izquierdo")
		f1 = gtk.Frame()
		f1.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		f1.add(l)
		hp.add1(f1)
		
		self.ed_mgr = editor_mgr.editor_manager()
		self.editor=self.ed_mgr.add_editor("Inicial")
		f2 = gtk.Frame()
		f2.set_shadow_type(gtk.SHADOW_ETCHED_IN)
		f2.add(self.ed_mgr)
		hp.add2(f2)
		
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
		import pdb; pdb.set_trace()
		buff = self.editor.get_buffer()
		startIter = buff.get_start_iter()
		endIter = buff.get_end_iter()
		text= self.editor.get_buffer().get_text(startIter,endIter)
		openfile = open(filename,"w")
		openfile.write(text)
		openfile.close() 

	def run(self):
		gtk.main()

def main():
	w = main_window()
	w.run()
		
	return 0

if __name__ == '__main__':
	main()
