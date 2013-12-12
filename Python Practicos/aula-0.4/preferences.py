#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gtk
import pygtk
import json

class button_box(gtk.HBox):
    """ A horizontal box with buttons. 
        The buttons are right-justified (and the left is filled
        with an expanding (empty) label.
        Default size is 80 pixels
        The constructor receives the definitions as a list of
        tuples, each with the button's label and the function to
        be called on activation.
    """
    def __init__(self, buttons, size = 80):
        gtk.HBox.__init__(self)
        self.set_spacing(4)
        self.set_border_width(2)
        self.pack_start(gtk.Label(" "))
        
        # Show the buttons
        for button in buttons:
            b = gtk.Button(button[0])
            b.connect("clicked", button[1])
            self.pack_start(b)
            

class pref_window(gtk.Window):
    """ Window to edit preferences
        The constructor receives the actual parameters in a dictionary
        and automatically organizes them, a category per page
    """
    def __init__(self, params):
        gtk.Window.__init__(self)
        
        self.connect("delete-event", self.on_destroy)
        self.set_modal(True)
        self.set_size_request(250, 150)
            
        vb = gtk.VBox()
        self.add(vb)
            
        self.cat_nb = gtk.Notebook()    # Categories
        vb.pack_start(self.cat_nb)
        
        hb = button_box((("Cancel", self.cancel), 
                         ("Ok", self.accept)))
        vb.pack_start(hb, expand = False)
        
        for cat in params:
            self.cat_nb.append_page(self.param_page(params[cat]), gtk.Label(cat))
            

    def param_page(self, params):
        """ Add a single page to the notebook ( = one category )
            The function receives the definition as a branch from
            the original tree
        """
        tbl = gtk.Table()
        tbl.set_border_width(6)
        tbl.set_row_spacings(4)
        tbl.set_col_spacings(8)
        y = 0

        for param in params:
            l = gtk.Label(param)
            tbl.attach(l, 0, 1, y, y+1, yoptions = gtk.FILL)
            if params[param][0] == 'e':
                w = gtk.Entry()
                w.set_text(params[param][1])
            elif params[param][0] == 'c':
                w = gtk.CheckButton("")
            elif params[param][0] == 's':
                adj = gtk.Adjustment(lower=0, upper=9999, step_incr=1, 
                                     page_size=10)
                w = gtk.SpinButton(adj)
            tbl.attach(w, 1, 2, y, y+1, yoptions = gtk.FILL)
            y += 1
        return tbl
  
    def run(self):
        self.show_all()
        gtk.main()
        self.destroy()
        return self.result
        
    def accept(self, event):
        """ Method called when the Accept button is pressed
        """
        self.result = True
        gtk.main_quit()
        
    def cancel(self, event):
        """ Method called when the Cancel button is pressed
        """
        self.result = False
        try:
            json.load(self.pref_fn)
        except:
            gtk.main_quit()
        
    def on_destroy(self, event, par):
        """ Method called when the window is closed forcibly
        """
        self.result = None
        gtk.main_quit()


class preferences():
    def __init__(self, fname):
        self.params = dict()            # Empty dictionary for the parameters
        self.pref_fn = fname
       
    def get(self, cat, key):
        try:
            return self.params[cat][key][2]     # Return real value if it exists
        except:
            return self.params[cat][key][1]     # Return default value
            
    def add_category(self, new_cats):
        for cat in new_cats.keys():
            self.params[cat] = new_cats[cat]
         
    def load(self):
        try:
            json.load(self.pref_fn)
        except:
            print "Cannot open the preferences, using defaults"
            self.params = dict()
        
    def save(self):
        try:
            json.dump(self.pref_fn)
        except:
            print "Cannot save the preferences. Permissions problem?"
            
    def edit(self):
        pref_edit = pref_window(self.params)
        return pref_edit.run()


def main():
    cat1 = {"Cat1": {"Par_1_1": ["e", "Default"],
                     "Par_1_2": ["e", "1234"]}
           }
    cat2 = {"Cat2": {"Par_2_1": ["e", "Default"],
                     "Par_2_2": ["s", "1234"],
                     "Par_2_3": ["c", True]},
            "Cat3": {"Par_3_1": ["e", "Default"],
                     "Par_3_3": ["c", True]}
           }
           
    prefs = preferences("/tmp/test_prefs")
    prefs.add_category(cat1)
    prefs.add_category(cat2)
    
    print "%s should be 1234" % prefs.get("Cat2", "Par_2_2")
    print "%s should be Default" % prefs.get("Cat3", "Par_3_1")
    
    if prefs.edit():
        print "Ok pressed"
                
    return 0

if __name__ == '__main__':
    main()

