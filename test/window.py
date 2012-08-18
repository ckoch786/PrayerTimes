#!/usr/bin/env python
import gtk
import test
class Win (gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_title("Prayer Times")
        self.connect("delete-event", self.delete_event)
        #create a virtical box to hold some widgets
        vbox = gtk.VBox(False)
        #create a label to say *something* and add to the vbox
        date = test.get_date()
        prayer_times = '\n'.join(self.display_prayer_times())
        label=gtk.Label(date)
        label2=gtk.Label(prayer_times)
        vbox.pack_start(label)
        vbox.pack_start(label2)
        
        #make a quit button
        quitbutton = gtk.Button("Quit")
        quitbutton.connect("clicked",self.quit)
        #add the quitbutton to the vbox
        vbox.pack_start(quitbutton)
  
        #add the vbox to the Window
        self.add(vbox)
        #show all of the stuff
        self.show_all()
        #make a status icon
        self.statusicon = gtk.status_icon_new_from_file("minbar.svg")
        
        # check if window is visible
        #if self.get_property("visible"):
            #self.statusicon.connect('activate', self.delete_event )
        #elif self.get_property("invisible"):
           # self.statusicon.connect('activate', self.status_clicked )
           # self.statusicon.set_tooltip("minimize")
            
       # else:
        self.statusicon.connect('activate', self.show_hide )
        self.statusicon.set_tooltip("minimize")
            
        #start the gtk main loop
        gtk.main()
    
    def quit(self,button):
        #quit the gtk main loop
        gtk.main_quit()
    
    def delete_event(self,window,event):
        #don't delete; hide instead
        self.hide_on_delete()
        times = '\n'.join(self.display_prayer_times())
        self.statusicon.set_tooltip(times )
        return True
        
    def status_clicked(self,status):
        #unhide the window
        self.show_all()
        self.statusicon.set_tooltip("minimize")
    
    def display_prayer_times(self):
        prayer_times = []
        prayer_times = test.get_prayer_times()
        return prayer_times
                
        
if __name__=="__main__":
    win = Win()
