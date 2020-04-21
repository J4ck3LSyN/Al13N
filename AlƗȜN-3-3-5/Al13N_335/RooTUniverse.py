import Al13N_335.Exceptions as Exceptions
import Al13N_335.Graphical  as Graphics
import subprocess, os
'''
> RooT()
# Usage: import Al13N_335.RooTUniverse
#        Root = Al13N_335.RooTUniverse.RooT()
>> __init__(self)
->  self.Universe['Main'/'SymL'/'Conf{'Min'/'Max'/'Pad'/'Hex'/'Bin'/'TyP','DiS'}']
->  self.BiTMaP
->  self.Display (Al13N_335.Graphical.Messages)
->>  Added Heads Via (Al13N_335.Graphical.Messages._AppendHeader_)
>> NewGalaxy(self,str)
#  For Generating A Galaxy Inside Of self.Universe (dict)
-> Takes str And Checks For Existance If Non Existant Than Continue
-> Takes Items From self.Universe['Conf'] For Generation, Mix,Max Being The Dimension Range
-> Hex,Bin Being The Characters To Pad Those Types With, TyP,DiS Being The Conversion Type And Displaced
-> Index(str) = {hex/bin(int in range(Min,Max)):(bit in self.BiTMaP)} = 'Main'{ID{BiT{Sys[Value]}}}
>> Write(self,list,str,list)
#  For Writing To BiT Locations
-> Takes list As Location To Target Must Be Validated Via self._ValidateBitLocation_
-> Takes str For Type Of Bit
-> Takes list For Inputs On Type
'''
class RooT:
    def __init__(self):
        self.Universe = {
            'Main' : {}, # Main Memory
            'Syml' : {}, # Symbolic Links
            'Conf' : {
                'Min' : 0,   # Dimension Lower
                'Max' : 1,   # Dimenion  Upper
                'Pad' : 0,   # Padding
                'Hex' : 'f', # Hex Pad
                'Bin' : '0', # Bin Pad
                'TyP' : 'h', # Current Type (If Not h/b Than Revert To h)
                'DiS' : 1    # Current Multiplier For Incriment
            }  # Configurations
        }
        self.BiTMaP   = [    # BiTMaP Addresses
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
        Graphics.TriggerAutoReset()
        self.Display   = Graphics.Messages()
        self.Display._AppendHeader_('Display-ID','{F.G}  (ID)\t(BiT)\t<->\t(System)')
        self.Display._AppendHeader_('Galaxy-ID', '{F.G}{S.B}->{F.W}')
        self.Display._AppendHeader_('BiT-ID',    '{F.Y}{S.B}\t')
        self.Display._AppendHeader_('SyS-ID',    '{F.B}{S.N}\t<->\t')
        self.Display._AppendHeader_('VaL-ID',    '{F.Y}\t')
    #########################################################################################################################################
    '''
    Al13N_335.RooTUniverse.NewGalaxy(str) -> Generates A Galaxy Inside Of self.Universe['Main']
    Takes configuration based off of internal operations configured at // str IO Being The source ID:
     self.Universe['conf']['Min'/'Max'/'Pad'/'Bin'/'Hex'/'TyP'/'DiS']
    Min will be the minimal for the dimension range
    Max will be the maximum for the dimension range
    Pad will be the amount of padding to add to the dimensions
    Hex/Bin are the configurations for the padding dependong on the TyP
    TyP will be the configuration of the conversion Bin being Binary Hex being Hexidecimal // Other will default to Hex
    DiS will be the displacment (DIMENSION*DiS)+str(Pad*Hex/Bin) == DIMENSION ID
    '''
    def NewGalaxy(self,Source):
        # Capture Configuration
        Min = self.Universe['Conf']['Min']
        Max = self.Universe['Conf']['Max']
        Pad = self.Universe['Conf']['Pad']
        Hex = self.Universe['Conf']['Hex']
        Bin = self.Universe['Conf']['Bin']
        TyP = self.Universe['Conf']['TyP']
        DiS = self.Universe['Conf']['DiS']
        # Validate Types And Existance
        if type(Source) is str and type(Max) is int and type(Pad) is int and type(Hex) is str and type(Bin) is str and type(TyP) is str:
            if str(Source) not in self.Universe['Main']:
                # Validate Configuration
                if int(DiS) == int(0):
                    DiS = 1
                if int(Min) < int(Max):
                    # Generate A Temp Index For Appending
                    SystemForAppend = {}
                    # Capture Dimensions From Range
                    for Dimension in range(int(Min),int(Max)):
                        # Convert
                        if str(TyP) == str('b'):
                            Dimension = str(bin(Dimension*DiS))+str(Bin)*Pad
                        else:
                            Dimension = str(hex(Dimension*DiS))+str(Hex)*Pad
                        # Append And Generate Sub Index
                        SystemForAppend[str(Dimension)]={}
                        # Capture A BiT From self.BiTMaP And Configure
                        for BiT in self.BiTMaP:
                            SystemForAppend[str(Dimension)][str(BiT)] = []
                    # Append
                    self.Universe['Main'][str(Source)]=SystemForAppend
                else:
                    raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.NewGalaxy','V','Got '+str(Min)+str('/')+str(Max)+'Expected Min<Max'))
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.NewGalaxy','K','Got '+str(Source)+' Already Exists'))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.NewGalaxy','T','Invalid Arugments Sent'))
    #########################################################################################################################################
    '''
    * Al13N_335.RooTUniverse().Write(list,str,list)
    / Takes 3 Static Inputs [0] - Location [1] - Type [2] - Inputs
    / If len Location is 1 Than Check Symbolic Link Else len Must Be 3 [0] - Galaxy [1] - BiT [2] - System
    / Types
    :  vS -> String        // IO Must Contian 1 entity
    :  vB -> String        // IO Must Contain 1 entity
    :  vL -> List          // IO Must Contain 1 entity
    :  vI -> Integer       // IO Must Contain 1 entity
    :  vE -> Excluded      // IO Can Be Anything
    :  l2 -> 2Lane Logic   // IO Must Contain 2 entity (list,list) Both Being Locations
    :  lS -> Set Logic     // IO Must Contain 4 entity (list,list,value,value) [0][1] Being Locations [2][3] Being Variables
    :  lE -> Execute Logic // IO Must Contain 5 entity (list,list,list,list,list) [0][1][2][3][4] Being Locations
    :  eS -> Execute Set   // IO Must Contain 2 entity (list,list) [0] Being A List Of Locations To Execute [1] Being The Output For Everything
    :  sS -> Execute Shell // IO Must Contain A List For Command Input ['ps','aux'] Same As 'ps aux'
    :  sE -> Execute Shell // IO Must Contain A List For Command Input ['clear','ifconfig'] Same As 'clear\nifconfig'
    '''
    def Write(self,Target,Type,IO):
        # Validate Type
        if type(Target) is list and type(Type) is str and type(IO) is list:
            if len(Target) == 1:
                if str(Target[0]) not in self.Universe['SymL']:
                    raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','K',str(Target[0])+str(' Got 1 Entity And No Symbolic Link To Represent')))
                else:
                    Target = self.Universe['SymL'][str(Target[0])]
            if self._ValidateBitLocation_(Target) == True:
                if str(Type) in ['vE','VE','varextend','VarExtend','VAREXTEND']: # Variable Catch Takes Anything Inside Of IO And Appends As Variables, Takes Anything
                    self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])]=[
                            'VAR_EXT',
                            IO
                    ]
                    return
                elif str(Type) in ['vS','VS','varstring','VarString','VARSTRING']: # Variable Catch Takes 1 Entity As Strins In IO
                    if len(IO) == 1:
                        if type(IO[0]) is str:
                            self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])]=[
                                'VAR_STR',
                                str(IO[0])
                            ]
                            return
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(Type)+str(' Expected 1 Enntity As str In ')+str(IO)))
                    else:
                        raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO)+str(' Expected 1 Entity Inside Of IO')))
                elif str(Type) in ['vB','VB','varboolean','VarBoolean','VARBOOLEAN']: # Variable Catch Takes 1 Entity As Boolean
                    if len(IO) == 1:
                        if IO[0] in ['true','True','1',1]:
                            IO = True
                        elif IO[0] in ['false','False','0',0]:
                            IO = False
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO[0])+str(' Expected 1 Entity As boolean Type')))
                        self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                            'VAR_BOL',
                            IO
                            ]
                        return
                elif str(Type) in ['vI','VI','varinteger','VarInteger','VARINTEGER']: # Variable Catch Takes 1 Entity As int
                    if type(IO[0]) is not int:
                        if IO[0].isdigit() == False:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO[0])+str(' Expected int')))
                        else:
                            IO[0] = int(IO[0])
                    self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                        'VAR_INT',
                        IO[0]
                    ]
                    return
                elif str(Type) in ['vL','VL','varlist','VarList','VARLIST']: # Variable Catch Takes 1 Entity As list
                    if type(IO[0]) is list:
                        self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                            'VAR_LST',
                            IO[0]
                        ]
                    return
                elif str(Type) in ['l2','L2','logic2way','Logic2Way','LOGIC2WAY']: # Logic Operation For Returning Boolean Values As VAR_BOL
                    if len(IO) == 2:
                        if self._ValidateBitLocation_(IO[0]) == True and self._ValidateBitLocation_(IO[1]) == True:
                            self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                                'LGK_2WY',
                                IO
                            ]
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO)+str(' Expected 2 Locations The Are Invalid')))
                    else:
                        raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO)+str(' Expected 2 Entities In IO Got '+str(len(IO)))))
                elif str(Type) in ['lS','LS','logicset','LogicSet','LOGICSET']: # Logic Operation For Returning A Value Configured In IO[2]
                    if len(IO) == 4:
                        if self._ValidateBitLocation_(IO[0]) == True and self._ValidateBitLocation_(IO[1]) == True:
                            self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                                'LGK_SET',
                                IO
                            ]
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(IO)+str(' Expected 4 Entities In IO Got '+str(len(IO)))))
                elif str(Type) in ['lE','LE','logicexecute','LogicExecute','LOGICEXECUTE']: # Logic Operation For Executing
                    if len(IO) == 5:
                        if self._ValidateBitLocation_(IO[0]) == True and self._ValidateBitLocation_(IO[1]) == True:
                            if self._ValidateBitLocation_(IO[2]) == True and self._ValidateBitLocation_(IO[3]) == True:
                                if self._ValidateBitLocation_(IO[4]) == True:
                                    self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                                        'LGK_EXE',
                                        IO
                                        ]
                                else:
                                    raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','K',str(IO[4])+str(' Expected A Valid Location [4]')))
                            else:
                                raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','K',str(IO[3]+str('/')+str(IO[2])+str(' Expected A Valid Location [2][3]'))))
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','K',str(IO[0])+str('/')+str(IO[1])+str(' Expected A Valid Location [0][1]')))
                    else:
                        raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(len(IO))+str(' Expected 5 Entities in IO ')))
                elif str(Type) in ['sS','SS','systemshell','SystemShell','SYSTEMSHELL']: # System Shell Trigger
                    if len(IO) > 0:
                        Out = []
                        for Item in IO:
                            if len(str(Item)) == 0:
                                continue
                            Out.append(str(Item))
                        self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                            'SYS_SHL',
                            Out
                        ]
                    else:
                        raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(len(IO))+str(' Expected More Than 0 Entities')))
                elif str(Type) in ['sE','SE','systemexecute','SystemExecute','SYSTEMEXECUTE']:
                    if len(IO) > 0:
                        Out = ''
                        for Item in IO:
                            if len(str(Item)) == 0:
                                continue
                            Out += str(Item)+'\n'
                        self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])] = [
                            'SYS_EXE',
                            Out
                        ]
                    else:
                        raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Write','V',str(len(IO))+str(' Expected More Thab 0 Entities')))
    #########################################################################################################################################
    '''
    * Al13N_335.RooTUniverse().Execute(list,list,IO=None/IO)
    / Takes 2 Static Input And 1 Transitional Input
    / Target (list) -> Is A Location To Execute If len Is 1 Than Check For Symbolic Links Else len Must Be 3 [0] - Galaxy [1] - BiT [2] - Page
    / Output (list) -> Is For The Output After Execution However A Value Will Be Sent Retured As list [0] - Type [1] - Output
    / IO   (None/*) -> Is For Any Inputs On Execution
    '''
    def Execute(self,Target,Output,IO=None):
        # Validate Types
        if type(Target) is list and type(Output) is list:
            # Capture Any Symbolic Links For Target And Output
            if len(Target) == 1:
                if str(Target) not in self.Universe['SymL']:
                    raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Execute',str(Target[0])+str(' Got 1 Entity And No Symbolic Link To Represent')))
                else:
                    Target = self.Universe['SymL'][str(Target[0])]
            if len(Output) == 1:
                if str(Output) not in self.Universe['SymL']:
                    raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Execute',str(Output[0])+str(' Got 1 Entity And No Symbolic Link To Represent')))
                else:
                    Output = self.Universe['SymL'][str(Output[0])]
            # Validate They Are Both Valid locations
            if self._ValidateBitLocation_(Target) == True and self._ValidateBitLocation_(Output) == True:
                # Capture Values Or Both Locations
                Target_IO = self.Universe['Main'][str(Target[0])][str(Target[1])][str(Target[2])]
                Output_IO = self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])]
                if len(Target_IO) == 0:
                    raise KeyError(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Execute','V',str(Target)+str(' Cannot Execute A Non Configured Location')))
                else:
                    # Capture Variable Types And Send Configuration
                    if str(Target_IO[0]) in [ # Variables
                            'VAR_EXT',
                            'VAR_STR',
                            'VAR_INT',
                            'VAR_LST',
                            'VAR_BOL'
                                            ]:
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])]=Target_IO
                        return Target_IO
                    elif str(Target_IO[0]) in [ 'LGK_2WY' ]: # Logic Configuration // Boolean
                        Operands = Target_IO[1]
                        Locate_1 = Operands[0] # Location To Pull
                        Locate_2 = Operands[1] # Location To Verify
                        if self.Universe['Main'][str(Locate_1[0])][str(Locate_1[1])][str(Locate_1[2])] == self.Universe['Main'][str(Locate_2[0])][str(Locate_2[1])][str(Locate_2[2])]:
                            Out  = ['VAR_BOL',True]
                        else:
                            Out  = ['VAR_BOL',False]
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])]=Out
                        return Out
                    elif str(Target_IO[0]) in [ 'LGK_SET' ]: # Logic Configuration // Variable
                        Operands = Target_IO[1]
                        Locate_1 = Operands[0] # Location To Pull
                        Locate_2 = Operands[1] # Location To Verify
                        True_Op  = Operands[2] # Output If True
                        Fals_Op  = Operands[3] # Output If False
                        if self.Universe['Main'][str(Locate_1[0])][str(Locate_1[1])][str(Locate_1[2])] == self.Universe['Main'][str(Locate_2[0])][str(Locate_2[1])][str(Locate_2[2])]:
                            Out  = ['VAR_EXT',True_Op]
                        else:
                            Out  = ['VAR_EXT',Fals_Op]
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])]=Out
                        return Out
                    elif str(Target_IO[0]) in [ 'LGK_EXE' ]: # Logic Configuration // Execute
                        Operands = Target_IO[1]
                        Locate_1 = Operands[0] # Location To Pull
                        Locate_2 = Operands[1] # Location To Verify
                        Locate_3 = Operands[2] # Location If True
                        Locate_4 = Operands[3] # Location If False
                        Locate_5 = Operands[4] # Target Output
                        if self.Universe['Main'][str(Locate_1[0])][str(Locate_1[1])][str(Locate_1[2])] == self.Universe['Main'][str(Locate_2[0])][str(Locate_2[1])][str(Locate_2[2])]:
                            Out  = self.Execute(Locate_3,Locate_5)
                        else:
                            Out  = self.Execute(Locate_4,Locate_5)
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])] = Out
                        return Out
                    elif str(Target_IO[0]) in [ 'SYS_SHL' ]: # For Executing Shell Commands (subprocess)
                        Operands   = Target_IO[1]
                        Output_T   = []
                        Output_O   = []
                        for Command in Operands:
                            if str(' ') in str(Command):
                                Command = Command.split(' ')
                            else:
                                Command = [str(Command)]
                            Output_T.append(subprocess.Popen(Command,stdout=subprocess.PIPE,shell=True))
                        for Outputs_E in Output_T:
                            Output_O.append(Outputs_E.stdout.read())
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])] = [ 'VAR_EXT', Output_O]
                        return [ 'VAR_EXT', Output_O]
                    elif str(Target_IO[0]) in [ 'SYS_EXE' ]: # For Execute Shell Commands (os.system)
                        Command = str(Target_IO[1])
                        os.system(str(Command))
                        self.Universe['Main'][str(Output[0])][str(Output[1])][str(Output[2])] = [ 'VAR_EXT', 'NULL']
                        return [ 'VAR_EXT', 'NULL']
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT.Execute','V',str(Target)+str('/')+str(Output)+str(' Expected Valid Locations')))
    #########################################################################################################################################
    def _ValidateBitLocation_(self,Location):
        # Validatation Tree
        if type(Location) is list:
            if len(Location) == 3:
                if str(Location[0]) in self.Universe['Main']:
                    if str(Location[1]) in self.Universe['Main'][str(Location[0])]:
                        if str(Location[2]) in self.Universe['Main'][str(Location[0])][str(Location[1])]:
                            # If All Is Ok Than Return True If Different Send False
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.RooT._ValidateBitLocation_','V',str(Location)+' Expected 3 Entities'))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooT._ValidateBitLocation_','T',str(Location)+' Expected list With 3 Entities'))
    #########################################################################################################################################
    def _CaptureBitType_(self,Location):
        if self._ValidateBitLocation_(Location) == True:
            Value = self.Universe['Main'][str(Location[0])][str(Location[1])][str(Location[2])]
            if len(Value) != 0:
                return str(Value[0])
            else:
                return None
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.RooTUniverse.RooT._CaptureBitType_','K',str(Location)+str(' Expected A Valid Location')))
    #########################################################################################################################################
