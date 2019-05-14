__author__   = "Anonymous"
__version__  = [[0],[1],[0]]
import os, time, sys, random, hashlib
import src
__usage__    = [
'*-- Used For Bot/Exploition Development & Implementation --*',
' All opreations can be impoted through Python2.7, however the',
' Enviroment can be executed via sys.argv(Terminal) via:',
'  python al13n.py -u,--usage',
'  ^ Will Display This Usage',
'\n',
' Al13N is a enviroment based off chain commands, this allows',
' for inputs and actions to be maintained and managed in a',
' clean and functional manner. Everything is devleoped to assist',
' with handling and executing system functions for our own operations',
' IE: control the system for operational purposes.',
' All operations are also built to assist in internal security not only',
' on the lines of defense but also on the lines of offense. We want to',
' hide when we want to hide, show when we want to show, and act when we',
' want to act. Al13N handles operations via the Al13N-Chain-Strucure',
' this operations allows for universes to be created for operations',
' and configured for optimization.'
'\n',
' When Working With Python2:',
'  When Creating Operations Mount The Al13N Module To A Mount-Point',
'  import al13n',
'  All function outputs are sent as arrays [True/False,[MESSAGE]]',
'  Message will depend on the status of [0], False is the ERROR Flag',
'  communicating [1] to _LogMessage.'
'  root_ops = al13n.Al13N(mods=None)',
'  Changing mods from None will import that directory as Al13N Script',
'  after mounting Al13N to root_ops you can then operate on the module.',
'  On creation several variables are made:',
'   .Complex {}  -> This is where everything is remembered and handled',
'   .Status  T/F -> This is the status if False no operations will succeed',
' -> This is the logging is True than Messages sent to LogIndX',
'   .LogIndX  [] -> Output from .Logging',
'   .Template {} -> Template for translating script to Al13N',
'   .Modules  [] -> This is where modules are added for extended out-of-box ops',
'  All logging operations are sent through the _LogMessage Function:',
'   ._LogMessage([r,m,i,f]) r Is the root of the message ',
'    m Is the message, i Is the invalid argument, f Is the fix for the issue',
'    Everything will only be triggered is .Logging is True.',
'    You can find logs in .LogIndX',
' All string based operations are send through the following functions:',
'   .GenerateString([a,[l,r]]) a Is the character alphabet to use, [1][0]',
'    l Is the length of the string to generate and r Is the ratio to use for',
'    character configuration.',
'    When working with the array a random number will be generted between 1 and',
'    l, after this if the the number(g) is lower than l/r pull from a[:len(a)/2]',
'    else pull from a[len(a)/2:].',
'   .IndexString([i,c]) i Is the input string to use for compare, c Is the string',
'    to compare against, if c is None than it will be ignored returning the count',
'    of characters.',
'   .HashString([i,h]) i Is the input string to hash, h Is the hashtype to use.'
'\n',
' When Working With Al13N:',
'\n',
' When Working With Terminal-Ops:'
'  -u, --usage  - Displays This Help Message',
'  -g, --generate a1b2c3d! 123455 1/2/3/4/5/6/7/8/9',
'   Generated Random Strigs Tie: Al13N.GenerateString',
'  -i, --index string_1 string_2',
'   Compares string_1 Against string_2',
'  -h, --hash string_1 hash_type',
'   Hashes string_1 into hash_type'
]
# Al13N Module
class Al13N:
    def __init__(self,mods=None):
        ### Configure Variables ###
        self.Status   = True # Current Status Boolean
        self.Logging  = True # Current Logging Boolean
        self.LogIndX  = []   # Current Logging Index
        self.Genome   = None # Current Genome Labels
        self.Pages    = {}   # Pages For universes
    ### Action Operations ###
    def _LogMessage(self,LogArray): # For Logging Messages
        # [0] - Root
        # [1] - Message
        # [2] - Error Variable
        # [3] - Fix For Problem
        if self.Logging == False: # Verify Logging
            return
        message  = str(LogArray[0])+str(' @ ')+str(LogArray[1])
        message += str(' ERROR:')+str(LogArray[2])+str(' FIX:')+str(LogArray[3])
        self.LogIndX.append(str(message))
        return
    def _NewUniverse(self,GenerateArray): # For Generating New Univereses In Pages
        # [0] - int ID Generator ID PAGE
        # [1] - str ID Generator ID INDEX
        # [2] - lst [str] Tags For Indexing
        if self.Status == False: # Verify Status
            return [False,['_NewUniverse','Status-False','False','Configure Status To True See Usage']]
        elif type(GenerateArray) is not list: # Verify Type PT 1
            return [False,['_NewUniverse','Invalid-Type',str(GenerateArray),'Must Be List See Usage']]
        elif len(GenerateArray) != 3: # Verify Length
            return [False,['_NewUniverse','Invalid-Length',str(GenerateArray),'Must Be 3 See Usage']]
        elif type(GenerateArray[0]) is not int or type(GenerateArray[1]) is not str: # Verify Type PT 2
            return [False,['_NewUniverse','Invalid-Type','[0][1]','Not int/str See Usage']]
        elif type(GenerateArray[2]) is not list: # Verify Type PT 3
            return [False,['_NewUniverse','Invalid-Type','[2]','Not lst See Usage']]
        elif int(GenerateArray[0]) in self.Pages: # Verify NonExistance
            return [False,['_NewUniverse','Invalid-ID',str(GenerateArray[0]),'Exists See Usage']]
        self.Pages[int(GenerateArray[0])] = [str(GenerateArray[1]),GenerateArray[2],{}] # Generate Universe Object
        return [True,['_NewUniverse','Generated-Universe',str(GenerateArray[0]),'This Can Now Me Modulated']]
    #def _ModUniverse(self,GenerateArray): # For Generating Systems In Universes
    ### Method Based Operations ###
    def GenerateString(self,GenerateArray): # For Generating Random Strings
        # [0] - Complex Alphabet To Use NULL For None
        # [1] - [char_len(*),split_value(1)]
        if self.Status == False: # Verify Status
            return [False,['GenerateString','Status-False','False','Configure Status To True See Usage']]
        generated_string = '' # Variable To Use On Generation
        if type(GenerateArray) is not list: # Verify List Type
            return [False,['Genome.GenerateString','Invalid-Types',str(GenerateArray),'Invalid Type Must Be List See Usage']]
        elif len(GenerateArray) != 2: # Verify Array Length
            return [False,['Genome.GenerateString','Invalid-Types',str(GenerateArray),'Invalid Length Must Be 2 See Usage']]
        elif len(GenerateArray[1]) != 2: # Verify Array [1] Legth
            return [False,['Genome.GenerateString','Invalid-Types',str(GenerateArray[1],'Invalid Legth Must Be 2 See Usage')]]
        alphabet = GenerateArray[0]    # Alphabet To Use
        charlen  = int(len(alphabet))  # Capture Length Of Alphabet
        chartre  = int(charlen)/2      # Split The List By Half
        charupp  = alphabet[int(chartre):] # Capture Lower Alphabet
        charlow  = alphabet[:int(chartre)] # Capture Upper Alphabet
        charlen  = GenerateArray[1][0] # Character Length (range)
        charrat  = GenerateArray[1][1] # Character Ratio  (range/charrat)
        if len(str(charrat)) > int(1): # Verify Ratio Length
            return [False,['Genome.GenerateString','Invalid-Types',str(charrat),'Invalid Length Of Ration Must Be 1 See Usage']]
        if type(alphabet) is not str or type(charlen) is not int or type(charrat) is not int: # Verify Types
            return [False,['Genome.GenerateString','Invalid-Types','ALL','Invalid Types Sent See Usage']]
        for i in range(int(charlen)): # Open For Loop By Range Of charlen
            rint = random.randint(1,int(charlen)) # Generate Random Int
            rchr = '' # Generate Random Char Static Varaible For Compilation
            if int(rint) > int(charlen)/2: # Capture True Boolean
                if len(charupp) == 1: # Capture Length Of 1 (NoOtherOption)
                    rchr = str(charupp[0])
                else: # Generate And Capture
                    rloc = random.randint(1,len(charupp))
                    rchr = charupp[int(rloc)-1]
            else: # Follow Above
                if len(charlow) == 1:
                    rchr = str(charlow[0])
                else:
                    rloc = random.randint(1,len(charlow))
                    rchr = charlow[int(rloc)-1]
            generated_string += str(rchr)
        return [True,str(generated_string)]
    def IndexString(self,IndexArray): # For Finding Recurring Characters In Strings
        # [0] - str Input-String
        # [1] - str Returnable Chars Turn None If None
        if self.Status == False: # Verify Status
            return [False,['IndexString','Status-False','False','Configure Status To True See Usage']]
        elif type(IndexArray) is not list:
            return [False,['IndexString','Invaid-Types',str(IndexArray),'Invalid Type Not List See Usage']]
        elif len(IndexArray) != 2:
            return [False,['IndexString','Invalid-Length',str(IndexArray),'Must Be 2 See Usage']]
        elif type(IndexArray[0]) is not str: # Verify Type
            return [False,['IndexString','Invalid-Types',str(IndexArray[0]),'Must Be String See Usage']]
        elif type(IndexArray[1]) is not str and IndexArray != None:
            return [False,['IndexString','Invalid-Types',str(IndexArray[1]),'Must Be List Or None See Usage']]
        char_index  = {} # Character Memory Index
        char_string = str(IndexArray[0]) # Capture Input String
        char_compar = str(IndexArray[1]) # Capture Compare String
        for char in char_string: # Open For Loop
            if str(char) not in char_index: # Check For Existance
                char_index[str(char)] = [1,False]
            else:
                char_index[str(char)][0] += 1 # Incriment
            if str(char) in str(char_compar): # Catch Match
                char_index[str(char)][1] = True
        return [True,[str(IndexArray[0]),str(IndexArray[1])],char_index]
    def HashString(self,HashArray): # For Hashing Strings
        # [0] - str String To Hash
        # [1] - lst Hash Structure Follows List Iteration
        if self.Status == False: # Verify Status
            return [False,['HashString','Status-False','False','Configure Status To True See Usage']]
        elif type(HashArray) is not list: # Verify Type
            return [False,['HashString','Invalid-Types',str(HashArray),'Must Be List See Usage']]
        elif type(HashArray[0]) is not str or type(HashArray[1]) is not str: # Verify Type Pt 2
            return [False,['HashString','Invalid-Types','ALL','Must Be [str,[]] See Usage']]
        input_string = str(HashArray[0]) # Capture Input String
        hash_type    = HashArray[1]      # Capture hash List
        if str(hash_type) not in hashlib.algorithms_available: # Validate Fail
            return [False,['HashString','Invalid-Hash',str(hash),'Invalid Hash Type Sent See Usage']]
        hash_objct = hashlib.new(hash_type)  # Open hashlib Under type
        hash_objct.update(str(input_string)) # Update Objects
        hash_strng = hash_objct.digest()     # Digest Value \
        return [True,str(input_string),str(hash_strng)]
if len(sys.argv) > 1: # Capture Sys.Argv
    tree = sys.argv[1:]
    if str(tree[0]) in ['-u','--usage']: # Takes 0 inputs
        for line in __usage__:
            print(str(line))
        sys.exit(1)
    elif str(tree[0]) in ['-g','--generate']: # Takes 3 Inputs Pluts *ARGS
        if len(tree) < 4: # Verify Length
            print(str('(sInvalid Command String Sent alpha_set 9999 5'))
            sys.exit(1)
        alpha = tree[1]
        maxch = tree[2]
        ratio = tree[3]
        temp_mount      = Al13N()
        try:
            generate_string = temp_mount.GenerateString([str(alpha),[int(maxch),int(ratio)]])
            print(str(generate_string))
        except Exception as e:
            print(str('ERROR:')+str(e))
        sys.exit(1)
    elif str(tree[0]) in ['-i','--index']: # Takes 2 Inputs Plus *ARGS
        if len(tree) < 2: # Verify Length
            print(str('Invalid Command String Sent input_string compare_string'))
            sys.exit(1)
        input_string = tree[1]
        compr_string = tree[2]
        temp_mount   = Al13N()
        if str(compr_string) == str('None'): # Capture None Input
            compr_string = None
        else:
            compr_string = str(compr_string)
        validate_string = temp_mount.IndexString([str(input_string),compr_string])
        print(str(validate_string))
    elif str(tree[0]) in ['-h','--hash']: # Takes 2 Inputs Pluts *ARGS
        if len(tree) < 2: # Verify Length
            print(str('Invalid Command String Sent input_string hashtype hashtype hashtype....'))
            sys.exit(1)
        input_string = tree[1]
        hash_type    = tree[2]
        temp_mount   = Al13N()
        hash_compile = temp_mount.HashString([str(input_string),hash_type])
        print(str(hash_compile))
    sys.exit(1)
