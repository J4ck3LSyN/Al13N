import os
import time
import sys
import hashlib
import random
################################################################################
Author  = ('J4ck3LSyN')
Version = (3,4,5)
################################################################################
def Al13NException(Root,Mesg):
    Message = 'Al13N(3.4.5)!J4ck3LSyN! '+str(time.asctime())+' @ '+str(os.getcwd())+' Function: '+str(Root)+' Gave Exception: '+str(Mesg)
    raise Exception(Mesg)
################################################################################
class Utils:
    class String:
        def append(Value,Append): return str(Value)+str(Append)
        def remove(Value,Target):
            if str(Target) in str(Value): return Value.strip(str(Target))
            else: return Value
        def replace(Value,Target,Replacement):
            if str(Target) in str(Value): return Value.replace(str(Target),str(Replacement))
            else: raise Al13NException('Utils.String.replace(...)','Target '+str(Target)+' Does Not Occur In '+str(Value))
    class Integer:
        def add(Value,Target):
            if Logic.Type('m',[Value,Target],'i') == True: return int(Value+Target)
            else: raise Al13NException('Utils.Integer.add(...)','Expected int Got '+str(type(Value)))
        def sub(Valu,Target):
            if Logic.Type('m',[Value,Target],'i') == True: return int(Value-Target)
            else: raise Al13NException('Utils.Integer.sub(...)','Expected int Got '+str(type(Value)))

    def Brain_Mount(Operation):
        if str('FetchValues.Output') in Operation:
            if len(Operaion['FetchValues.Output']) >= 3:
                Mode   = str(Operation[0])
                Target = Operation[1]
                Value  = Operation[2:]
                if str(Mode) in ['s','str','string'] and str(Target) in ['+','append']: return str(Utils.String.append(Target,Value))
################################################################################
class Logic:
    def Type(Mode,Args,Types):
        if Mode in ['00',0,'s']:
            if Types in ['l','L','00',0] and type(Args) is list: return True
            elif Types in ['s','S','01',1] and type(Args) is str : return True
            elif Types in ['i','I','02',2] and type(Args) is int : return True
            elif Types in ['d','D','03',3] and type(Args) is dict: return True
            elif Types in ['b','B','04',4] and type(Args) is bool: return True
            elif Types in ['a','A','05',5] and type(Args) is array: return True
            elif Types in ['t','T','06',6] and type(Args) is tuple: return True
            elif Types in ['f','F','07',7] and str(type(Args)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>"]: return True
            else: return False
        elif Mode in ['01',1,'m']:
            if type(Args) in [list,tuple]:
                Return_Value = False
                Global_False = True
                for Arg in Args:
                    Temp_Return_Value = Logic.Type('s',Arg,str(Types))
                    if Temp_Return_Value == False: Global_False = False
                    if Temp_Return_Value == True and Global_False == True: Return_Value = True
                return Return_Value
            else: return False

    def IsEqual(Mode,Value_A,Value_B):
        if Mode == 1 and Value_A == Value_B: return True
        elif Mode == 2 and Value_A != Value_B: return True
        else: return False
################################################################################
class Brain:
    def __init__(self,verbosity=False):
        self.Registry  = {}
        self.Verbosity = verbosity
        self.Logger    = [False,[]]
    # Logger Check
    def _logg_(self,Mesg):
        if self.Logger[0] == True: self.Logger[1].append([str(time.asctime().replace(' ','~')),str(Mesg)])
        self._verb_(str(Mesg))
    # Verbose Check
    def _verb_(self,Mesg):
        if self.Verbosity == True: print('> Al13N 3.4.5 (Brain-Internal-Verbose) > '+str(Mesg))
    # For Generating Registry Objects
    def append(self,GenerationRoot,GenerationOffset,GenerationCount,GenerationCountOffset,GenerationCountXoR):
        self._logg_('append() {} {} {} {} {}'.format(GenerationRoot,GenerationOffset,GenerationCount,GenerationOffset,GenerationCountXoR))
        if Logic.Type('m',[GenerationRoot,GenerationOffset,GenerationCount,GenerationCountOffset,GenerationCountXoR],'i') == True:
            RegisterID = int(GenerationRoot) ** int(GenerationOffset) ^ ( int(GenerationCountOffset) ** int(GenerationCountXoR) )
            print(str(hex(RegisterID)).strip('0x'))
            self.Registry[str(hex(RegisterID)).strip('0x')] = {}
            for Segment in range(0x0,int(GenerationCount)):
                Segment = str(hex(Segment)).strip('0x')
                if len(Segment) == 0: Segment = '00'
                if len(Segment) == 1: Segment = '0'+str(Segment)
                self.Registry[str(hex(RegisterID)).strip('0x')][str(Segment)]=('0000000000000000.0000')
            self._logg_('append() Finished Generated ID: '+str(hex(RegisterID)).strip('0x')+' With '+str(len(self.Registry[hex(RegisterID).strip('0x')]))+' Objects')
            return [str(hex(RegisterID)).strip('0x'),len(self.Registry[str(hex(RegisterID)).strip('0x')])]
        else: raise self.BrainException('append(^)','Expected Int')
    # Converts Things Into Strings
    def _conv_(self,Mode,StringsToConvert,CharacterRange):
        self._logg_('_conv_() {} {} {}'.format(Mode,StringsToConvert,CharacterRange))
        if Logic.Type('s',StringsToConvert,'s') == True and Logic.Type('s',CharacterRange,'i') and Mode in [1,2]:
            # Generate Character Index
            Characters = {}
            for C in range(0,int(CharacterRange)):
                V = chr(C)
                H = str(hex(C)).strip('0x')
                if len(H) == 0: H ='00'
                if len(H) == 1: H = '0'+str(H)
                Characters[str(V)]=str(H)
            # Check Mode And Convert
            # Convert Into
            if Mode == 1:
                Output = ''
                for Char in str(StringsToConvert):
                    if str(Char) in Characters:
                        if len(Output) == 0: Output = Characters[Char]
                        else: Output += ':'+str(Characters[Char])
                self._logg_('_conv_() Output: '+str(Output))
                return str(Output)
            # Convert From
            elif Mode == 2:
                if str(':') in str(StringsToConvert): OpTree = StringsToConvert.split(':')
                else: OpTree = [StringsToConvert]
                Output = ''
                for Char in OpTree:
                    for Var in Characters:
                        if str(Char) == Characters[Var]:
                            if str(Var) == str(''): Var = ''
                            if len(Output) == 0: Output = str(Var)
                            else: Output += str(Var)
                self._logg_('_conv_() Output: '+str(Output))
                return str(Output)
        else: raise self.BrainException('_conv_(...)','Invalid Types Sent')
    # Writes Information To The Registry
    def write(self,RID,SID,SIG,VAL):
        self._logg_('write() {} {} {} {}'.format(RID,SID,SIG,VAL))
        if str(RID) in self.Registry:
            if str(SID) in self.Registry[RID]:
                # NOP
                if str(SIG) == '0000000000000000.0000': self.Registry[RID][SID]=(str(SIG))
                # EXE NO-VAL
                if str(SIG) == '0000000000000001.0000' and str(VAL) in self.Registry[RID]: self.Registry[RID][SID]=(str(SIG),str(VAL))
                # EXE LGK ISEQUAL
                if str(SIG) == '0000000000000001.0001' and Logic.Type('s',VAL,'l') == True:
                    if len(VAL) == 3:
                        if str(VAL[0]) in self.Registry[RID] and str(VAL[1]) in self.Registry[RID] and str(VAL[2]) in self.Registry[RID]: self.Registry[RID][SID]=(str(SIG),(VAL[0],VAL[1],VAL[2]))
                        else: raise self.BrainException('write(VAL)','Expected Segment Values Got Invalid...')
                    else: raise self.BrainException('write(VAL)','Expected A Lit Got '+str(type(VAL)))
                # VAR STRING
                if str(SIG) == '0000000000000002.0000': self.Registry[RID][SID] = (str(SIG),self._conv_(1,str(VAL),0xff))
                # VAR INTEGER
                if str(SIG) == '0000000000000002.0001': self.Registry[RID][SID] = (str(SIG),int('0x'+self._conv_(1,str(VAL),0xff).replace(':',''),16))
                # VAR LIST
                if str(SIG) == '0000000000000002.0002' and Logic.Type('s',VAL,'l') == True: self.Registry[RID][SID] = (str(SIG),self._conv_(1,str(VAL),0xff))
                # LGK BOOL
                if str(SIG) == '0000000000000003.0000' and Logic.Type('s',VAL,'l') == True:
                    if len(VAL) == 2:
                        if VAL[0] in self.Registry[RID] and VAL[1] in self.Registry[RID]: self.Registry[RID][SID] = ('0000000000000003.0000',VAL)
                        else: raise self.BrainException('write(VAL)','Expected All Values To Be Segments')
                    else: raise self.BrainException('write(VAL)','Expected VAL To Contain 3 Values')
                # PY3 Types (Non-Interpreter)
                if str(SIG) == '0000000000000004.0000' and Logic.Type('s',VAL,'l') == True:
                    if len(VAL) == 2:
                        if Logic.Type('s',VAL[0],'f') == True and Logic.Type('s',VAL[1],'d') == True:
                            # [0] Being Your Target Function And [1] Being Handles For That Function
                            self.Registry[RID][SID] = ('0000000000000004.0000',VAL)
                        else: raise self.BrainException('write(VAL)','Expected A Function Than Dictionary')
                    else: raise self.BrainException('write(VAL)','Expected 2 Entries')
    # Executes A Segment Or Complete Register
    def execute(self,RID,**OperationInputs):
        self._logg_('execute() {} {}'.format(RID,str(OperationInputs)))
        if str(RID) in self.Registry and len(OperationInputs) == 0:
            for Segment in self.Registry[RID]:
                Output = self.execute(RID,Target_Segment=Segment,From_Operation=RID)
        elif str(RID) in self.Registry and len(OperationInputs) != 0:
            Target_Segment = None
            From_Operation = None
            Jump_After     = None
            Fail_Safe      = False
            if str('Target_Segment') in OperationInputs and str(OperationInputs['Target_Segment']) in self.Registry[RID]: Target_Segment = str(OperationInputs['Target_Segment'])
            if str('From_Operation') in OperationInputs: From_Operation = str(OperationInputs['From_Operation'])
            if str('Jump_After')     in OperationInputs and str(OperationInputs['Jump_After']) in self.Registry[RID]: Jump_After = str(OperationInputs['Jump_After'])
            if str('Fail_Safe')      in OperationInputs and OperationInputs['Fail_Safe'] == True: Fail_Safe = True
            if Target_Segment != None:
                try:
                    RegistryValue = self.Registry[RID][Target_Segment]
                    # NOP Value
                    if RegistryValue[0] == '0000000000000000.0000': return None
                    # Execute No Input Value
                    if RegistryValue[0] == '0000000000000001.0000': return self.execute(RID,Target_Segment=RegistryValue[1])
                    # Execute Based Off Value Of Segments
                    if RegistryValue[0] == '0000000000000001.0001':
                        Value_a = self.Registry[RID][RegistryValue[1][0]]
                        Value_b = self.Registry[RID][RegistryValue[1][1]]
                        if Value_a == Value_b: return self.execute(str(RID),Target_Segment=RegistryValue[1][2])
                        else: return False
                    # String Variable
                    if RegistryValue[0] == '0000000000000002.0000': return self._conv_(2,str(RegistryValue[1]),0xff)
                    # Integer Variable
                    if RegistryValue[0] == '0000000000000002.0001': return str(hex(RegistryValue[1]))
                    # List Variable
                    if RegistryValue[0] == '0000000000000002.0002':
                        List = self._conv_(2,str(RegistryValue[1]),0xff)
                        if str('[') in str(List): List = List.strip('[')
                        if str(']') in str(List): List = List.strip(']')
                        if str(',') in str(List):
                            List = List.split(',')
                        else: List = [List]
                        return List
                    # Logic Execution Boolean IsEqual
                    if RegistryValue[0] == '0000000000000003.0000':
                        if self.Registry[RID][RegistryValue[1][0]] == self.Registry[RID][RegistryValue[1][1]]: return True
                        else: return False
                    # Python3 Internal Function Mounts Handle
                    if RegistryValue[0] == '0000000000000004.0000':
                        PythonFunction  = RegistryValue[1][0]
                        PythonHandle    = RegistryValue[1][1]
                        if str('FetchValues') in PythonHandle:
                            PythonHandle['FetchValues.Output'] = []
                            for Segment in PythonHandle['FetchValues']:
                                SegmentValue = self.execute(str(RID),Target_Segment=Segment)
                                PythonHandle['FetchValues.Output'].append(SegmentValue)
                        try:
                            Output = PythonFunction(PythonHandle)
                        except Exception as e:
                            sys.exit(1)
                            raise self.BrainException('execute(...)',str(e))
                    ### Catch Jump_After ###
                    if Jump_After != None:
                        return self.execute(RID,Target_Segment=Jump_After)

                except Exception as e:
                    self._logg_('execute(^^^) Caught Exception: '+str(e))
                    if Fail_Safe == False: raise self.BrainException('execute(^)','Exception Caught: '+str(e))
    def BrainException(self,Root,Message):
        Message = str('Brain.'+Root)+str(' -> ')+str(Message)
        raise Exception(Message)


################################################################################
