# Author   :: J3ck3LS/yN
# Version  :: 3.3.5
import sys
import os
import random
import Al13N_335
################################################################################
class Application:
    def __init__(self):
        # Interpreter
        self.Root   = Al13N_335.Main.Interpreter()
        # Settings
        self.Sett   = {
            'Interpreter':True,
            'FailSafe'   :True,
            'Output-File':str(os.getcwd())+str('/Output-')+str(random.randint(0,99999999))+str('.log'),
            'Output-Recd':str(os.getcwd())+str('/Record-')+str(random.randint(0,99999999))+str('.aln'),
            'Commands'   :''
            }
        # Handlers
        self.EHandle = Al13N_335.Exceptions
        self.DHandle = Al13N_335.Graphical.Messages()
        Title = '''
{F.G}================================================================================
                            {F.Y} Author :: {F.B}J4ck3LSyN
                            {F.Y}Version :: {F.B}3.3.5
{F.G}================================================================================
        '''
        self.DHandle._AppendHeader_('Al13N_UI.Title',Title)
        # Memory For Multiple Universes
    #########################################################################################################################################
    def Configure(self,Target,Value):
        if str(Target) in self.Sett:
            if str(Value) in ['true','True','1']:
                Value = True
            elif str(Value) in ['false','False','0']:
                Value = False
            if type(Value) == type(self.Sett[Target]):
                self.Sett[Target] = Value
            else:
                raise Exception(self.EHandle.RaiseToUser('Al13N_UI.Application.Configure','V',str(Value)+str(' Does Not Match Set Value ')+str(self.Sett[Target])))
        else:
            raise Exception(self.EHandle.RaiseToUser('Al13N_UI.Application.Configure','V',str(Target)+str(' Target Configuration Does Not Exist')))
    #########################################################################################################################################
    def RunInterpreter(self):
        if len(self.Sett['Commands']) != 0:
            self.HandlePipe(str(self.Sett['Commands']))
        if self.Sett['Interpreter'] == True:
            self.Root._Loop0Start_(FailSafe=self.Sett['FailSafe'])
    #########################################################################################################################################
    def HandlePipe(self,Command):
        self.Root._HandleIO_(str(Command))
    #########################################################################################################################################
#############################################################################################################################################
def ExecuteApp():
    Args = sys.argv[1:]
    App  = Application()
    App.DHandle.Display_String('@Al13N_UI.Title')
    #########################################################################################################################################
    # No Args Trigger
    # python3 Al13N_UI.py
    if len(Args) == 0:
        App.RunInterpreter()
    #########################################################################################################################################
    else:
    #########################################################################################################################################
        # Argument Parser Basic
        for A in Args:
            # python3 Al13N_UI.py -i
            # If Arg Is Found Than No Shell Will Be Triggered
            if str(A) in ['-i','--interpreter']:
                if App.Sett['Interpreter'] == True:
                    App.Configure('Interpreter',False)
                else:
                    App.Configure('Interpreter',True)
            # If Arg Is Found Than No Failsafe Will Be Used
            elif str(A) in ['-fs','--failsafe']:
                if App.Sett['FailSafe'] == True:
                    App.Configure('FailSafe',False)
                else:
                    App.Configure('FailSafe',True)
    #########################################################################################################################################
            # Advanced Handler Seperated Based Off '='
            elif str('=') in str(A):
                T = A.split('=')
                # Takes 2 Options -c/--command='COMMAND'
                # These Commands Get Passed Into The Handler
                if str(T[0]) in ['-c','--command']:
                    App.Configure('Commands',str(T[1]))
                elif str(T[0]) in ['-fl','--file']:
                    if os.path.isfile(str(T[1])) == True:
                        try:
                            text  = open(str(T[1])).read().split('\n')
                            for line in text:
                                if len(line) != 0:
                                    App.HandlePipe(str(line))
                        except Exception as e:
                            App.DHandle.Display_String('{F.R} Recieved Error From File : {F.W}'+str(T[1])+'{F.Y} '+str(e))
                    else:
                        App.DHandle.Display_String('{F.R} Recieved Error For Non Existant File : {F.W}'+str(T[1]))
                # Takes 2 Options -rm/--readme=Chapter
                # These Are For Handling The ReadMe As A Chapter File
                elif str(T[0]) in ['-rm','--readme']:
                    if os.path.isfile(str('ReadMe')) == True:
                        App.Root.IG._AppendChapter_('ReadMe')
                        if str(T[1]) == str('*'):
                            App.Root.IG._ReadChapter_(Target='ReadMe')
                        else:
                            App.Root.IG._ReadChapter_(Target=str(T[1]))
                    else:
                        App.DHandle.Display_String('{F.R} Recieved Error For -rm/--readme Because Its Non-Existant')
        App.RunInterpreter()
if __name__ == '__main__':
    ExecuteApp()
