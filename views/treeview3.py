import pygtk
import gtk
import os, os.path
import time
 
class Responsables (gtk.TreeView):
    def __init__(self):
        gtk.TreeView.__init__(self)
 
    def columns(self, cols):
        types = (str,) * len(cols)
        self.store = gtk.ListStore(*types)
       
        for i in range(len(cols)):
            renderer = gtk.CellRendererText()
            col = gtk.TreeViewColumn(cols[i], renderer, text = i)
            self.append_column(col)
           
        self.set_model(self.store)
       
    def add_person(self, person):
        self.store.append(person)
       
class Directory (gtk.TreeView):
    def __init__(self):
        gtk.TreeView.__init__(self)
       
    def columns(self, cols):
        types = (str,) * len(cols)
        self.store = gtk.TreeStore(*types)
       
        for i in range(len(cols)):
            renderer = gtk.CellRendererText()
            col = gtk.TreeViewColumn(cols[i], renderer, text = i)
            col.set_sort_column_id(i)
            self.append_column(col)
           
        self.set_model(self.store)
       
    def format_file_time(self, file):
        mtime = time.localtime(os.path.getmtime(file))
        return time.strftime("%Y/%m/%d %H:%M", mtime)
       
    def fill(self, path):
        def visit(path, parent):
            os.chdir(path)
            for file in os.listdir("."):
                if os.path.isfile(file):
                    self.store.append(parent, (file, self.format_file_time(file), os.path.getsize(file)))
                elif os.path.isdir(file):
                    iter = self.store.append(parent, (file, self.format_file_time(file), ""))
                    visit(file, iter)
            os.chdir("..")
           
        visit(path, None)
       
       
class MiVentana (gtk.Window):
    def terminar(self, event):
        gtk.main_quit()
       
    def __init__(self):
        gtk.Window.__init__(self)
       
        self.connect("destroy", self.terminar)
       
        hb = gtk.HBox()
        self.add(hb)
       
        self.left = Responsables()
        sep = gtk.VSeparator()
        self.right = Directory()
 
        hb.pack_start(self.left, expand = False)
        hb.pack_start(sep, expand = False)
       
        scrw = gtk.ScrolledWindow()
        scrw.add(self.right)
        
        hb.pack_start(scrw)
       
        self.show_all()
       
    def l_columns(self, cols):
        self.left.columns(cols)
       
    def add_person(self, person):
        self.left.add_person(person)
       
    def dir_columns(self, cols):
        self.right.columns(cols)
       
    def dir_show(self, path):
        self.right.fill(path)
       
    def run(self):
        gtk.main()
       
       
def main():
        miv = MiVentana()
        miv.l_columns(("Fecha", "Tarea", "Respnsable"))
       
        for person in [["2013/09/05", "Clases", "John"],
                       ["2013/09/05", "Practico", "Alumnos"]]:
            miv.add_person(person)
           
        miv.dir_columns(("Archivo", "fecha", "Tamanio"))
       
        miv.dir_show(".") # path (direccion del directorio que mostrar)
      
        miv.run()
        return 0
 
if __name__ == '__main__':
        main()
