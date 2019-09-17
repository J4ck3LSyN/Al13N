# Version 3.2.5
# Revision Under Al13N-3.1.0
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
        if type(Byte_To_Hash) is not bytes:
            Byte_To_Hash = self.ConvertToByte(str(Byte_To_Hash))
        if Return_Hex in ['true','True'] or Return_Hex == True:
            Return_Hex = True
        elif Return_Hex in ['false','False'] or Return_Hex == False:
            Return_Hex = False
        else:
            Return_Hex = True
        Failed = False
        Reason = None
        Output = None
        try:
            H = hashlib.new(str(Hash_Type))
            H.update(Byte_To_Hash)
            if Return_Hex == True:
                Output = str(H.hexdigest())
            else:
                Output = str(H.digest())
        except Exception as E:
            Failed = True
            Reason = str(e)
        finally:
            if Failed == False and Output != None:
                return Output
            else:
                raise Exception('Opration Failed : '+str(e))
    # Root Pipe
    def RootPipe(self,IO):
        if type(IO) is list:
            if len(IO) == 2:
                Action = str(IO[0])
                Extend = IO[1]
                if type(Extend) is list:
                    # Function Based Operations
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
                            return [IO,self.ConvertFromByte(Extend[0])]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('Hash_Them_Out'):
                        if len(Extend[0]) == 3:
                            return [IO,self.HashThemOut(Extend[0][1],Extend[0][0],Extend[0][2])]
                        else:
                            raise ValueError(str(len(Extend))+' Expected 3 Entities (Extend)')
                    # Simplistic Operations
                    elif str(Action) == str('Convert_To_Hex'):
                        if len(Extend) == 1:
                            if type(Extend[0]) is int:
                                return hex(int(Extend[0]))
                            else:
                                raise TypeError(str(type(Extend))+' Expected int')
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('Convert_To_Bin'):
                        if len(Extend) == 1:
                            if type(Extend[0]) is int:
                                return bin(int(Extend[0]))
                            else:
                                raise TypeError(str(type(Extend))+' Expected int')
                        else:
                            raise ValueError(str(len(Extend))+' Expected 1 Entity (Extend)')
                    elif str(Action) == str('ShiftIntRight'):
                        if len(Extend) == 2:
                            if type(Extend[0]) is int and type(Extend[1]) is int:
                                return int(Extend[0]) >> int(Extended[1])
                            else:
                                raise TypeError(str(type(Extend[0]))+'/'+str(type(Extend[1]))+' Expected int,int')
                        else:
                            raise ValueError(str(len(Extend))+' Expteced 2 Entity (Extend)')
                    elif str(Action) == str('ShiftIntLeft'):
                        if len(Extend) == 2:
                            if type(EXtend[0]) is int and type(Extend[1]) is int:
                                return int(Extend[0]) << int(Extend[1])
                            else:
                                raise TypeError(str(type(Extend[0]))+'/'+str(type(Extend[1]))+' Expected int,int')
                        else:
                            raise ValueError(str(len(Extend))+' Expected 2 Entitie (Extend)')
                    elif str(Action) == str('XoR'):
                        if len(Extend) == 2:
                            if type(Extend[0]) is int and type(Extend[1]) is int:
                                return int(Extend[0])^int(Extend[1])
                            else:
                                raise TypeError(str(type(Extend[0]))+'/'+str(type(Extend[1]))+' Expected int,int')
                        else:
                            raise ValueError(str(len(Extend))+' Expected 2 Entities (Extend)')
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

 -- |> g-tb,toolbox,ToolBox,TOOLBOX
 ... |> Used For Working Inside Of The ToolBox Function Returns Output
 ... |> [1] Must Be The Action To Operate On

 -- |> c-ap,compileappend,CompileAppend,COMPILEAPPEND
 ... |> Used For Comning str,int,list Objects
 ... |> [1] Must Be The Variable To Fetch
 ... |> [2] Must Be The Location To Append To
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
                    # Capture Location Call
                    if len(MDIO) != 0:
                        if len(MDIO) == 3 and type(MDIO[0]) is str and str(MDIO[0][0]) == str('@'):
                            Possible_Location    = MDIO
                            Possible_Location[0] = MDIO[0].strip('@')
                            if self._RooTHandle_(['v-l',Possible_Location,[]])[0] == True:
                                Location_Value   = self.RooTUniverse[str(Possible_Location[0])][str(Possible_Location[1])][str(Possible_Location[2])]
                                if len(Location_Value) != 0:
                                    MDIO = Location_Value[len(Location_Value)-1]
                                else:
                                    raise ValueError(str(len(Possible_Location))+' Expected Configured BiT ')
                            else:
                                raise KeyError(str(Possible_Location)+" Does'nt Exist")
                        else:
                            # Indepth
                            Possible_Index  = 0
                            Possible_Fail   = False
                            Possible_Reason = None
                            for Possible_Location in MDIO:
                                if type(Possible_Location) is list:
                                    if len(Possible_Location) == 3 and str('@') in str(Possible_Location[0]):
                                        Possible_Location[0] = Possible_Location[0].strip('@')
                                        if self._RooTHandle_(['v-l',Possible_Location,[]])[0] == True:
                                            Location_Value   = self.RooTUniverse[str(Possible_Location[0])][str(Possible_Location[1])][str(Possible_Location[2])]
                                            if len(Location_Value) != 0:
                                                Location_Value = Location_Value[len(Location_Value)-1]
                                                MDIO[int(Possible_Index)]=Location_Value
                                                Possible_Index += 1
                                                continue
                                            else:
                                                Possible_Fail   = True
                                                Possible_Reason = str(Possible_Location)+str('Expected Configured BiT')
                                                break
                                        else:
                                            Possible_Fail   = True
                                            Possible_Reason = str(Possible_Location)+str(" Does'nt Exist")
                                            break
                                    else:
                                        Possible_Index += 1
                                        continue
                                else:
                                    Possible_Index += 1
                                    continue
                            if Possible_Fail == True:
                                raise Exception(str(Possible_Reason))
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
                                for D in range(int(Dimensions[0]),int(Dimensions[1])):
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
                    # Tree[0].MDIO[0] And Called As A Single Locationprint(MDIO)
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
                    # Usually Gets Used By t-b For Outputs
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
                                    if str(Action) in ['Reverse_String','Convert_To_Byte','Convert_From_Byte','Hash_Them_Out','Convert_To_Hex','Convert_To_Bin',
                                                       'Convert_From_Hex','Convert_From_Bin','ShiftRight','ShiftLeft','XoR']:
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
                    # Compilation Trigger For Appneding One Output To Another
                    # [0] - list // Location 1
                    # [1] - lsit // Location 2
                    elif str(Mode) in ['CompileAppend','COMPILEAPPEND','conpileappend','c-ap']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                if len(MDIO) == 2:
                                    Location_1 = MDIO[0]
                                    Location_2 = MDIO[1]
                                    if self._RooTHandle_(['v-l',Location_1,[]])[0] == True and self._RooTHandle_(['v-l',Location_2,[]])[0] == True:
                                        self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['C-APP',[Location_1,Location_2]]
                                    else:
                                        raise ValueError(str(Location_1)+'/'+str(Location_2)+" Does'nt Exist")
                                else:
                                    raise ValueError(str(len(MDIO))+' Expected 2 Entities (MDIO)')
                            else:
                                raise ValueError(str(Tree)+" Does'nt Exit (Tree)")
                        else:
                            raise ValueError(str(len(Tree))+' Expected Full Location (Tree)')
                    # Carries A List Of Locations to Exeecute
                    # [...] - Location List To Be Sent
                    elif str(Mode) in ['TriggerMaP','TRIGGERMAP','triggermap','t-m']:
                        if len(Tree) == 3:
                            if self._RooTHandle_(['v-l',Tree,[]])[0] == True:
                                if len(MDIO) > 0:
                                    Failed = False
                                    Reason = None
                                    MaP    = []
                                    for Index in MDIO:
                                        if type(Index) is list:
                                            if len(Index) == 1:
                                                if str(Index[0]) in self.SymLUniverse:
                                                    MaP.append(self.SymLUniverse[str(Index[0])])
                                                    continue
                                                else:
                                                    Failed = True
                                                    Reason = str(Index[0])+str(' From '+str(Index)+' Expected SymLink')
                                                    break
                                            elif len(Index) == 3:
                                                if self._RooTHandle_(['v-l',Index,[]])[0] == True:
                                                    MaP.append(Index)
                                                else:
                                                    Failed = True
                                                    Reason = str(Index)+str(" Does'nt Exist ")
                                                    break
                                            else:
                                                Failed = True
                                                Reason = str(len(Index))+' Expecteed 1 Or 3 Entities'
                                                break
                                        else:
                                            if str(Index) in self.SymLUniverse:
                                                MaP.append(self.SymLUniverse[str(Index)])
                                            else:
                                                Failed = True
                                                Reason = str(Index)+' Recieved Seperate Entity Not SymLink'
                                                break
                                    if Failed == True:
                                        raise Exception('Recieved Exception: '+str(Reason)+' From Operation')
                                    else:
                                        self.RooTUniverse[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['T-MP',MaP]
                                else:
                                    raise ValueError(str(len(MDIO))+' Expected More Than 0 Entities (MDIO)')
                            else:
                                raise ValueError(str(Tree)+" Doesn'nt Exist (Tree)")
                        else:
                            raise ValueError(str(len(Tree))+' Expected 3 Entities (Tree)')
                    # For Configuring One Output To A Input
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
                                    # Tool Box Trigger
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
                                            raise Exception('In '+str(Tree)+'/'+str(BiT)+' Got Error '+str(E))
                                    # Compile Append
                                    elif str(Trigger) in ['C-APP']:
                                        Target_1 = Value[0]
                                        Target_2 = Value[1]
                                        Value_1  = self.RooTUniverse[str(Target_1[0])][str(Target_1[1])][str(Target_1[2])]
                                        Value_2  = self.RooTUniverse[str(Target_1[0])][str(Target_2[1])][str(Target_2[2])]
                                        Output   = None
                                        if type(Value_2[1]) is str and type(Value_1[1]) is str:
                                            Output = str(Value_2[1])+str(Value_1[1])
                                        elif type(Value_2[1]) is list and type(Value_1[1]) is list:
                                            for Line in Value_1[1]:
                                                self.RooTUniverse[str(Target_2[0])][str(Target_2[1])][str(Target_2[2])][1].append(Line)
                                            Output = self.RooTUniverse[str(Target_2[0])][str(Target_2[1])][str(Target_2[2])][1]
                                            if ReT == None:
                                                return [Tree,BiT,[str(Target_1)+'/'+str(Value_1),str(Target_2)+'/'+str(Value_2)],Output]
                                            else:
                                                self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[1])]=['Gl-O',Output]
                                        elif type(Value_2[1]) is int and type(Value_1[1]) is int:
                                            Output = str(Value_2[1])+str(Value_1[1])
                                            Output = int(Output)
                                        else:
                                            raise TypeError(str(Value_1)+'/'+str(Value_2)+' Type Collision Or Does Not Work With Variable Type')
                                        self.RooTUniverse[str(Target_2[0])][str(Target_2[1])][str(Target_2[2])] = [str(Value_2),Output]
                                        if ReT == None:
                                            return [Tree,BiT,[str(Target_1)+'/'+str(Value_1),str(Target_2)+'/'+str(Target_2)]]
                                        else:
                                            self.RooTUniverse[str(MDIO[0])][str(MDIO[1])][str(MDIO[2])]=['GL-O',Output]
                                    # Trigger Map
                                    elif str(Trigger) in ['T-MP']:
                                        Target_Map = Value
                                        Output     = []
                                        for Target in Target_Map:
                                            if self._RooTHandle_(['v-l',Target,[]])[0] == True:
                                                O  = self._RooTHandle_(['t-b',Target,[]])[2]
                                                Output.append([Target,O])
                                        return [Tree,BiT,Output]
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
--Interpreter._ChapterFileHandle_(File,Chapter)
 |> For Handling Chapter Based Files
 |> If Chapter Is null Than Send Full File
 |> If Chapter Is ...  Than Send Chapters
 |> Else Send Chapter Called
--Interpreter._MountDiR_(File)
 |> For Importing Directories
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
                            '{F.B}  (Basic)',
                            '{F.Y}  |>{F.C} !exit,!Exit,!EXIT,!X',
                            '{F.R}  ->{F.M}    Exits The Interpreter',
                            '{F.Y}  |>{F.C} !help,!Help,!HELP,!?',
                            '{F.R}  ->{F.M}    Displays This Help Message',
                            '{F.Y}  |>{F.C} !log,!Log,!LOG,!L',
                            '{F.R}  ->{F.M}    Convert Log',
                            '{F.Y}  |>{F.C} !verbose,!Verbose,!VERBOSE,!V',
                            '{F.R}  ->{F.M}    Convert Verbose'
                            '{F.B}  (Advanced) CMD->IO',
                            '{F.W}  |>{F.C} !index,!Index,!INDEX,!IDX',
                            '{F.G}  ->{F.M}    Indexs The IO Sent',
                            '{F.W}  |>{F.C} !chapter,!Chapter,!CHAPTER,!',
                            '{F.G}  ->{F.M}    Takes 2 Inputs From IO',
                            '{F.G}  ->{F.M}    1 - File, 2 - Chapter'
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
        if str(Command) == str(''):
            return None
        elif str('||') not in str(Command):
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
                    raise ValueError('CommandToInstruction Handler : Expected 4 Or Greater Items For "-"')
            elif str(Stem[0]) in ['$','mount','Mount','MOUNT']:
                if len(Stem) == 2:
                    Target  = Stem[1]
                    self._MountDiR_(str(Target))
                else:
                    raise ValueError('CommandToInstruction Handler : Expected 2 Items For "$"')
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
        if Stage_1 == None: # Capture If No Input Was Sent Validation 2 Incase Pre Flag Not Sent
            self.Settings['memory']['output-logg'].append([str(Script),'NoneValue'])
            return
        for Option in Stage_1:
            if str(Option[0]) == str('/') or str(Option) == str(''):
                continue
            Stage_2     = self._CommandToInstructionLvl1_(Option)
            Stage_3     = self._CommandToInstructionLvl2_(Stage_2)
            Center_IO   = self._ExecuteInstructionLvl0_(Stage_3)
            self.Settings['memory']['output-logg'].append([str(Script),str(Center_IO)])
    # For Running Our Loops
    def Loop0(self,Flags_IN=None):
        self._PipeLog_('Loop0(Flags_IN='+str(Flags_IN)+')')
        Flags = {
            # Settings
            'Verbose'            :True,
            'Logging'            :False,
            'Record'             :False,
            # Output For Log
            'Output-Path-Log'    :str(os.getcwd())+str('/Output/'),
            'Output-Name-Log'    :str(random.randint(1111111,1111111111)),
            'Output-Ext-Log'     :str('.log'),
            # Output For Recorded Entries
            'Output-Path-Record' :'Null',
            'Output-Name-Record' :'Null',
            'Output-Ext-Record'  :'Null'
        }
        # Configure From Input
        if Flags_IN != None:
            if type(Flags_IN) is dict:
                for Entity in Flags_IN:
                    if str(Entity) in Flags:
                        if type(Flags_IN[Entity]) is type(Flags[Entity]):
                            Flags[Entity] = Flags_IN[Entity]
                        else:
                            raise TypeError(str(Entity)+' In '+str(Flags_IN)+' Contains Invlaid Type For '+str(Flags))
                    else:
                        raise KeyError(str(Entity)+' In '+str(Flags_IN)+' Contains Invalid Location For '+str(Flags))
            else:
                raise TypeError(str(type(Flags))+' Expected dict')
        # Configure Internals
        self.Settings['conf']['verbose-status'] = Flags['Verbose']
        self.Settings['conf']['logging-status'] = Flags['Logging']
        # Begin Handling
        Record = []
        Status = True
        # Print Information If Need Be
        if Flags_IN['Verbose'] == True:
            for Entity in Flags:
                self._PipeOut_('Flags :: '+str(Entity)+'>'+str(Flags[Entity]))
            self._PipeOut_('Initiating Enviroment')
        # Central Loop
        while Status == True:
            # Capture UEntry
            Uentry = str(self._PipeColor_(self.Settings['memory']['message-header']['user-entry']))
            Uinput = input(str(Uentry))
            # Capture Record If True
            if Flags['Record'] == True:
                Record.append(str(Uinput))
            # Internal Command Handle
            if str(Uinput) == str(''):
                continue
            elif str(Uinput)   in ['!exit','!Exit','!EXIT','!X']: # Exit
                Status = False
            elif str(Uinput) in ['!help','!Help','!HELP','!?']: # Help (Basic)
                for Message in self.Settings['memory']['message-header']['user-help']:
                    Message = str(self._PipeColor_(Message))
                    self._PipeOut_(str(Message))
            elif str(Uinput) in ['!log','!Log','!LOG','!L']: # Logging Switch
                if self.Settings['conf']['logging-status'] == True:
                    self.Settings['conf']['logging-status'] = False
                else:
                    self.Settings['conf']['logging-status'] = True
            elif str(Uinput) in ['!verbose','!Verbose','!VERBOSE','!V']: # Verbose Switch
                if self.Settings['conf']['verbose-status'] == True:
                    self.Settings['conf']['verbose-status'] = False
                else:
                    self.Settings['conf']['verbose-status'] = True
            elif str(Uinput[0]) == str('!') and str('->') in str(Uinput): # Seperator For Advanced Inputs
                Utree = Uinput.split('->')
                if str(Utree[0]) in ['!index','!Index','!INDEX','!IDX']: # !Index->*/Galaxy
                    if str(Utree[1]) in str(self.RootMount.RooTUniverse):
                        Index = self.RootMount.RooTUniverse[str(Utree[1])]
                        for Dimension in Index:
                            Lines = Index[str(Dimension)]
                            self._PipeOut_('[LOC]{BiT}\t@\tAddress   > LeN\t||\tItems')
                            #               {0x1}	@	1111x1111 >> 0	||	[]
                            for Line in Lines:
                                Message  = '{F.G}[{F.Y}'+str(Utree[1])+'{F.G}]'
                                Message += '{F.G}{{F.W}'+str(Dimension)+'{F.G}}\t{F.R}@{F.G}\t'+str(Line)+str(' {F.B}>>{F.G} ')
                                Message += str(len(Index[Dimension][Line]))+str('\t{F.M}||{F.G}\t')
                                Message += str(Index[Dimension][Line])
                                Message  = str(self._PipeColor_(Message))
                                self._PipeOut_(str(Message))
                            self._PipeOut_('-------------------------------------------')
                    else:
                        if str(Utree[1]) == str('*'): # * Catch Why Not elif? IdoNtKnoW
                            Index = self.RootMount.RooTUniverse
                            for I in Index:
                                Message  = '{F.B}[{F.R}'+str(I)+'{F.B}]'
                                Message += '[{F.G}'+str(len(Index[I]))+'{F.B}]'
                                Entities = {}
                                for E in Index[I]:
                                    for P in Index[I][E]:
                                        if len(Index[I][E][P]) != 0:
                                            Entities[str(E)+'/'+str(E)+'/'+str(P)]=Index[I][E][P]
                                self._PipeOut_(str(self._PipeColor_('{F.W}[{F.B}'+str(I)+'{F.W}] Galaxy')))
                                for E in Entities:
                                    self._PipeOut_(str(self._PipeColor_(str('\t')+Message+str(E)+str('\t')+str(Entities[E]))))
                        else:
                            self._PipeOut_(str(Utree[1])+' Is Not Valid')
                elif str(Utree[0]) in ['!show','!Show','!SHOW','!S']: # Informational ! !show->log/out/msg
                    if str(Utree[1]) in ['log','Log','LOG']:
                        Message = self.Settings['memory']['logging-logg']
                        for MSG in Message:
                            self._PipeOut_(str(MSG))
                    elif str(Utree[1]) in ['out','Out','OUT']:
                        Message = self.Settings['memory']['output-logg']
                        for MSG in Message:
                            self._PipeOut_(str(MSG))
                    elif str(Utree[1]) in ['msg','Msg','MSG']:
                        Message = self.Settings['memory']['verbose-logg']
                        for MSG in Message:
                            self._PipeOut_(str(MSG))
                    else:
                        self._PipeOut_('Invalid Location Sent For !show '+str(Utree[1]))
                elif str(Utree[0]) in ['!chapter','!Chapter','!CHAPTER']: # self._ChapterFileHandle_ Pipe
                    if len(Utree) == 3:
                        File = str(Utree[1])
                        Page = str(Utree[2])
                        if str(Page) in ['null','Null','NULL','None']:
                            Page = None
                        if os.path.isfile(str(File)) == True:
                            self._ChapterFileHandle_(str(File),Page)
                        else:
                            self._PipeOut_('Invalid Location Sent For !chapter '+str(File))
                    else:
                        self._PipeOut_('Expected 3 Seperation Points Recieved '+str(len(Utree)))
            else: # Fail Catch
                # Attempt Command Catch
                try:
                    self._ExecuteInstructionLvl1_(str(Uinput))
                except ValueError as V:
                    self._PipeOut_('Recieved ValueError From ('+str(Uinput)+') - '+str(V))
                except TypeError   as T:
                    self._PipeOut_('Recieved TypeError  From ('+str(Uinput)+') - '+str(T))
                except KeyError    as K:
                    self._PipeOut_('Recieved KeyError   From ('+str(Uinput)+') - '+str(K))
                except Exception   as E:
                    self._PipeOut_('Recieved Exception  From ('+str(Uinput)+') - '+str(E))
        # When Done Validate Record And Send To File
        if Flags['Record'] == True:
            if os.path.isdir(str(Flags['Output-Path-Record'])) == True:
                File_Name = str(Flags['Output-Name-Record'])+str('.')+str(Flags['Output-Ext-Record'])
                File_Path = str(Flags['Output-Path-Record'])+str('/')+str(File_Name)
                File_Text = ''
                for Line in Record:
                    File_Text += str(Line)+str('\n')
                try:
                    F = open(str(File_Path),'w')
                    F.write(str(File_Text))
                    F.close()
                except Exception as e:
                    raise Exception(str('Recieved Exception From : ')+str(e))
            else:
                raise ValueError(str(Flags['Output-Path-Record'])+' Is Not A Valid Directory')
        # Capture Log And Send To File
        if Flags['Logging'] == True and self.Settings['conf']['logging-status'] == True:
            if os.path.isdir(str(Flags['Output-Path-Log'])) == True:
                File_Name = str(Flags['Output-Name-Log'])+str('.')+str(Flags['Output-Ext-Log'])
                File_Path = str(Flags['Output-Path-Log'])+str('/')+str(File_Name)
                File_Text = ''
                for V in self.Settings['memory']['verbose-logg']:
                    File_Text += str('VERBOSE ::')+str(V)+str('\n')
                for L in self.Settings['memory']['logging-logg']:
                    File_Text += str('LOGGING ::')+str(L)+str('\n')
                for O in self.Settings['memory']['output-logg']:
                    File_Text += str('OUTPUT  ::')+str(O)+str('\n')
                for F in Flags:
                    File_Text += str('FLAGS   ::')+str(F)+str(Flags[F])+str('\n')
                for R in Record:
                    File_Text += str('RECORD  ::')+str(R)+str('\n')
                for G in self.RootMount.RooTUniverse:
                    File_Text += str('MEMORY  ::')+str(G)+str(self.RootMount.RooTUniverse[G])+str('\n')
                try:
                    F = open(str(File_Path),'w')
                    F.write(str(File_Text))
                    F.close()
                except Exception as e:
                    raise Exception(str('Recieved Exception From : ')+str(e))
            else:
                raise Exception(str(Flags['Output-Path-Log'])+' Is Not A Valid Directory')
        return
    ###########################################################################
    # For Converting Entry Values For Flags On IO To Be Sent To:
    # self.Loop0(Flags_IN=Flags)
    # Takes Inputs Check Usage
    def _FlagsConvert_(self,IO):
        self._PipeLog_('_FlagsConvert_('+str(IO)+')')
        Flags = {
            # Settings
            'Verbose'            :True,
            'Logging'            :False,
            'Record'             :False,
            # Output For Log
            'Output-Path-Log'    :str(os.getcwd())+str('/Output/'),
            'Output-Name-Log'    :str(random.randint(1111111,1111111111)),
            'Output-Ext-Log'     :str('.log'),
            # Output For Recorded Entries
            'Output-Path-Record' :'Null',
            'Output-Name-Record' :'Null',
            'Output-Ext-Record'  :'Null'
        }
        Trigger_File  = None
        Trigger_Cmd   = None
        Trigger_Loop0 = False
        Failed        = False
        Usage         = {
            'Help@-h,--help,-?':[
                'Displays This Help Message',
                'Can Take 1 Input Or Nothing',
                'The Input Would Be Handled Via',
                'Command Wanted, If None than Send All'
            ],
            'Interpreter@-i,--interpreter':[
                'Triggers The Interpreter'
            ],
            'Silence@-q,--quite':[
                'Configures The Verbose A Input Pronmt Will',
                'Be Sent If -i Is Provided But All Output',
                'Can Be Displayed Via !show-out'
            ],
            'Logging@-l,--nolog':[
                'Configures Internal Log If False Dont Log',
                'Can Be Configured With More:',
                ' -onl,-opl,-oel'
            ],
            'Recording@-r,--record':[
                'Configures Internal Record Boolean If True',
                'Use Record For All Interpreter Input'
            ],
            'Output_Loggh@-opn.--output-path-log':[
                'Takes 1 Input And Must Be A Valid Path',
                'Configures Path For Logging Output'
            ],
            'Output_Logg@-onl.--output-name-log':[
                'Takes 1 Input',
                'Configures Name For Logging Output'
            ],
            'Output_Logg@-oel,--output-extension-log':[
                'Takes 1 Input And Cannot Contain "."',
                'Configures Extension For Logging Output'
            ],
            'Output_Record@-opr,--output-path-record':[
                'Takes 1 Input And Must Be A Valid Path',
                'Configures Path For Record Output'
            ],
            'Output_Record@-onr.--output-name-record':[
                'Takes 1 Input',
                'Configures Name For Record Output'
            ],
            'Output_Record@-oer,--output-extension-record':[
                'Takes 1 Input And Cannot Contain "."',
                'Confgures Extension For Record Output'
            ],
            'Execution@-e,--execute':[
                'Takes 1 Input Within Quotes ""',
                'Sends Input Through Internal Command Handler'
            ],
            'Reading_File@-f,--file':[
                'Takes 1 Input And must Be A Valid File',
                'Sends All Lines Through Internal Command Handler'
            ],
            'Chapters@-ch,--chapter':[
                'Takes 1 Input And Must Be A Valid File',
                'Sends All Lines Through Internal Chapter Handler',
                'Takes A Second Input Seperated Via ":"',
                'If null Than Send Whole File',
                'If ...  Than Send All Chapters',
                'If Other Than Send Chapter',
                '!! All Entities Are Color Coded As Well !!',
                'See ReadMe.txt:Handling_Colour'
            ],
            'Info@Information':[
                'All Command Inputs Are Based Off "=""',
                'Every Command Takes A Specific Input'
            ]
        }
        for I in IO:
            # Basic Commands
            if str(I) in ['-i','--interpreter']:
                Trigger_Loop0 = True
                continue
            elif str(I) in ['-q','--quite']:
                Flags['Verbose'] = False
                continue
            elif str(I) in ['-l','--nolog']:
                Flags['Logging'] = False
                continue
            elif str(I) in ['-r','--record']:
                Flags['Record']  = True
                continue
            elif str(I) in ['-h','-?','--help']:
                for Command in Usage:
                    Message  = str('Usage> ')
                    ComTree  = Command.split('@')
                    Title    = str(ComTree[0])
                    Operas   = str(ComTree[1])
                    Message += str('Title('+str(Title)+')['+str(Operas)+'] ::')
                    self._PipeOut_(str(Message))
                    for Line in Usage[str(Command)]:
                        Line = self._PipeColor_(str('\t')+str(Line))
                        self._PipeOut_(str(Line))
            elif str('=') in str(I):
                T = I.split('=')
                if str(T[0]) in ['-opl','--output-path-log']:
                    if os.path.isdir(str(T[1])) == True:
                        Flags['Output-Path-Log'] = str(T[1])
                        continue
                    else:
                        self._PipeOut_('Recieved Invalid Directory: '+str(T[1])+' For Output Log')
                        Failed = True
                        break
                elif str(T[0]) in ['-onl','--output-name-log']:
                    Flags['Output-Name-Log']=str(T[1])
                    continue
                elif str(T[0]) in ['-oel','--output-extension-log']:
                    if str('.') in str(T[1]):
                        T[1] = str(T[1]).strip('.')
                    Flags['Output-Ext-Log'] = str(T[1])
                    continue
                elif str(T[0]) in ['-opr','--output-path-record']:
                    if os.path.isdir(str(T[1])) == True:
                        Flags['Output-Path-Record'] = str(T[1])
                        continue
                    else:
                        self._PipeOut_('Recieved Invalid Directory: '+str(T[1])+' For Record Script')
                        Failed = True
                        break
                elif str(T[0]) in ['-onr','--output-name-record']:
                    Flags['Output-Name-Record'] = str(T[1])
                    continue
                elif str(T[0]) in ['-oer','--output-extension-record']:
                    if str('.') in str(T[1]):
                        T[1] = str(T[1]).strip('.')
                    Flags['Output-Ext-Record'] = str(T[1])
                    continue
                elif str(T[0]) in ['-e','--execute']:
                    Trigger_Cmd = str(T[1])
                    continue
                elif str(T[0]) in ['-f','--file']:
                    if os.path.isfile(str(T[1])) == True:
                        F = open(str(T[1])).read()
                        Trigger_File = str(F)
                        continue
                    else:
                        self._PipeOut_('Recieved Invalid Directory: '+str(T[1])+' For File Execution')
                        Failed = True
                        break
                elif str(T[0]) in ['-ch','--chapter']:
                    if str(':') in str(T[1]):
                        F = str(T[1]).split(':')
                        if os.path.isfile(str(F[0])) == True:
                            if str(F[1]) in ['null','Null','NULL','None']:
                                F[1] = None
                            self._ChapterFileHandle_(str(F[0]),F[1])
                elif str(T[0]) in ['-h','--help']:
                    Index = {}
                    for U in Usage:
                        O = U.split('@')
                        if str(T[1]) in str(O[0]):
                            for line in Usage[U]:
                                Index[str(O[0])] = Usage[U]
                    for Operation in Index:
                        Message = str('Title('+str(Operation)+') :: ')
                        self._PipeOut_(str(Message))
                        for Line in Index[str(Operation)]:
                            Line = self._PipeColor_(str(Line))
                            self._PipeOut_(str('\t')+str(Line))
        if Failed == True:
            raise Exception('Recieved Error...')
        if Trigger_Cmd != None:
            self._ExecuteInstructionLvl1_(str(Trigger_Cmd))
        if Trigger_File != None:
            File = Trigger_File.split('\n')
            for Line in File:
                self._ExecuteInstructionLvl1_(str(Line))
        if Trigger_Loop0 == True:
            self.Loop0(Flags_IN=Flags)
    ############################################################################
    # For Handling Chapter Files
    # Takes 2 Inputs (File,Chapter)
    # If Chapter Is None Than Send Entire Index
    # If Chapter Is ...  Than Send All Chapters
    # Else Index For Chapter Item
    def _ChapterFileHandle_(self,File,Chapter):
        # Capture A Chapter <TITLE@PAGE>
        # You Can Seperate Chapters Into Indivitual Indexs Via The '@'
        # TITLE Can Remain The Same While Page Can Differ
        #  <Example@1.1>
        #  Example 1
        #  <Example@1.2>
        #  Example 2
        # Calling Exmple Would Send
        #  Example 1
        #  Example 2
        # While Calling 1.1
        #  Example 1
        # And Calling 1.2
        #  Example 2
        self._PipeLog_('_ChapterFileHandle_('+str(File)+','+str(Chapter)+')')
        if os.path.isfile(str(File)) == True:
            Text    = open(str(File)).read().split('\n')
            Pages   = {}
            Current = None
            Failed  = False
            for Line in Text:
                if len(Line) == 0:
                    continue
                elif str(Line[0]) == str('<') and str('@') in str(Line) and str('>') in str(Line):
                    Page = Line.strip("<")
                    Page = Page.strip('>')
                    if str(Page) not in Pages:
                        Pages[str(Page)] = []
                        Current = str(Page)
                else:
                    if Current == None:
                        self._PipeOut_('Recieved Input While No Chapter Is Set: '+str(Line))
                        Failed = True
                        break
                    else:
                        Pages[str(Page)].append(str(Line))
            if Chapter == None:
                for Page in Pages:
                    for Line in Pages[Page]:
                        self._PipeOut_(self._PipeColor_('Page('+str(Page)+') > '+str(Line)))
                return
            else:
                if str(Chapter) == str('...'):
                    for Page in Pages:
                        self._PipeOut_(str(Page))
                    return
                else:
                    for Page in Pages:
                        Tree = Page.split('@')
                        if str(Chapter) == str(Tree[0]) or str(Chapter) == str(Tree[1]) or str(Chapter) == str(Page):
                            Text = Pages[Page]
                            for Line in Text:
                                self._PipeOut_(str(self._PipeColor_('Page('+str(Page)+')['+str(Chapter)+'] > '+str(Line))))
                    return
        else:
            self._PipeOut_('_ChapterFileHandle_ Handler :: '+str(File)+' Is Invalid')
    ############################################################################
    # For Mounting Directory Via '~'
    # Takes PATH As Str If . Or ~ It Will Replace With "/"
    # Must Be A Valid Directory
    def _MountDiR_(self,PATH):
        if type(PATH) is str:
            if str('~') in str(PATH):
                PATH = PATH.replace('~','/')
            elif str('.') in str(PATH):
                PATH = PATH.replace('.','/')
            if os.path.isdir(str(PATH)) == True:
                File_Entities = os.listdir(str(PATH))
                File_Index    = {}
                for File in File_Entities:
                    SPath     = str(PATH)+str('/')+str(File)
                    if os.path.isfile(str(SPath)) == True:
                        File_Index[str(SPath)] = open(str(SPath)).read().split('\n')
                for Index in File_Index:
                    for Line in File_Index[str(Index)]:
                        self._ExecuteInstructionLvl1_(str(Line))
            else:
                raise ValueError('Mount Handler : Invalid File Sent Is It DIR? '+str(PATH))
        else:
            raise TypeError('Mount Handler : Expected str Got '+str(type(PATH))+' For '+str(PATH))
    ############################################################################
################################################################################
if len(sys.argv) > 0 and str(sys.argv[0]) != str(''): # Does Secondary Check Due To '' Showing On Leaving [''] As sys.argv
    Args = sys.argv[1:]
    I = Interpreter()
    T = I._FlagsConvert_(Args)
