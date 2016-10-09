
from tkinter import filedialog
from tkinter import messagebox

class Files(object):
    def __init__(self):
        self.save_file_fields = 'Location, S/N \n' #first row in files saved to

    def load_file(self, Items):
        try:
            file_name = filedialog.askopenfile( initialdir = "/",
                                                            title = "Load File",
                                                            filetypes = \
                                                            ( ("csv files","*.csv"), \
                                                            ("all files","*.*") ) )
            load_file = open( file_name.name, 'r+' )

            #removes current data since new data is going to be loaded
            Items.killTree()

            for line in load_file:
                if line == '': #if line is empty
                    break #eof

                elif line == self.save_file_fields: #starting category line
                    continue

                line = line.split(',')

                if len( line ) == 2:
                    Items.entry_validate( True, line[0].strip(),
                                          line[1].strip() )
            load_file.close()
        except Exception as e:
            error_loading_file = 'ERROR: There is a problem loading the .csv '\
                                 + 'file'
            error_title = 'ERROR: Loading file'

            print( 'Exception:{0}'.format(e) )
            messagebox.showinfo( message = error_loading_file,
                                 title = error_title )


        return None

    def save_file(self, Items):
        try:
            file_name = filedialog.asksaveasfilename(initialdir = '/',
                                                                 title = 'Save File',
                                                                 filetypes = \
                                                                 ( ("csv files", "*.csv"),
                                                                 ("all files", "*.*") ) ) \
                                                                 .strip( '.csv' ) + '.csv'

            save_file = open( file_name, 'w' )
            save_file.write( self.save_file_fields )

            for key, val in Items.sn_values.items(): # writes each location :
                                                     # s/n to the file
                current_output = val.strip() + ',' + key.strip() + '\n'
                save_file.write( current_output )

            save_file.close()
        except Exception as e:
            print( 'Exception: {0}'.format(e) )
            messagebox.showinfo( message = 'ERROR: There is a' \
                                 + 'problem saving ' \
                                 + 'the .csv file.',
                                 title = 'ERROR: Saving file' )

        return None
