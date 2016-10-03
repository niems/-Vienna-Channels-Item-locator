from tkinter import ttk

class StyleConfig(object):
    def __init__(self, color_scheme):
        #self.style = ttk.Style()

        if color_scheme == 'default': #default color scheme
            self.field_bg_label_color = '#494949'
            self.field_fg_label_color = '#34B767'
            self.field_bg_active_label_color = '#34B767'
            self.field_fg_active_label_color = '#222222'
            self.main_frame_bg_color = '#383838'
            self.separator_color = '#34B767'

            self.treeview_selected_item_bg_color = ''
            self.treeview_selected_item_fg_color = ''
            self.treeview_header_bg_color = '#373737'
            self.treeview_header_fg_color = '#309970'#34B767
            self.treeview_item_bg_color = '#454545' #'#383838'
            self.treeview_item_fg_color = '#34b867'#
            self.treeview_separator_bg_color = '#5D6361'

        #self.configure() #configures the styles using the colors above
        #self.configure( style )

    def configure(self, style):
        style.configure('field_label_color',
                            background = self.field_bg_label_color,
                            foreground = self.field_fg_label_color )

        style.configure('field_active_label_color',
                            background = self.field_bg_active_label_color,
                            foreground = self.field_fg_active_label_color  )

        style.configure('main_frame_bg_color',
                            background = self.main_frame_bg_color  )

        style.configure('separator_color',
                            background = self.separator_color )

        style.configure( 'treeview_selected_item_color',
                            background = self.treeview_selected_item_bg_color,
                            foreground = self.treeview_selected_item_fg_color  )

        style.configure( 'treeview_item_color',
                            background = self.treeview_item_bg_color,
                            foreground = self.treeview_item_fg_color,
                            underline = self.treeview_separator_bg_color  )

        style.configure( 'treeview_header_color',
                            background = self.treeview_header_bg_color,
                            foreground = self.treeview_header_fg_color,
                            underline = self.treeview_separator_bg_color  )

        style.configure( 'NLabel.TLabel',
                            background = self.field_bg_label_color,
                            foreground = self.field_fg_label_color,
                            padx = 6, pady = 3,
                            width = 15 )

        style.configure( 'LabelSpacer.TLabel',
                            background = self.main_frame_bg_color  )

        style.configure( 'NTreeview.Treeview',
                            fieldbackground = self.treeview_item_bg_color,
                            underline = self.treeview_separator_bg_color,
                            background = self.treeview_item_bg_color,
                            foreground = self.treeview_item_fg_color,
                            height = 400,
                            borderwidth = 10,
                            relief = 'sunken' )

        style.configure( 'VScroll.Vertical.TScrollbar',
                            background = '#00FF00',
                            foreground = 'green',
                            highlightcolor = 'red',
                            highlightthickness = 3,
                            highlightbackground = 'blue',
                            activebackground = 'purple' )

        style.configure( 'NFrame.TFrame',
                            background = self.main_frame_bg_color  )

        style.configure( 'NEntry.TEntry',
                            borderwidth = 2,
                            relief = 'sunken',
                            background = self.main_frame_bg_color,
                            foreground = self.field_fg_label_color  )

        style.configure( 'NSeparator.TSeparator',
                            background = self.separator_color )

        style.configure( 'Entry.TFrame',
                            background = self.main_frame_bg_color )

        style.configure( 'Tree.TFrame',
                            background = self.treeview_item_bg_color,
                            foreground = self.treeview_item_fg_color,
                            underline = self.treeview_separator_bg_color  )

        return style

    '''
    def getStyle(): #returns the ttk.Style() object that has been configured
        return self.style

    def getStyleLookup(obj_style):
        return self.style.lookup(obj_style)

    def getStyleLookupOption(obj_style, obj_option):
    '''


    def __str__(self):
        return "Field bg label color: {}\
                \nField fg label color: {}\
                \nField bg active label color: {}\
                \nField fg active label color: {}\
                \nSeparator color: {}\
                \nTreeview header bg color: {}\
                \nTreeview header fg color: {}\
                \nTreeview item bg color: {}\
                \nTreeview item fg color: {}\
                \nTreeview separator bg color: {}\n\n".\
                format( self.field_bg_label_color, self.field_fg_label_color,
                        self.field_bg_active_label_color, self.field_fg_active_label_color,
                        self.separator_color, self.treeview_header_bg_color,
                        self.treeview_header_fg_color, self.treeview_item_bg_color,
                        self.treeview_item_fg_color, self.treeview_separator_bg_color )
