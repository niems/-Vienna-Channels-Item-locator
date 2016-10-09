
import webbrowser, sys, pyperclip

def commandArgs():
    if len( sys.argv ) > 1: #command line argument passed
        args = '+'.join( sys.argv[2:] )
    
    else: #clipboard is used as argument
        args = pyperclip.paste()
        
    return args
    
def argCheck(): #determines which option is called, if any
    address = ''
    
    for i in range(0, len(sys.argv) ):
        print( str(i) + ": " )
        print( sys.argv[i], end='\n\n' )
        
    
    if len( sys.argv ) > 1: #command line argument passed
        if( sys.argv[1] == 'search' ):
            address = search() 
        
        elif( sys.argv[1] == 'map' ):
            address = map()
            
        else:
            print('Error: Invalid command line argument')
        
        return address
    
def search():
    base_search = 'https://www.google.com/#q='
    args = commandArgs() 
    
    args.replace('"', '%22') #replaces the double quote with the google search symbol
    args.replace("'", '%27') #replaces the single quote with the google search symbol
    
    
    return( base_search + args ) 
    
def map():
    base_url = 'https://www.google.com/maps/place/'
    
    return( base_url + commandArgs() )
    

#execution
address = argCheck()
webbrowser.open( address )
    



    

    
    
    
    