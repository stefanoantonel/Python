#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  edit_mgr.py
#  

import pygtk
import gtk
import edit_win

class editor_manager(gtk.Notebook):
	def __init__(self):
		gtk.Notebook.__init__(self)
		
		self.set_size_request(350, 300)
		
	def add_editor(self, label):
		self.new_editor = edit_win.edit_window()
		new_label = gtk.Label(label)
		#~ self.append_page(self.new_editor, new_label) #son los tab de arriba 
		#~ print(self.query_tab_label_packing(new_editor))
		
		
		hbox=self.createButton(label) 
		
		hbox.show_all()

		#the tab will have a single widget: a label
		
		
		#add the tab
		self.insert_page(self.new_editor, hbox) #widget + tabLabel
		#~ self.add(self.new_editor, hbox)
		return self.new_editor
		
		
	def createButton(self,title):
		
		#~ def create_tab(self, title):
		#hbox will be used to store a label and button, as notebook tab title
		hbox = gtk.HBox(False, 0)
		label = gtk.Label(title)
		hbox.pack_start(label)

		#get a stock close button image
		close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
		image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
		
		#make the close button
		btn = gtk.Button()
		btn.set_relief(gtk.RELIEF_NONE)
		btn.set_focus_on_click(False)
		btn.add(close_image)
		hbox.pack_start(btn, False, False)
		
		#~ #this reduces the size of the button
		style = gtk.RcStyle()
		style.xthickness = 0
		style.ythickness = 0
		btn.modify_style(style)

		
		
		#connect the close button
		
		btn.connect('clicked', self.on_closetab_button_clicked, self.new_editor)
		return hbox
	
	def on_closetab_button_clicked(self, sender, widget):
		#get the page number of the tab we wanted to close
		pagenum = self.page_num(widget)
		#and close it
		self.remove_page(pagenum)
		
	def set_title (self, label):
		#~ hbox=self.createButton("viejo") 
		hbox=self.createButton(label) 
		hbox.show_all()
		self.set_tab_label(self.get_nth_page(self.get_current_page()), hbox)

def main():
	
	return 0

if __name__ == '__main__':
	main()

