#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
import gtk
import gtksourceview2 as gtksv
import editor_mgr

class main_window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect("destroy", self.destroy)
        
        # subdivisor para menu y resto
        vb = gtk.VBox()
        self.add(vb)
        
        l = gtk.Label("Espacio para menu")
        vb.pack_start(l, expand = False)
        
        # subdivisor para editor/archivos
        hp = gtk.HPaned()
        vb.pack_start(hp, expand = False)
        
        l = gtk.Label("Espacio panel izquierdo")
        f1 = gtk.Frame()
        f1.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        f1.add(l)
        hp.add1(f1)
        
        self.ed_mgr = editor_mgr.editor_manager()
        self.ed_mgr.add_editor("Inicial")
        f2 = gtk.Frame()
        f2.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        f2.add(self.ed_mgr)
        hp.add2(f2)
        
        self.show_all()
        
    def destroy(self, event):
        gtk.main_quit()
        
    def run(self):
        gtk.main()

def main():
	w = main_window()
        w.run()
        
	return 0

if __name__ == '__main__':
	main()

