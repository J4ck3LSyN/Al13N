import ColourFullDisplay.CFD as CFD
import os
def CHECK_INSTALL():
    Commands = 'pip3 install pyfiglet && pip3 install colorama'
    Output   = str( bytes( subprocess.Popen( [Commands], stdout=subprocess.PIPE,shell=True ).stdout.read(),'utf-8') )

    return str(Output)

def CHECKFONTS_INSTALL():
    if os.path.isdir('CFD/fonts') == True:
        Installed = CFD.Fonts.PyFigletOps.CurrentInstalledFonts()
        Not       = []
        for Name in os.listdir('CFD/fonts'):
            if str('Name').strip('.flf') not in Installed: Not.append(str('CFD/fonts/')+str(Name))


        Out  = []
        for Target in Not:
            try:
                Commands = ['pyfiglet -L '+str(Target)]
                Output   = bytes.decode(subprocess.Popen(Commands,stdout=subprocess.PIPE,shell=True),'utf-8')
                Out.append(Output)
            except:
                print('Failed On {} '.format(str(Target)))
        return Out

if __name__ == "__main__": Check  = CHECK_INSTALL()
