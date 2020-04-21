try:
    import os,sys,time,socket,subprocess,random,hashlib
    import colorama
    from   colorama import Fore  as C_F
    from   colorama import Back  as C_B
    from   colorama import Style as C_S
    colorama.init(autoreset=True)
except ImportError as IE: raise Exception('Al13N (3.4.75) Expected A Import For '+str(IE)+' Use "pip3" To Install...')
except Exception   as EX: raise Exception('AL13N (3.4.75) Exception Raised From '+str(EX))
except NameError   as NM: raise Exception('Al13N (3.4.75) NameError Raised From '+str(NM))
################################################################################
class Al13N3475:
    '''
    >> (Al13N3475) (3.4.75) (Author: J4ck3LSyN)
       Class Al13N3475((0,0,0,0,0),(0,0,0,0,0))
       # Usage: Brain = Al13N3475.Al13N3475((int,int,int,int,int),(int,int,int,int,int))
       # Takes 2 Tuples With 5 Ints For Key Generation
       Al13N3475.__init__(SecureKeyArgs(tuple:len(5)),CharacterOffsetArgs(tuple:len(5)),_MountBuiltInOpCodes=bool)
           # Makes Variables
           self.Registry(dict)
           self.opKeys(dict)
           self.KEY(str)
           self.COF(str)
       Al13N3475.GenerateKey(LowOpen,HighOpen,Seed,LowPost,HighPost)
           # Generates A Key
           # Each Variables Must Be int
       Al13N3475.MountOperationKey(KeyID,Function,Input_Length)
           # Takes A Key And Function For Segment Operation And Configuration
       Al13N3475._MountBuiltIn()
           # Mounts Internal Functions
       Al13N3475.new(Keys,SegmentCount)
           # Generates A Register Inside Of self.Registry
           # Keys Must Be A tuple With 5 Items All int Types (self.GenerateKey)
           # Generates Segments With 4 Characters And Above
       Al13N3475.write(RegisterID,SegmentID,OpKey,Value)
           # RegisterID Must Exist Inside Of self.Registry And SegmentID Must Be Inside Of RegisterID
           # OpKey Must Exist Inside Of self.OpKeys And Value Must Be A tuple With Matching Items For self.MountOperationKey()
       Al13N3475.Display()
           # For Display Handling Is Nested Class And Mounted To A Function
           Display = Al13N3475.Display()
           Display.__init__()
               # Generates self.Color_Index For colorama Handling
               # Generates self.Message_Index For Message Handling
               # Generates self.HotKey For Keyword Stripping
       Al13N3475.Neuro.Logic.Operate(Mode,Operator,Input,Value)
       Al13N3475.Neuro.Type.Operate(Mode,Input,Value)
       Al13N3475.Neuro.Variables.String.Operate(Mode,Operand,Input,Value)
       Al13N3475.Neuro.Variables.Integer.Operate(Mode,Operand,Input,Value)
       Al13N3475.Neuro.OpMount(ARGS)
       Al13N3475.Al13N3475Exception(root,Mesg)
           # Exception Raiser
################################################################################
Once You Mount Al13N3475 With 2 Keys You Can Operate Inside Of The Method With,
.new,.write,.execute...
To Generate New Registers Use .new
To Write To A Register Segment Use .write With A OpKey Set Via ._MountBuiltIn
To Execute A OpCode Use .execute
    '''
    def __init__(self,SecureKeyArgs,CharacterOffsetArgs,_MountBuiltInOpCodes=True):
        self.Registry                                   = {}
        self.OpKeys                                     = {}
        if len(SecureKeyArgs) != 5 or len(CharacterOffsetArgs) != 5 or len(CharacterOffsetArgs) != 5: raise self.Al13N3475Exception('__init__(...)',str(SecureKeyArgs)+' '+str(CharacterOffsetArgs)+' Expected 5 int Values')
        self.KEY                                        = self.GenerateKey(SecureKeyArgs[0],SecureKeyArgs[1],SecureKeyArgs[2],SecureKeyArgs[3],SecureKeyArgs[4])
        self.COF                                        = self.GenerateKey(CharacterOffsetArgs[0],CharacterOffsetArgs[1],CharacterOffsetArgs[2],CharacterOffsetArgs[3],CharacterOffsetArgs[4])
        if _MountBuiltInOpCodes                        == True: self._MountBuiltIn()
    ############################################################################
    # For Generating Keys
    def GenerateKey(self,LowOpen,HighOpen,Seed,LowPost,HighPost):
        if Al13N3475.Neuro.Type.Operate(1,'i',(LowOpen,HighOpen,Seed,LowPost,HighPost)) == [True,True,True,True,True]:
            # Take LowOpen And HighOpen And Test For 0 Values
            if LowOpen  == 0: LowOpen  = random.randint(0xffff,0xffffff)
            if HighOpen == 0: HighOpen = random.randint(0xffffff,0xffffffffff)
            if Seed     == 0: Seed     = random.randint( int(random.randint(0xffffff,0xffffffffff)), int(random.randint(0xffffffffff,0xffffffffffffff)) )
            if LowPost  == 0: LowPost  = random.randint(0xffff,0xffffff)
            if HighPost == 0: HighPost = random.randint(0xffffff,0xffffffffff)
            Key          = int( int(LowOpen) ** int(LowPost) // int(Seed) ) * int( int(HighOpen) ** int(HighPost) ) // int(Seed)
            Gen          = str( hex( Key  )).strip('0x')+str( hex( Seed )).strip('0x')
            # Send Output
            return str(Gen)
        else: raise self.Al13N3475Exception('GenerateKey(...)','Expected ints')
    ############################################################################
    # For Mounting Op Keys To self.OpKeys
    def MountOperationKey(self,KeyID,Function,Input_Length):
        if str(KeyID) not in self.OpKeys and self.Neuro.Type.Operate(0,'f',Function) == True and self.Neuro.Type.Operate(0,'l',Input_Length) == True: self.OpKeys[str(KeyID)] = (Function,Input_Length,[])
        else: raise self.Al13N3475Exception('MountOperationKey(...)','Invalid Type Sent...')
    ############################################################################
    # For Mounting Internal Operations Into self.OpKeys Via self.MountOperationKey
    def _MountBuiltIn(self):
        # Mount Neural Handling
        # Takes 4-5 Inputs
        # If [0] Is l(logic)
        #    [1] -> Mode(Al13N(3.4.75)
        #    [2] -> Operator
        #    [3] -> Input
        #    [4] -> Value
        # If [0] Is t(type)
        #    [1] -> Mode
        #    [2] -> Input
        #    [3] -> Value
        # [NOTE: Returns bool Types]
        self.MountOperationKey('Al13N.Neuro',self.Neuro.OpMount,[4,5])
    ############################################################################
    # For Generating New Registers Takes 2 Inputs
    # Keys -> tuple With 5 Int Values (To Be Passed To self.GenerateKey)
    # SegmentCount -> int for Segment in range(0,int): ...
    def new(self,Keys,SegmentCount):
        if type(Keys) is tuple and len(Keys) == 5:
            if type(SegmentCount) is int:
                Key = self.GenerateKey(Keys[0],Keys[1],Keys[2],Keys[3],Keys[4])
                if str(Key) not in self.Registry:
                    self.Registry[str(Key)] = {}
                    for Segment in range(0,int(SegmentCount)):
                        Segment = str(hex(Segment)).strip('0x')
                        if len(Segment) == 0: Segment = str('0000')
                        if len(Segment) == 1: Segment = str('000') +str(Segment)
                        if len(Segment) == 2: Segment = str('00')  +str(Segment)
                        if len(Segment) == 3: Segment = str('0')   +str(Segment)
                        self.Registry[str(Key)][str(Segment)] = ()
                    return Key
                else: raise self.Al13N3475Exception('new(...)',str(Key)+' Already Exists')
            else: raise self.Al13N3475Exception('new(...)','Expected Int For Segment Count Got: '+str(type(SegmentCount)))
        else: raise self.Al13N3475Exception('new(...)','Expected tuple Type With 5 Itesm Got: '+str(type(Keys))+', '+str(len(Keys)))
    ############################################################################
    # For Writing Into Generated Registers From self.new
    # Takes 4 Inputs
    # RegisterID -> str ID For Register
    # SegmentID  -> str ID For Segments
    # OpKey      -> str OpKey From self.OpKeys Set By self.MountOperationKey
    # Valu       -> tuple Inputs For OpKey
    def write(self,RegisterID,SegmentID,OpKey,Value):
        if str(RegisterID)    in self.Registry:
            if str(SegmentID) in self.Registry[str(RegisterID)]:
                if str(OpKey) in self.OpKeys and type(Value) is tuple or type(Value) is list:
                    Operation  = self.OpKeys[OpKey]
                    Value_Out  = []
                    for Item in Value:
                        if type(Item) is str and Item.isdigit() == True: Item = int(Item)
                        Value_Out.append(Item)
                    if len(Value_Out) in Operation[1]:
                        self.Registry[RegisterID][SegmentID]=(OpKey,Value_Out,[])
                    else: raise self.Al13N3475Exception('write(...)','Invalid Length Needed For Input Expected: '+str(Operation[1])+' Got: '+str(len(Value)))
                else: raise self.Al13N3475Exception('write(...)','Invalid Operation Key Sent and or Value Was Not Tuple')
            else: raise self.Al13N3475Exception('write(...)','Invalid Segment ID Sent: '+str(SegmentID))
        else: raise self.Al13N3475Exception('write(...)','Invalid Register ID Sent: '+str(RegisterID))
    ############################################################################
    def execute(self,RegisterID,SegmentID=None,RecordOut=None):
        if str(RegisterID) in self.Registry:
            if SegmentID != None:
                if str(SegmentID) in self.Registry[RegisterID]:
                    Operations = self.Registry[RegisterID][SegmentID]
                    if len(Operations) != 0:
                        Function   = self.OpKeys[Operations[0]]
                        Input      = Operations[1]
                        IInput     = []
                        for PossibleHome in Input:
                            if PossibleHome != None:
                                if type(PossibleHome) is str and len(PossibleHome) != 0:
                                    if str(PossibleHome[0]) == '@' and str(PossibleHome[1:]) in self.Registry[RegisterID]: PossibleHome = self.execute(RegisterID,SegmentID=str(PossibleHome[1:]))
                            IInput.append(PossibleHome)
                        Exec        = Function[0]
                        if len(IInput) in Function[1]:
                            Out     = Exec(IInput)
                            if RecordOut == None: return Out
                            elif RecordOut == 'HOME':self.Registry[RegisterID][SegmentID][2].apend(Out)
                        else: raise self.Al13N3475Exception('execute(...)','Invalid Amount Of Items Sent')
                    else: return None
                else: raise self.Al13N3475Exception('execute(...)','Invalid SegmentID ID For '+str(RegisterID))
            else:
                Output = []
                for Segment in self.Registry[RegisterID]: Output.append(self.execute(str(RegisterID),SegmentID=str(Segment)))
                if RecordOut == None: return Output
        else: raise self.Al13N3475Exception('execute(...)','Invalid RegisterID Sent')
    ############################################################################
    class Display:
        def __init__(self):
            self.Message_Index = {}
            self.Color_Index   = {
                # Fore And Back
                'fg':C_F.GREEN,   'bg':C_B.GREEN,'fb':C_F.BLUE,    'bb':C_B.BLUE,'fc':C_F.CYAN,    'bc':C_B.CYAN,'fm':C_F.MAGENTA, 'bm':C_B.MAGENTA,
                'fw':C_F.WHITE,   'bw':C_B.WHITE,'fr':C_F.RED,     'br':C_B.RED,'fy':C_F.YELLOW,  'by':C_B.YELLOW,'f0':C_F.RESET,   'b0':C_B.RESET,
                #################################
                # Style
                'sb':C_S.BRIGHT,'sn':C_S.NORMAL,'sd':C_S.DIM,'s0':C_S.RESET_ALL}
                ##################################
            self.HotKey = {'C':'@/','M':'!/'}
        ########################################################################
        def __readFile__(self,TargetFile):
            Record = False
            Lines   = {}
            Target = None
            if os.path.isfile(str(TargetFile)) == True:
                Text = open(str(TargetFile)).read().split('\n')
                for Line in Text:
                    if str('{/') in str(Line) and str(' ') in str(Line) and Record == False:
                        Target = Line.split(' ')[0]
                        Record = True
                        Lines[str(Target)] = []
                    elif str(Line) == str('/}'):
                        Target = None
                        Record = False
                    elif Record == True and Target != None: Lines[str(Target)].append(str(Line))
                for MessageHeader in Lines:
                    self.Message_Index[str(MessageHeader)] = ''
                    for Line in Lines[MessageHeader]:
                        if len(self.Message_Index[MessageHeader]) == 0: self.Message_Index[MessageHeader] = Line
                        else: self.Message_Index[MessageHeader]   += '\n'+str(Line)
        ########################################################################
        def FindColor(self,Message):
            for Color in self.Color_Index:
                CID = str(self.HotKey['C'])+str(Color)
                if str(CID) in str(Message):Message = Message.replace(str(CID),self.Color_Index[Color])
            return Message
        def FindMessage(self,Message):
            for MesgI in self.Message_Index:
                MID = str(self.HotKey['M'])+str(MesgI)
                if str(MID) in str(Message):Message = Message.replace(str(MID),self.Message_Index[MesgI])
            return Message
        def RainbowString(self,Mode,Message):
            if Mode == 0:
                TempMessage = str(Message)
                Message     = ''
                for Character in str(TempMessage):
                    Fore         = []
                    Back         = []
                    Style        = []
                    for Color in self.Color_Index:
                        if str('f') in str(Color): Fore.append(Color)
                        if str('b') in str(Color): Back.append(Color)
                        if str('s') in str(Color) and str('0') not in Color: Style.append(Color)
                    Fore_Rand    = Fore[random.randint(0,len(Fore)-1)]
                    Back_Rand    = Back[random.randint(0,len(Back)-1)]
                    Style_Rand   = Style[random.randint(0,len(Style)-1)]
                    Message += str(self.Color_Index[Fore_Rand])+str(self.Color_Index[Back_Rand])+str(self.Color_Index[Style_Rand])+str(Character)
                return str(Message)
            elif Mode == 1:
                Fores   = []
                for Color in self.Color_Index:
                    if str('f') in str(Color): Fores.append(self.Color_Index[Color])
                Output  = ''
                for Character in str(Message):
                    RandomColor = random.randint(0,len(Fores)-1)
                    Output     += str(Fores[RandomColor])+str(Character)
                return str(Output)
            elif Mode == 2:
                Backs   = []
                for Color in self.Color_Index:
                    if str('b') in str(Color): Backs.append(str(self.Color_Index[Color]))
                Output  = ''
                for Character in str(Message):
                    RandomColor = random.randint(0,len(Backs)-1)
                    Output     += str(Backs[RandomColor])+str(Character)
                return str(Output)
            elif Mode == 3:
                Styles   = []
                for Style in self.Color_Index:
                    if str('s') in str(Style): Styles.append(str(self.Color_Index[Style]))
                Output = ''
                for Character in str(Message):
                    RandomStyle = random.randint(0,len(Styles)-1)
                    Output     += str(Styles[RandomStyle])+str(Character)
                return str(Output)
        def Display(self,Message):
            Message = str(self.FindMessage(Message))
            Message = str(self.FindColor(Message))
            print(str(Message))
    ############################################################################
    # Logic (Al13N3475.Neuro.Logic.FUNCTION(INPUTS))
    class Neuro:
        '''
        OpKey: Al13N.Neuro
        Neuro.OpMount(Arguments) -> For Signal Handling
            [0]                  -> Root
            [1:]                 -> Args
            Roots:
                0,l,L,logic MODE OPERAND INPUT VALUE
                    Operand
                    -------
                    ==
                    !=
                    >
                    <
                    !
                    $
                1,t,Y,type  MODE INPUT VALUE
                     Input
                    -------
                    i
                    s
                    l
                    b
                    d
                    f
                    t
                2,s,S,string MODE OPERAND INPUT VALUE
                    /
                    ;
                    +
                    v
                3,i,I,integer MODE OPERAND INPUT VALUE
                    +
                    -
                    /
                    @
                    ^
                    v
                --------------------------------------
                4,~,list MODE OPERAND INPUT VALUE
                    +
                    %
                    ^
                    $
                    v
        Neuro.Logic (Logical Operations)
        Neuro.Logic.Operate(Mode,Operator,Input,Value)
            Mode: (0:Single,1:Multiple(Input Must Be Tuple))
            Operator:
                ==  -> Equal To     (I==V       :True)
                !=  -> Not Equal    (I!=V       :True)
                <   -> Less Than    (I<V        :True)
                >   -> Greater Than (I>V        :True)
                !   -> In           (I in V     :True)
                $   -> Not In       (I not in V :True)
                --------------------------------------
        Neuro.Type.Operate(Mode,Input,Value)
            Mode: (0:Single,1:Multiple(I Must Be Tuple))
            Operands:
                i   -> int
                s   -> str
                l   -> list
                b   -> bool
                f   -> function
                d   -> dict
                t   -> tuple
                --------------------------------------
        Neuro.Variables
            Neuro.Variables.String.Operate(Mode,Operand,I,V)
                Mode: (0:single,1:multiple(I Must Be Tuple))
                Operands:
                    / -> split
                    ; -> strip
                    + -> append
                    v -> value
                    ----------------------------------
            Neuro.Variables.Integer.Operate(Mode,Operand,I,V)
                Mode: (0:single,1:multiple(I Must Be Tuple))
                Operands:
                    + -> add
                    - -> sub
                    / -> div
                    @ -> exp
                    ^ -> xor
                    v -> value
                    ----------------------------------
            Neuro.Variables.List.Operate(Mode,Operand,I,V)
                Mode: (0:single,1:multiple(V Must Be Tuple))
                Operands:
                    + -> append
                    % -> index
                    ^ -> add
                    $ -> pull (V Must Be Tuple With 2 Ints [int:int])
                    v -> value
                    ----------------------------------
        '''
        class Logic:
            def Operate(Mode,Operator,Input,Value):
                if Mode in [0,'s','S','single']: # Single Value Operation
                    if Operator in ['==','iq','isequal','IsEqual']  : return Al13N3475.Neuro.Logic.IsEqual(Input,Value)
                    elif Operator in ['!=','nq','notequal','NotEqual']: return Al13N3475.Neuro.Logic.NotEqual(Input,Value)
                    elif Operator in ['>','gr','greater','Greater']   : return Al13N3475.Neuro.Logic.GreaterThan(Input,Value)
                    elif Operator in ['<','lt','lessthan','LessThan'] : return Al13N3475.Neuro.Logic.LessThan(Input,Value)
                    elif Operator in ['!','in','In']                  : return Al13N3475.Neuro.Logic.IsIn(Input,Value)
                    elif Operator in ['$','ni','Ni']                  : return Al13N3475.Neuro.Logic.NotIn(Input,Value)
                    else: raise Al13N3475.Neuro.Logic.LogicException('Operate(...)','Invalid Operator Sent')
                elif Mode in [1,'m','M','multiple']:
                    if type(Input) is tuple and len(Input) != 0:
                        Output = []
                        for Input_Input in Input: Output.append(Al13N3475.Neuro.Logic.Operate('s',Operator,Input_Input,Value))
                        return Output
                    else: raise Al13N3475.Neuro.Logic.LogicException('Operate(...)','Expected Input To Be tuple With Values')
                else: raise Al13N3475.Neuro.Logic.LogicException('Operate(...)','Expected A Valid Mode Got: '+str(Mode))
            ####################################################################
            # ==
            def IsEqual(I,V):
                if I == V: return True
                else: return False
            # !=
            def NotEqual(I,v):
                if I != V: return True
                else: return False
            # >
            def GreaterThan(I,V):
                if type(I) is int and type(V) is int:
                    if I > V: return True
                    else: return False
                else: raise Al13N3475.Neuro.Logic.LogicException('GreaterThan(',+str(I)+','+str(V)+')','Expected int Values')
            # <
            def LessThan(I,V):
                if type(I) is int and type(V) is int:
                    if I < V: return True
                    else: return False
                else: raise Al13N3475.Neuro.Logic.LogicException('LessThan(',+str(I)+','+str(V)+')','Expected int Values')
            # in
            def IsIn(I,V):
                if I in V: return True
                else: return False
            # not in
            def NotIn(I,V):
                if I not in V: return True
                else: return False
            # Exception
            def LogicException(Root,Mesg):
                Message = str('Al13N3475.Neuro.Logic.')+str(Root)+' | '+str(Mesg)
                raise Exception(Message)
        ########################################################################
        # Al13N3475.Neuro.Type.Operate(0/1,V,(...)/IN)
        class Type:
            def Operate(Mode,V,I):
                if Mode in [0,'s','S','single']:
                    if   V in [0,'i','I','int','Int']   and type(I) is     int or type(I) is str and I.isdigit() == True: return True
                    elif V in [1,'s','S','str','Str']   and type(I) is     str: return True
                    elif V in [2,'l','L','list','List']   and type(I) is  list: return True
                    elif V in [3,'t','T','tuple','Tuple'] and type(I) is tuple: return True
                    elif V in [4,'d','D','dict','Dict']   and type(I) is  dict: return True
                    elif V in [5,'b','B','bool','Bool']   and type(I) is  bool: return True
                    elif V in [6,'f','F','function','Function']:
                        if str(type(I)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>"]: return True
                        else: return False
                    else: return False
                elif Mode in [1,'m','M','multiple'] and type(I) is tuple:
                    Output = []
                    for Operand in I: Output.append(Al13N3475.Neuro.Type.Operate('s',V,Operand))
                    return Output
                else: raise Al13N3475.Neuro.Type.TypeException('Operate('+str(M)+','+str(V)+','+str(I)+')','Invalid Mode Sent')
            def TypeException(Root,Mesg):
                Message = str('Al13N3475.Neuro.Logic.')+str(Root)+' | '+str(Mesg)
                raise Exception(Message)
        ########################################################################
        # Al13N3475.Neuro.Variables.Operate
        class Variables:
            class String:
                def Split(I,V):
                    if str(I) in str(V): return I.split(V)
                    else: raise Al13N3475.Neuro.Variables.String.StringException('String('+str(I)+','+str(V)+')',str(I)+' Is Not In '+str(V))
                def Strip(I,V):
                    if str(I) in str(V): return I.strip(V)
                    else: raise Al13N3475.Neuro.Variables.String.StringException('String('+str(I)+','+str(V)+')',str(V)+' Is Not In '+str(I))
                def Append(I,V):
                    return str(I)+str(V)
                def Operate(Mode,Operand,I,V):
                    if Mode in [0,'s','S','single','Single','SINGLE']:
                        if Operand in ['/','split','Split','SPLIT']: return Al13N3475.Neuro.Variables.String.Split(I,V)
                        # Split
                        elif Operand in [';','strip','Strip','STRIP']: return Al13N3475.Neuro.Variables.String.Strip(I,V)
                        # Strip
                        elif Operand in ['+','append','Append','APPEND']: return Al13N3475.Neuro.Variables.String.Append(I,V)
                        # Append
                        elif Operand in ['v','value','Value','VALUE'] and len(V) == 0: return str(I)
                        # Return Value Of I
                        else: raise Al13N3475.Neuro.Variables.String.StringException('Operate(...)','Invalid Operand Sent: '+str(Operand))
                    elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and type(I) is tuple:
                        Output = []
                        for Input_Input in I:Output.append(Al13N3475.Neuro.Variables.String.Operate(0,Operand,Input_Input,V))
                        return Output
                    else: raise Al13N3475.Neuro.Variables.String.StringException('Operate(...)','Invalid Mode Sent')

                def StringException(Root,Mesg):
                    Message = str('Al13N3475.Neuro.Variables.String.')+str(Root)+' | '+str(Mesg)
                    raise Exception(Message)
            # Al13N3475.Neuro.Variables.String END #
            class Integer:
                def Add(I,V):
                    return I+V
                def Sub(I,V):
                    return I-V
                def Mul(I,V):
                    return I*V
                def Exp(I,V):
                    return I ** V
                def Div(I,V):
                    return I // V
                def XoR(I,V):
                    return I ^ V
                def Operate(Mode,Operator,I,V):
                    if Mode in [0,'s','S','single','Single','SINGLE']:
                        if type(I) is int or type(I) is str and I.isdigit() == True and type(V) is int or type(V) is str and V.isdigit() == True:
                            I = int(I)
                            V = int(V)
                            if Operator in [0,'+','add','Add','ADD']: return Al13N3475.Neuro.Variables.Integer.Add(I,V)
                            # Add
                            elif Operator in [1,'-','sub','Sub','SUB']: return Al13N3475.Neuro.Variables.Integer.Sub(I,V)
                            # Sub
                            elif Operator in [2,'*','mul','Mul','MUL']: return Al13N3475.Neuro.Variables.Integer.Mul(I,V)
                            # Mul
                            elif Operator in [3,'@','exp','Exp','EXO']: return Al13N3475.Neuro.Variables.Integer.Exp(I,V)
                            # Exp
                            elif Operator in [4,'/','div','Div','DIV']: return Al13N3475.Neuro.Variables.Integer.Div(I,V)
                            # XoR
                            elif Operator in [5,'^','xor','Xor','XOR']: return Al13N3475.Neuro.Variables.Integer.XoR(I,V)
                            # Value
                            elif Operator in [6,'v','val','Val','VAL'] and V == 0: return int(I)
                            # Fail
                            else: raise Al13N3475.Neuro.Variables.Integer.IntegerException('Operate(...)','Invalid Operator Sent: '+str(Operator))
                        else: raise Al13N3475.Neuro.Variables.Integer.IntegerException('Operate(...)','Expected int Types')
                    elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and type(I) is tuple:
                        Output = []
                        for Input_Input in I: Output.append(Al13N3475.Neuro.Variables.Integer.Operate(0,Operator,Input_Input,V))
                        return Output
                def IntegerException(Root,Mesg):
                    Message = 'Al13N3475.Neuro.Variables.Integer.'+str(Root)+' | '+str(Mesg)
                    raise Exception(Message)
            # Al13N3475.Neuro.Variables.Integers END #
            class List:
                def Append(I,V):
                    if type(I) is list and type(V) is list:
                        Output = []
                        for A in I: Output.append(A)
                        for A in V: Output.append(A)
                        return Output
                    else: raise Al13N3475.Neuro.Variables.List.ListException('Append(...)','Expected 2 Lists Got: '+str(I)+' '+str(V))
                def Index(I,V):
                    if Al13N3475.Neuro.Type.Operate(0,'l',I) == True and Al13N3475.Neuro.Type.Operate(0,'i',V) == True:
                        if int(V) <= len(I)-1: return I[V]
                        else: raise Al13N3475.Neuro.Variables.List.ListException('Index(...)','Got A Target Index Value Outside Of Scope: '+str(len(I)-1))
                    else: raise Al13N3475.Neuro.Variables.List.ListException('Index(...)','Expected 1 List And 1 Int Got Else...')
                def Add(I,V):
                    if Al13N3475.Neuro.Type.Operate(0,'l',I) == True and Al13N3475.Neuro.Type.Operate(0,'l',V) == False and Al13N3475.Neuro.Type.Operate(0,'t',V) == False:
                        if Al13N3475.Neuro.Type.Operate(0,'f',V) == False: return I.append(V)
                        else: raise Al13N3475.Neuro.Variables.List.ListException('Add(...)','Expected A str Or int Type For "Function"')
                    else: raise Al13N3475.Neuro.Variables.List.ListException('Add(...)','Expected A str Or int Type Got Else')
                def Pull(I,V):
                    if type(I) is list and type(V) is list and len(V) == 2:
                        if type(V[0]) is str and str(V[0]).isdigit() == True: V[0] = int(V[0])
                        if type(V[1]) is str and str(V[1]).isdigit() == True: V[1] = int(V[1])
                        if type(V[0]) is int and type(V[1]) is int:
                            if V[0] < V[1] and V[1] <= len(I)-1: return I[int(V[0]):int(V[1])]
                            else: raise Al13N3475.Neuro.Variables.List.ListException('Pull(...)','Expected V To Contain 2 ints Low<High And High<length(I)')
                        else: raise Al13N3475.Neuro.Variables.List.ListException('Pull(...)','Expected 2 Ints Inside Of V')
                    else: raise Al13N3475.Neuro.Variables.List.ListException('Pull(...)','Expected A List And A tuple With 2 Int Values')
                def Operate(Mode,Operand,I,V):
                    if Mode in [0,'s','S','single','Single','SINGLE']:
                        if Operand in ['+','append','Append','APPEND']: return Al13N3475.Neuro.Variables.List.Append(I,V)
                        elif Operand in ['%','index','Index','INDEX']   : return Al13N3475.Neuro.Variables.List.Index(I,V)
                        elif Operand in ['^','add','Add','ADD']         : return Al13N3475.Neuro.Variables.List.Add(I,V)
                        elif Operand in ['$','pull','Pull','PULL']      : return Al13N3475.Neuro.Variables.List.Pull(I,V)
                        elif Operand in ['v','value','Value','VALUE'] and len(V) == 0: return I
                        else: raise Al13N3475.Neuro.Variables.List.ListException('Operate(...)','Invalid Operand Sent: '+str(Operand))
                    elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and Al13N3475.Neuro.Type.Operate(0,'t',V):
                        Output = []
                        for Variables in V: Output.append(Al13N3475.Neuro.Variables.Operate(0,Operand,I,Variables))
                        return Output
                    else: raise Al13N3475.Neuro.Variables.List.ListException('Operate(...)','Invalid Mode Sent')
                def ListException(Root,Message):
                    Message = 'Al13N3475.Neuro.Variables.List.'+str(Root)+' | '+str(Message)
                    raise Exception(Message)
        # Al13N3475.Neuro.Variables END #
        ########################################################################
        # Used For Communication Inside Of self.OpKeys As (Al13N(3.4.75))
        def OpMount(Arguments):
            if type(Arguments) is tuple or type(Arguments) is list and len(Arguments) >= 3:
                CIndex = 0
                for Arg in Arguments:
                    # Conversion For String Inputs
                    if str(Arg).isdigit() == True: Arguments[CIndex] = int(Arg)
                    CIndex += 1
                if Arguments[0] in [0,'l','L','logic','Logic','LOGIC']       and len(Arguments) == 5: return Al13N3475.Neuro.Logic.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
                elif Arguments[0] in [1,'t','T','type','Type','TYPE']          and len(Arguments) == 4: return Al13N3475.Neuro.Type.Operate(Arguments[1],Arguments[2],Arguments[3])
                elif Arguments[0] in [2,'s','S','string','String','STRING']    and len(Arguments) == 5: return Al13N3475.Neuro.Variables.String.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
                elif Arguments[0] in [3,'i','I','integer','Integer','INTEGER'] and len(Arguments) == 5: return Al13N3475.Neuro.Variables.Integer.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
                elif Arguments[0] in [4,'~','list','List','LIST']              and len(Arguments) == 5: return Al13N3475.Neuro.Variables.List.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
                else: raise Al13N3475.Neuro.NeuroException('OpMount('+str(Arguments)+')','Invalid Open Signal '+str(Arguments[0]))
        def NeuroException(Root,Mesg):
            Message = 'Al13N3475.Neuro.'+str(Root)+' | '+str(Mesg)
            raise Exception(Message)
    # Neuro END #
    ############################################################################
    def Al13N3475Exception(self,Root,Mesg):
        Message = str('Al13N3475.')+str(Root)+' | '+str(Mesg)
        raise Exception(Message)
