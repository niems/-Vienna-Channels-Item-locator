import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys


def openFile():
    filename = tkinter.filedialog.askopenfile(initialdir = "/", title = "Load it up :D", filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(filename)
    
    return None

def saveFile():
    filename = tkinter.filedialog.asksaveasfilename(initialdir = '/', title = 'Save that file, brooo', filetypes = ( ("csv files", "*.csv"), ("all files", "*.*") ) )

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
    window['bg'] = '#00ff00' #test - should never show on main window if the frame expands correctly
    
    window.grid_columnconfigure( 0, weight = 1 )
    window.grid_rowconfigure( 0, weight = 1 )
    
    #window.grid_rowconfigure( 1, weight = 6 ) #for old build with everything attached to the Tk() window
    
    return window


def createMenu(window):
    
    window.option_add( '*tearOff', False )
    menubar = tkinter.Menu( window ) #creates menu widget
    window['menu'] = menubar #attach the menu widget to the window
    
    file_menu = tkinter.Menu( menubar ) #create a menu widget for the file menu
    menubar.add_cascade( menu = file_menu, label = 'File' ) #adds the file menu to the menubar
    
    file_menu.add_command( label = 'New', command = None )
    file_menu.add_command( label = 'Open', command = openFile )
    file_menu.add_command( label = 'Save', command = saveFile )
    file_menu.add_separator()
    file_menu.add_command( label = 'Exit', command = sys.exit )    
    
    return window       

    
def createStyles():
    color_main_background2 = '#BDBDBD' #500
    color_accent2 = '#00E676' #200
    color_secondary_background2 = '#212121' #800
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
    styles.configure( 'NTreeview.Treeview', fieldbackground = '#FF0000', background = color_secondary_background2, foreground = color_accent2, borderwidth = 10, relief = 'sunken' )
    styles.configure( 'VScroll.Vertical.TScrollbar', background = '#00FF00' )
    
    styles.configure( 'NFrame.TFrame', background = color_secondary_background2 )
    styles.configure( 'NEntry.TEntry', borderwidth = 2, relief = 'sunken',  background = '#ff0000' )
    styles.configure( 'NSeparator.TSeparator',  background = color_accent2 )
    
    styles.configure( 'Entry.TFrame', background = 'red' )
    styles.configure( 'Tree.TFrame', background = 'green' )

    return styles #returns all the configured styles
    

def snDictionarySetup(): #creates the dictonary for storing the data    
    sn_values = {} #format is s/n : location
    
    return sn_values    
    
    
#goes from the location to the sn entry field when the user presses 'enter'
def locationToSnEntry(event, sn_entry):
    if event.widget.get() == '': #no location was given
        #print('Enter a location to proceed.')
        messagebox.showinfo( message = 'Enter a location to proceed. ', title = 'Error' )
        
    else:
        sn_entry.focus() #moves focus to next field
    
    return None
    
    
def snEntryValidate( event, location_entry, main_frame, sn_values, treeview ):
    current_sn = event.widget.get()
    current_location = location_entry.get()
    
    if current_location == '': #no valid location was given. 
        location_entry.focus() #refocus location field
        messagebox.showinfo( message = 'ERROR: Enter a location entry to proceed. ', title = 'Error' )
        
    elif current_sn == '': #no valid sn was given
        messagebox.showinfo( message = 'ERROR: Enter a S/N to proceed. ', title = 'Error' )
        
    else: #valid location and sn given, check if data exists. 
        
        if treeview.exists( current_sn ): #if the s/n exists
            
            if current_location in sn_values.values(): #if the location exists on the root
                if isItemInParent( current_sn, current_location, treeview ): #if the s/n exists in the current location
                    error_message = 'ERROR - S/N: ' + current_sn + ' already exists in location: ' + current_location
                    messagebox.showinfo( message = error_message, title = 'Error' )
                
                else: #s/n exists in different location
                    error_message = 'ERROR - S/N: ' + current_sn + ' already exists in location: ' + sn_values[ current_sn ] + '\nWould you like to move it to location: ' + current_location + '?'
                    option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location
                    
                    if option == True: #user wants to change s/n location
                        treeview['show'] = 'tree'
                        treeview.delete( current_sn ) 
                        treeview.insert( current_location, 0, current_sn, text = current_sn, open = True )
                        sn_values[ current_sn ] = current_location 
                        event.widget.delete( 0, 'end' ) #clears s/n field
            
            else: #the location does not exist on root
                error_message = 'ERROR - S/N: ' + current_sn + ' already exists in location: ' + sn_values[ current_sn ] + '\nWould you like to move it to location: ' + current_location + '?'
                option = messagebox.askyesno( message = error_message, title = 'S/N exists in another location' ) #returns if the user wants to change the s/n location
                 
                if option == True: #user to change s/n location. Creates new root location, then adds s/n
                    treeview['show'] = 'tree' 
                    treeview.delete( current_sn ) 
                    treeview.insert( '', 0, current_location, text = current_location, open = True ) #adds new location to root
                    treeview.insert( current_location, 0, current_sn, text = current_sn ) #adds s/n to new location
                    sn_values[ current_sn ] = current_location #^ update
                    event.widget.delete( 0, 'end' ) #clears s/n field            
        
        else: #s/n doesn't exist
        
            if isItemInParent( current_location, '', treeview ): #if the location exists on the root
                treeview.insert( current_location, 0, current_sn, text = current_sn ) #inserts the s/n under the current location
                
            else: #location doesn't exist on the root
                treeview['show'] = 'tree'
                treeview.insert( '', 0, current_location, text = location_entry.get(), open = True ) #creates location on root
                treeview.insert( current_location, 0, current_sn, text = current_sn ) #inserts s/n under new location
                
            sn_values[ current_sn ] = current_location #^ same for both conditions above
            event.widget.delete( 0, 'end' ) #clears s/n field
    
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
    addTreeNodesTest( 100, sn_values, treeview )
    
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
    
    '''
    new_location_entry.bind( '<Return>', lambda event: locationToSnEntry( event, new_sn_entry ) ) #user press enter in location field, and it goes to the s/n field    
    new_location_entry.bind( '<FocusIn>', lambda e: new_location_label.configure( background = ttk.Style().lookup(  'NSeparator.TSeparator', 'background' ) ) )
    new_location_entry.bind( '<FocusOut>', lambda e: new_location_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    
    new_sn_entry.bind( '<Return>', lambda event: snEntryValidate( event, new_location_entry, entry_frame, sn_values, sn_treeview ) )    
    new_sn_entry.bind( '<FocusIn>', lambda e: new_sn_label.configure( background = ttk.Style().lookup( 'NSeparator.TSeparator', 'background' ) ) )
    new_sn_entry.bind( '<FocusOut>', lambda e: new_sn_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    '''
    
    return entry_frame, new_location_entry, new_location_label, new_sn_entry, new_sn_label 
    
    #return entry_frame
    
    
def createMainFrame(window):
    sn_values = snDictionarySetup() #creates the dictionary to store the s/n : location

    style = createStyles()
    
    #padding left top right bottom
    main_frame = ttk.Frame( window, padding = '10 5 10 10', style = 'NFrame.TFrame' )
    main_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )
    
    main_frame.grid_columnconfigure( 0, weight = 1 ) #for both frames to expand to fill main_frame
    main_frame.grid_rowconfigure( 1, weight = 1 ) #for entry frame
    main_frame.grid_rowconfigure( 2, weight = 6 ) #for treeview frame
    
    treeview, treeview_frame = createTreeview( style, sn_values, main_frame )
    entry_frame, location_entry, location_label, sn_entry, sn_label = createEntryFrame( style, sn_values, treeview, main_frame )
    
    location_entry.bind( '<Return>', lambda event: locationToSnEntry( event, sn_entry ) ) #user press enter in location field, and it goes to the s/n field    
    location_entry.bind( '<FocusIn>', lambda e: location_label.configure( background = ttk.Style().lookup(  'NSeparator.TSeparator', 'background' ) ) )
    location_entry.bind( '<FocusOut>', lambda e: location_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    
    sn_entry.bind( '<Return>', lambda event: snEntryValidate( event, location_entry, entry_frame, sn_values, treeview ) )    
    sn_entry.bind( '<FocusIn>', lambda e: sn_label.configure( background = ttk.Style().lookup( 'NSeparator.TSeparator', 'background' ) ) )
    sn_entry.bind( '<FocusOut>', lambda e: sn_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )

    
    #entry frame column configure here
    
    '''
    main_frame = ttk.Frame( window,  name = 'main_frame', padding = '3 3 12 12', style = 'NFrame.TFrame' )
    main_frame.grid( row = 0, column = 0, sticky = ( 'N', 'W', 'E', 'S' ) )    
    main_frame.grid_columnconfigure( 2, weight = 1 )    
    
    sn_treeview = ttk.Treeview( window, style = 'NTreeview.Treeview' ) 
    sn_treeview.grid( row = 1, column = 0, sticky = ( 'N', 'S', 'E', 'W' ) )
    addTreeNodesTest( 100, sn_treeview )
    
    sn_scrollbar = ttk.Scrollbar( window, orient = 'vertical', command = sn_treeview.yview, style = 'VScroll.Vertical.TScrollbar' ) #creates the scrollbar for the treeview
    sn_scrollbar.grid( row = 0, rowspan = 2, column = 7, sticky = ( 'N', 'S' ) )
    sn_treeview[ 'yscrollcommand' ] = sn_scrollbar.set
    '''
    
    
    
    '''
    new_location_label = ttk.Label( main_frame, name = 'new_location', text = 'Current Location: ', style = 'NLabel.TLabel' )
    new_location_label.grid( row = 1, column = 1, sticky = ( 'W', 'E' ) )    
    new_location_entry = ttk.Entry( main_frame, textvariable = new_location_data, style = 'NEntry.TEntry' )
    new_location_entry.grid( row = 1, column = 2, sticky = ( 'W', 'E' ) )
    
    new_sn_label = ttk.Label( main_frame, text = 'New S/N: ', style = 'NLabel.TLabel' )
    new_sn_label.grid( row = 2, column = 1, sticky = ( 'W', 'E' ) )
    new_sn_entry = ttk.Entry( main_frame, textvariable = new_sn_data, style = 'NEntry.TEntry' )
    new_sn_entry.grid( row = 2, column = 2, columnspan = 4, sticky = ( 'W', 'E' ) )
    
    ttk.Label( main_frame, text = '', style = 'LabelSpacer.TLabel' ).grid( row = 3, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    ttk.Separator( main_frame, orient = 'horizontal', style = 'NSeparator.TSeparator' ).grid( row = 4, column = 1, columnspan = 3, sticky = ( 'N', 'W', 'E', 'S' ) )
    
    
    new_location_entry.bind( '<Return>', lambda event: locationToSnEntry( event, new_sn_entry ) ) #user press enter in location field, and it goes to the s/n field    
    new_location_entry.bind( '<FocusIn>', lambda e: new_location_label.configure( background = ttk.Style().lookup(  'NSeparator.TSeparator', 'background' ) ) )
    new_location_entry.bind( '<FocusOut>', lambda e: new_location_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    
    new_sn_entry.bind( '<Return>', lambda event: snEntryValidate( event, new_location_entry, main_frame, sn_values, sn_treeview ) )    
    new_sn_entry.bind( '<FocusIn>', lambda e: new_sn_label.configure( background = ttk.Style().lookup( 'NSeparator.TSeparator', 'background' ) ) )
    new_sn_entry.bind( '<FocusOut>', lambda e: new_sn_label.configure( background = ttk.Style().lookup( 'NLabel.TLabel', 'background' ) ) )
    '''
    
    #----------------------------------------------------------------
    
    #insert arguments( parent, insert index 0 - 'end', 'name in treeview to reference', 'text displayed in treeview' )
   
    
    
    return window

        
def main():    
    window = createMainFrame( createMenu( createWindow() ) ) #returns fully build gui
    
    #frame_children = window.winfo_children()[0].winfo_children()    
    #frame_children.children['new_location'].focus()
    
    window.mainloop()
    return None
    
main()