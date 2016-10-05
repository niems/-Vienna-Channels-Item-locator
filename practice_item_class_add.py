import tkinter
from tkinter import ttk
from tkinter import Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import sys
import random
from ItemStorage import ItemStorage


save_file_fields = 'Location, S/N \n'


def loadFile( Items ):

    #put in functionality that will ask the user if they want to save their data first if they have entries in sn_values and treeview.
    #after that, it will load the file.

    try:
        filename = tkinter.filedialog.askopenfile( initialdir = "/", title = "Load File", filetypes = ( ("csv files","*.csv"),("all files","*.*") ) )
        load_file = open( filename.name, 'r+' )

        Items.killTree() #clears current stored values

        for line in load_file: #goes through each line in file
            if line == '': #if line is empty (THIS WILL BREAK IF USER MANUALLY ENTERS A BLANK IN THE FILE, THEN ADDS DATA AFTERWARDS)
                break #eof

            elif line == save_file_fields:
                continue #go to the next line. These are the categories

            dict_entry = line.split( ',' )

            if len( dict_entry ) == 2:
                print(' passed sn : ' + dict_entry[1].strip() )
                entryValidate(True, Items)
                #entryValidate( True, dict_entry[0].strip(), dict_entry[1].strip(), sn_entry, sn_values, treeview )

    except Exception as e:
        print( 'Exception:{0}'.format(e) )
        messagebox.showinfo( message = 'ERROR: There is a problem loading the .csv file', title = 'ERROR: Loading file' )

        load_file.close()
    return None


def saveFile( Items ):
    try:
        filename = tkinter.filedialog.asksaveasfilename(initialdir = '/', title = 'Save File', filetypes = ( ("csv files", "*.csv"), ("all files", "*.*") ) ).strip( '.csv' ) + '.csv'

        save_file = open( filename, 'w' )
        save_file.write( save_file_fields )

        for key, val in Items.sn_values.items(): #writes each location : s/n to the file
            current_output = val.strip() + ',' + key.strip() + '\n'
            save_file.write( current_output )

        save_file.close()
    except:
        massagebox.showinfo( message = 'ERROR: There is a problem saving the .csv file.', title = 'ERROR: Saving file' )

    return None


def createroot():

    root = tkinter.Tk()
    root.geometry('500x650')
    root.title('Item Locator')
    root.wm_iconbitmap('images\\vienna_channels.ico')
    root['bg'] = '#000000' #test - should never show on root if the frame expands correctly

    root.grid_columnconfigure( 0, weight = 1 )
    root.grid_rowconfigure( 0, weight = 1 )

    available_fonts = font.families()

    #print( available_fonts )

    return root


def createMenu( root, Items ):

    user = '|   USER    |'
    dev =  '|    DEV    |'
    root.option_add( '*tearOff', False )
    menubar = tkinter.Menu( root ) #creates menu widget
    root['menu'] = menubar #attach the menu widget to the root

    user_menu = tkinter.Menu( menubar ) #create a menu widget for the user menu
    menubar.add_cascade( menu = user_menu, label = user ) #adds the user menu to the menubar

    user_menu.add_command( label = 'New', command = lambda : Items.killTree() )
    user_menu.add_command( label = 'Open', command = lambda : loadFile( Items ) )
    user_menu.add_command( label = 'Save', command = lambda : saveFile( Items ) )
    user_menu.add_separator()
    user_menu.add_command( label = 'Exit', command = sys.exit )

    dev_menu = tkinter.Menu( menubar ) #create a menu widget for the developer menu
    menubar.add_cascade( menu = dev_menu, label = dev ) #adds the dev menu to the menubar

    dev_menu.add_command( label = 'Erase All Data', command = lambda: Items.killTree() )
    dev_menu.add_command( label = 'Generate Data', command = lambda : Items.generateTree() )
    dev_menu.add_command( label = 'Debug', command = lambda : snOutputDebug( Items ) )
    dev_menu.add_separator()
    dev_menu.add_command( label = 'Exit', command = sys.exit )

    return root


def createStyles():
    treeview_header_img = tkinter.PhotoImage( file = r'images\folder_navy.gif' )

    color_main_background2 = '#BDBDBD' #500
    color_accent2 = '#00E676' #200
    color_secondary_background2 = '#212121' #900
    color_object2 = '#616161' #700
    color_field_background2 = '#F5F5F5' #100

    color_main_background = '#607D8B' #500
    color_accent = '#18FFFF' #200
    color_secondary_background = '#37474F' #800
    color_object = '#455A64' #700
    color_field_background = '#CFD8DC'

    # ------------------------------------
    #purple style
    field_bg_label_color_purple = '#494949' #'#555555'
    field_fg_label_color_purple = '#34B767' #34B767
    field_bg_active_label_color_purple = '#34B767' #color accent
    field_fg_active_label_color_purple = '#222222'
    main_frame_bg_color_purple = '#383838' #383838
    separator_color_purple = '#34B767'

    treeview_selected_item_bg_color_purple = ''
    treeview_selected_item_fg_color_purple = ''
    treeview_header_bg_color_purple = '#373737'
    treeview_header_fg_color_purple = '#309970'#34B767
    treeview_bg_color_purple = '#454545' #'#383838'
    treeview_fg_color_purple = '#34b867'#
    treeview_separator_bg_color_purple = '#5D6361'

    # ------------------------------------

    #new color theme -----------------------------------------
    field_bg_label_color = '#494949' #'#555555'
    field_fg_label_color = '#34B767' #34B767
    field_bg_active_label_color = '#34B767' #color accent
    field_fg_active_label_color = '#222222'
    main_frame_bg_color = '#383838' #383838
    separator_color = '#34B767'

    treeview_selected_item_bg_color = ''
    treeview_selected_item_fg_color = ''
    treeview_header_bg_color = '#373737'
    treeview_header_fg_color = '#309970'#34B767
    treeview_bg_color = '#454545' #'#383838'
    treeview_fg_color = '#34b867'#
    treeview_separator_bg_color = '#5D6361'
    # -----------------------------------------------------------

    styles = ttk.Style()
    styles.configure('field_label_color', background = field_bg_label_color_purple, foreground = field_fg_label_color_purple )
    styles.configure('field_active_label_color', background = field_bg_active_label_color_purple , foreground = field_fg_active_label_color_purple  )
    styles.configure('main_frame_bg_color', background = main_frame_bg_color_purple  )
    styles.configure('separator_color', background = separator_color_purple  )

    styles.configure( 'treeview_header_img', image = treeview_header_img )
    styles.configure( 'treeview_selected_item_color', background = treeview_selected_item_bg_color_purple , foreground = treeview_selected_item_fg_color_purple  )
    styles.configure( 'treeview_item_color', background = treeview_bg_color_purple, foreground = treeview_fg_color_purple, underline = treeview_separator_bg_color_purple  )
    styles.configure( 'treeview_header_color', background = treeview_header_bg_color_purple , foreground = treeview_header_fg_color_purple , underline = treeview_separator_bg_color_purple  )

    styles.configure( 'NLabel.TLabel',  background = field_bg_label_color_purple, foreground = field_fg_label_color_purple , padx = 6, pady = 3, width = 15 )
    styles.configure( 'LabelSpacer.TLabel', background = main_frame_bg_color_purple  )
    styles.configure( 'NTreeview.Treeview', fieldbackground = treeview_bg_color_purple , underline = treeview_separator_bg_color_purple , background = treeview_bg_color_purple , foreground = treeview_fg_color_purple , height = 400, borderwidth = 10, relief = 'sunken' )
    styles.configure( 'VScroll.Vertical.TScrollbar', background = '#00FF00', foreground = 'green', highlightcolor = 'red', highlightthickness = 3, highlightbackground = 'blue', activebackground = 'purple' )

    styles.configure( 'NFrame.TFrame', background = main_frame_bg_color_purple  )
    styles.configure( 'NEntry.TEntry', borderwidth = 2, relief = 'sunken',  background = main_frame_bg_color_purple, foreground = field_fg_label_color_purple  )
    styles.configure( 'NSeparator.TSeparator',  background = separator_color_purple  )

    styles.configure( 'Entry.TFrame', background = main_frame_bg_color_purple  )
    styles.configure( 'Tree.TFrame', background = treeview_bg_color_purple , foreground = treeview_fg_color_purple , underline = treeview_separator_bg_color_purple  )

    return styles #returns all the configured styles


def snOutputDebug( Items ): #used to output
    print( 'S/N length: ' + str( len( Items.sn_values ) ) )
    for key, val in Items.sn_values.items(): #goes through all values, outputting the letter and corresponding ascii code
        print( 'key: ' + key )
        print( 'val: ' + val )

        for letter in key:
            print( str( ord( letter ) ) + ':' + letter, end= ', ' )

        print()

        for letter in val:
            print( str( ord( letter ) ) + ':' + letter, end= ',' )

        print( end='\n\n' )

    return None


#goes from the location to the sn entry field when the user presses 'enter'
def locationToSnEntry(event, sn_entry):
    if event.widget.get() == '': #no location was given
        messagebox.showinfo( message = 'Enter a location to proceed. ', title = 'Error' )
    else:
        sn_entry.focus() #moves focus to next field

    return None


def createTreeview( style, Items, main_frame ): #defines treeview frame, with treeview taking up the full frame
    treeview_frame = ttk.Frame( main_frame, style = 'Tree.TFrame' )
    treeview_frame.grid( row = 2, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )

    treeview_frame.grid_columnconfigure( 1, weight = 1 ) #treeview expands across the x axis
    treeview_frame.grid_rowconfigure( 1, weight = 1 ) #treeview expands across the y axis

    Items.setup_treeview(style, treeview_frame)
    '''
    treeview = ttk.Treeview( treeview_frame, style = 'NTreeview.Treeview' )
    treeview.tag_configure( 'selected_item', background = style.lookup( 'treeview_selected_item_color', 'background' ), foreground = style.lookup( 'treeview_selected_item_color', 'foreground' ) )
    treeview.tag_configure( 'category', background = style.lookup( 'treeview_header_color', 'background' ), foreground = style.lookup( 'treeview_header_color', 'foreground' ) )
    treeview.tag_configure( 'item', background = style.lookup( 'treeview_item_color', 'background' ), foreground = style.lookup( 'treeview_item_color', 'foreground' ) )
    treeview.grid( row = 1, column = 1, sticky = ( 'N', 'W', 'E', 'S' ) )

    scrollbar = ttk.Scrollbar( treeview_frame, orient = 'vertical', command = treeview.yview, style = 'VScroll.Vertical.TScrollbar' ) #creates the scrollbar for the treeview
    scrollbar.grid( row = 0, rowspan = 2, column = 2, sticky = ( 'N', 'S' ) )
    treeview[ 'yscrollcommand' ] = scrollbar.set
    '''
    return treeview_frame

def createEntryFrame( style, Items, main_frame ):
    entry_frame = ttk.Frame( main_frame, style = 'Entry.TFrame' )
    entry_frame.grid( row = 1, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    entry_frame.grid_columnconfigure( 2, weight = 1 )

    location_label = ttk.Label( entry_frame, name = 'new_location', text = 'Location: ', style = 'NLabel.TLabel' )
    location_label.grid( row = 1, column = 1, sticky = ( 'W', 'E' ) )
    Items.set_location_entry_field( ttk.Entry( entry_frame, textvariable = Items.get_location_field(), style = 'NEntry.TEntry' ) )
    Items.get_location_entry_field().grid( row = 1, column = 2, sticky = ( 'W', 'E' ) )

    sn_label = ttk.Label( entry_frame, text = 'New S/N: ', style = 'NLabel.TLabel' )
    sn_label.grid( row = 2, column = 1, sticky = ( 'W', 'E' ) )
    Items.set_sn_entry_field( ttk.Entry( entry_frame, textvariable = Items.get_sn_field(), style = 'NEntry.TEntry' ) )
    Items.get_sn_entry_field().grid( row = 2, column = 2, columnspan = 4, sticky = ( 'W', 'E' ) )


    ttk.Label( entry_frame, text = '', style = 'LabelSpacer.TLabel' ).grid( row = 3, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    ttk.Separator( entry_frame, orient = 'horizontal', style = 'NSeparator.TSeparator' ).grid( row = 4, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )

    Items.get_location_entry_field().bind( '<Return>', lambda e: locationToSnEntry( e, Items.get_sn_entry_field() ) ) #user press enter in location field, and it goes to the s/n field
    Items.get_location_entry_field().bind( '<FocusIn>', lambda e: location_label.configure( background = ttk.Style().lookup(  'field_active_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_active_label_color', 'foreground' ) ) )
    Items.get_location_entry_field().bind( '<FocusOut>', lambda e: location_label.configure( background = ttk.Style().lookup( 'field_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_label_color', 'foreground' ) ) )

    Items.get_sn_entry_field().bind( '<Return>', lambda e: Items.user_validate(e) )
    Items.get_sn_entry_field().bind( '<FocusIn>', lambda e: sn_label.configure( background = ttk.Style().lookup(  'field_active_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_active_label_color', 'foreground' ) ) )
    Items.get_sn_entry_field().bind( '<FocusOut>', lambda e: sn_label.configure( background = ttk.Style().lookup('field_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_label_color', 'foreground' ) ) )

    return entry_frame


def createSearchFrame( style, Items, search_frame, search_image ):
    search_key_data = ''
    search_frame.grid_columnconfigure( 1, weight = 2 )
    search_frame.grid_columnconfigure( 2, weight = 4 )

    search_key_label = ttk.Label( search_frame, text = 'Search S/N: ', compound = tkinter.RIGHT, style = 'NLabel.TLabel' )
    search_key_label.image = search_image
    #search_key_entry = ttk.Entry( search_frame, textvariable = Items.get_search_field(), style = 'NEntry.TEntry' )
    Items.set_search_entry_field( ttk.Entry( search_frame, textvariable = Items.get_search_field(), style = 'NEntry.TEntry' ) )

    search_key_label.grid( row = 1, column = 1, sticky = ( 'W', 'E' ), columnspan = 5 )
    Items.get_search_entry_field().grid( row = 1, column = 2, sticky = ( 'W', 'E' ), columnspan = 4 )

    Items.get_search_entry_field().bind('<Return>', lambda e : Items.itemSearch(e) )
    Items.get_search_entry_field().bind('<FocusIn>', lambda e: search_key_label.configure( text = 'Search S/N: ', background = style.lookup(  'field_active_label_color', 'background' ), foreground = style.lookup( 'field_active_label_color', 'foreground' ) ) )
    Items.get_search_entry_field().bind( '<FocusOut>', lambda e: search_key_label.configure( text = 'Search S/N: ', background = style.lookup( 'field_label_color', 'background' ), foreground = style.lookup( 'field_label_color', 'foreground' ) ) )

    return search_frame



def createFrames(root):
    Items = ItemStorage() #
    sn_values = {} #creates the dictionary to store the s/n : location
    style = createStyles()
    treeview_header_img = tkinter.PhotoImage( file = r'images\folder_navy.gif' )
    search_image = tkinter.PhotoImage( file = 'images\\search.gif' )
    main_notebook = ttk.Notebook( root )
    main_notebook.grid_rowconfigure( 0, weight = 1 )
    main_notebook.grid_columnconfigure( 0, weight = 1 )

    #padding left top right bottom
    main_frame = ttk.Frame( main_notebook, padding = '10 5 10 10', style = 'NFrame.TFrame' )
    main_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )

    main_frame.grid_columnconfigure( 0, weight = 1 ) #for both frames to expand to fill main_frame
    main_frame.grid_rowconfigure( 1, weight = 1 ) #for entry frame
    main_frame.grid_rowconfigure( 2, weight = 6 ) #for treeview frame

    treeview_frame = createTreeview(style, Items, main_frame) #new
    entry_frame = createEntryFrame(style, Items, main_frame) #new

    search_frame = ttk.Frame( main_notebook, padding = '10 5 10 5', style = 'NFrame.TFrame' )
    search_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    search_frame = createSearchFrame( style, Items, search_frame, search_image )

    main_notebook.add( main_frame, text = "New Items" )
    main_notebook.add( search_frame, text = "Search", image = search_frame )
    main_notebook.image = search_frame

    main_notebook.grid( row = 0, column = 0, sticky = ('N', 'W', 'E', 'S'), padx = 5, pady = 3, ipadx = 10, ipady = 2 )
    root = createMenu( root, Items )

    return root


def main():
    root = createFrames( createroot() ) #returns fully build gui

    #frame_children = root.winfo_children()[0].winfo_children()
    #frame_children.children['new_location'].focus()

    root.mainloop()
    return None

main()
