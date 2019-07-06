# Author   : J4ck3lSyN
# Verision : 1.5.0
import os, time, sys, subprocess
# ^ Central Imports
# Colorama Import
try:
    import colorama
    from   colorama import Fore  as F
    from   colorama import Back  as B
    from   colorama import Style as S
    colorama.init(autoreset=True)
except Exception as e:
    print(str(e))
    print('Would You Like To Install colorama Via pip3?')
    uentry = input('(Y/N)::> ')
    if str(uentry) in ['No','NO','FuckNo']:
        print('colorama Is Needed For Graphic Fun Stuff Dont Be That Way...')
        print('YOU Can Install It With: pip3 install colorama')
        sys.exit(1)
    else:
        os.system('pip3 install colorama')
        print('Please Restart...')
        sys.exit(1)
# Central Handle
class Globe:
    def __init__(self):
        self.Memory  = {}   # Memory
        # Settings #
        self.Status  = True # Status  Setting
        self.QueExe  = []   # Que     Setting
        self.Scope   = None # Scope   Setting
        return
    ############################################################################
    # Used For Displaying Inforation To The Screen #
    # Usage: (root->Al13N.Globe())
    # screen = root.Display()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #/
    # Display._ColorIndex
    #  This is the relative index for all color handing, translated through
    #  Display.Colorize
    # Display._MessageLog
    #  Log For all Messages Returned
    # Display.Colorize(str)
    #  Takes a string and checks for hotkeys based of '{}'
    #  if a ColorID is detected inside of a string {COLOR}
    #  it will replace, this is for looped over Display._ColorIndex
    #  every color resets after sent to screen.
    class Display:
        # Displaying Things To Screen
        def __init__(self):
            self._ColorIndex = { # For Colorizing Messages By Code
                'F.W':F.WHITE,
                'B.W':B.WHITE,
                # White
                'F.R':F.RED,
                'B.R':B.RED,
                # Red
                'F.G':F.GREEN,
                'B.G':B.GREEN,
                # GREEN
                'F.M':F.MAGENTA,
                'B.M':F.MAGENTA,
                # Magenta
                'F.C':F.CYAN,
                'B.C':B.CYAN,
                # Cyan
                'F.B':F.BLUE,
                'B.B':B.BLUE,
                # Blue
                'F.Z':F.BLACK,
                'B.Z':B.BLACK,
                # Black
                'F.X':F.RESET,
                'B.X':B.RESET,
                # Brightness
                'S.B':S.BRIGHT,
                'S.N':S.NORMAL,
                'S.D':S.DIM,
                # RESET ALL
                'S.X':S.RESET_ALL
                }
            self._MessageLog = [] # For Logging Messages
        # For Colorizing Messages
        def Colorize(self,Message):
            for Color in self._ColorIndex:
                Current_Color = str('{')+str(Color)+str('}')
                if str(Current_Color) in str(Message):
                    Message = str(Message).replace(str(Current_Color),str(self._ColorIndex[Color]))
                else:
                    pass
            self._MessageLog.append(str(Message))
            return str(Message)

def init():
    Running = True
    Logging = []
    Root    = Globe()
    RDis    = Root.Display()
    Mesg    = {
        0:[
            RDis.Colorize('{F.G}{S.B}-- {F.B}Al13N{F.G} --'),
            RDis.Colorize('{F.B}Author: {F.R}J4ck3lSyN {F.B}@{F.W} '+str(os.getcwd()))
        ]
    }
    Umesg   = RDis.Colorize('{F.G}{S.N}::> ')
    Home    = 0
    while Running == True:
        for line in Mesg[Home]:
            print(str(line))
        Uentry = input(str(Umesg))
        if str(Uentry) in ['exit','Exit','EXIT']:
            print(str(RDis.Colorize('{F.R}{S.B}Exiting...')))
            Running = False

if len(sys.argv) == 1:
    init()
