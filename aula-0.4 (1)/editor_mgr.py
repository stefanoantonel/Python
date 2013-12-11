#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  edit_mgr.py
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
	a=[("File"),[("Open"),("Save")]]
	for i in a[1]:
		print i
	print a
	return 0

if __name__ == '__main__':
	main()

