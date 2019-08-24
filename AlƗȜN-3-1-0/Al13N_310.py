# Version 3.1.0
# Revision Under Al13N-3.0.0
import os,time,socket,threading,subprocess,sys
import hashlib
import colorama
import random
from   colorama import Fore  as F
from   colorama import Back  as B
from   colorama import Style as S
colorama.init(autoreset=True)
class ToolBox:
    def __init__(self):
        self.AlphaL   = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.AlphaU   = str(self.AlphaL.upper())
        self.ReverseL = '9876543210zyxwvutsrqponmlkjihgfedcba'
        self.ReverseU = str(self.ReverseL.upper())
        self.Special  = '~`!@#$%^&*()_-+={}[]:;"<>,./'
    # For Reversing Indexs In Simple Pythonic Alphabetical Strings
    # Takes Item As str
    def ReverseString(self,String_To_Reverse):
        if type(String_To_Reverse) is str:
            Return_String = ''
            for C in String_To_Reverse:
                if str(C) in self.AlphaL:
                    I = self.AlphaL.index(str(C))
                    Return_String += str(self.ReverseL[int(I)])
                elif str(C) in self.AlphaU:
                    I = self.AlphaU.index(str(C))
                    Return_String += str(self.ReverseU[int(I)])
                else:
                    Return_String += str(C)
            return str(Return_String)
        else:
            raise TypeError(str(type(String_To_Reverse))+' Expected str')
    # For Converting Strings to Bytes Takes Item As str
    def ConvertToByte(self,String_To_Convert):
        if type(String_To_Convert) is str:
            return bytes(str(String_To_Convert),'utf-8')
        else:
            raise TypeError(str(type(String_To_Convert))+' Expected str')
    # For Converting Bytes Back Takes Item As bytes
    def ConvertFromByte(self,Byte_To_Convert):
        if type(Byte_To_Convert) is bytes:
            return str(Byte_To_Convert.decode('utf-8'))
        else:
            raise TypeError(str(type(Byte_To_Convert))+' Expected bytes')
    # For Hashing Things Takes Items As bytes,str,bool
    def HashThemOut(self,Byte_To_Hash,Hash_Type,Return_Hex):
        if type(Byte_To_Convert) is bytes and type(Hash_Type) is str and type(Return_Hex) is bool:
            if str(Hash_Type) in hashlib.algorithms_available:
                H = hashlib.new(str(Hash_Type))
                H.update(Byte_To_Convert)
                if Return_Hex == True:
                    return H.hexdigest()
                else:
                    return H.digest()
            else:
                return ValueError(str(Hash_Type)+' Must Exist Inside Of hashlib.algorithms_available')
        else:
            return TypeError(str(Byte_To_Convert)+'//'+str(Hash_Type)+'//'+str(Return_Hex)+' Expected bytes,str,bool')
    # Root Pipe
    def RootPipe(self,IO):
        if type(IO) is list:
            if len(IO) == 2:
                Action = str(IO[0])
                Extend = IO[1]
                if type(Extend) is list:
                    if str(Action) == str('Reverse_String'):
                        if len(Extend) == 1:
                            return [IO,str(self.ReverseString(Extend[0]))]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('Convert_To_Byte'):
                        if len(Extend) == 1:
                            return [IO,self.ConvertToByte(str(Extend[0]))]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('Convert_From_Byte'):
                        if len(Extend) == 1:
                            return [IO,self.Convert_From_Byte(Extend[0])]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('Hash_Them_Out'):
                        if len(Extend) == 3:
                            return [IO,self.Hash_Them_Out(Extend)]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 3 Entities (Extend)')
class Root:
################################################################################
    '''
[Version]     >> Al13N 3.1.0
[Information] >> POC For OOP Based Operations
Objects:
--Root.__init__(self)
 |> Triggered When Mounting Root()
 |> self.RooTUniverse (dict) // Central Memory
 |> self.SymLUniverse (dict) // Symbloic Link Memory
 |> self.DimensionLoW (int)  // Dimension Generation Low
 |> self.DimensionHiG (int)  // Dimension Generation High
 |> self.DimensionPaD (int)  // Padding Count
 |> self.BiTMaP       (list) // Memory Pages For Dimensions
 |> self.Tools      (method) // ToolBox() Mount
--Root._RooTHandle_(self,IO)
 |> Used For Working With Root() Takes 1 Input As list
 |> IO Takes 3 Itmes [str,list,list]
 |> [0] - Mode
 |> [1] - Location
 |> [2] - Mode Input If Needed
----Modes:
 -- |> v-l,validationlocation,ValidateLocation,VALIDATELOCATION
 ... |> Used For Validating Locations Inside [1] // [2] Is Ignored
 ... |> Returns list [bool,location,error/location]
 ... |> If Invalid [2] Will Carry Invalid Location

 -- |> g-g,generategalaxy,GenerateGalaxy,GENERATEGALAXY
 ... |> Used For Generating Galaxies [1] Must Contain 1 Entity
 ... |> If [2] Has 0 Entities The Settings Will Default Elif
 ... |> [2] Has 3 Entities As [int,int,int] That Will Be Used

 -- |> g-sl,generatesymlink,GenerateSymLink,GENERATESYMLINK
 ... |> Used For Generating Symbolic Links [1] Must Be A Full
 ... |> Location And [2] Must Carry 1 Entity For Labeling
 ... |> The Mount Will Carry [1][0].[2][0] And Can Be Called
 ... |> As Its String Value Inside Of [1]

 -- |> g-vs,variablesimple,VariableSimple,VARIABLESIMPLE
 ... |> Used For Configuring Simple Variables [1] Must Be
 ... |> Valid And [2] Must Carry 1 Entity As int,str,list, Or bool

 -- |> g-va,variableadvanced,VariableAdvanced,VARIABLEADVANCED
 ... |> Used For Configuring Advanced Variables [1] Must Be
 ... |> Valid And [2] Must Varry 1 Entity As dict,tuple, Or bytes

 -- |> t-b,triggerbit,TriggerBiT,TRIGGERBIT
 ... |> Used For Triggering BiTs [1] Must Be Valid If [2] Is Empty
 ... |> Than Return A list Elif [2] Carries A Location Than Redirect
 ... |> To That Location

 -- |> l-bl,logicbool,LogicBool,LOGICBOOL
 ... |> Used For Processing BiT Values And Returning A Boolean IfEqual
 ... |> [1] Must Be Valid [2] Must Carry To Entities As [list,list]
 ... |> [2][0] & [2][1] Must Be Valid Locations
 ... |> If [2][0] == [2][1] Return True
 ... |> Sends Output As list [Type,[[2][0],[2][1]],bool]

 -- |> g-f,generatefunction,GenerateFunction,GENERATEFUNCTION
 ... |> Used For Mounting Internal Functions And Returns The Output
 ... |> [1] Must Be Valid [2] Must Carry A Valid Location Or If
 ... |> len() Is 0 Than Execute Without Location
    '''
################################################################################
    def __init__(self):
        # Variable Generation (Root)
        self.RooTUniverse  = {}   # Root Memory
        self.SymLUniverse  = {}   # Symbolic Memory
        self.DimensionLoW  = 0    # Dimension Range Lower
        self.DimensionHiG  = 1    # Dimension Range High
        self.DimensionPaD  = 0    # Padding Count Adds 'f' To Hexed Dimensions
        self.BiTMaP        = [    # BiTMaP Addresses
            '0000x0000','0000x0001','0000x0010','0000x0100','0000x1000','0000x0011','0000x0101','0000x1001','0000x1011','0000x1111', # lvl 0
            '0001x0000','0001x0001','0001x0010','0001x0100','0001x1000','0001x0011','0001x0101','0001x1001','0001x1011','0001x1111', # lvl 1
            '0010x0000','0010x0001','0010x0010','0010x0100','0010x1000','0010x0011','0010x0101','0010x1001','0010x1011','0010x1111', # lvl 2
            '0100x0000','0100x0001','0100x0010','0100x0100','0100x1000','0100x0011','0100x0101','0100x1001','0100x1011','0100x1111', # lvl 3
            '1000x0000','1000x0001','1000x0010','1000x0100','1000x1000','1000x0011','1000x0101','1000x1001','1000x1011','1000x1111', # lvl 4
            '0011x0000','0011x0001','0011x0010','0011x0100','0011x1000','0011x0011','0011x0101','0011x1001','0011x1011','0011x1111', # lvl 5
            '0101x0000','0101x0001','0101x0010','0101x0100','0101x1000','0101x0011','0101x0101','0101x1001','0101x1011','0101x1111', # lvl 6
            '1001x0000','1001x0001','1001x0010','1001x0100','1001x1000','1001x0011','1001x0101','1001x1001','1001x1011','1001x1111', # lvl 7
            '1011x0000','1011x0001','1011x0010','1011x0100','1011x1000','1011x0011','1011x0101','1011x1001','1011x1011','1011x1111', # lvl 8
            '1111x0000','1111x0001','1111x0010','1111x0100','1111x1000','1111x0011','1111x0101','1111x1001','1111x1011','1111x1111'  # lvl 9
        ]
        self.Tools              = ToolBox() # ToolBox Mount
    ############################################################################
    # // Revision: Moved _GenerateGalaxy_,_ValidateLocation_,_HandleBiT_ Into
    # // One Entity
    # Takes IO As list
    # [0] - str  // Mode
    # [1] - list // Location
    # [2] - list // Extended
    def _RooTHandle_(self,IO):
        # Validation
        if type(IO) is list:
            if len(IO) == 3:
                if type(IO[0]) is str and type(IO[1]) is list and type(IO[2]) is list:
                    # Capture Arguments
                    Mode = str(IO[0])
                    Tree = IO[1]
                    MDIO = IO[2]
                    # Capture Symbloic Locations
                    if len(Tree) == 1:
                        if str(Tree[0]) in self.SymLUniverse:
                            Tree = self.SymLUniverse[str(Tree[0])]
                    # Validaton Location Mode Catch Takes From Location
                    if str(Mode) in ['ValidateLocation','VALIDATELOCATION','validationlocation','v-l']:
                        if len(Tree) == 1:
                            if str(Tree[0]) in self.RooTUniverse:
                                return [True,Tree]
                            else:
                                return [False,Tree]
                        elif len(Tree) == 2:
                            if str(Tree[0]) in self.RooTUniverse:
                                if str(Tree[1]) in self.RooTUniverse[str(Tree[0])]:
                                    return [True,Tree,Tree]
                                else:
                                    return [False,Tree,Tree[1]]
                            else:
                                return[False,Tree,Tree[0]]
                        elif len(Tree) == 3:
                            if str(Tree[0]) in self.RooTUniverse:
                                if str(Tree[1]) in self.RooTUniverse[str(Tree[0])]:
                                    if str(Tree[2]) in self.RooTUniverse[str(Tree[0])][str(Tree[1])]:
                                        return [True,Tree,Tree]
                                    else:
                                        return [False,Tree,Tree[2]]
                                else:
                                    return [False,Tree,Tree[1]]
                            else:
                                return [False,Tree,Tree[0]]
                        else:
                            raise ValueError(str(len(Tree))+' Expected 1-3 Entities')
                    # Galaxy Generation Mode Takes 1 Location Target And Configures
                    # If MDIO Carries 3 Items Than Configure As Dimension Else Use
                    # Global Configurations
                    elif str(Mode) in ['GenerateGalaxy','GENERATEGALAXY','generategalaxy','g-g']:
                        if len(Tree) == 1:
                            Target = str(Tree[0])
                            if str(Target) not in self.RooTUniverse:
                                if len(MDIO) == 3:
                                    if type(MDIO[0]) is int and type(MDIO[1]) is int and type(MDIO[2]) is int:
                                        if int(MDIO[0]) < int(MDIO[1]):
                                            Dimensions = MDIO
                                        else:
                                            raise ValueError(str(int(MDIO[0]))+'>'+str(int(MDIO[1]))+' Must Be <')
                                    else:
                                        raise TypeError(str(type(MDIO))+' Expected ints only')
                                else:
                                    Dimensions = [int(self.DimensionLoW),int(self.DimensionHiG),int(self.DimensionPaD)]
                                self.RooTUniverse[str(Target)] = {}
                                for D in range(Dimensions[0],Dimensions[1]):
                                    P = 'f'
                                    P = P*Dimensions[2]
                                    H = hex(int(D))+str(P)
                                    self.RooTUniverse[str(Target)][str(H)]={}
                                    for B in self.BiTMaP:
                                        self.RooTUniverse[str(Target)][str(H)][str(B)]=[]
                            else:
                                raise KeyError(str(Target)+' Already Exists')
                        else:
                            raise ValueError(str(len(Tree))+' Expected 1 Entity')
                    # Symbloic Link Generation Mode Takes A Full Location Once Complete It Can Be Found At
                    # Tree[0].MDIO[0] And Called As A Single Location
                    elif str(Mode) in ['GenerateSymLink','GENERATESYMLINK','generatesymlink','g-sl']:
                        if len(Tree) == 3:
                            if len(MDIO) == 1:
                                if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                    if str(MDIO[0]) not in self.SymLUniverse:
                                        self.SymLUniverse[str(Tree[0])+str('.')+str(MDIO[0])]=Tree
                                    else:
                                        raise KeyError(str(MDIO[0])+' Already Exists')
                                else:
                                    raise ValueError(str(Tree)+" Location Does'nt Exist")
                            else:
                                raise ValueError(str(len(MDIO))+' Expected 1 Entity (MDIO)')
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # Simple Variable Generation Mode Takes A Full Location And 1 Entity In
                    # MDIO As int/str/list/bool
                    elif str(Mode) in ['VariableSimple','VARIABLESIMPLE','variablesimple','g-vs']:
                        if len(Tree) == 3:
                            if len(MDIO) == 1:
                                if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                    if type(MDIO[0]) is str or type(MDIO[0]) is int or type(MDIO[0]) is list or type(MDIO[0]) is bool:
                                        self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VR-S',MDIO[0]]
                                    else:
                                        raise TypeError(str(type(MDIO[0]))+' Expected str/int/list')
                                else:
                                    raise KeyError(str(Tree)+" Entity Does'nt Exist")
                            else:
                                raise ValueError(str(len(MDIO))+' Expected 1 Entity (MDIO)')
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # Advanced Variable Generation Mode Takes A Full Location And 1 Entity In
                    # MDIO As dict/tuple/bytes
                    elif str(Mode) in ['VariableAdvanced','VARIABLEADVANCED','variableadvanced','g-va']:
                        if len(Tree) == 3:
                            if len(MDIO) >= 1:
                                if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                    self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VR-A',MDIO]
                                else:
                                    raise KeyError(str(Tree)+" Entity Does'nt Exist")
                            else:
                                raise ValueError(str(len(MDIO))+' Expected 1 Entity (MDIO)')
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # Generate Output Variable Mode Takes A Full Location And No Entities In MDIO
                    elif str(Mode) in ['GenerateOutput','GENERATEOUTPUT','generateoutput','g-o']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['GL-O',None]
                            else:
                                raise KeyError(str(Tree)+" Entity Does'nt Exist")
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # Generate Python Internal Function Mount Communicates Info
                    elif str(Mode) in ['GenerateFunction','GENERATEFUNCTION','generatefunction','g-f']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                if len(MDIO) == 2:
                                    Function  = MDIO[0]
                                    InputLoc  = MDIO[1]
                                    if str(type(Function)) in ["<class 'function'>","<class 'method'>","<class 'builtin_function_or_method'>"]:
                                        if type(InputLoc) is list:
                                            if len(InputLoc) == 0:
                                                pass
                                            elif len(InputLoc) == 1:
                                                if str(InputLoc[0]) in self.SymLUniverse:
                                                    InputLoc = self.SymLUniverse[str(InputLoc[0])]
                                                else:
                                                    raise ValueError(str(InputLoc[0])+' Invalid Location Sent Or Length')
                                            elif len(InputLoc) == 3:
                                                if self._RooTHandle_(['v-l',InputLoc,[]])[0] == False:
                                                    raise ValueError(str(InputLoc[0])+" Entity Does'nt Exist")
                                            else:
                                                raise ValueError(str(len(InputLoc))+' Expected 3 Entities (InputLoc)')
                                            self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['FN-I',[Function,InputLoc]]
                                        else:
                                            raise TypeError(str(type(InputLoc))+' Expected list')
                                    else:
                                        raise TypeError(str(type(InputLoc))+' Expected "function-ids"')
                                else:
                                    raise ValueError(str(len(MDIO))+' Expected 2 Entities (MDIO)')
                            else:
                                raise KeyError(str(Tree)+" Entity Does'nt Exist (Tree)")
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # True/False IsEqual Check Takes A Full Location And 2 Entities In MDIO
                    # [0] - list // Target For Value
                    # [1] - list // Target For Comparison
                    elif str(Mode) in ['LogicBool','LOGICBOOL','logicbool','l-bl']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                # MDIO Validation
                                if len(MDIO) == 2:
                                    if type(MDIO[0]) is list and type(MDIO[1]) is list:
                                        if len(MDIO[0]) == 1:
                                            if str(MDIO[0]) in self.SymLUniverse:
                                                MDIO[0] = self.SymLUniverse[str(MDIO[0])]
                                            else:
                                                raise ValueError(str(MDIO[0])+' Expected Symlink Or Length')
                                        elif len(MDIO[1]) == 1:
                                            if str(MDIO[1]) in self.SymLUniverse:
                                                MDIO[1] = self.SymLUniverse[str(MDIO[1])]
                                            else:
                                                raise ValueError(str(MDIO[1])+' Expected Symlink Or Length')
                                        elif len(MDIO[0]) == 3:
                                            if self._RooTHandle_(['v-l',MDIO[0],[]])[0] == False:
                                                raise ValueError(str(MDIO[0])+" Entity Does'nt Exist")
                                        elif len(MDIO[1]) == 3:
                                            if self._RooTHandle_(['v-l',MDIO[1],[]])[0] == False:
                                                raise ValueError(str(MDIO[1])+" Entity Does'nt Exist")
                                        self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['LG-B',[MDIO[0],MDIO[1]]]
                                    else:
                                        raise TypeError(str(type(MDIO[0]))+'//'+str(type(MDIO[1]))+' In '+str(MDIO)+' Expected list')
                                else:
                                    raise ValueError(str(len(MDIO))+' Expected 2 Entities (MDIO)')
                            else:
                                raise KeyError(str(Tree)+" Entity Does'nt Exist")
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities')
                    # Shell Triggering Takes list And Captures Output
                    # [*] Commands
                    elif str(Mode) in ['ShellTrigger','SHELLTRIGGER','shelltrigger','s-t']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['SH-T',MDIO]
                            else:
                                raise ValueError(str(Tree)+" Doesn'nt Exist")
                        else:
                            raise ValueError(str(len(Tree))+' From '+str(Tree)+' Expected 3 Entities')
                    # ToolBox Pipe Handling Takes Operations And Waits For Trigger
                    # Takes A Full Location And 2 Entities In MDIO
                    # [0] - str   // Action
                    # [1] - list  // Inputs For Actions
                    elif str(Mode) in ['ToolBox','TOOLBOX','toobox','g-tb']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                if len(MDIO) == 2:
                                    Action = str(MDIO[0])
                                    if str(Action) in ['Reverse_String','Convert_To_Byte','Convert_From_Byte','Hash_Them_Out']:
                                        Inputs = MDIO[1]
                                        self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['TL-BX',[Action,Inputs]]
                                    else:
                                        raise ValueError(str(Action)+' Invalid Operational Argument')
                                else:
                                    raise ValueError(str(len(MDIO))+' Expected 2 (MDIO)')
                            else:
                                raise ValueError(str(Tree)+" Does't Exist")
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # Address Triggering Handler Mode Takes A Full Location And A Possible Second
                    # Location Inside Of MDIO If MDIO Is Left Empty Than Return A List
                    # [Tree,BiT,value]
                    # If There Is A Output From The Action It Will Also Be Redirected
                    elif str(Mode) in ['TriggerBiT','TRIGGERBIT','triggerbit','t-b']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                BiT = self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]
                                # BiT Validation
                                if len(MDIO) == 0:
                                    ReT = None
                                else:
                                    # MDIO Validation
                                    if len(MDIO) == 3:
                                        if self._RooTHandle_(['v-l',MDIO,[]])[0] == True:
                                            ReT = MDIO
                                        else:
                                            raise ValueError(str(len(MDIO))+" Entity Does'nt Exist")
                                    elif len(MDIO) == 1:
                                        if str(MDIO[0]) in self.SymLUniverse:
                                            ReT = self.GenerateSymLink[str(MDIO[0])]
                                        else:
                                            raise ValueError(str(len(MDIO))+' Expected 1/3 Entities (MDIO)')
                                    else:
                                        raise ValueError(str(len(MDIO))+' Expected 1/3 Entities (MDIO)')
                                # Non Configured BiT Catch
                                if len(BiT) == 0:
                                    if ReT == None:
                                        return [Tree,BiT,[]]
                                    else:
                                        if len(self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]) == 0:
                                            self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=BiT
                                        else:
                                            if str(self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])][0]) in ['GL-O']:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=BiT
                                            else:
                                                raise KeyError(str(MDIO)+' Expected Output Type Variable or None Conigure')
                                else:
                                    # BiT Handling If Configured
                                    Trigger = BiT[0] # Type
                                    Value   = BiT[1] # Value
                                    # Variables
                                    if str(Trigger) in ['VR_S','VR_A']:
                                        if ReT == None:
                                            return [Tree,BiT,Value]
                                        else:
                                            self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=[str(Trigger),Value]
                                    # Output Type
                                    elif str(Trigger) in ['GL-O']:
                                        if ReT == None:
                                            return [Tree,BiT,Value]
                                        else:
                                            self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=[str(Trigger),Value]
                                    # Logic Type
                                    elif str(Trigger) in ['LG-B']:
                                        Input_Value  = [Value[0],self.RooTUniverse[str(Value[0][0])][str(Value[0][1])][str(Value[0][2])]]
                                        Check_Value  = [Value[1],self.RooTUniverse[str(Value[1][0])][str(Value[1][1])][str(Value[1][2])]]
                                        if len(Input_Value[1]) == 0 or len(Check_Value[1]) == 0:
                                            raise ValueError(str(Input_Value)+str('//')+str(Check_Value)+' Not Configured')
                                        if str(Input_Value[1][0]) == str(Check_Value[1][0]):
                                            if Input_Value[1][1]  == Check_Value[1][1]:
                                                if ReT == None:
                                                    return [Trigger,Value,True]
                                                else:
                                                    self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',True]
                                            else:
                                                if ReT == none:
                                                    return [Trigger,Value,False]
                                                else:
                                                    self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',False]
                                        else:
                                            if ReT == None:
                                                return [Trigger,Value,False]
                                            else:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',False]
                                    # Internal Function
                                    elif str(Trigger) in ['FN-I']:
                                        Func = Value[0]
                                        Loct = Value[1]
                                        if len(Loct) == 0:
                                            Outp = Func()
                                            if ReT == None:
                                                return [Tree,BiT,Outp]
                                            else:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',Outp]
                                        else:
                                            Valu = self.RooTUniverse[str(Loct[0])][str(Loct[1])][str(Loct[2])]
                                            if str(Valu[0]) in ['GL-O','VR-S','VR-A']:
                                                Outp = Func(Valu[1])
                                                if ReT == None:
                                                    return [Tree,BiT,Outp]
                                                else:
                                                    self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',Outp]
                                            else:
                                                raise ValueError(str(Loct)+'//'+str(Valu)+' Expected Var/Output Type')
                                    elif str(Trigger) in ['SH-T']:
                                        Command = Value
                                        try:
                                            Output = subprocess.Popen(Command,stdout=subprocess.PIPE,shell=True)
                                            Output = str(Output.stdout.read())
                                            if ReT == None:
                                                return [Tree,BiT,Output]
                                            else:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',Output]
                                        except Exception as e:
                                            raise Exception(str(e)+' From '+str(Command))
                                    elif str(Trigger) in ['TL-BX']:
                                        Action = Value[0]
                                        Inputs = Value[1]
                                        try:
                                            Output = self.Tools.RootPipe([str(Action),[Inputs]])
                                            if ReT == None:
                                                return [Tree,BiT,Output]
                                            else:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',Output]
                                        except ValueError as V:
                                            raise ValueError('In '+str(Tree)+'/'+str(BiT)+' Got Error '+str(V))
                                        except TypeError  as T:
                                            raise TypeError('In '+str(Tree)+'/'+str(BiT)+' Got Error '+str(T))
                                        except KeyError   as K:
                                            raise KeyError('In '+str(Tree)+'/'+str(BiT)+' Got Error '+str(K))
                                        except Exception as  E:
                                            raise Exception('In '+str(Tree)+'/'+str(BiT)+' Got Errir '+str(E))
################################################################################
class Interpreter:
    '''
[Version]     >> Al13N 3.1.0
[Information] >> Interpreter For Root()
Objects:
--Interpreter.__init__(verbose=bool,logging=bool)
 |> Used On Mounting Interpreter
 |> self.Settings                              (dict) // Settings For Everything
---|> 'conf':'verbose-status'/'logging-status' (bool) // Configuration
---|> 'memory':'verbose-logg'/'logging-logg'   (list) // Log list
-----|> 'memory':'message-header':'user-entry'/'user-mesg'
-----                                           (str) // Messages For Printing
---|> 'colors':'F.*'/'B.*'/'S.*'
 |> self.RootMount                             (func) // Mount For Root()
--Interpreter._PipeColor_(str)
 |> Used For Colorizing Messages
 |> Takes Color Codes As {T.C}
--Interpreter._PipeLog_(str)
 |> Used For Logging Messages
 |> Takes str And Appends To self.Settings['memory']['logging-logg']
 |> If self.Settings['conf']['logging-status'] If False Do Nothing
--Interpreter._PipeOut_(str)
 |> Used For Sending Messages To The Screen
 |> Logs Into self.Settings['conf']['verbose-logg'] If False Do Nothing
--Interpreter._CommandToInstructionLvl0_(str)
 |> Used For The Opening Steps Of Instruction Conversion
 |> Returns list Of Items [[Parsed-Items],...]
--Interpreter._CommandToInstructionLvl1_(list)
 |> Used For Secondary Steps Of Instruction Converrsion
 |> Returns list Of Items [Parsed-Items]
--Interpreter._CommandToInstructionLvl2_(list)
 |> Used As The Final Step Of Instruction Conversion
 |> Returns Instruction For Root._RooTHandle_()
--Interpreter._ExecuteInstructionLvl0_(list)
 |> Used For Triggering Root._RooTHandle_()
--Interpreter._ExecuteInstructionLvl1_(str)
 |> Used For Running Through THe Parsing And Generation Process
 |> Stage_1 = self._CommandToInstructionLvl0_
 |> Stage_2 = self._CommandToInstructionLvl1_
 |> Stage_2 = self._CommandToInstructionLvl2_
 |> Stage_4 = self._ExecuteInstructionLvl0_
--Interpreter.Loop0()
 |> Loop For The Interpreter
    '''
    def __init__(self,verbose=True,logging=True):
        if type(verbose) is bool and type(logging) is bool:
            self.Settings = {
                'conf':{
                    'verbose-status' :verbose,
                    'logging-status' :logging
                },
                'memory':{
                    'verbose-logg'   :[],
                    'logging-logg'   :[],
                    'output-logg'    :[],
                    'message-header' :{
                        'user-entry':'{F.G}{S.N}--[{F.C}User Entry{F.G}]{F.Y}>{F.W} ',
                        'user-messg':'{F.B}{S.B}--[{F.C}Message{F.B}]{F.M}>{F.W} '   ,
                        'user-help' :[
                            '{F.G}Help: ({F.W}Interpreter-Functions{F.G})',
                            '{F.Y}  |>{F.C} !exit,!Exit,!EXIT',
                            '{F.W}  ->{F.B} \tExists The Terminal',
                            '{F.Y}  |>{F.C} !fetch-log,!Fetch-Log,!FETCH-LOG',
                            '{F.W}  ->{F.B} \tSends Current Logger Log To System',
                            '{F.Y}  |>{F.C} !fetch-vrb,!Fetch-Vrb,!FETCH_VRB',
                            '{F.W}  ->{F.B} \tSends Current Verbose Log To System',
                            '{F.Y}  |>{F.C} !fetch-out,!Fetch-Out,!FETCH-OUT',
                            '{F.W}  ->{F,B} \tSends Current Output Log To System',
                            '{F.Y}  |>{F.C} !config-log,!Config-Log,!CONFIG-LOG',
                            '{F.W}  ->{F.B} \tConfigures Logger',
                            '{F.Y}  |>{F.C} !config-vrb,!Config-Vrb,!CONFIG-VRB',
                            '{F.W}  ->{F.B} \tConfigures Verbose',
                            '{F.Y}  |>{F.C} !display-galaxies,!Display-Galaxies,!DISPLAY-GALAXIES',
                            '{F.W}  ->{F.B} \tReads Out Existing Galaxies With BiT Count',
                            '{F.Y}  |>{F.C} !help,!Help,!HELP,/?',
                            '{F.W}  ->{F.B} \tSends Out This Help Screen',
                            '{F.R}  |>{F.M}---{F.B} Advanced {F.W}(!OP->IO)',
                            '{F.Y}  |>{F.C} !index,!Index,!INDEX',
                            '{F.W}  ->{F.B} \tMessage Containing Entities',
                            '{F.Y}  |>{F.C} !set-entry,!Set-Entry,!SET-ENTRY',
                            '{F.W}  ->{F.B} \tConfigures New Entry Message',
                            '{F.Y}  |>{F.C} !set-head,!Set-Head,!SET-HEAD',
                            '{F.W}  ->{F.B} \tConfigures New Head Message',
                            '{F.Y}  |>{F.C} !color-item,!Color-Item,!COLOR-ITEM',
                            '{F.W}  ->{F.B} \tColorize A Message',
                            '{F.G}Help: ({F.W}Interpreter-Syntax{F.G})',
                            '{F.M}  |>{F.R} Takes Commands And Handles',
                            '{F.M}  |>{F.B} Key ({F.G}||{F.B}) End Line Seperator',
                            '{F.M}  |>{F.B} Key ({F.G}::{F.B}) Central Seperator',
                            '{F.M}  |>{F.B} Key ({F.G}:-{F.B}) Location Parser',
                            '{F.M}  |>{F.B} Key ({F.G},{F.B})  List Based Parsing'
                        ]
                    }
                },
                'colors':{
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
            }
            self.RootMount = Root()
        else:
            raise TypeError('Values Sent Are Invalid Expected bool')
    ############################################################################
    # For Colorizing Messages
    def _PipeColor_(self,StringToColor):
        self._PipeLog_('_PipeColor_('+str(StringToColor)+')')
        for color in self.Settings['colors']:
            cid = str('{'+color+'}')
            if str(cid) in str(StringToColor):
                StringToColor = StringToColor.replace(str(cid),self.Settings['colors'][color])
        return StringToColor
    # For Sending Messages To The Screen
    def _PipeOut_(self,StringToSend):
        self._PipeLog_('_PipeOut_('+str(StringToSend)+')')
        Message_Head = self._PipeColor_(str(self.Settings['memory']['message-header']['user-messg']))
        if self.Settings['conf']['verbose-status'] == True:
            print(str(Message_Head)+str(StringToSend))
            self.Settings['memory']['verbose-logg'].append([str(time.asctime()),str(StringToSend)])
        else:
            return None
    # For Logging Messages And TimeStamps
    def _PipeLog_(self,LogToSend):
        if self.Settings['conf']['logging-status'] == True:
            self.Settings['memory']['logging-logg'].append([str(time.asctime()),str(LogToSend)])
        else:
            return None
    # For Parsing And Returning Structures Based Off Command Lvl0 (Strips NewLine And Seprator)
    def _CommandToInstructionLvl0_(self,Command):
        self._PipeLog_('_CommandToInstruction_('+str(Command)+')')
        if str('||') not in str(Command):
            raise ValueError('CommandToInstruction Handler : No Seperator Sent "||" '+str(Command))
        else:
            Tree_Pre = Command.split('||')
            Tree     = []
            for Item in Tree_Pre:
                if str(Item) == str(''):
                    continue
                elif str('::') in str(Item):
                    Tree.append(Item.split('::'))
                else:
                    raise ValueError('CommandToInstruction Handler : Invalid Argument Sent '+str(Item)+' @ '+str(Command))
            return Tree
    # For Parsing And Returning Structures Based Off Tree Lvl1 (Split And Valids Location And Variables)
    def _CommandToInstructionLvl1_(self,Tree):
        self._PipeLog_('_CommandToInstructionLvl1_('+str(Tree)+')')
        if type(Tree) is list:
            Stem = []
            for Item in Tree:
                if str(':-') in str(Item):
                    Location = str(Item).split(':-')
                    if len(Location) == 2:
                        Location = [str(Location[0])+'.'+str(Location[1])]
                        Stem.append(Location)
                    elif len(Location) == 3:
                        Stem.append(Location)
                    else:
                        raise ValueError('CommandToInstruction Handler : Invalid Location Sent '+str(Location))
                elif str(',') in str(Item):
                    List_Value = Item.split(',')
                    List_Outpt = []
                    List_Index = 0
                    for Entity in List_Value:
                        if Entity.isdigit() == True:
                            List_Outpt.append(int(Entity))
                        else:
                            List_Outpt.append(str(Entity))
                        List_Index += 1
                    Stem.append(List_Outpt)
                else:
                    Stem.append(str(Item))
            return Stem
        else:
            raise ValueError('CommandToInstruction Handler : Invalid Argument Sent '+str(Tree))
    # For Converting Lvl1 Conversions Into Instructions
    def _CommandToInstructionLvl2_(self,Stem):
        self._PipeLog_('_CommandToInstructionLvl2_('+str(Stem)+')')
        if type(Stem) is list:
            if str(Stem[0]) in ['+','new','New','NEW']:
                if len(Stem) == 3:
                    Target    = [str(Stem[1])]
                    Dimension = Stem[2]
                    if Dimension in ['null','Null','NULL']:
                        Dimension = []
                        return ['g-g',Target,[]]
                    elif type(Dimension) is list:
                        if len(Dimension) == 3:
                            return [ 'g-g', Target, Dimension]
                        else:
                            raise ValueError('CommandToInstruction Handler : Invalid Dimension Sent '+str(Dimension))
                    else:
                        raise ValueError('CommandToInstruction Handler : Invalid Dimension Sent '+str(Dimension))
                else:
                    raise ValueError('CommandToInstruction Handler : Stem Recieved Had Write Signature But Not Valid Length '+str(Stem))
            elif str(Stem[0]) in ['-', 'write','Write','WRITE']:
                if len(Stem) >= 4:
                    Target    = Stem[1]
                    Action    = str(Stem[2])
                    if len(Stem) == 4:
                        if str(Stem[3]) in ['null','Null','NULL']:
                            MDIO = []
                        elif type(Stem[3]) is list:
                            MDIO  = Stem[3]
                        else:
                            MDIO  = [Stem[3]]
                    else:
                        MDIO  = Stem[3:]
                    return [str(Action),Target,MDIO]
            else:
                raise ValueError('CommandToInstruction Handler : Stem Home Is Invalid '+str(Stem))
        else:
            raise ValueError('CommandToInstruction Handler : Expected list '+str(Stem))
    # For Running Instructions Into Root
    def _ExecuteInstructionLvl0_(self,Instruction):
        self._PipeLog_('_ExecuteInstructionLvl0_('+str(Instruction)+')')
        try:
            Output = self.RootMount._RooTHandle_(Instruction)
            return Output
        except ValueError as V:
            self._PipeOut_('Recieved ValueError From ('+str(Instruction)+') '+str(V))
            return 'ERROR:'+str(V)
        except TypeError  as T:
            self._PipeOut_('Recieved TypeError  From ('+str(Instruction)+') '+str(T))
            return 'ERROR:'+str(T)
        except KeyError   as K:
            self._PipeOut_('Recieved KeyError   From ('+str(Instruction)+') '+str(K))
            return 'ERROR:'+str(K)
        except Exception  as E:
            self._PipeOut_('Recieved Exception  From ('+str(Instruction)+') '+str(E))
    # For Running All Validations Fluidly
    def _ExecuteInstructionLvl1_(self,Script):
        self._PipeLog_('_ExecuteInstructionLvl1_('+str(Script)+')')
        Stage_1 = self._CommandToInstructionLvl0_(str(Script))
        for Option in Stage_1:
            if str(Option[0]) == str('/') or str(Option) == str(''):
                continue
            Stage_2   = self._CommandToInstructionLvl1_(Option)
            Stage_3   = self._CommandToInstructionLvl2_(Stage_2)
            Center_IO = self._ExecuteInstructionLvl0_(Stage_3)
            self.Settings['memory']['output-logg'].append([str(Script),str(Center_IO)])
    # For Running Our Loops
    def Loop0(self):
        self._PipeLog_('Loop0()')
        Status = True
        while Status == True:
            Uentry = self._PipeColor_(str(self.Settings['memory']['message-header']['user-entry']))
            Uentry = input(str(Uentry))
            self._PipeLog_('Loop0 -> User-Entry :: '+str(Uentry))
            if str(Uentry) == str(''):
                continue
            elif str(Uentry) in ['!exit','!Exit','!EXIT']:
                Status = False
            elif str(Uentry) in ['!Fetch-Log','!FETCH-LOG','!fetch-log']:
                self._PipeOut_(str(self.Settings['memory']['logging-logg']))
            elif str(Uentry) in ['!Fetch-Vrb','!FETCH-VRB','!fetch-vrb']:
                self._PipeOut_(str(self.Settings['memory']['verbose-logg']))
            elif str(Uentry) in ['!Config-Log','!CONFIG-LOG','!config-log']:
                if self.Settings['conf']['logging-status'] == True:
                    self.Settings['conf']['logging-status'] = False
                else:
                    self.Settings['conf']['logging-status'] = True
            elif str(Uentry) in ['!Config-Vrb','!CONFIG-VRB','!config-vrb']:
                if self.Settings['conf']['verbose-status'] == True:
                    self.Settings['conf']['verbose-status'] = False
                else:
                    self.Settings['conf']['verbose-status'] = True
            elif str(Uentry) in ['!Display-Galaxies','!DISPLAY-GALAXIES','!display-galaxies']:
                for Galaxy in self.RootMount.RooTUniverse:
                    Message  = '{'+str(Galaxy)+'}'
                    Message += '['+str(len(self.RootMount.RooTUniverse[Galaxy]))+']'
                    self._PipeOut_(str(Message))
            elif str(Uentry) in ['!Fetch-Out','!FETCH-OUT','!fetch-out']:
                for Output in self.Settings['memory']['output-logg']:
                    Message  = '{'+str(Output[0])+'}'
                    Message += '-> '+str(Output[1])
                    self._PipeOut_(str(Message))
            elif str(Uentry) in ['!help','!Help','!HELP','/?']:
                for Command in self.Settings['memory']['message-header']['user-help']:
                    Command = str(self._PipeColor_(Command))
                    self._PipeOut_(str(Command))
            elif str(Uentry[0]) == str('!') and str('->') in str(Uentry):
                Tree = Uentry.split('->')
                if str(Tree[0]) in ['!Index','!INDEX','!index']:
                    if str(Tree[1]) in self.RootMount.RooTUniverse:
                        Galaxy = self.RootMount.RooTUniverse[str(Tree[1])]
                        BitAdd = []
                        for Dimension in Galaxy:
                            for BiT in Galaxy[Dimension]:
                                if len(Galaxy[Dimension][BiT]) != 0:
                                    BitAdd.append(str(Dimension)+':'+str(BiT)+':'+str(Galaxy[Dimension][BiT]))
                        for Address in BitAdd:
                            self._PipeOut_(str(Galaxy)+str(':')+str(Address))
                    else:
                        self._PipeOut_(str(Uentry)+' | '+str(Tree)+' | '+str(Tree[1])+' Non Existant')
                elif str(Tree[0]) in ['!Set-Entry','!SET-ENTRY','!set-entry']:
                    Entry_Colorized = str(self._PipeColor_(Tree[1]))
                    self.Settings['memory']['message-header']['user-entry']=str(Entry_Colorized)
                elif str(Tree[0]) in ['!Set-Head','!SET-HEAD','!set-head']:
                    Entry_Colorized = str(self._PipeColor_(Tree[1]))
                    self.Settings['memory']['message-header']['user-messg']=str(Entry_Colorized)
                elif str(Tree[0]) in ['!Color-Item','!COLOR-ITEM','!color-item']:
                    Entry_Colorized = str(self._PipeColor_(Tree[1]))
                    self._PipeOut_(str(Entry_Colorized))
            else:
                try:
                    RootOut = self._ExecuteInstructionLvl1_(str(Uentry))
                except Exception as e:
                    self._PipeOut_(str(e)+' From '+str(Uentry))
        return
################################################################################
# Shell Call Configuration
Flag = {
    'interpreter':False,
    'execute'    :[False,None],
    'no-verbose' :False,
    'no-logging' :False,
    'output-path':str(os.getcwd()+str('/Output/')),
    'output-name':str(random.randint(1,99999999)),
    'output-extn':'.log',
    'input-path' :None
}
if len(sys.argv) > 1:
    CLoc = 0
    # Flag Handling
    for Arg in sys.argv[1:]:
        if str(Arg) in ['-i','--interpreter']:
            Flag['interpreter']=True
            CLoc += 1
            continue
        elif str(Arg) in ['-q','--quite']:
            Flag['no-verbose']=True
            CLoc += 1
            continue
        elif str(Arg) in ['-l','--no-logg']:
            Flag['no-logging']=True
            CLoc += 1
            continue
        elif str('=') in str(Arg):
            Arg = Arg.split('=')
            if str(Arg[0]) in ['-oP','--output-path']:
                if os.path.isdir(str(Arg[1])) == True:
                    Flag['output-path']=str(Argv[1])
                    CLoc += 1
                    continue
                else:
                    raise ValueError(str(Arg[1])+' Invalid Path Sent')
            elif str(Arg[0]) in ['-oN','--output-name']:
                Flag['output-name']=str(Arg[1])
                CLoc += 1
                continue
            elif str(Arg[0]) in ['-oE','--output-extension']:
                Flag['output-extn']=str(Arg[1])
                CLoc += 1
                continue
            elif str(Arg[0]) in ['-r','--execute']:
                Command = str(Arg[1])
                Flag['execute']=[True,str(Command)]
                CLoc += 1
                continue
            elif str(Arg[0]) in ['-iP','--input-path']:
                File = str(Arg[1])
                if os.path.isfile(str(File)) == True:
                    Flag['input-file']=str(File)
                else:
                    raise ValueError(str(Arg[1])+' Invalid Path Sent Non Existant')
            else:
                raise ValueError(str(Arg[1])+' Invalid Argument Sent By Seperator')
        else:
            raise ValueError(str(Arg[0])+' Invalid Argument Sent By Root')
    ############################################################################
    I = Interpreter()
    M = str('Al13N(3.1.0){}').format(str(time.asctime()))+str(' >> Flags Mounted')
    I._PipeOut_(str(M))
    for Entity in Flag:
        I._PipeOut_(str('Al13N(3.1.0) >> '+str(Entity))+' | '+str(Flag[Entity]))
    # Mount Interpreter And Handle Flags
    if Flag['no-verbose'] == True:
        I.Settings['conf']['verbose-status']=False
    elif Flag['no-logging'] == True:
        I.Settings['conf']['logging-status']=False
    elif Flag['execute'][0] == True:
        I._ExecuteInstructionLvl1_(str(Flag['execute'][1]))
        I._PipeOut_(str('Al13N(3.1.0) >> Script {} Handled').format(str(Flag['execute'][1])))
    elif Flag['input-path'] != None:
        Text   = open(str(Flag['input-path'])).read()
        Text_P = Text.split('\n')
        Text_S = []
        for line in Text_P:
            if str(line) != str(''):
                Text_S.append(str(line))
        I._ExecuteInstructionLvl1_(str(Text_S))
        I._PipeOut_(str('Al13N(3.1.0) >> Script {} Handled').format(str(Text)))
    elif Flag['interpreter'] == True:
        I._PipeOut_(str('Al13N(3.1.0) >> Opening Interpreter'))
        I.Loop0()
    ### Finishing Operations ###
    I._PipeOut_(str('Al13N(3.1.0) >> Checking Flags For Output Functions'))
    F = str(Flag['output-path'])+str('/{}').format(str(Flag['output-name'])+str(Flag['output-extn']))
    L = I.Settings['memory']['logging-logg']
    V = I.Settings['memory']['verbose-logg']
    O = I.Settings['memory']['output-logg']
    T = ''
    for LIndex in L:
        T += str('Logging::')+str(L[0])+str(' @ ')+str(L[1])+str('\n')
    for VIndex in V:
        T += str('Verbose::')+str(V[0])+str(' @ ')+str(V[1])+str('\n')
    for OIndex in O:
        T += str('Output ::')+str(O)+str("\n")
    for FIndex in Flag:
        T += str('Flags  ::')+str(Flag)+str(' @ '+str(Flag[FIndex]))
    T += str(I.RootMount.RooTUniverse)
    if Flag['no-logging'] == False:
        H = open(str(F),'w')
        H.write(str(T))
        H.close()
    if Flag['no-verbose'] == False:
        Message = str('Ended With '+str(len(I.RootMount.RooTUniverse))+' Items In Memory <')
        Message+= str(I.RootMount.RooTUniverse)+str('>')
        I._PipeOut_(str(Message))
    sys.exit(1)
