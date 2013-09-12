#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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
 
import pygtk
import gtk
 
class Responsables(gtk.TreeView):
    def __init__(self):
        gtk.TreeView.__init__(self)
       
    def columnas(self, cols):
        types = (str,) * len(cols)
        self.store = gtk.ListStore(*types)
       
        for i in range(len(cols)):
            renderer = gtk.CellRendererText()
            col = gtk.TreeViewColumn(cols[i], renderer, text=i)
            self.append_column(col)
           
        self.set_model(self.store)
       
    def agregar_fila(self, person):
        self.store.append(person)
     
class Directory(gtk.TreeView):
    def columnas(self, cols):
        types = (str,) * len(cols)
        self.store = gtk.TreeStore(*types)
       
        for i in range(len(cols)):
            renderer = gtk.CellRendererText()
            col = gtk.TreeViewColumn(cols[i], renderer, text=i)
            self.append_column(col)
           
        self.set_model(self.store)
       
       
 
class MiVentana (gtk.Window):
    def terminar(self, event):
        gtk.main_quit()
       
    def __init__(self):
        gtk.Window.__init__(self)
       
        self.connect("destroy", self.terminar)
       
        hb = gtk.HBox()
        self.add(hb)
       
        self.left = Responsables()
        self.left.columnas(("Fecha", "Tarea", "Respnsable"))
        hb.pack_start(self.left)
       
        sep = gtk.VSeparator()
        hb.pack_start(sep)
       
        self.right = Directory()
        self.right.columnas(("Archivo", "fecha"))
       
        hb.pack_start(self.right)
       
        self.show_all()
       
       
    def agregar_persona(self, persona):
        self.left.agregar_fila(persona);
       
    def run(self):
        gtk.main()
       
       
       
def main():
        miv = MiVentana()
       
        for person in [["2013/09/05", "Clases", "John"],
                       ["2013/09/05", "Practico", "Alumnos"]]:
            miv.agregar_persona(person)
           
        miv.run()
        return 0
 
if __name__ == '__main__':
        main()
