import Al13N_330.RooTUniverse as RU # RooTUniverse Mount
import Al13N_330.Exceptions   as Exceptions # For Handling Exceptions
import Al13N_330.VirtualPath  as RD # VirtualDIR   Mount
import Al13N_330.Graphical    as RG # Graphics
import random                       # For Randomness
import time                         # For Time
import os, sys                      # For OS And SYS Based Ops
##############################################################################################################################################

class Interpreter:
    '''
    * Al13N_330.Main.Interpreter.__init__(Configure_Heads=True/False,FlowIntoLoop=True/False,FailSafe=True/False)
    / Configured Everything Inside Of Interpreter()
    / If Configure_Heads Is True And Al13N_330.Main.Interpreter._AddHeads_ Will Be Triggered
    / If FlowIntoLoop Is True Than Go Into Al13N_330.Main.Interpreter._Loop0Start_(FailSafe=FailSafe)
    '''
    def __init__(self,Configure_Heads=True,FlowIntoLoop=False,FailSafe=False):
        RG.TriggerAutoReset()
        self.IG   = RG.Messages() # Mount Display
        self.IR   = RU.RooT()     # Mount Memory
        self.Logs = {
            'verbose':[True,[]],
            'logging':[True,[]],
            'output' :[True,[]],
            'record' :[True,[]]
            }
        if Configure_Heads == True:
            self._AddHeads_()
        if FlowIntoLoop    == True:
            self._Loop0Start_(FailSafe=FailSafe)
    #########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._AddHeads_()
    / Takes No Inputs: Works inside of the Al13N_330.Graphical.Messages Functions
    '''
    def _AddHeads_(self):
        self.IG._AppendHeader_('Interpreter-3.3.0','{F.G}{S.B}>> Interpreter [ Author :: {F.B}J{F.R}4{F.B}ck{F.R}3{F.B}lS{F.M}y{F.B}N{F.G} ]{S.N}')
        self.IG._AppendHeader_('Interpreter-Out'  ,'{F.G}{S.B}>> Interpreter {F.M} >> {F.W}{S.N}')
        self.IG._AppendHeader_('Verbose-Configure','{F.W}Verbose{F.G}{S.B}\t'+str(self.Logs['verbose'][0]))
        self.IG._AppendHeader_('Logging-Configure','{F.W}Logging{F.G}{S.B}\t'+str(self.Logs['logging'][0]))
        self.IG._AppendHeader_('Output-Configure', '{F.W}Output{F.G}{S.B}\t'+str(self.Logs['output'][0]))
        self.IG._AppendHeader_('Record-Configure', '{F.W}Record{F.G}{S.B}\t'+str(self.Logs['record'][0]))
        self.IG._AppendHeader_('Closing-Message',  '{F.B}\t\tCatch You Next Time {F.G}{F.W}:}')
        self.IG._AppendHeader_('User-Entry',       '{F.G}{S.B} >->\t{S.N}{F.W}')
        self.IG._AppendHeader_('Index-Output',     '{F.M}{S.B}{Index}->{F.W}\t')
    #########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._Logging_(str,str,source=None/str)
    / Takes 2 Static Inputs And 1 Transitional
    / Handle (str)    -> Operation
    / Target (str)    -> Index To Operate On :: self.Logs
    / source (None/*) -> Input For Object
    - Handle(s) -> For Configuring A Object
    - Handle(l) -> For Logging Into Entity (If Not Switched Than Do Nothing)
    '''
    def _Logging_(self,Handle,Target,source=None):
        if str(Target) in self.Logs:
            if str(Handle) in ['s','S','switch','Switch','SWITCH']:
                if self.Logs[Target][0] == False:
                    self.Logs[Target][0] = True
                else:
                    self.Logs[Target[0]] = False
            elif str(Handle) in ['l','L','logging','Logging','LOGGING'] and source != None:
                if self.Logs[Target][0] == True:
                    self.Logs[Target][1].append(str(source))
                else:
                    raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._Logging_','K',str(Target)+str(' Is Not Configured')))
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._Logging_','K',str(Handle)+str(' Is Not A Valid Handle')))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._Logging_','K',str(Target)+str(' Target Does Not Exist')))
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._ToScreen_(str)
    / For Sending Messages To The Screen :: Al13N_330.Graphical.Messages.Display_String
    '''
    def _ToScreen_(self,Message):
        if self.Logs['verbose'][0] == True:
            self.IG.Display_String(str(Message))
            self._Logging_('l','verbose',source=str(Message))
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._FetchIO_()
    / Returns A User Input
    '''
    def _FetchIO_(self):
        return str(input(self.IG.Headers['User-Entry']))
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._Loop0Close_()
    / Sends Some Logs And Exits Via sys.exit(1)
    '''
    def _Loop0Close_(self):
        self._ToScreen_('@Interpreter-3.3.0 @Closing-Message')
        self._ToScreen_('@Interpreter-3.3.0 \t '+str(self.Logs))
        self._ToScreen_('@Interpreter-3.3.0 \t '+str(self.IR.Universe))
        self.Status = False
        sys.exit(1)
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._HandleIO_(str)
    / For Level 0 Operations (Interpreter)
    '''
    def _HandleIO_(self,Command):
        if len(Command) == 0:
            return 'NULL'
        else:
            if str(Command[0]) == str('~'):
                if str(Command[1:]) in ['$exit','$Exit','$EXIT']:
                    return 'EXIT'
                elif str('<->') in str(Command[1:]):
                    LogicSwitch = Command[1:].split('<->')
                    # Root Of Advanced Command [0]
                    # Type Of Command [1] (Usually)
                    # Type Of Input For Command (Rare))
                    RooT = str(LogicSwitch[0])
                    Stem = str(LogicSwitch[1])
                    if str(RooT) in ['$index','$Index','$INDEX']: # Needs More Work For Inner Processing For Now Use ~$index<->* For Operations
                        print(str(Stem))
                        if str(Stem) == str('*'):
                            if len(self.IR.Universe['Main']) != 0:
                                for Galaxy in self.IR.Universe['Main']:
                                    Message_0 = '@Interpreter-Out\t(BiT)\t<->\t(SyS)\t\t//\t(VaL)'
                                    Message_1 = '@Interpreter-Out '+str(Galaxy)+' --> '
                                    self._ToScreen_(str(Message_0))
                                    self._ToScreen_(str(Message_1))
                                    for BiT in self.IR.Universe['Main'][str(Galaxy)]:
                                        for SyS in self.IR.Universe['Main'][str(Galaxy)][str(BiT)]:
                                            VaL =  self.IR.Universe['Main'][str(Galaxy)][str(BiT)][str(SyS)]
                                            Message_2 = '@Interpreter-Out\t'+str(BiT)+str('{F.B}\t<->\t{F.W}')+str(SyS)+str('{F.M}\t//\t{F.G}')+str(VaL)
                                            self._ToScreen_(str(Message_2))
                        elif str(Stem) in self.IR.Universe['Main']:
                            Message_0 = '@Interpreter-Out\t(BiT)\t<->\t(SyS)\t\t//\t(VaL)'
                            Message_1 = '@Interpreter-Out '+str(Stem)
                            self._ToScreen_(str(Message_0))
                            self._ToScreen_(str(Message_1))
                            for BiT in self.IR.Universe['Main'][str(Stem)]:
                                for SyS in self.IR.Universe['Main'][str(Stem)][str(BiT)]:
                                    VaL =  self.IR.Universe['Main'][str(Stem)][str(BiT)][str(SyS)]
                                    Message_2 = '@Interpreter-Out\t'+str(BiT)+str('{F.B}\t<->\t{F.W}')+str(SyS)+str('{F.M}\t//\t{F.G}')+str(VaL)
                                    self._ToScreen_(str(Message_2))
            elif str('||') not in Command:
                raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._HandleIO_','V',str(Command)+str(' Expected A Seperator Got Nothing')))
            else:
                self._TriggerOp_(str(Command))
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._TriggerOp_(Command)
    / For Level 1 Operations (Al13N 3.3.0)
    '''
    def _TriggerOp_(self,Command):
        if str('||') in str(Command):
            Command_Tree = Command.split('||')
            Command_Indx = 0
            Command_Post = []
            Command_Fail = False
            Command_Reas = None
            for C in Command_Tree:
                if str(C) == str(''):
                    continue
                elif str('::') in str(C):
                    Command_Post.append(str(C).split('::'))
                else:
                    Command_Fail = True
                    Command_Reas = str(Command)+str(' Expected A Seperator From A Whole Got None ')+str(C)
            if Command_Fail == True:
                raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','E',str(Command_Reas)))
            else:
                for C in Command_Post:
                    Root = C[0]
                    Tree = C[1:]
                    if str(Root) in [ '+', 'new', 'New', 'NEW' ]: # Capture Al13N_330.RooTUniverse.RooT.NewGalaxy Call
                        # Command: +::name::null/bitmin,bitmax,bitpad,bittype,bitdis
                        if len(Tree) == 2:
                            Name = str(Tree[0])
                            Set  = str(Tree[1])
                            if str(Set) in [ 'null', 'Null', 'NULL' ]:
                                self.IR.NewGalaxy(str(Name))
                            else:
                                if str(',') in str(Set):
                                    Set = Set.split(',')
                                    if len(Set) == 5:
                                        BitMin = Set[0]
                                        BitMax = Set[1]
                                        BitPad = Set[2]
                                        BitTyp = Set[3]
                                        Bitdis = Set[4]
                                        if BitMin.isdigit() == True and BitMin.isdigit() == True and BitPad.isdigit() == True and str(BitTyp) in ['h','b'] and Bitdis.isdigit() == True:
                                            Current_Conf = self.IR.Universe['Conf']
                                            self.IR.Universe['Conf']['Min'] = int(BitMin)
                                            self.IR.Universe['Conf']['Max'] = int(BitMax)
                                            self.IR.Universe['Conf']['Pad'] = int(BitPad)
                                            self.IR.Universe['Conf']['TyP'] = str(BitTyp)
                                            self.IR.Universe['Conf']['DiS'] = int(Bitdis)
                                            self.IR.NewGalaxy(str(Name))
                                            self.IR.Universe['Conf'] = Current_Conf
                                        else:
                                            raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Tree[1])+str(' Expected Valid Types int,int,int,str,int')))
                                    else:
                                        raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Tree[1])+str(' Expected 5 Inputs Got ')+str(len(Set))))
                                else:
                                    raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Set)+str(' Expected null Or Seperator ","')))
                        else:
                            raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Tree)+str(' Expected 2 Entities For Generation Got ')+str(len(Tree))))
                    elif str(Root) in [ '/', 'comment',' Comment',' COMMENT']:
                        continue
                    elif str(Root) in ['>','write','Write','WRITE']:
                        Target = Tree[0]
                        if str(':-') in str(Target):
                            Target = Target.split(':-')
                            Type   = Tree[1]
                            Value  = Tree[2]
                            if str('/') in str(Value):
                                Value = Value.split('/')
                                Idx   = 0
                                for V in Value:
                                    if str(':-') in str(V) and str(V[0]) != str('%'): # Target Catch
                                        Value[Idx]=V.split(':-')
                                        Idx += 1
                                    elif len(V) == 0: # No Length Catch
                                        Idx += 1
                                    else:
                                        if str(V[0]) == str('%') and str(':-') in str(V): # Variable Catch
                                            V = V[1:].split(':-')
                                            if self.IR._ValidateBitLocation_(V) == True and self.IR._CaptureBitType_(V) != None:
                                                Value[Idx] = self.IR.Universe['Main'][str(V[0])][str(V[1])][str(V[2])][1]
                                        Idx += 1
                            elif str(Value[0]) == str('%'):
                                Value = Value[1:]
                                if str(':-') in str(Value):
                                    Value = Value.split(':-')
                                    if self.IR._ValidateBitLocation_(Value) == True and self.IR._CaptureBitType_(Value) != None:
                                        Value = self.IR.Universe['Main'][str(Value[0])][str(Value[1])][str(Value[2])][1]
                                    else:
                                        raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Value)+str(' Got A Variable Catch But Non Existant Or Configured')))
                                else:
                                    raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','V',str(Value)+str(' Got A Variable Catch But No Seperator')))
                            try:
                                if type(Value) is list:
                                    self.IR.Write(Target,Type,Value)
                                else:
                                    self.IR.Write(Target,Type,[Value])
                            except Exception as e:
                                raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','E',str(e)+str(' From Operation '+str(C))))
                    elif str(Root) in ['!','execute','Execute','EXECUTE']:
                        Target = Tree[0]
                        Output = Tree[1]
                        if str(':-') in str(Target) and str(':-') in str(Output):
                            TTree = Target.split(':-')
                            OTree = Output.split(':-')
                            print(TTree)
                            print(OTree)
                            try:
                                Signal = self.IR.Execute(TTree,OTree)
                                self._ToScreen_('@Interpreter-3.3.0 '+str(Signal))
                            except Exception as e:
                                raise Exception(Exceptions.RaiseToUser('Al13N_330.Main.Interpreter._TriggerOp_','E',str(e)+str(' From Operation ')+str(C)))
    ########################################################################################################################################
    '''
    * Al13N_330.Main.Interpreter._Loop0Start_(FaleSafe=True/False)
    / For Opening A Loop If FailSafe Is True And All Exceptions Will Be Displayed And Ignored
    / Used $EXIT To Exit
    '''
    def _Loop0Start_(self,FailSafe=False):
        self.Status = True
        try:
            while self.Status == True:
                UserInput  = self._FetchIO_()
                UserOutput = self._HandleIO_(str(UserInput))
                if UserOutput == 'EXIT':
                    self._Loop0Close_()
                elif UserOutput == 'NULL':
                    continue
        except KeyboardInterrupt as K:
            if FailSafe != True:
                self._Loop0Close_()
        except Exception as E:
            self._ToScreen_(str('@Interpreter-3.3.0 ')+str(E))
            if FailSafe != True:
                self._Loop0Close_()
        if FailSafe == True:
            self._Loop0Start_(FailSafe=True)
    ########################################################################################################################################
###########################################################################################################################################
