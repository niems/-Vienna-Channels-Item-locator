import tkinter
from tkinter import ttk
from tkinter import Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import sys
import random
from ItemStorage import ItemStorage
#from StyleConfig import StyleConfig as Styles

#styles = StyleConfig.StyleConfig() #file.Class() is the format. No one class, one file rule in python
#print( Styles() )
save_file_fields = 'Location, S/N \n'
item_separator = '____________________'


def newFile( Items ):
    killTree( Items ) #erases all data
    return None


def loadFile( Items ):

    #put in functionality that will ask the user if they want to save their data first if they have entries in sn_values and treeview.
    #after that, it will load the file.

    try:
        filename = tkinter.filedialog.askopenfile( initialdir = "/", title = "Load File", filetypes = ( ("csv files","*.csv"),("all files","*.*") ) )
        load_file = open( filename.name, 'r+' )

        Items.sn_values.clear()
        Items.treeview.delete( *treeview.get_children() )

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


def isItemInParent( item, parent, treeview ):
    item_found = False

    try:
        child_list = []

        if parent == treeview:
            child_list = treeview.get_children()

        else:
            child_list = treeview.get_children( parent ) #returns the list of children for the parent

        for child in child_list:
            if child == item:
                item_found = True #found item in parent
                break
    except:
        pass

    return item_found #returns True if the item was found


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

    user_menu.add_command( label = 'New', command = lambda : newFile( Items ) )
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


def treeviewCollapse( treeview ): #collapses all other branches when the user switches branches
    category_list = treeview.tag_has('category') #pulls all children on the treeview with this tag, returns a list
    for category in category_list: #collapses all children of root
        treeview.item( category, open = False )

    return None


def killTree( Items ): #erases all items in memory
    Items.sn_values.clear() #clears all items & locations
    Items.get_treeview().delete( *treeview.get_children() ) #kills all children on root

    return None

def generateTree( Items ):

    killTree( Items )

    base_category = 'Category '
    base_item = 'item '
    current_category = base_category #current category modified by loops
    current_item = base_item #current item modified by loops
    num_of_categories = 10
    num_of_items = 15

    for i in range( 1, num_of_categories + 1 ): #creates this number of categories
        current_category = base_category + str( i )

        for k in range( 1, num_of_items + 1 ): #creates this number of items per category
            current_item = base_item + str( ( num_of_items * i ) + k )
            entryValidate(True, Items)
            #entryValidate( True, current_category, current_item, None, sn_values, treeview )

    return None

'''
def entryValidate( loading_file, location, sn, sn_field, sn_values, treeview ):
    if sn in sn_values.keys(): #if the s/n exists
        #print('validate: S/N exists')
        if location in sn_values.values(): #if the location exists on the root
            #print('validate: location exists on root')
            if sn_values[ sn ] == location: #if the s/n exists in the current location
            #if isItemInParent( sn, location, treeview ): #if the s/n exists in the current location
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ]

                if not loading_file:
                    messagebox.showinfo( message = error_message, title = 'ERROR: S/N already exists' )

                print( error_message + '\nERROR: There is a duplicate entry in the .csv file', end='\n\n' )

            else: #if the s/n exists in a different location
                #print( 'validate: S/N exists in a different location' )
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location

                if option == True: #user wants to change s/n location
                    #print('validate: user changed S/N location')
                    treeview.delete( sn )

                    treeviewCollapse( treeview ) #collapses all branches

                    #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
                    treeview.get_children()[0].focus()
                    treeview.insert( location, 'end', sn, text = sn, open = True, tags = 'item' )
                    sn_values[ sn ] = location
                    if sn_field is not None:
                        sn_field.delete( 0, 'end' ) #clears field

        else: #the location does not exist on root
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location

                if option == True: #user to change s/n location. Creates new root location, then adds s/n
                    #print('validate: user changed S/N location')
                    treeview.delete( sn )

                    treeviewCollapse( treeview ) #collapses all branches

                    treeview.insert( '', 0, location, text = location, tags = 'category', open = True ) #adds new location to root
                    #treeview.get_int( 0 ).image = ttk.Style().lookup( 'treeview_header_img', 'image' )

                    #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
                    treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #adds s/n to new location
                    sn_values[ sn ] = location #^ update
                    if sn_field is not None:
                        sn_field.delete( 0, 'end' ) #clears s/n field

    else: #s/n doesn't exist

        if isItemInParent( location, '', treeview ): #if the location exists on the root
            #print('validate: adds s/n to existing location')
            sn_values[ sn ] = location

            #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item

            treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #inserts the s/n under the current location

        else: #location doesn't exist on the root
            #print('validate: adds s/n to new location')
            sn_values[ sn ] = location

            treeviewCollapse( treeview ) #collapses all branches

            treeview.insert( '', 0, location,  text = location, tags = 'category', open = True ) #creates location on root
            #treeview.get_int( 0 ).image = ttk.Style().lookup( 'treeview_header_img', 'image' )

            #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
            treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #inserts s/n under new location
        if sn_field is not None:
            sn_field.delete( 0, 'end' ) #clears s/n field

    return None
'''

def entryValidate( loading_file, Items ):
    if sn in sn_values.keys(): #if the s/n exists
        #print('validate: S/N exists')
        if location in sn_values.values(): #if the location exists on the root
            #print('validate: location exists on root')
            if sn_values[ sn ] == location: #if the s/n exists in the current location
            #if isItemInParent( sn, location, treeview ): #if the s/n exists in the current location
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ]

                if not loading_file:
                    messagebox.showinfo( message = error_message, title = 'ERROR: S/N already exists' )

                print( error_message + '\nERROR: There is a duplicate entry in the .csv file', end='\n\n' )

            else: #if the s/n exists in a different location
                #print( 'validate: S/N exists in a different location' )
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location

                if option == True: #user wants to change s/n location
                    #print('validate: user changed S/N location')
                    treeview.delete( sn )

                    Items.treeCollapse() #collapses all branches

                    #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
                    treeview.get_children()[0].focus()
                    treeview.insert( location, 'end', sn, text = sn, open = True, tags = 'item' )
                    sn_values[ sn ] = location
                    if sn_field is not None:
                        sn_field.delete( 0, 'end' ) #clears field

        else: #the location does not exist on root
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location

                if option == True: #user to change s/n location. Creates new root location, then adds s/n
                    #print('validate: user changed S/N location')
                    treeview.delete( sn )

                    Items.treeCollapse() #collapses all branches

                    treeview.insert( '', 0, location, text = location, tags = 'category', open = True ) #adds new location to root
                    #treeview.get_int( 0 ).image = ttk.Style().lookup( 'treeview_header_img', 'image' )

                    #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
                    treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #adds s/n to new location
                    sn_values[ sn ] = location #^ update
                    if sn_field is not None:
                        sn_field.delete( 0, 'end' ) #clears s/n field

    else: #s/n doesn't exist

        if isItemInParent( location, '', treeview ): #if the location exists on the root
            #print('validate: adds s/n to existing location')
            sn_values[ sn ] = location

            #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item

            treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #inserts the s/n under the current location

        else: #location doesn't exist on the root
            #print('validate: adds s/n to new location')
            sn_values[ sn ] = location

            Items.treeCollapse() #collapses all branches

            treeview.insert( '', 0, location,  text = location, tags = 'category', open = True ) #creates location on root
            #treeview.get_int( 0 ).image = ttk.Style().lookup( 'treeview_header_img', 'image' )

            #treeview.insert( location, 0, item_separator, text = item_separator, tags = 'item_separator' ) #separates each item
            treeview.insert( location, 'end', sn, text = sn, tags = 'item' ) #inserts s/n under new location
        if sn_field is not None:
            sn_field.delete( 0, 'end' ) #clears s/n field

    return None

'''
def userEntryValidate( event, location_entry, sn_values, treeview ):
    current_sn = event.widget.get()
    current_location = location_entry.get()

    if current_location == '': #no valid location was given.
        location_entry.focus() #refocus location field
        messagebox.showinfo( message = 'ERROR: Enter a location entry to proceed. ', title = 'Error' )

    elif current_sn == '': #no valid sn was given
        messagebox.showinfo( message = 'ERROR: Enter a S/N to proceed. ', title = 'Error' )

    else: #valid location and sn given, check if data exists.
        entryValidate( False, current_location.strip(), current_sn.strip(), event.widget, sn_values, treeview )

    return None
'''

def userEntryValidate( event, Items ):
    current_sn = Items.get_sn_field().get()
    current_location = Items.get_location_field().get()

    if current_location == '': #no valid location was given.
        Items.get_location_field.focus() #refocus location field
        messagebox.showinfo( message = 'ERROR: Enter a location entry to proceed. ', title = 'Error' )

    elif current_sn == '': #no valid sn was given
        messagebox.showinfo( message = 'ERROR: Enter a S/N to proceed. ', title = 'Error' )

    else: #valid location and sn given, check if data exists.
        entryValidate( False, Items )

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
    location_entry = ttk.Entry( entry_frame, textvariable = Items.get_location_field(), style = 'NEntry.TEntry' )
    location_entry.grid( row = 1, column = 2, sticky = ( 'W', 'E' ) )

    sn_label = ttk.Label( entry_frame, text = 'New S/N: ', style = 'NLabel.TLabel' )
    sn_label.grid( row = 2, column = 1, sticky = ( 'W', 'E' ) )
    Items.set_sn_entry_field( ttk.Entry( entry_frame, textvariable = Items.get_sn_field(), style = 'NEntry.TEntry' ) )
    Items.get_sn_entry_field().grid( row = 2, column = 2, columnspan = 4, sticky = ( 'W', 'E' ) )
    #sn_entry = ttk.Entry( entry_frame, textvariable = Items.get_sn_field(), style = 'NEntry.TEntry' )
    #sn_entry.grid( row = 2, column = 2, columnspan = 4, sticky = ( 'W', 'E' ) )

    ttk.Label( entry_frame, text = '', style = 'LabelSpacer.TLabel' ).grid( row = 3, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    ttk.Separator( entry_frame, orient = 'horizontal', style = 'NSeparator.TSeparator' ).grid( row = 4, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )

    location_entry.bind( '<Return>', lambda e: locationToSnEntry( e, Items.get_sn_entry_field() ) ) #user press enter in location field, and it goes to the s/n field
    location_entry.bind( '<FocusIn>', lambda e: location_label.configure( background = ttk.Style().lookup(  'field_active_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_active_label_color', 'foreground' ) ) )
    location_entry.bind( '<FocusOut>', lambda e: location_label.configure( background = ttk.Style().lookup( 'field_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_label_color', 'foreground' ) ) )

    #sn_entry.bind( '<Return>', lambda e: userEntryValidate( e, location_entry, sn_values, treeview ) )
    #sn_entry.bind( '<Return>', lambda e: userEntryValidate( e, Items ) )
    Items.get_sn_entry_field().bind( '<Return>', lambda e: Items.user_validate(e) )
    Items.get_sn_entry_field().bind( '<FocusIn>', lambda e: sn_label.configure( background = ttk.Style().lookup(  'field_active_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_active_label_color', 'foreground' ) ) )
    Items.get_sn_entry_field().bind( '<FocusOut>', lambda e: sn_label.configure( background = ttk.Style().lookup('field_label_color', 'background' ), foreground = ttk.Style().lookup( 'field_label_color', 'foreground' ) ) )

    return entry_frame

def search( e, Items ): #update view in real time based on what is searched

    #current_sn = e.widget.get().strip()
    current_sn = Items.get_sn_field.get().strip()

    if current_sn in sn_values.keys(): #sn exists
        message_output = 'S/N: ' + current_sn + ' is in location ' + sn_values[ current_sn ]
        messagebox.showinfo( message = message_output, title = 'S/N found :D' )

    else:
        message_output = 'S/N: ' + current_sn + ' does not exist. '
        messagebox.showinfo( message = message_output, title = 'S/N not found D:' )

    return None


def createSearchFrame( style, Items, search_frame, search_image ):
    search_key_data = ''
    search_frame.grid_columnconfigure( 1, weight = 2 )
    search_frame.grid_columnconfigure( 2, weight = 4 )

    search_key_label = ttk.Label( search_frame, text = 'Search S/N: ', compound = tkinter.RIGHT, style = 'NLabel.TLabel' )
    search_key_label.image = search_image
    search_key_entry = ttk.Entry( search_frame, textvariable = Items.get_search_field(), style = 'NEntry.TEntry' )

    search_key_label.grid( row = 1, column = 1, sticky = ( 'W', 'E' ), columnspan = 5 )
    search_key_entry.grid( row = 1, column = 2, sticky = ( 'W', 'E' ), columnspan = 4 )

    search_key_entry.bind('<Return>', lambda e : search( e, Items ) )
    search_key_entry.bind('<FocusIn>', lambda e: search_key_label.configure( text = 'Search S/N: ', background = style.lookup(  'field_active_label_color', 'background' ), foreground = style.lookup( 'field_active_label_color', 'foreground' ) ) )
    search_key_entry.bind( '<FocusOut>', lambda e: search_key_label.configure( text = 'Search S/N: ', background = style.lookup( 'field_label_color', 'background' ), foreground = style.lookup( 'field_label_color', 'foreground' ) ) )

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

    #treeview, treeview_frame = createTreeview( style, sn_values, main_frame )
    #entry_frame, location_entry, sn_entry = createEntryFrame( style, sn_values, treeview, main_frame )
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
