from tkinter import ttk
from tkinter import messagebox
import random

#class is used to hold all data relating to the location : sn storage
class ItemStorage(object):
    def __init__(self):
        self.sn_values = {} #stores location : sn values
        self.sn_entry_field = '' #keeps track of sn entry field
        self.location_entry_field = '' #keeps track of location entry field
        self.search_entry_field = '' #keeps track of search entry field
        self.treeview = '' #stores the current sn values in the treeview

    def setup_treeview(self, style, frame): #defines treeview attached to frame
        self.treeview = ttk.Treeview(frame, style = 'NTreeview.Treeview')

        self.treeview.tag_configure('category',
                                    background = style.treeview_header_bg_color,
                                    foreground = style.treeview_header_fg_color)

        self.treeview.tag_configure('item',
                                    background = style.treeview_item_bg_color,
                                    foreground = style.treeview_item_fg_color)

        self.treeview.grid(row = 1, column = 1, sticky = ('N', 'W', 'E', 'S') )

        scrollbar = ttk.Scrollbar(frame, orient = 'vertical',
                                  command = self.treeview.yview,
                                  style = 'VScroll.Vertical.TScrollbar')

        scrollbar.grid(row = 0, rowspan = 2, column = 2, sticky = ('N', 'S') )
        self.treeview['yscrollcommand'] = scrollbar.set

        return None #check this, might need return the frame


    def set_sn_entry_field(self, entry): #used to setup sn entry field
        self.sn_entry_field = entry

        return None

    def set_location_entry_field(self, entry): #used to setup location entry field
        self.location_entry_field = entry

        return None

    def set_search_entry_field(self, entry): #used to setup search entry field
        self.search_entry_field = entry

        return None


    def killTree(self): #erases all items
        self.sn_values.clear()
        self.treeview.delete( *self.treeview.get_children() )

        return None

    def treeCollapse(self): #collapses all treeview branches
        category_list = self.treeview.tag_has('category') #pulls all children on the treeview with this tag, returns a list
        for category in category_list: #collapses all children of root
            self.treeview.item( category, open = False )

        return None

    def treeExpand(self): #expands all treeview branches
        category_list = self.treeview.tag_has('category') #pulls all children on the treeview with this tag, returns a list
        for category in category_list: #collapses all children of root
            self.treeview.item( category, open = True )

        return None

    def generateTree(self): #generates dummy values to demonstrate treeview
        self.killTree()

        base_category = 'Category '
        base_item = 'item '
        current_category = base_category #current category modified by loops
        current_item = base_item #current item modified by loops
        num_of_categories = 10
        max_num_of_items = 15
        current_num_of_items = -1
        item_count = 0 #total number of items

        for i in range( 1, num_of_categories + 1 ): #creates this number of categories
            current_category = base_category + str( i )

            #random number of items per category
            current_num_of_items = random.randint(1, max_num_of_items)
            for k in range( 1, current_num_of_items + 1 ): #creates this number of items per category
                item_count += 1
                current_item = base_item + str(item_count)
                self.entry_validate(True, current_category, current_item)

        return None


    def user_validate(self, event): #checks for valid user input, then valid entry

        if self.location_entry_field.get() == '': #valid location has not been given
            self.location_entry_field.focus() #refocus location field
            messagebox.showinfo(message = 'ERROR: Enter a location entry to proceed.',
                                title = 'Error')

        elif self.sn_entry_field.get() == '': #valid serial number has not been given
            self.sn_entry_field.focus() #refocus sn field
            messagebox.showinfo(message = 'Error: Enter a serial number to proceed.',
                                title = 'Error')

        else: #valid location and serial number given, check validity of entries
            self.entry_validate() #passed 'False' since there is no file

        return None

    def entry_validate(self, isFileBeingLoaded = False, category = '', item = ''):
        sn = ''
        sn_text = '' #text to be stored in treeview (doesn't have the '_')
        location = ''

        #adds a '_' for all sn names, this way the location and sn
        #can be the same value and there is no name conflict
        if isFileBeingLoaded:
            sn_text = item.strip('_') #removes the _ if it exists for duplication purposes
            sn = '_' + sn_text
            location = category

        else:
            sn_text = self.sn_entry_field.get().strip() #see above reason for '_'
            sn = '_' + sn_text
            location = self.location_entry_field.get().strip()

        #Error messages for dialogbox output
        title_sn_exists = 'ERROR: Serial Number exists'
        sn_exists_message = 'ERROR: - Serial Number: "' + sn \
                            + '" already exists in Location: "'

        move_location_message = '\nWould you like to move it to Location: "' \
                                + location + '"?'

        if sn in self.sn_values.keys(): #if the sn exists
            sn_exists_message += self.sn_values[sn] + '"'

            if location in self.sn_values.values(): #if location exists on root

                if self.sn_values[sn] == location: #if sn exists at location

                    if not isFileBeingLoaded: #user entered data
                        messagebox.showinfo(message = sn_exists_message,
                                            title = title_sn_exists)

                    #log that duplicate entry in .csv file was found
                else: #the sn exists in a different location
                    option = messagebox.askyesno(message = sn_exists_message
                                                 + move_location_message,
                                                 title = title_sn_exists)

                    if option: #moves sn to alternate location

                        self.treeview.delete(sn)

                        self.treeCollapse() #collapses all branches
                        self.treeview.insert(location, 'end', sn, text = sn_text,
                                            open = True, tags = 'item')

                        self.treeview.item(location, open = True)
                        self.sn_values[sn] = location #transferred sn location

                    if not isFileBeingLoaded:
                        self.sn_entry_field.delete(0, 'end') #clears field

            else: #location does not exist on root
                option = messagebox.askyesno(message = sn_exists_message
                                             + move_location_message,
                                             title = title_sn_exists)

                if option: #creates new location, then moves sn to it
                    self.treeCollapse() #collapses all branches

                    self.treeview.delete(sn)

                    self.sn_values[sn] = location #^update

                    self.treeview.insert('', 0, location, text = location,
                                         tags = 'category', open = True)

                    self.treeview.insert(location, 'end', sn, text = sn_text,
                                         tags = 'item') #adds sn to new location

                    self.treeview.item(location, open = True)

                    if not isFileBeingLoaded:
                        self.sn_entry_field.delete(0, 'end') #clears field

        else: #sn does not exist
            if location in self.sn_values.values(): #if location exists on root
                self.treeCollapse()
                self.sn_values[sn] = location #stores new sn at location
                self.treeview.insert(location, 'end', sn, text = sn_text,
                                     tags = 'item')

                self.treeview.item(location, open = True)

            else: #location does not exist on root
                self.treeCollapse() #collapses all branches
                self.sn_values[sn] = location #stores new sn at location

                self.treeview.insert('', 0, location, text = location,
                                     tags = 'category', open = True) #new location

                self.treeview.insert(location, 'end', sn, text = sn_text,
                                     tags = 'item') #sn at new location

                self.treeview.item(location, open = True)

            if not isFileBeingLoaded:
                self.sn_entry_field.delete(0, 'end') #clears field


        return None


    def itemSearch(self, e):
        sn = self.search_entry_field.get().strip()

        if sn in self.sn_values.keys(): #sn exists
            title_found = 'Serial number found :D'
            sn_found = 'Serial Number: "' + sn + '" is in Location: "' \
                       + self.sn_values[sn] + '"'

            messagebox.showinfo(message = sn_found, title = title_found)

        else: #sn does not exists
            title_not_found = 'Serial number not found D:'
            sn_not_found = 'Serial Number: "' + sn + '" does not exist.'

            messagebox.showinfo(message = sn_not_found,
                                title = title_not_found)

        return None
