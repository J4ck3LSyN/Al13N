import random
import sys, os
import time
import Al13N_335.Exceptions as Exceptions

class RegeX:
    def __init__(self,CharacterRange=500,Displace=1):
        self.Logs   = [False,[]]
        self.Char   = {}
        if type(CharacterRange) is int:
            for i in range(0,CharacterRange):
                if Displace != 1:
                    self.Char[str(chr(i))] = int(i)**int(Displace)
                else:
                    self.Char[str(chr(i))] = int(i)
        else:
            raise Excepton(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.__init__','V',str(CharacterRange)+str(' Expected int')))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX._LogIntoLogs_(str)
    - For Logging Things Into self.Logs
    '''
    def _LogIntoLogs_(self,Message):
        if self.Logs[0] == True:
            Message = str(time.asctime())+str('\t')+str(Message)
            self.Logs[1].append(str(Message))
        else:
            pass
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX._SwitchLog_()
    - Triggers Logging Status To Oposite Current Settings True=False=True...
    '''
    def _SwitchLog_(self):
        if self.Logs[0] == True:
            self.Logs[0] = False
        else:
            self.Logs[0] = True
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX._ReadOutLog_()
    - Returns List Of Log Events
    '''
    def _ReadOutLog_(self):
        return self.Logs[1]
    #########################################################################################################################################
    def IsIn(self,Variable,Target):
        self._LogIntoLogs_('IsIn('+str(Variable)+','+str(Target)+')')
        if Variable in Target:
            return True
        else:
            return False
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.IsFile(str)
    - Takes A Path And Returns True If Its A File
    '''
    def IsFile(self,PathToFile):
        return os.path.isfile(str(PathToFile))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.IsPath(str)
    - Takes A Path And Returns True Is Its A Path
    '''
    def IsPath(self,PathToDirectory):
        return os.path.isdir(str(PathToDirectory))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ListContents(str)
    - Takes A Path And Lists The Contents
    '''
    def ListContents(self,PathToDirectory):
        if self.IsPath(str(PathToDirectory)) == True:
            return os.listdir(str(PathToDirectory))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.ListContents','V',str(PathToDirectory)+str(' Expected A Valid Directory')))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ReadFile(str)
    - Takes A File And Returns The Text
    '''
    def ReadFile(self,PathToFile):
        if self.IsFile(str(PathToFile)) == True:
            Text = open(str(PathToFile)).read()
            return str(Text)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.ReadFile','V',str(PathToFile)+str(' Expected A Valid File')))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.CombinePath(str,str)
    - Takes A Path And Appends A File With It
    '''
    def CombinePath(self,PathToDirectory,PathToFile):
        if self.IsPath(str(PathToDirectory)) == True:
            return os.path.join(str(PathToDirectory),str(PathToFile))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.CombinePath','V',str(PathToDirectory)+str(' Expected A Valid Path')))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.MakeDir(str,str)
    - Takes A Path And Makes A Directory
    '''
    def MakeDir(self,PathToDirectory,PathName):
        if self.IsPath(str(PathToDirectory)) == True:
            PathName = self.CombinePath(str(PathToDirectory),str(PathToFile))
            os.mkdir(str(PathName))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.MakeDir','V',str(PathToDirectory)+str(' Expected A Valid Path')))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.IsNot(var,var)
    - Returns Value If Var[0] Contains Var[1]
    '''
    def IsNot(self,Variable,Target):
        self._LogIntoLogs_('IsNot('+str(Variable)+','+str(Target)+')')
        if Variable not in Target:
            return True
        else:
            return False
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.Replace(var,var,var)
    - Will Replace Any Occurance Or var[1] Inside Of var[0] And Replace With Var[2]
    '''
    def Replace(self,Variable,Target,Replacement):
        self._LogIntoLogs_('Replace('+str(Variable)+','+str(Target)+','+str(Replacement)+')')
        if self.IsIn(Variable,Target) == True:
            return Target.replace(Variable,Replacement)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.Replace','V',str(Variable)+str(' Is Not In ')+str(Target)))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.Split(var,var)
    - Will Split Var[0] By Var[1]
    '''
    def Split(self,Variable,Target):
        self._LogIntoLogs_('Split('+str(Variable)+','+str(Target)+')')
        if self.IsIn(Variable,Target) == True:
            return Target.split(Variable)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.Split','V',str(Variable)+str(' Is Not In ')+str(Target)))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.Remove(var,var)
    - Will Remove And Occurance Of Var[1] Inside Of Var[0]
    '''
    def Remove(self,Variable,Target):
        self._LogIntoLogs_('Remove('+str(Variable)+','+str(Target)+')')
        if self.IsIn(Variable,Target) == True:
            return Target.strip(Variable)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.Remove','V',str(Variable)+str(' Is Not In ')+str(Target)))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ConvertToChar(var,var)
    - Takes var[0] And Converts It To Its ASCII Character Number Than Appeds V[1] To It For Seperation
    '''
    def ConvertToChar(self,Variable,Seperator):
        self._LogIntoLogs_('ConvertToChar('+str(Variable)+','+str(Seperator)+')')
        OutputString = ''
        for Character in Variable:
            if Character in self.Char:
                OutputString += str(self.Char[Character])+str(Seperator)
        return OutputString
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ConvertFromChar(var,var)
    - Takes var[0] (Post ConvertToChar) And Seperates Based Off var[1] And Converts Back From Its ASCII Character Number
    '''
    def ConvertFromChar(self,Variable,Seperator):
        self._LogIntoLogs_('ConvertFromChar('+str(Variable)+','+str(Seperator)+')')
        if self.IsIn(Seperator,Variable) == True:
            Tree =  self.Split(Seperator,Variable)
            OutputString = ''
            for Character in Tree:
                for Index in self.Char:
                    Value =  self.Char[Index]
                    if str(Character) == str(Value):
                        OutputString  += str(Index)
            return OutputString
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.ConvertFromChar','V',str(Seperator)+str(' Not In ')+str(Variable)))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ConvertEncodeIntoHex(var,var)
    - Takes var[0] (Post ConvertToChar) And Seperates Based Off var[1] And Converts Its ASCII Character Number And Turns Into Hex
    '''
    def ConvertEncodeIntoHex(self,Variable,Seperator):
        self._LogIntoLogs_('ConvertEncodeIntoHex('+str(Variable)+','+str(Seperator)+')')
        if self.IsIn(Seperator,Variable) == True:
            Tree = self.Split(Seperator,Variable)
            OutputString = ''
            for Character in Tree:
                if str(Character).isdigit() == True:
                    OutputString += hex(int(Character))+str(Seperator)
            return OutputString
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.ConvertEncodeIntoHex','V',str(Seperator)+str(' Not In ')+str(Variable)))
    #########################################################################################################################################
    '''
    ^ Al13N_335.RegeX.RegeX.ConvertEncodeFromHex(var,var)
    - Takes var[0] (Post ConvertEncodeIntoHex) And Seperates Based Off var[1] And Converts From Hex Into ASCII Character Number
    '''
    def ConvertEncodeFromHex(self,Variable,Seperator):
        self._LogIntoLogs_('ConvertencodeFromHex('+str(Variable)+','+str(Seperator)+')')
        if self.IsIn(Seperator,Variable) == True:
            Tree = self.Split(Seperator,Variable)
            OutputString = ''
            for Character in Tree:
                if str(Character[:2]) == str('0x'):
                    Character = int(Character,0)
                    OutputString += str(Character)+str(Seperator)
            return OutputString
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RegeX.RegeX.ConvertencodeFromHex','V',str(Seperator)+str(' Not In ')+str(Variable)))
    ##########################################################################################################################################
