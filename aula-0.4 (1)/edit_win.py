#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  edit_win.py
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
import gtksourceview2 as gtksv
import gobject

class timeout():
    """ Timeout: cuando se instancia esta clase, se inicia un timer
        que puede resetearse repetidamente llamando a 'tick'.
        Si el timer llega a cero, llamara al metodo 'callback'
        Uso:
          tmr = timeout(10, callbackfunc)
          (10 es el tiempo en decimas de segundo)
    """
    def __init__(self, period, callback):
        self.period = period
        self.callback = callback
        self.timer = gobject.timeout_add(100, self.ticks)
        
    def tick(self):
        self.count = self.period;
        
    def ticks(self):
        self.count -= 1
        if self.count == 0:
            self.callback()
        return True

class edit_window(gtksv.View):
    """ Encargada de realizar la ventana, y crear el buffer de
        texto correspondiente. Luego agregaremos manejo de archivos...
    """
    def __init__(self):
        self.bff = gtksv.Buffer()
        gtksv.View.__init__(self, self.bff)
        
        self.set_show_line_numbers(True)
        self.bff.connect("changed", self.modified)

    def modified(self, event):
        """ Este evento es llamado cada vez que se detecta un cambio
            en el editor. Cuando no hay cambios en el plazo previsto,
            entonces se llamara al siguiente metodo, quien se
            podrá encargar de distribuir el contendio.
        """
        try:
            self.timer
        except:
            print "+"
            self.timer = timeout(19, self.timedout)
        self.timer.tick()
        
    def timedout(self):
        print "Timed out"

def main():
    w = gtk.Window()
    e = edit_window()
    w.add(e)
    
    w.show_all()
    gtk.main()
    return 0

if __name__ == '__main__':
    main()

