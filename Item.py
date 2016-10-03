from tkinter import ttk
from tkinter import messagebox

#class is used to hold all data relating to the location : sn storage
class ItemStorage(object):
    def __init__(self):
        self.sn_values = {} #stores location : sn values
        self.sn_field = '' #connected to sn field
        self.location_field = '' #connected to location field
        self.treeview = '' #stores the current sn values in the treeview


    def sn_field_setup(self): #connects sn_field to associated text var
        return self.sn_field

    def location_field_setup(self): #connects location_field to associated text var
        return self.location_field


    def user_validate(self, event): #checks for valid user input, then valid entry

        if self.location_field == '': #valid location has not been given
            location_field.focus() #refocus location field
            messagebox.showinfo(message = 'ERROR: Enter a location entry to proceed.',
                                title = 'Error')

        elif self.sn_field == '': #valid serial number has not been given
            self.sn_field.focus() #refocus sn field
            messagebox.showinfo(message = 'Error: Enter a serial number to proceed.',
                                title = 'Error')

        else: #valid location and serial number given, check validity of entries
            #entryValidate here
            pass #placeholder

        return None

    def entry_validate(self, isFileBeingLoaded):
        sn = self.sn_field.strip()
        location = self.location_field.strip()

        #Error messages for dialogbox output
        title_sn_exists = 'ERROR: Serial Number exists'
        sn_exists_message = 'ERROR: - Serial num: ' + sn
                            + ' already exists in Location: '
                            + self.sn_values[sn]

        move_location_message = '\nWould you like to move it to Location: '
                                + location + '?'

        if sn in self.sn_values.keys(): #if the sn exists

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
                        self.treeview.delete( sn ) #delete sn from current location
                        #treeviewCollapse() #collapses all branches
                        #focus the branch that's receiving the transferred sn
                        self.treeview.insert(location, 'end', sn, text = sn
                                            open = True, tags = 'item')
                        self.sn_values[sn] = location #transferred sn location

                        if self.sn_field is not None:
                            self.sn_field.delete(0, 'end') #clears field

            else: #location does not exist on root
                option = messagebox.askyesno(message = sn_exists_message
                                            + move_location_message,
                                            title = title_sn_exists)

                if option: #creates new location, then moves sn to it
                    self.treeview.delete(sn)
                    #treeviewCollapse() #collapses all branches
                    self.treeview.insert('', 0, location, text = location,
                                        tags = 'category', open = True)
