NAME = 'Neuro'
# Logic (Al13N3480.Neuro.Logic.FUNCTION(INPUTS))
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
                if Operator in ['==','iq','isequal','IsEqual']  : return Al13N3480.Neuro.Logic.IsEqual(Input,Value)
                elif Operator in ['!=','nq','notequal','NotEqual']: return Al13N3480.Neuro.Logic.NotEqual(Input,Value)
                elif Operator in ['>','gr','greater','Greater']   : return Al13N3480.Neuro.Logic.GreaterThan(Input,Value)
                elif Operator in ['<','lt','lessthan','LessThan'] : return Al13N3480.Neuro.Logic.LessThan(Input,Value)
                elif Operator in ['!','in','In']                  : return Al13N3480.Neuro.Logic.IsIn(Input,Value)
                elif Operator in ['$','ni','Ni']                  : return Al13N3480.Neuro.Logic.NotIn(Input,Value)
                else: raise Al13N3480.Neuro.Logic.LogicException('Operate(...)','Invalid Operator Sent')
            elif Mode in [1,'m','M','multiple']:
                if type(Input) is tuple and len(Input) != 0:
                    Output = []
                    for Input_Input in Input: Output.append(Al13N3480.Neuro.Logic.Operate('s',Operator,Input_Input,Value))
                    return Output
                else: raise Al13N3480.Neuro.Logic.LogicException('Operate(...)','Expected Input To Be tuple With Values')
            else: raise Al13N3480.Neuro.Logic.LogicException('Operate(...)','Expected A Valid Mode Got: '+str(Mode))
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
            else: raise Al13N3480.Neuro.Logic.LogicException('GreaterThan(',+str(I)+','+str(V)+')','Expected int Values')
        # <
        def LessThan(I,V):
            if type(I) is int and type(V) is int:
                if I < V: return True
                else: return False
            else: raise Al13N3480.Neuro.Logic.LogicException('LessThan(',+str(I)+','+str(V)+')','Expected int Values')
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
            Message = str('Al13N3480.Neuro.Logic.')+str(Root)+' | '+str(Mesg)
            raise Exception(Message)
    ########################################################################
    # Al13N3480.Neuro.Type.Operate(0/1,V,(...)/IN)
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
                for Operand in I: Output.append(Al13N3480.Neuro.Type.Operate('s',V,Operand))
                return Output
            else: raise Al13N3480.Neuro.Type.TypeException('Operate('+str(M)+','+str(V)+','+str(I)+')','Invalid Mode Sent')
        def TypeException(Root,Mesg):
            Message = str('Al13N3480.Neuro.Logic.')+str(Root)+' | '+str(Mesg)
            raise Exception(Message)
    ########################################################################
    # Al13N3480.Neuro.Variables.Operate
    class Variables:
        class String:
            def Split(I,V):
                if str(I) in str(V): return I.split(V)
                else: raise Al13N3480.Neuro.Variables.String.StringException('String('+str(I)+','+str(V)+')',str(I)+' Is Not In '+str(V))
            def Strip(I,V):
                if str(I) in str(V): return I.strip(V)
                else: raise Al13N3480.Neuro.Variables.String.StringException('String('+str(I)+','+str(V)+')',str(V)+' Is Not In '+str(I))
            def Append(I,V):
                return str(I)+str(V)
            def Operate(Mode,Operand,I,V):
                if Mode in [0,'s','S','single','Single','SINGLE']:
                    if Operand in ['/','split','Split','SPLIT']: return Al13N3480.Neuro.Variables.String.Split(I,V)
                    # Split
                    elif Operand in [';','strip','Strip','STRIP']: return Al13N3480.Neuro.Variables.String.Strip(I,V)
                    # Strip
                    elif Operand in ['+','append','Append','APPEND']: return Al13N3480.Neuro.Variables.String.Append(I,V)
                    # Append
                    elif Operand in ['v','value','Value','VALUE'] and len(V) == 0: return str(I)
                    # Return Value Of I
                    else: raise Al13N3480.Neuro.Variables.String.StringException('Operate(...)','Invalid Operand Sent: '+str(Operand))
                elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and type(I) is tuple:
                    Output = []
                    for Input_Input in I:Output.append(Al13N3480.Neuro.Variables.String.Operate(0,Operand,Input_Input,V))
                    return Output
                else: raise Al13N3480.Neuro.Variables.String.StringException('Operate(...)','Invalid Mode Sent')

            def StringException(Root,Mesg):
                Message = str('Al13N3480.Neuro.Variables.String.')+str(Root)+' | '+str(Mesg)
                raise Exception(Message)
        # Al13N3480.Neuro.Variables.String END #
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
                        if Operator in [0,'+','add','Add','ADD']: return Al13N3480.Neuro.Variables.Integer.Add(I,V)
                        # Add
                        elif Operator in [1,'-','sub','Sub','SUB']: return Al13N3480.Neuro.Variables.Integer.Sub(I,V)
                        # Sub
                        elif Operator in [2,'*','mul','Mul','MUL']: return Al13N3480.Neuro.Variables.Integer.Mul(I,V)
                        # Mul
                        elif Operator in [3,'@','exp','Exp','EXO']: return Al13N3480.Neuro.Variables.Integer.Exp(I,V)
                        # Exp
                        elif Operator in [4,'/','div','Div','DIV']: return Al13N3480.Neuro.Variables.Integer.Div(I,V)
                        # XoR
                        elif Operator in [5,'^','xor','Xor','XOR']: return Al13N3480.Neuro.Variables.Integer.XoR(I,V)
                        # Value
                        elif Operator in [6,'v','val','Val','VAL'] and V == 0: return int(I)
                        # Fail
                        else: raise Al13N3480.Neuro.Variables.Integer.IntegerException('Operate(...)','Invalid Operator Sent: '+str(Operator))
                    else: raise Al13N3480.Neuro.Variables.Integer.IntegerException('Operate(...)','Expected int Types')
                elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and type(I) is tuple:
                    Output = []
                    for Input_Input in I: Output.append(Al13N3480.Neuro.Variables.Integer.Operate(0,Operator,Input_Input,V))
                    return Output
            def IntegerException(Root,Mesg):
                Message = 'Al13N3480.Neuro.Variables.Integer.'+str(Root)+' | '+str(Mesg)
                raise Exception(Message)
        # Al13N3480.Neuro.Variables.Integers END #
        class List:
            def Append(I,V):
                if type(I) is list and type(V) is list:
                    Output = []
                    for A in I: Output.append(A)
                    for A in V: Output.append(A)
                    return Output
                else: raise Al13N3480.Neuro.Variables.List.ListException('Append(...)','Expected 2 Lists Got: '+str(I)+' '+str(V))
            def Index(I,V):
                if Al13N3480.Neuro.Type.Operate(0,'l',I) == True and Al13N3480.Neuro.Type.Operate(0,'i',V) == True:
                    if int(V) <= len(I)-1: return I[V]
                    else: raise Al13N3480.Neuro.Variables.List.ListException('Index(...)','Got A Target Index Value Outside Of Scope: '+str(len(I)-1))
                else: raise Al13N3480.Neuro.Variables.List.ListException('Index(...)','Expected 1 List And 1 Int Got Else...')
            def Add(I,V):
                if Al13N3480.Neuro.Type.Operate(0,'l',I) == True and Al13N3480.Neuro.Type.Operate(0,'l',V) == False and Al13N3480.Neuro.Type.Operate(0,'t',V) == False:
                    if Al13N3480.Neuro.Type.Operate(0,'f',V) == False: return I.append(V)
                    else: raise Al13N3480.Neuro.Variables.List.ListException('Add(...)','Expected A str Or int Type For "Function"')
                else: raise Al13N3480.Neuro.Variables.List.ListException('Add(...)','Expected A str Or int Type Got Else')
            def Pull(I,V):
                if type(I) is list and type(V) is list and len(V) == 2:
                    if type(V[0]) is str and str(V[0]).isdigit() == True: V[0] = int(V[0])
                    if type(V[1]) is str and str(V[1]).isdigit() == True: V[1] = int(V[1])
                    if type(V[0]) is int and type(V[1]) is int:
                        if V[0] < V[1] and V[1] <= len(I)-1: return I[int(V[0]):int(V[1])]
                        else: raise Al13N3480.Neuro.Variables.List.ListException('Pull(...)','Expected V To Contain 2 ints Low<High And High<length(I)')
                    else: raise Al13N3480.Neuro.Variables.List.ListException('Pull(...)','Expected 2 Ints Inside Of V')
                else: raise Al13N3480.Neuro.Variables.List.ListException('Pull(...)','Expected A List And A tuple With 2 Int Values')
            def Operate(Mode,Operand,I,V):
                if Mode in [0,'s','S','single','Single','SINGLE']:
                    if Operand in ['+','append','Append','APPEND']: return Al13N3480.Neuro.Variables.List.Append(I,V)
                    elif Operand in ['%','index','Index','INDEX']   : return Al13N3480.Neuro.Variables.List.Index(I,V)
                    elif Operand in ['^','add','Add','ADD']         : return Al13N3480.Neuro.Variables.List.Add(I,V)
                    elif Operand in ['$','pull','Pull','PULL']      : return Al13N3480.Neuro.Variables.List.Pull(I,V)
                    elif Operand in ['v','value','Value','VALUE'] and len(V) == 0: return I
                    else: raise Al13N3480.Neuro.Variables.List.ListException('Operate(...)','Invalid Operand Sent: '+str(Operand))
                elif Mode in [1,'m','M','multiple','Multiple','MULTIPLE'] and Al13N3480.Neuro.Type.Operate(0,'t',V):
                    Output = []
                    for Variables in V: Output.append(Al13N3480.Neuro.Variables.Operate(0,Operand,I,Variables))
                    return Output
                else: raise Al13N3480.Neuro.Variables.List.ListException('Operate(...)','Invalid Mode Sent')
            def ListException(Root,Message):
                Message = 'Al13N3480.Neuro.Variables.List.'+str(Root)+' | '+str(Message)
                raise Exception(Message)
    # Al13N3480.Neuro.Variables END #
    ########################################################################
    # Used For Communication Inside Of self.OpKeys As (Al13N(3.4.75))
    def NeuroException(Root,Mesg):
        Message = 'Al13N3480.Neuro.'+str(Root)+' | '+str(Mesg)
        raise Exception(Message)

################################################################################
def Al13N_HooK(Version,*Arguments):
    if Version not in [(3,4,75),(3,4,80)]:
        raise Exception('Invalid Version For Operations...')
    Arguments = Arguments[0]
    if type(Arguments) is tuple or type(Arguments) is list and len(Arguments) >= 3:
        CIndex = 0
        for Arg in Arguments:
            # Conversion For String Inputs
            if str(Arg).isdigit() == True: Arguments[CIndex] = int(Arg)
            CIndex += 1
        if Arguments[0] in [0,'l','L','logic','Logic','LOGIC']       and len(Arguments) == 5: return Al13N3480.Neuro.Logic.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
        elif Arguments[0] in [1,'t','T','type','Type','TYPE']          and len(Arguments) == 4: return Al13N3480.Neuro.Type.Operate(Arguments[1],Arguments[2],Arguments[3])
        elif Arguments[0] in [2,'s','S','string','String','STRING']    and len(Arguments) == 5: return Al13N3480.Neuro.Variables.String.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
        elif Arguments[0] in [3,'i','I','integer','Integer','INTEGER'] and len(Arguments) == 5: return Al13N3480.Neuro.Variables.Integer.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
        elif Arguments[0] in [4,'~','list','List','LIST']              and len(Arguments) == 5: return Al13N3480.Neuro.Variables.List.Operate(Arguments[1],Arguments[2],Arguments[3],Arguments[4])
        else: raise Al13N3480.Neuro.NeuroException('OpMount('+str(Arguments)+')','Invalid Open Signal '+str(Arguments[0]))
