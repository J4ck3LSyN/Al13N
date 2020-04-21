import Al13N3480 as UFO_Frame
import os,sys,time,random
import readline
################################################################################
# Fatal Exception Handler
def UFO150Exception(Root,Reason,Mesg,Extend='',Fatal=True):
    Message  = '> Al13N(3.4.80(UFO(1.5.0))) Exception: '+str(Root)+str(' | ')
    Message += str(Mesg)+' ('+str(Extend)+')'
    if Fatal == True:
        raise Exception(Message)
    else: print(Message)
################################################################################
class UFO:
    def __init__(self,**Handles):
        Default_Handles         = {
            'Secure_Key':(0x9,0x9a, 0x4134134,0x2,0x9 ),
            'Char_Key'  :(0x9,0x9a,0x9878987,0x2,0x9),
            'PreOp'     :[],       # PreExecution Operations
            'Debugging' :False,    # Debugging Functions
            'Logging'   :True,     # Logging
            'Interface' :'SKIDDY', # Interface Type
            'Inter_Lvl' :0,        # Interface Level
            'Modules'   :'Mods'   # Moduler Functions
            }
        if len(Handles) != 0:
            for Op in Handles:
                if str(Op) in Default_Handles:
                    if type(Handles[Op]) == type(Default_Handles[Op]):
                        Default_Handles[str(Op)] = Handles[Op]
        self.Configure_Out  = Default_Handles # Configure
        self.Logging_Out    = [] # Output for Logging
        self.FailSafe       = [True,0,15] # Failsafe If [0] == True And [1] ==/> [2] EXIT
        self.Internal_Brain = UFO_Frame.Al13N3480(Default_Handles['Secure_Key'],Default_Handles['Char_Key']) # Mount Internal Memory Complex
        self.Projects       = {}

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        App = UFO()
