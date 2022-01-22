import os as os
import shutil as shutil
import sys as sys

class Terminal(object):
    """
        Noé Favier
        24/06/2021
    """

    sizeX = None
    sizeY = None

    def clear(self):
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
  
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')


    def __init__(self,L,l):
        self.sizeX = L
        self.sizeY = l
        
        os.system('mode con: cols='+str(self.sizeX)+' lines='+str(self.sizeY))
            
    def write(self, o):
        sys.stdout.write(str("\b%s" % (o)))
        #print(o, end='', flush=True)
        #print(o)


    def flush(self):
        self.clear()
        #os.system('mode con: cols='+str(L)+' lines='+str(l))
        


    def getSize(self):
        return shutil.get_terminal_size
