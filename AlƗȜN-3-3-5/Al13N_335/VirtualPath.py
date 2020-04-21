import Al13N_335.Exceptions as Exceptions
import Al13N_335.LogicK     as LogicK
import os     # For Handling OS Based Operations
import sys    # For Handling System Based Operations
import random # For Randomness

class Translate:
    def __init__(self,CMax=500,Disp=1):
        self.Crypt = RegeX.RegeX(CharacterRange=int(CMax),Displace=int(Disp))
        self.Confg = {
            'Root':'...@...',
            'SDir':'.../...',
            'SFle':'...$...',
            'Sepr':'...#...',
            'Unkw':'...?...'
        }
    #########################################################################################################################################
    def _SwitchConfig_(self,Target,Value):
        if str(Target) in self.Confg:
            self.Confg[str(Target)] = str(Value)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.VirtualPath.Translate._SwitchConfig_','K',str(Target)+' Is Not a Valid Location'))
    #########################################################################################################################################
    def Translate(self,PathToVP):
        if self.Crypt.IsPath(str(PathToVP)) == True:
            Root     = self.Confg['Root']
            Root    += self.Crypt.ConvertToChar(str(PathToVP),str(self.Confg['Sepr']))
            Contents = self.Crypt.ListContents(str(PathToVP))
            Output   = []
            for Entity in Contents:
                if self.Crypt.IsFile(str(Entity)) == True:
                    Type = 'SFle'
                elif self.Crypt.IsPath(str(Entity)) == True:
                    Type = 'SDir'
                else:
                    Type = 'Unkw'
