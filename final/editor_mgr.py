#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
import gtk
import edit_win

class editor_manager(gtk.Notebook):
    def __init__(self):
        gtk.Notebook.__init__(self)
        self.set_size_request(350, 300)
        
    def add_editor(self, label):
        new_editor = edit_win.edit_window()
        new_label = gtk.Label(label)
        self.append_page(new_editor, new_label)
        
        return new_editor

def main():
	
	return 0

if __name__ == '__main__':
	main()

