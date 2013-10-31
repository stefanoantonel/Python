#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_win.py
#  
#  Copyright 2013 John Coppens <john@jcoppens.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pdb
import pygtk
import gtk
import gtksourceview2 as gtksv
import preferences as pref
import editor_mgr
import os.path as osp

pref_fn = osp.expanduser("~/.aula.config")

class about_window(gtk.MessageDialog):
    def __init__(self, event):
        gtk.MessageDialog.__init__(self, flags = gtk.DIALOG_MODAL, 
                                         buttons = gtk.BUTTONS_OK, 
                                         message_format = "(c) John Coppens")
        
        self.show_all()
        if self.run():
            self.destroy()
        

class main_menu(gtk.MenuBar):
    def __init__(self):
        gtk.MenuBar.__init__(self)
        
        fileitem = gtk.MenuItem("_File")
        filemenu = gtk.Menu()
        fileitem.set_submenu(filemenu)
        print "hola"
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
        
        mnu = main_menu()
        vb.pack_start(mnu, expand = False)
        
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
        pdb.set_trace()
        
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
