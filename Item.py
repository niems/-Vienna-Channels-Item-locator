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


    def user_validate(self, event): #checks if user input is valid, then checks entryValidate

        if self.location_field == '': #valid location has not been given
            location_field.focus() #refocus location field
            messagebox.showinfo( message = 'ERROR: Enter a location entry to proceed.',
                                title = 'Error' )

        elif self.sn_field == '': #valid serial number has not been given
            self.sn_field.focus() #refocus sn field
            messagebox.showinfo( message = 'Error: Enter a serial number to proceed.',
                                title = 'Error' )

        else: #valid location and serial number given, check validity of entries
            #entryValidate here
            pass #placeholder

        return None

    def entry_validate( isFileBeingLoaded ):
        sn = self.sn_field.strip()
        location = self.location_field.strip()

        if sn in self.sn_values.keys(): #if the sn exists

            if location in self.sn_values.values(): #if location exists on root

                if self.sn_values[sn] == location: #if sn exists at location
                    error_message = 'ERROR: - Serial num: ' + sn
                                    + ' already exists in Location: '
                                    + self.sn_values[sn]


                    
