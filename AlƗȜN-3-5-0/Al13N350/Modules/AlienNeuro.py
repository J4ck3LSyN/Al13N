class Neuro:
    class Variables:
        def String(Mode,Operand,Input,Value):
            '''
            v -> value
            + -> append
            / -> split
            - -> strip
            i -> index
            '''
            if Mode in [0,'s','S']: # Single
                if Operand in [0,'v','V']: # Value
                    return str(Input)
                elif Operand in [1,'+','a']: # Append
                    return str(Input)+str(Value)
                elif Operand in [2,'/','s']: # split
                    if str(Input) in str(Value): return Value.split(str(Input))
                    else: raise Neuro.NeuroException('Variables.String(...)',str(Value)+' not in '+str(Input))
                elif Operand in [3,'-','r']: # strip
                    if str(Input) in str(Value): return Value.strip(str(Input))
                    else: raise Neuro.NeuroException('Variables.String(...)',str(Value)+' not in '+str(Input))
                elif Operand in [4,'!','i']: # index
                    if str(Input) in str(Value) and len(Input) == 1: return Value.index(str(Input))
                    else: raise Neuro.NeuroException('Variables.String(...)',str(Value)+' not in '+str(Input))
                else: raise Neuro.NeuroException('Variables.String(...)','Invalid Operand Sent')
            elif Mode in [1,'m','M']: # Multiple
                if type(Input) is list or type(Input) is tuple:
                    Outputs = []
                    for Arg in Input:
                        Outputs.append(str(Neuro.Variables.String('s',Arg,Value)))
                    return Outputs
                else: raise Neuro.NeuroException('Variables.String(...)','Expected A list Or tuple For Mode 1')
            else: raise Neuro.NeuroException('Variables.String(...)','Invalid Mode Sent')
        def Integer(Mode,Operand,Input,Value):
            '''
            v -> value
            + -> add
            - -> sub
            * -> mul
            ^ -> xor
            $ -> exp
            > -> hex
            < -> hex-decode
            '''
            if Mode in [0,'s','S']:
                if type(Input) is str and Input.isdigit() == True: Input = int(Input)
                if type(Value) is str and Value.isdigit() == True: Value = int(Value)
                if str(Operand) in [0,'v','V']: # Value
                    return int(Input)
                elif str(Operand) in [1,'+','a']: # Add
                    return int(Input)+int(Value)
                elif str(Operand) in [2,'-','s']: # Sub
                    return int(Input)-int(Value)
                elif str(Operand) in [3,'*','m']: # Mul
                    return int(Input)*int(Value)
                elif str(Operand) in [4,'^','x']: # Xor
                    return int(Input)^int(Value)
                elif str(Operand) in [5,'$','e']: # Exp
                    return int(Input)**int(Value)
                elif str(Operand) in [6,'>','ih']: # Into Hex
                    return hex(Input)
                elif str(Operand) in [7,'<','if']: # From Hex
                    return int(str(hex),16)
                else: raise Neuro.NeuroException('Variables.Integer(...)','Invalid Operand')
            elif Mode in [1,'m','M']:
                if type(Input) is list or type(Input) is tuple:
                    Outputs = []
                    for Arg in Input:
                        if type(Arg) is int: Outputs.append(int(Neuro.Variables.Integer('s',int(Arg),int(Value))))
                    return Outputs
                else: raise Neuro.NeuroException('Variables.Integer(...)','Expected list Or tuple For Input')
            else: raise Neuro.NeuroException('Variables.Integer(...)','Invalid Mode Sent')
        def Boolean(Mode,Operand,Input,Value):
            '''
            v -> value
            = -> equal to
            '''
            if Mode in [0,'s','S']:
                if str(Input) in [0,'f','F','false','False']: Input = False
                if str(Input) in [1,'t','T','true', 'True' ]: Input = True
                if str(Value) in [0,'f','F','false','False']: Value = False
                if str(Value) in [1,'t','T','true','True'  ]: Value = True
                if type(Input) is bool:
                    if Operand in [0,'v','V']: return Input
                    elif Operand in [1,'=','e']: # Equal
                        if Input == True and Value == True: return True
                        elif Input == False and Value == False: return True
                        else: return False
                    elif Operand in [2,'<','f']: # Flip
                        if Input == True: return False
                        else: return True
                    else: raise Neuro.NeuroException('Variables.Boolean(...)','Invalid Operand Sent')
                else: raise Neuro.NeuroException('Variables.Boolean(...)','Expected Boolean Type')
            elif Mode in [1,'m','M']:
                if type(Input) is list or type(Input) is tuple:
                    Output = []
                    for Arg in Input:
                        if type(Arg) is bool: Outputs.append(Neuro.Variables.Boolean('s',Operand,Arg,Value))
                else: raise Neuro.NeuroException('Variables.Boolean(...)','Expected List For Mode 1')
            else: raise Neuro.NeuroException('Variables.Boolean(...)','Invalid Mode Sent')
        def List(Mode,Operand,Input,Value):
            if Mode in [0,'s','S']:
                if Operand in [0,'+','a']: # Append
                    if type(Input) is list and type(Value) is list:
                        for V in Value: Input.append(V)
                        return Input
                    elif type(Input) is list and type(Value) is not list:
                        return Input.append(Value)
                    else: raise Neuro.NeuroException('Variables.List(...)','Expected A list Type For Input')
                elif Operand in [1,'!','i']: # Index
                    if type(Input) is list:
                        if Value in Input: return True
                        else: return False
                    else: raise Neuro.NeuroException('Variables.List(...)','Expected A list Type For Input')
                elif Operand in [2,'.','l']: # length
                    if type(Input) is list: return len(Input)
                    else: raise Neuro.NeuroException('Variables.List(...)','Expected a list Type For Input')
                elif Operand in [3,'<','p']: # pop
                    if type(Input) in list and len(Input) != 0: return Input[len(Input)-1]
                    else: raise Neuro.NeuroException('Variables.List(...)','Expected a list Type For Input')
                elif Operand in [4,'>','t']: # Target
                    if type(Input) is list and type(Value) is int:
                        if int(Value) < len(Input)-1: return Input[int(Value)]
                        else: raise Neuro.NeuroException('Variables.List(...)','Expected A int Lower Than Needed Length {}'.format(str(len(Input))))
                    else: raise Neuro.NeuroException('Variables.List(...)','Expected A list Type And A int Type')
                else: raise Neuro.NeuroException('Variables.List(...)','Invalid Operand')
            else: raise Neuro.NeuroException('List(...)','Does Not Accept Any Modes Past 0')

    def Logical(Mode,Operand,Input,Value):
        if Mode in [0,'s','S']:
            if   Operand in [0,'==','equal','Equal','EQUAL']:
                if Input == Value: return True
                else: return False
            elif Operand in [1,'!=','notequal','NotEqual','NOTEQUAL']:
                if Input != Value: return True
                else: return False
            elif Operand in [2,'^','in','In','IN']:
                if type(Input) == type(Value):
                    if Input in Value: return True
                    else: return False
                else: raise Neuro.NeuroException('Logical(...)','Types Must Match')
            else: raise Neuro.NeuroException('Logical(...)','Invalid Operand')
        elif Mode in [1,'m','M']:
            if type(Input) is list or type(Input) is tuple:
                Outputs = []
                for Arg in Input: Output.append(Neuro.Logical('s',Operand,Arg,Value))
            else: raise Neuro.NeuroException('Logical(...)','Expected list Or tuple For Mode 1')
        else: raise Neuro.NeuroException('Logical(...)','Invalid Mode')
    def Type(Mode,Operand,Input):
        if Mode in [0,'s','S']:
            if Operand in [0,'str','Str','STR']:
                if type(Input) is str: return True
                else: return False
            elif Operand in [1,'int','Int','INT']:
                if type(Input) is int: return True
                else: return False
            elif Operand in [2,'Variables.List','Variables.List','Variables.List']:
                if type(Input) is list: return True
                else: return False
            elif Operand in [3,'bool','Bool','BOOL']:
                if type(Input) is bool: return True
                else: return False
            elif Operand in [4,'func','Func','FUNC']:
                if str(type(Input)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]:
                    return True
                else: return False
            else: raise Neuro.NeuroException('Type(...)','Invalid Operand Sent')
        elif Mode in [1,'m','M']:
            if type(Input) is list or type(Input) is tuple:
                Outputs = []
                for Arg in Input: Outputs.append('s',Operand,Arg)
                return Outputs
            else: raise Neuro.NeuroException('Type(...)','Expected list Or tuple For Mode 1')
        else: raise Neuro.NeuroException('Type(...)','Invalid Mode Sent')
    def NeuroException(Root,Mesg): raise Exception('Neuro.'+str(Root)+' -> '+str(Mesg))
# Module Plugin
# Will Recieve One Value For Input As List
# [0]       -> Must Have Matching Values
# [0][0]    -> Target Action Type
# [0][1]    -> Target Mode
# [0][2]    -> Target Operand
# [0][3]    -> Target Inputs
# [0][4]    -> Target Values
def Operate(*Args):
    if len(Args) == 1:
        if type(Args[0]) is list or type(Args[0]) is tuple:
            if len(Args[0]) == 5:
                TARGET      = Args[0][0]
                MODE        = Args[0][1]
                OPERAND     = Args[0][2]
                Inputs      = Args[0][3]
                Values      = Args[0][4]
                if TARGET in   ['v.s','str','Str','STR','string','String','STRING']      : return Neuro.Variables.String(MODE,OPERAND,Inputs,Values)
                elif TARGET in ['v.i','int','Int','INT','integer','Integer','INTEGER']   : return Neuro.Variables.Integer(MODE,OPERAND,Inputs,Values)
                elif TARGET in ['v.b','bool','Bool','BOOL','boolean','Boolean','BOOLEAN']: return Neuro.Variables.Boolean(MODE,OPERAND,Inputs,Values)
                elif TARGET in ['v.l','Variables.List','Variables.List','Variables.List'] : return Neuro.Variables.List(MODE,OPERAND,Inputs,Values)
                elif TARGET in ['l','logic','Logic','LOGIC']                             : return Neuro.Logical(MODE,OPERAND,Inputs,Values)
                elif TARGET in ['t','type','Type','TYPE']                                : return Neuro.Type(MODE,OPERAND,Inputs)
                else: raise Neuro.NeuroException('(<- Operand:...)','Invalid Argument Sent')
            else: raise Neuro.NeuroException('(<- Operand:...)','Invalid Length Sent Expected 5 Entities Even If One Is Ignored')
        else:raise Neuro.NeuroException('(<- Operand:...)','Expected A List or Tuple As Main Argument Due To Al13N Handling')
    else:raise Neuro.NeuroException('(<- Operand:...)','Expected 1 Arg')
