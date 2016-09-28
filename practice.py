import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys

save_file_fields = 'Location, S/N \n'


def loadFile( sn_values, treeview, location_entry, sn_entry ):

    #put in functionality that will ask the user if they want to save their data first if they have entries in sn_values and treeview.
    #after that, it will load the file.
    
    try:
        filename = tkinter.filedialog.askopenfile( initialdir = "/", title = "Load File", filetypes = ( ("csv files","*.csv"),("all files","*.*") ) )        
        load_file = open( filename.name, 'r+' )
        
        sn_values.clear() 
        treeview.delete( *treeview.get_children() )
        
        for line in load_file: #goes through each line in file
            if line == '': #if line is empty (THIS WILL BREAK IF USER MANUALLY ENTERS A BLANK IN THE FILE, THEN ADDS DATA AFTERWARDS)
                break #eof
                
            elif line == save_file_fields:
                continue #go to the next line. These are the categories
                
            dict_entry = line.split( ',' )
            
            if len( dict_entry ) == 2:
                print(' passed sn : ' + dict_entry[1].strip() )
                entryValidate( True, dict_entry[0].strip(), dict_entry[1].strip(), sn_entry, sn_values, treeview )
        
    except Exception as e:
        print( 'Exception:{0}'.format(e) )
        messagebox.showinfo( message = 'ERROR: There is a problem loading the .csv file', title = 'ERROR: Loading file' )    
    
        load_file.close()
    return None
    

def saveFile( sn_values ):
    try:
        filename = tkinter.filedialog.asksaveasfilename(initialdir = '/', title = 'Save File', filetypes = ( ("csv files", "*.csv"), ("all files", "*.*") ) ).strip( '.csv' ) + '.csv'
        
        save_file = open( filename, 'w' )
        
        
        save_file.write( save_file_fields )
        
        for key, val in sn_values.items(): #writes each location : s/n to the file
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

    
def createWindow():
    window = tkinter.Tk()
    window.geometry('500x650')
    window.title('Item Locator')
    window.wm_iconbitmap('images\\vienna_channels.ico')
    window['bg'] = '#000000' #test - should never show on main window if the frame expands correctly
    
    window.grid_columnconfigure( 0, weight = 1 )
    window.grid_rowconfigure( 0, weight = 1 )
    
    return window


def createMenu( window, sn_values, treeview, location_entry, sn_entry ):
    
    window.option_add( '*tearOff', False )
    menubar = tkinter.Menu( window ) #creates menu widget
    window['menu'] = menubar #attach the menu widget to the window
    
    file_menu = tkinter.Menu( menubar ) #create a menu widget for the file menu
    menubar.add_cascade( menu = file_menu, label = 'File' ) #adds the file menu to the menubar
    
    file_menu.add_command( label = 'New', command = None )
    file_menu.add_command( label = 'Open', command = lambda : loadFile( sn_values, treeview, location_entry, sn_entry ) )
    file_menu.add_command( label = 'Save', command = lambda : saveFile( sn_values ) )
    file_menu.add_command( label = 'DEBUG', command = lambda : snOutputDebug( sn_values ) )
    file_menu.add_separator()
    file_menu.add_command( label = 'Exit', command = sys.exit )    
    
    return window       

    
def createStyles():
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
    
    styles = ttk.Style()
    styles.configure( 'NLabel.TLabel',  background = color_object2 )
    styles.configure( 'LabelSpacer.TLabel', background = color_secondary_background2 )
    styles.configure( 'NTreeview.Treeview', fieldbackground = '#FF0000', background = color_secondary_background2, foreground = color_accent2, height = 400, borderwidth = 10, relief = 'raised' )
    styles.configure( 'VScroll.Vertical.TScrollbar', background = '#00FF00' )
    
    styles.configure( 'NFrame.TFrame', background = color_secondary_background2 )
    styles.configure( 'NEntry.TEntry', borderwidth = 2, relief = 'sunken',  background = '#ff0000' )
    styles.configure( 'NSeparator.TSeparator',  background = color_accent2 )
    
    styles.configure( 'Entry.TFrame', background = color_secondary_background2 )
    styles.configure( 'Tree.TFrame', background = color_secondary_background2 )

    return styles #returns all the configured styles
    

def snOutputDebug( sn ): #used to output     
    print( 'S/N length: ' + str( len( sn ) ) )
    for key, val in sn.items(): #goes through all values, outputting the letter and corresponding ascii code
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
    
def entryValidate( loading_file, location, sn, sn_field, sn_values, treeview ):
    print('sn_values length: ' + str( len( sn_values ) ) )
    print( 'Validate location( ' + location + ' ), S/N( ' + sn + ' ) ' )

    if sn in sn_values.keys(): #if the s/n exists
        print('validate: S/N exists')
        if location in sn_values.values(): #if the location exists on the root
            print('validate: location exists on root')
            if sn_values[ sn ] == location: #if the s/n exists in the current location
            #if isItemInParent( sn, location, treeview ): #if the s/n exists in the current location
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] 
                
                if not loading_file:
                    messagebox.showinfo( message = error_message, title = 'ERROR: S/N already exists' )
                    
                print( error_message + '\nERROR: There is a duplicate entry in the .csv file', end='\n\n' )
            
            else: #if the s/n exists in a different location
                print( 'validate: S/N exists in a different location' )
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location
                
                if option == True: #user wants to change s/n location
                    print('validate: user changed S/N location')
                    treeview.delete( sn ) 
                    treeview.insert( location, 0, sn, text = sn, open = True )
                    sn_values[ sn ] = location 
                    sn_field.delete( 0, 'end' ) #clears field
                        
        else: #the location does not exist on root
                error_message = 'ERROR - S/N: ' + sn + ' already exists in location: ' + sn_values[ sn ] + '\nWould you like to move it to location: ' + location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location
                 
                if option == True: #user to change s/n location. Creates new root location, then adds s/n
                    print('validate: user changed S/N location')
                    treeview.delete( sn ) 
                    treeview.insert( '', 0, location, text = location, open = True ) #adds new location to root
                    treeview.insert( location, 0, sn, text = sn ) #adds s/n to new location
                    sn_values[ sn ] = location #^ update
                    sn_field.delete( 0, 'end' ) #clears s/n field            
        
    else: #s/n doesn't exist
    
        if isItemInParent( location, '', treeview ): #if the location exists on the root
            print('validate: adds s/n to existing location')
            sn_values[ sn ] = location
            treeview.insert( location, 0, sn, text = sn ) #inserts the s/n under the current location
            
        else: #location doesn't exist on the root
            print('validate: adds s/n to new location')
            sn_values[ sn ] = location
            treeview.insert( '', 0, location, text = location, open = True ) #creates location on root
            treeview.insert( location, 0, sn, text = sn ) #inserts s/n under new location            
        
        sn_field.delete( 0, 'end' ) #clears s/n field                
    
    return None
    
    
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
    
def addTreeNodesTest( node_count, sn_values, treeview ):
    
    treeview.insert( '', 0, 'Test Nodes', text = 'Test Nodes', open = True )
    
    for node in range( node_count ):
        treeview.insert( 'Test Nodes', 0, str( node ), text = str( node ) )
        sn_values [ str( node ) ] = 'Test Nodes'
        
    return None
    

def createTreeview( style, sn_values, main_frame ): #defines treeview frame, with treeview taking up the full frame
    treeview_frame = ttk.Frame( main_frame, style = 'Tree.TFrame' )
    treeview_frame.grid( row = 2, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    
    treeview_frame.grid_columnconfigure( 1, weight = 1 ) #treeview expands across the x axis
    treeview_frame.grid_rowconfigure( 1, weight = 1 ) #treeview expands across the y axis
    
    treeview = ttk.Treeview( treeview_frame, style = 'NTreeview.Treeview' )
    treeview.grid( row = 1, column = 1, sticky = ( 'N', 'W', 'E', 'S' ) )
    #addTreeNodesTest( 100, sn_values, treeview )
    
    scrollbar = ttk.Scrollbar( treeview_frame, orient = 'vertical', command = treeview.yview, style = 'VScroll.Vertical.TScrollbar' ) #creates the scrollbar for the treeview
    scrollbar.grid( row = 0, rowspan = 2, column = 2, sticky = ( 'N', 'S' ) )
    treeview[ 'yscrollcommand' ] = scrollbar.set    
    
    return treeview, treeview_frame
    
def createEntryFrame( style, sn_values, sn_treeview, main_frame ): 
    entry_frame = ttk.Frame( main_frame, style = 'Entry.TFrame' )
    entry_frame.grid( row = 1, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    entry_frame.grid_columnconfigure( 2, weight = 1 )
    
    new_location_data = ''
    new_sn_data = ''
    
    new_location_label = ttk.Label( entry_frame, name = 'new_location', text = 'Current Location: ', style = 'NLabel.TLabel' )
    new_location_label.grid( row = 1, column = 1, sticky = ( 'W', 'E' ) )    
    new_location_entry = ttk.Entry( entry_frame, textvariable = new_location_data, style = 'NEntry.TEntry' )
    new_location_entry.grid( row = 1, column = 2, sticky = ( 'W', 'E' ) )
    
    new_sn_label = ttk.Label( entry_frame, text = 'New S/N: ', style = 'NLabel.TLabel' )
    new_sn_label.grid( row = 2, column = 1, sticky = ( 'W', 'E' ) )
    new_sn_entry = ttk.Entry( entry_frame, textvariable = new_sn_data, style = 'NEntry.TEntry' )
    new_sn_entry.grid( row = 2, column = 2, columnspan = 4, sticky = ( 'W', 'E' ) )
    
    ttk.Label( entry_frame, text = '', style = 'LabelSpacer.TLabel' ).grid( row = 3, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    ttk.Separator( entry_frame, orient = 'horizontal', style = 'NSeparator.TSeparator' ).grid( row = 4, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    
    
    return entry_frame, new_location_entry, new_location_label, new_sn_entry, new_sn_label 
    

def createSearchFrame( style, sn_treeview, search_frame ):
    
    return search_frame
    
    
def createFrames(window):
    sn_values = {} #creates the dictionary to store the s/n : location
    style = createStyles()
    
    
    main_notebook = ttk.Notebook( window )
    main_notebook.grid_rowconfigure( 0, weight = 1 )
    main_notebook.grid_columnconfigure( 0, weight = 1 )
 
 
    #padding left top right bottom
    main_frame = ttk.Frame( main_notebook, padding = '10 5 10 10', style = 'NFrame.TFrame' )    
    main_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    
    main_frame.grid_columnconfigure( 0, weight = 1 ) #for both frames to expand to fill main_frame
    main_frame.grid_rowconfigure( 1, weight = 1 ) #for entry frame
    main_frame.grid_rowconfigure( 2, weight = 6 ) #for treeview frame
    
    treeview, treeview_frame = createTreeview( style, sn_values, main_frame )   
    entry_frame, location_entry, location_label, sn_entry, sn_label = createEntryFrame( style, sn_values, treeview, main_frame )
    
    
    search_frame = ttk.Frame( main_notebook, padding = '10 5 10 5', style = 'NFrame.TFrame' )
    search_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    search_frame = createSearchFrame( style, treeview, search_frame )
    
    #move the binds back
    location_entry.bind( '<Return>', lambda event: locationToSnEntry( event, sn_entry ) ) #user press enter in location field, and it goes to the s/n field    
    location_entry.bind( '<FocusIn>', lambda e: location_label.configure( background = ttk.Style().lookup(  'NSeparator.TSeparator', 'background' ) ) )
    location_entry.bind( '<FocusOut>', lambda e: location_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    
    sn_entry.bind( '<Return>', lambda event: userEntryValidate( event, location_entry, sn_values, treeview ) )    
    sn_entry.bind( '<FocusIn>', lambda e: sn_label.configure( background = ttk.Style().lookup( 'NSeparator.TSeparator', 'background' ) ) )
    sn_entry.bind( '<FocusOut>', lambda e: sn_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    
  
    main_notebook.add( main_frame, text = "Enter New S/N's" )
    main_notebook.add( search_frame, text = "Search for S/N" )
    main_notebook.grid( row = 0, column = 0, sticky = ('N', 'W', 'E', 'S'), padx = 5, pady = 3, ipadx = 10, ipady = 2 )
    window = createMenu( window, sn_values, treeview, location_entry, sn_entry )
    
    return window

        
def main():    
    window = createFrames( createWindow() ) #returns fully build gui  
    
    #frame_children = window.winfo_children()[0].winfo_children()    
    #frame_children.children['new_location'].focus()
    
    window.mainloop()
    return None
    
main()