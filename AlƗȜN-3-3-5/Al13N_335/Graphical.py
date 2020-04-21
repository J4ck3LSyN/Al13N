# Requires colorama
# Author  :: J3ck3LSyN
# Version :: 3.3.5
import Al13N_335.Exceptions as Exceptions
import os
Failed = False
Reason = None
# Colorama Import Test
try:
    import colorama
    from   colorama import Fore  as  F
    from   colorama import Back  as  B
    from   colorama import Style as  S
except ImportError as I:
    Failed = True
    Reason = str(I)
finally:
    if Failed == True:
        raise Exception(Exceptions.RaiseToUser('Al13N_335.Graphical','I',str(Reason)+' Install Colorama\n\t:: pip3 install colorama'))
    else:
        pass

# For Reseting The Screen
def TriggerAutoReset():
    colorama.init(autoreset=True)

class Messages:
    Colours = { # Colour Index
        'F.G'            :F.GREEN,
        'F.W'            :F.WHITE,
        'F.R'            :F.RED,
        'F.B'            :F.BLUE,
        'F.X'            :F.BLACK,
        'F.M'            :F.MAGENTA,
        'F.Y'            :F.YELLOW,
        'F.C'            :F.CYAN,
        'F.0'            :F.RESET,
        'B.G'            :B.GREEN,
        'B.W'            :B.WHITE,
        'B.R'            :B.RED,
        'B.B'            :B.BLUE,
        'B.X'            :B.BLACK,
        'B.M'            :B.MAGENTA,
        'B.Y'            :B.YELLOW,
        'B.C'            :B.CYAN,
        'B.0'            :B.RESET,
        'S.B'            :S.BRIGHT,
        'S.N'            :S.NORMAL,
        'S.D'            :S.DIM,
        'S.0'            :S.RESET_ALL
    }
    Headers  = {}   # Header  Index
    OpenKey  = '{'  # Colour  Catch Opener
    CloseKey = '}'  # Colour  Catch Close
    MessKey  = '@'  # Message Catch
    Logging  = []   # Loggin For Messages
    Log      = True # For Logging
    Verb     = True # For Verbose
    Index    = {}   # For Chapter Files
    #########################################################################################################################################
    def _CatchColour_(self,String):
        for Colour in self.Colours:
            CID = str(self.OpenKey)+str(Colour)+str(self.CloseKey)
            if str(CID) in str(String):
                String = str(String).replace(str(CID),self.Colours[str(Colour)])
        return String
    #########################################################################################################################################
    def _CatchMessage_(self,String):
        for Head in self.Headers:
            HID = str(self.MessKey)+str(Head)
            if str(HID) in str(String):
                String = str(String).replace(str(HID),self.Headers[str(Head)])
        return String
    #########################################################################################################################################
    def _AppendHeader_(self,ID,Value):
        Value = self._CatchColour_(str(Value))
        Value = self._CatchMessage_(str(Value))
        self.Headers[str(ID)]=str(Value)
        return Value
    #########################################################################################################################################
    def _AppendChapter_(self,PathToFile):
        if os.path.isfile(str(PathToFile)):
            try:
                Text = open(str(PathToFile)).read().split('\n')
                CLne = None
                for Line in Text:
                    if len(Line) > 0:
                        if str(Line[:2]) == str('<<') and str('@') in str(Line) and str('>>') in str(Line):
                            Chapter = Line[2:].split('>>')[0]
                            CLne = Chapter
                            self.Index[str(Chapter)] = []
                        else:
                            if CLne != None:
                                self.Index[str(CLne)].append(str(Line))
                            else:
                                raise Exception(Exceptions.RaiseToUser('Al13N_335.Graphical.Messages._AppendChapter_','E',str('No Chapter Configured')))
                    else:
                        continue
            except Exception as e:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.Graphical.Messages._AppendChapter_','E',str(e)+str(' From Operaion Of File ')+str(PathToFile)))
    #########################################################################################################################################
    def _ReadChapter_(self,Target=None,Header=None):
        # INFO: Use Al13N_335.Graphical.TriggerAutoReset() Prior To Running For Colors Not To Leak
        if len(self.Index) != 0:
            if Target != None:
                for Entity  in self.Index:
                    ETree = Entity.split('@')
                    if str(Target) == str(ETree[0]) or str(Target) == str(ETree[1]) or str(Target) == str(Entity):
                        for Line in self.Index[Entity]:
                            Message = '{F.W}{S.B}({F.R}'+str(Entity)+'{F.W})\t'+str(Line)
                            if Header != None:
                                if str(Header) in self.Headers:
                                    Message = self.Headers[str(Header)]+str(Message)
                            self.Display_String(str(Message))
            else:
                for Chapter in self.Index:
                    Message = '{F.W}{S.B}({F.R}'+str(Chapter)+'{F.W})'
                    if Header != None:
                        if str(Header) in self.Headers:
                            Message = str(self.Headers[Header])+str(Message)
                    self.Display_String(str(Message))
    ########################################################################################################################################
    def Display_String(self,String):
        String = self._CatchColour_(str(String))
        String = self._CatchMessage_(str(String))
        if self.Verb == True:
            print(str(String))
        if self.Log  == True:
            self.Logging.append(str(String))
    #########################################################################################################################################
