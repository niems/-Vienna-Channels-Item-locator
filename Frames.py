import sys
import tkinter
from tkinter import ttk
from tkinter import Image
from tkinter import messagebox
from ItemStorage import ItemStorage
from StyleConfig import StyleConfig
from Files import Files

class Frames(object):
    def __init__(self, root_window):
        self.styles = StyleConfig('default') #holds the style of all objects
        self.items = ItemStorage() #stores the items for all objects
        self.root = root_window #holds the root window
        self.root_notebook = '' #stores the notbook that's attached to root

        self.new_items_frame = '' #main frame for adding items. Has entry frame
                                  #tree frame inside

        self.entry_frame = '' #stores the data for the entry fields frame
        self.location_label = '' #^stores the label for the location
        self.sn_label = '' #^stores the label for the serial number

        self.tree_frame = '' #stores the treeview
        self.tree_closed_toggle = False #True if treeview is toggled closed

        self.search_frame = '' #stores the frame and treeview to search through
        self.search_image = '' #stores the image used in the search label
        self.search_label = '' #stores the label in the searching frame


    def location_to_sn_entry(self, event): #if valid location, moves focus to sn field
        if self.items.location_entry_field.get() == '': #no location given
            messagebox.showinfo(message = 'Enter a location to proceed.',
                                title = 'Error')

        else:
            self.items.sn_entry_field.focus() #moves focus to next field

        return None

    def tree_toggle(self): #toggles treeview branches between expanded and collapsed

        if self.tree_closed_toggle: #treeview is closed, so expand it
            self.items.treeExpand()
            self.tree_closed_toggle = False

        else: #treeview is open, so close it
            self.items.treeCollapse()
            self.tree_closed_toggle = True

        return None

    def setup_root(self):
        self.root.geometry('500x650')
        self.root.title('Item Locator')
        self.root.wm_iconbitmap('images\\vienna_channels.ico')
        self.root['bg'] = '#000000' #test

        self.root.grid_columnconfigure( 0, weight = 1 )
        self.root.grid_rowconfigure( 0, weight = 1 )

        self.root_notebook = ttk.Notebook(self.root) #holds the tabs for root
        self.root_notebook.grid_rowconfigure(0, weight = 1)
        self.root_notebook.grid_columnconfigure(0, weight = 1)

        #toggles the treeview branches between expanded and collapsed
        self.root.bind('<Control_L>',
                        lambda e: self.tree_toggle() )

        return None

    def setup_tree_frame(self):
        self.tree_frame = ttk.Frame(self.new_items_frame,
                                     style = 'NTreeview.Treeview')

        self.tree_frame.grid( row = 2, column = 0,
                              sticky = ('N', 'W', 'E', 'S') )

        self.tree_frame.grid_columnconfigure(1, weight = 1)
        self.tree_frame.grid_rowconfigure(1, weight = 1)
        self.items.setup_treeview(self.styles, self.tree_frame)

        return None

    def setup_entry_frame(self):
        self.entry_frame = ttk.Frame(self.new_items_frame,
                                     style = 'Entry.TFrame')

        self.entry_frame.grid( row = 1, column = 0,
                               sticky = ('N', 'W', 'E', 'S') )

        self.entry_frame.grid_columnconfigure(2, weight = 1)
        self.location_label = ttk.Label(self.entry_frame,
                                        text = 'Location: ',
                                        style = 'NLabel.TLabel' )

        self.location_label.grid(row = 1,
                                 column = 1,
                                 sticky = ('W', 'E') )

        self.items.set_location_entry_field( ttk.Entry(self.entry_frame) )

        self.items.location_entry_field.grid(row = 1,
                                                   column = 2,
                                                   sticky = ('W', 'E') )

        self.sn_label = ttk.Label(self.entry_frame,
                                  text = 'New Serial Num: ',
                                  style = 'NLabel.TLabel')

        self.sn_label.grid(row = 2, column = 1, sticky = ('W', 'E') )
        self.items.set_sn_entry_field( ttk.Entry(self.entry_frame) )

        self.items.sn_entry_field.grid(row = 2, column = 2,
                                             columnspan = 4, sticky = ('W', 'E') )

        #separator between sn field and ttk separator for treeview
        ttk.Label(self.entry_frame, text = '',
                  style = 'NLabel.TLabel').grid(row = 3,
                                                column = 1,
                                                columnspan = 3,
                                                sticky = ('N', 'W', 'E', 'S') )

        ttk.Separator(self.entry_frame, orient = 'horizontal').grid(row = 4,
                                                               column = 1,
                                                               columnspan = 3,
                                                               sticky = ('N', 'W', 'E', 'S') )

        self.items.location_entry_field.bind('<Return>',
                                                   lambda e: self.location_to_sn_entry(e) )

        self.items.location_entry_field.bind('<FocusIn>',
                                             lambda e: self.location_label.configure(
                                             background = self.styles.config.lookup('field_active_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_active_label_color', 'foreground') ) )

        self.items.location_entry_field.bind('<FocusOut>',
                                             lambda e: self.location_label.configure(
                                             background = self.styles.config.lookup('field_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_label_color', 'foreground') ) )

        self.items.sn_entry_field.bind('<Return>',
                                             lambda e: self.items.user_validate(e) )

        self.items.sn_entry_field.bind('<FocusIn>',
                                             lambda e: self.sn_label.configure(
                                             background = self.styles.config.lookup('field_active_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_active_label_color', 'foreground') ) )

        self.items.sn_entry_field.bind('<FocusOut>',
                                             lambda e: self.sn_label.configure(
                                             background = self.styles.config.lookup('field_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_label_color', 'foreground') ) )
        return None

    def setup_search_frame(self):
        self.search_frame = ttk.Frame(self.root_notebook,
                                      padding = '10 5 10 5',
                                      style = 'NFrame.TFrame')

        self.search_frame.grid(row = 0,
                               column = 0,
                               sticky = ('N', 'W', 'E', 'S') )

        self.search_frame.grid_columnconfigure(1, weight = 1)
        self.search_frame.grid_columnconfigure(2, weight = 1)

        self.search_label = ttk.Label(self.search_frame,
                                      text = 'Search Serial Num: ',
                                      compound = tkinter.RIGHT,
                                      style = 'NLabel.TLabel')

        self.search_image = tkinter.PhotoImage(master = self.search_label,
                                               file = 'images\\search.gif')

        self.search_label['image'] = self.search_image
        self.search_label.grid(row = 1, column = 1,
                               sticky = ('W', 'E'), columnspan = 5)

        self.items.set_search_entry_field( ttk.Entry(self.search_frame) )

        self.items.search_entry_field.grid(row = 1,
                                                 column = 2,
                                                 sticky = ('W', 'E'),
                                                 columnspan = 4)

        self.items.search_entry_field.bind('<Return>',
                                                 lambda e: self.items.itemSearch(e) )

        self.items.search_entry_field.bind('<FocusIn>',
                                             lambda e: self.search_label.configure(
                                             background = self.styles.config.lookup('field_active_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_active_label_color', 'foreground') ) )

        self.items.search_entry_field.bind('<FocusOut>',
                                             lambda e: self.search_label.configure(
                                             background = self.styles.config.lookup('field_label_color', 'background'),
                                             foreground = self.styles.config.lookup('field_label_color', 'foreground') ) )
        return None

    def setup_menu(self): #sets up menu items for root
        files = Files()
        user = '|   USER    |'
        dev =  '|    DEV    |'

        self.root.option_add('*tearOff', False) #removes the -- from menu options
        menubar = tkinter.Menu(self.root) #creates menu widget
        self.root['menu'] = menubar #attaches menu widget to root

        user_menu = tkinter.Menu(menubar) #creates a menu widget for user menu
        menubar.add_cascade(menu = user_menu, label = user) #adds to menubar

        user_menu.add_command(label = 'New', command = self.items.killTree )
        user_menu.add_command(label = 'Open',
                              command = lambda : files.load_file(self.items) )
        user_menu.add_command(label = 'Save',
                              command = lambda : files.save_file(self.items) )
        user_menu.add_separator()
        user_menu.add_command(label = 'Exit', command = sys.exit)


        dev_menu = tkinter.Menu(menubar) #creates menu widget for dev menu
        menubar.add_cascade(menu = dev_menu, label = dev) #adds menu to menubar

        dev_menu.add_command(label = 'Erase All Data',
                             command = self.items.killTree )
        dev_menu.add_command(label = 'Generate Data',
                             command = self.items.generateTree )
        dev_menu.add_separator()
        dev_menu.add_command(label = 'Exit', command = sys.exit)

        return None

    def setup_new_items_frame(self):
        self.new_items_frame = ttk.Frame(self.root_notebook,
                                         padding = '10 5 10 5',
                                         style = 'NFrame.TFrame')

        self.new_items_frame.grid(row = 0, column = 0,
                                  sticky = ('N', 'E', 'W', 'S') )

        self.new_items_frame.grid_columnconfigure(0, weight = 1) #for both frames
        self.new_items_frame.grid_rowconfigure(1, weight = 1) #for entry frame
        self.new_items_frame.grid_rowconfigure(2, weight = 6) #for treeview frame

        self.setup_tree_frame() #sets up the tree frame with treeview object
        self.setup_entry_frame() #sets up the entry frame with all objects
        self.setup_search_frame() #sets up search frame with all objects

        self.root_notebook.add(self.new_items_frame, text = 'New Inventory')
        self.root_notebook.add(self.search_frame, text = 'Search Inventory')
        self.root_notebook.grid(row = 0, column = 0,
                                sticky = ('N', 'W', 'E', 'S'),
                                padx = 5, pady = 3,
                                ipadx = 10, ipady = 2)

        self.setup_menu() #sets menu items up on root

        return None

    def setup_all_frames(self):
        self.setup_root() #sets up root window
        self.setup_new_items_frame() #sets up all frames inside root

        return None
