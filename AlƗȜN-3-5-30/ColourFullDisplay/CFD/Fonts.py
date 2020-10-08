try:
    import pyfiglet as Figlet
except ImportError as I: raise Exception('Attempted To Import "pyfiglet" Use "pip3 install pyfiglet" To Continue')
import os,sys,time,subprocess,random
##################################################################################################################
class PyFigletOps:
    def CurrentInstalledFonts(): return str( bytes.decode( subprocess.Popen( ['pyfiglet -l'],stdout=subprocess.PIPE,shell=True ).stdout.read() ,'utf-8') ).split('\n')
    def CheckForInstall(Directory):
        if os.path.isdir(str(Directory)) == True:
            Target_Items = os.listdir(str(Directory))
            Valid_Items  = []
            Invalid_Items = []
            for Item in Target_Items:
                if str('.flf') in str(Item): Valid_Items.append(str(Item))
                else: Invalid_Items.append(str(Item))

            Status_Items = {}
            Current_Install = PyFigletOps.CurrentInstalledFonts()
            for Object in Valid_Items:
                if str(Object.strip('.flf')) in Current_Install: Status_Items[str(Object)]=True
                else: Status_Items[str(Object)]=False
            return Status_Items
        else: raise Exception('PyFigletOps.CheckForInstall Directory Fault...')

# For Handling Fonts
class FontStrings:
    def __init__(self,SetUpFontRange=5):

        self.Fonts = PyFigletOps.CurrentInstalledFonts()
        self.Mount = []
        self.MNTID = []



    def ReturnFontList(self):
        Fonts = []
        for I in self.Fonts:
            if len(I) != 0: Fonts.append(str(I))
        Out   = []
        for F in Fonts:
            if str('\n') in str(F): F = F.strip('\n')
            if len(F) != 0: Out.append(str(F))
        return Out


    def RandomFont(self,Message):
        r = random.randint(0,len(self.Fonts)-1)
        return str( self.ReturnFont(Message,self.Fonts[r]) )

    def VerifyFont(self,Font):
        if str(Font) in self.ReturnFontList():
            return True
        else: return False

    def ReturnFont(self,Message,Font):
        Message_Comp = Figlet.Figlet(font=str(Font))
        return str(Message_Comp.renderText(str(Message)))

    def FontStringsException(self,Root,Message):
        Mesg = str('FontStrings.')+str(Root)+' || '+str(Message)
        raise Exception(Mesg)
