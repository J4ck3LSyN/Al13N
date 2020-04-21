# Author      :: J4ck3lSyN
# Version     :: 3.5.0
# BackTrack   :: 3.4.75 (3.4.80 Pre-Op)
# Interpreter :: 0.5.0
import Al13N350 as Al13N
import os,sys,time,subprocess,random
import readline
# readline.parse_and_bind("tab: complete")
class Application:
    '''
> Al13N 3.5.0
> __init__(IsTermux=bool)
- Configures Internal Objects
> RaiseMode() Returns prompt For self.Mode
> HandleInput(str) Operates Based Off String
> RandomBanner(ShowAll=bool,LowLevelOnly=False)
- ShowAll Will Display All Messages And LowLevelOnly Will
- Only Use Small Banners
> Logger(str) Appends Messages To self.Logs And Display If self.Debug Is True
> Start() Start Loop0 Based Off self.Status
> ERROR(ROOT,MESG) For Raising Exceptions
> MountBannerFile(File) For Mounting Banners
    '''
    def __init__(self,PreExec=[],IsTermux=False,BannerT='random'):
        #readline.set_completer=self.Completer
        self.Status   = True          # status
        self.BannerT  = str(BannerT)  # Banner
        self.Mode     = '0:0'         # Mode
        self.CDir     = os.getcwd()   # cwd
        self.CHome    = os.getcwd()   # twd
        self.Memory   = {}            # memory
        self.Display  = Al13N.Modules.AlienDisplay.Display() # Display
        self.Display.Message_Index['Author']  = '@/sb@/fg(@/fwAl@/fg13@/fwN 3.5.0@/fg) J@/fy4@/fgck@/fb3@/fgLS@/fry@/fgN'
        self.Display.Message_Index['Version'] = '@/sb@/fg(@/fwAl@/fg13@/fwN 3.5.0@/fg) @/fr3@/fw.@/fr5@/fw.@/fr0'
        self.MountBannerFile('Banners.txt') # Banners
        self.Fails    = [0,10,True]   # Fails
        self.ROOT     = None          # Root self.Memory
        self.SEGMENT  = []            # Segments self.Memory[ROOT].REG[REGISTER][SEGMENTS[SINDEX]]
        self.SINDEX   = 0
        self.REGISTER = None          # Register self.MEMORY[ROOT].REG[REGISTER]
        self.IsTermux = IsTermux      # Termux Boolean
        self.Debug    = False         # Debugging
        self.Logs     = []            # Logging
        self.Info     = {             # Information
            'OPKEY|var'          :['variable OpKey For Generation',
                                   'v.s -> string',
                                   '    || + append',
                                   '    || / split',
                                   '    || - strip',
                                   '    || i index',
                                   '    || v value',
                                   'v.i -> integer', # NEED TO ADD ALL OPERATIONS
                                   '    || + add',
                                   '    || - sub',
                                   '    || * mul',
                                   '    || ^ xor',
                                   '    || $ exp',
                                   '    || > hex encode',
                                   '    || < hex decode',
                                   'v.b -> boolean',
                                   'l   -> logical',
                                   't   -> type'],
            'h|H|help|Help|HELP' :['Displays This Help Message'],
            '>|s|S|set|Set|SET'  :['Configured Internal Setting',
                                   'set d -> Debugging Flip',
                                   'set f -> failsafe'],
            'DEV|dev-seed'       :['Developer Test Seed'],
            'q|Q|quit|Quit|QUIT' :['Terminates Al13N Command Console'],
            'cwd|CWD'            :['Current working Directory'],
            'twd|TWD'            :['Temp Working Directory'],
            'log|Log|LOG'        :['Shows Logs'],
            '$|shell|Shell|SHELL':['Changes Mode To SHELL (0:1)',
                                   'From Here Output Will Be Sent Depending On Input',
                                   'To Exit Use "}"'],
            '+|new|New|NEW'      :['Generates A New Register And Configures Mode',
                                   'Takes 16 Following Values As Hex Instance Without "0x"',
                                   'IE: 0x01 | 01',
                                   '+ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
                                   'Each Value Is Used To Compile A Key'],
            '1:0|REGST'          :['Register Mode:'],
            '1:0|k|K|key|Key|KEY':['Displays Current Key'],
            '1:0|c|C|cof|Cof|COF':['Displays Current Character Offset'],
            '1:0|i|I|info|Info|INFO':[
                                   'Displays All Info'],
            '1:0|r|R|reg|Reg|REG':['Registers Configured',
                                   'Can Take 1 Arg To Display All Registers For Arg'],
            '1:0|setup-builtin'  :['Mounts Al13N Modules Inside Of Registers',
                                   'Al13N350.Modules.AlienNeuro.Operats -> var'],
            '1:1|SEGMENT'        :['Segment Mode:'],
            '1:1|v|V|var|Var|VAR':['Variable Type Handling',
                                   'Takes 3,4,5 Values Based Off Internal Mount Of',
                                   'Al13N.Modules.AlienNeuro.Operate()',
                                   '[0] Is Your Type:',
                                   '   l - logic',
                                   '   s - string',
                                   '   i - integer',
                                   '   ~ - list',
                                   '   t - type',
                                   '[1] Is Your Current Mode',
                                   '   If s Do Single, m Do Multiple',
                                   '[2] Is Your Operand/Input',
                                   '[3] Is Your Inupt',
                                   '[4] Value'],
            '1:1|u-i'            :['User-Input Handler, 1-8  Args'],
            '1:1|ttd'            :['Display() Handler,  1-16 Args'],
            '1:1|pyexe'          :['Executes Pythonic Code As String'],
            '1:1|alexe'          :['Executes Other Alien Based Commands',
                                   '-----------------------------------',
                                   'shell ... (Shell Commands)',
                                   '(MORE COMING SOON!)'],
            '1:1|alinfo'         :['Information Pertaining To Alien',
                                   '-----------------------------------',
                                   'c :: cwd | t :: time | i :: iface',
                                   'r ARG :: read file',
                                   'w ARG STR :: write file'],
            '1:1|if'             :['Logical Operations For Internal Execution',
                                   '-----------------------------------',
                                   'if SEGMENT == SEGMENT TRUESEG/null FALSESEG/null',
                                   'if SEGMENT != SEGMENT TRUESEG/null FALSESEG/null',
                                   'When Operating If The True/False Segments Are False',
                                   'We Will NULL Out Else We Will Execute As Segment',
                                   '@/frSEGMENTS Are @/fgExecuted...@/fw']
                                   }
    ############################################################################
    '''
    def Completer(self,Prefix,Index):
        Completed = ''
        if self.Mode == '0:0': Completed = [k for k in self.Info if k.startswith(Prefix)]
        return str(Completed)
    '''
    # ReadFile For Command Execution
    def ReadFile(self,TargetFile):
        if os.path.isfile(str(TargetFile)) == True:
            File_Text = open(str(TargetFile)).read().split('\n')
            File_Exec = []
            for Line in File_Text:
                if str('->') in str(Line):
                    Line_S = Line.split('->')
                    for Line_S_L in Line_S: File_Exec.append(Line_S_L)
                else: File_Exec.append(str(Line))
            for Exec in File_Exec:
                if len(Exec) != 0:
                    if str(Exec[0]) != str('`'):self.HandleInput(str(Exec))
        else: raise self.ERROR('ReadFile(...)','Expected A Valid File: '+str(TargetFile))
    # Pythonic Execution Mount
    def PythonicExec(self,script):
        if type(script) is list:
            script_text = ''
            for line in script:
                if len(script_text) == 0:script_text = str(line)
                else: script_text += str(' ')+str(line)
            script = str(script_text)
        exec(str(script))
    # Change Directory
    def ChangeDirectory(self,directory):
        if type(directory) is list: directory=directory[0]
        if os.path.isdir(str(directory)) == True:os.chdir(str(directory))
    # Raise Usage
    def RaiseHelp(self,Command=None):
        if Command == None:
            for CMD in self.Info: self.RaiseHelp(Command=str(CMD))
        else:
            Helps  = []
            for Mesg in self.Info:
                if str(Command) in str(Mesg) or str(Command) == str(Mesg): Helps.append(str(Mesg))
            for H in Helps:
                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw)')
                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/brUSAGE@/b0) > {}'.format(str(H)))
                for line in self.Info[str(H)]: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/brUSAGE@/b0) > {} -> @/fm{}'.format(str(H),str(line)))
                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw)')
    # Raise Prompt For Current Mode
    def RaiseMode(self):
        self.Logger('RaiseMode: Raising Mode {}'.format(str(self.Mode)))
        if self.Mode == str('0:0'): # Basic User Input Mode (HOME)
            Prompt    = '@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/fgHOME@/fw)  @/fy:@/fg>@/fw '
            return self.Display.FindColor(str(Prompt))
        elif self.Mode == str('0:1'): # Shell
            Prompt    = '@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/fgSHELL@/fw) ({}) @/fy:@/fg>@/fw '.format(str(os.getcwd()).replace('/','.'))
            return self.Display.FindColor(str(Prompt))
        elif self.Mode == str('1:0'): # Register 1:0
            Prompt    = '@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/fgREGST@/fw) ({}) @/fy:@/fg>@/fw '.format(str(self.ROOT))
            return self.Display.FindColor(str(Prompt))
        elif self.Mode == str('1:1'): # Register Segments 1:1
            Prompt    = '@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/fgSEGMT@/fw) (@/fg{}@/fw) (@/fg{}@/fw) (@/fg{}@/fw) @/fy:@/fg>@/fw '.format(str(self.ROOT),str(self.REGISTER),str(self.SEGMENT[self.SINDEX]))
            return self.Display.FindColor(str(Prompt))
    # Handle Current User-Input
    def HandleInput(self,UI,WriteToRegister=[]):
        if type(UI) is list:
            UI_Text = ''
            for L in UI:
                if len(UI_Text) == 0: UI_Text = str(L)
                else: UI_Text += str(' ')+str(L)
            if str(';;') in str(UI_Text):
                Commands = UI_Text.split(';;')
                for CMD in Commands: self.HandleInput(str(CMD))
                return
            UI = str(UI_Text)
        self.Logger('HandleInput: {} User-Input Recieved '.format(str(UI)))
        ########################################################################
        if self.Mode == str('0:0'): # Basic User Input Mode (HOME)
            if str(UI) in ['h','H','help','Help','HELP']: self.RaiseHelp()
            elif str(UI) in ['q','Q','quit','Quit','QUIT']:
                self.Display.Display('@/fw[@/brEXITING@/b0] Due To User-Issued Need...')
                self.Status = False
            elif str(UI) in ['$','shell','Shell','SHELL']: self.Mode = '0:1'
            elif str(UI) in ['dev-seed']: self.HandleInput('+ 03 04 05 06 06 07 08 09 03 04 05 06 06 07 08 09')
            elif str(UI) in ['l','list','List','LIST']   :
                if len(self.Memory) == 0: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) No Objects Exist')
                for Object in self.Memory: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (Memory) > '+str(Object))
            elif str(UI) in ['cwd','CWD']: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (CWD) > '+str(self.CHome))
            elif str(UI) in ['twd','TWD']: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (TWD) > '+str(self.CDir))
            elif str(UI) in ['log','Log','LOG']:
                for Mesg in self.Logs: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (LOG) > '+str(Mesg))
            elif str(UI) in ['m','M','memory','Memory','MEMORY']:
                if len(self.Memory) != 0:
                    for ID in self.Memory: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (@/fgID@/fw) > '+str(ID))
                else:
                    self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) > @/frNo Memory Object Generated...')
                    self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) > @/frUse "help +"')
            # Advanced
            elif str(' ') in str(UI):
                TREE = UI.split(' ')
                if str(TREE[0]) in ['h','H','help','Help','HELP']: self.RaiseHelp(Command=str(TREE[1]))
                elif str(TREE[0]) in ['+','new','New','NEW']:
                    if len(TREE[1:]) == 16:
                        CONV    = []
                        for Operand in TREE[1:]: CONV.append(int( '0x'+str(Operand),16 ))
                        Register     = Al13N.Brain.Registry( [CONV[0],CONV[1],CONV[2],CONV[3],CONV[4],CONV[5],CONV[6],CONV[7]],[CONV[8],CONV[9],CONV[10],CONV[11],CONV[12],CONV[13],CONV[14],CONV[15]] )
                        self.Memory[str(Register.KEY)]=Register
                        self.ROOT    = str(Register.KEY)
                        self.Mode = '1:0'
                    else: raise self.ERROR('HandleInput()','Expected 16 Values Following "new" Command Got '+str(len(TREE[1:]))+'Expected More Values')
                elif str(TREE[0]) in ['>','set','Set','SET']:
                    if len(TREE[1:]) == 1:
                        if TREE[1] in ['d','D','debug','Debug','DEBUG']:
                            if self.Debug == True: self.Debug = False
                            else: self.Debug = True
                        elif TREE[1] in ['f','F','fail','Fail','FAIL']:
                            if self.Fails[2] == True: self.Fails[2] = False
                            else: self.Fails[2] = True
                        else: raise self.ERROR('HandleInput()','Expected A Value To Configure')
                    else: raise self.ERROR('HandleInput()','Expected A Length Of More Than One')
                elif str(TREE[0]) in ['^','read','Read','READ']:
                    if len(TREE[1:]) == 1:
                        self.ReadFile(str(TREE[1]))

            elif str(UI) in self.Memory:
                self.ROOT = str(UI)
                self.SEGMENT = []
                self.SINDEX  = 0
                self.Mode    = '1:0'
        ########################################################################
        elif self.Mode == str('0:1'): # Basic User Input Mode (SHELL)
            if len(UI) == 0: return
            if str(' ') in str(UI):
                CMD = UI.split(' ')
            else:
                CMD = [str(UI)]
            if str(CMD[0]) in [str('}'),str('q')]: self.Mode = '0:0'
            else:
                self.Logger('HandleInput: Shself.HandleInput(str(line))ell Command ({})'.format(str(UI)))
                Output     = subprocess.Popen(CMD,stdout=subprocess.PIPE)
                self.Display.Display('@/fw(@self.HandleInput(str(line))/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) Output From: '+str(UI))
                Output     = bytes.decode(Output.stdout.read(),'utf-8')
                ''' For Writing outputs Once Writin
                if len(WriteToRegister) != 0:
                    if str(WriteToRegister[0]) in self.Memory:
                        if str(WriteToRegister[1]) in self.Memory[WriteToRegister[0]].REG:
                            if str(WriteToRegister[2]) in self.Memory[WriteToRegister[0]].RED[WriteToRegister[1]]:
                '''
                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) '+str(Output))
        ########################################################################
        elif self.Mode == str('1:0'): # Registry Handler
            if len(UI) == 0: return
            elif str(UI) in ['q','Q','quit','Quit','QUIT']: self.Mode = '0:0'
            elif str(UI) in ['k','K','key','Key','KEY']   : self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (KEY) > '+str(self.Memory[self.ROOT].KEY))
            elif str(UI) in ['c','C','cof','Cof','COF']   : self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (COF) > '+str(self.Memory[self.ROOT].COF))
            elif str(UI) in ['r','R','reg','Reg','REG']   :
                for Register in self.Memory[str(self.ROOT)].REG: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) ('+str(self.ROOT)+')> '+str(Register))
            elif str(UI) in ['o','O','opk','Opk','OPK']   :
                for OpKey in self.Memory[str(self.ROOT)].OKY: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (OpKey) > '+str(OpKey))
            elif str(UI) in ['i','I','info','Info','INFO']:
                self.HandleInput('k')
                self.HandleInput('c')
                self.HandleInput('r')
                self.HandleInput('o')
            elif str(UI) in ['h','H','help','Help','HELP']:
                self.RaiseHelp(Command='1:0')
            elif str(UI) == str('setup-builtin'):
                ### OpKey Mount ###
                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) Configured Internal OpKey (var,u-i,ttd,hash,pyex,chdir,alexe,alinfo)')
                self.Memory[self.ROOT].MountOpKey('var',Al13N.Modules.AlienNeuro.Operate,[3,4,5]);self.Logger('HandleInput: Mounted var Operation Key')
                self.Memory[self.ROOT].MountOpKey('u-i',self.HandleInput,[1,2,3,4,5,6,7,8]);self.Logger('HandleInput: Mounted u-i Operation Key')
                self.Memory[self.ROOT].MountOpKey('ttd',self.Display.Display,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]);self.Logger('HandleInput: Mounted ttd Opertion Key')
                self.Memory[self.ROOT].MountOpKey('hash',Al13N.Brain.KeyGeneration.Operate,[2]);self.Logger('HandleInput: Mounted hash Operation Key')
                self.Memory[self.ROOT].MountOpKey('pyex',self.PythonicExec,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
                self.Memory[self.ROOT].MountOpKey('chdir',self.ChangeDirectory,[1])
                self.Memory[self.ROOT].MountOpKey('alexe',Al13N.Modules.AlienExecution.Operate,[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
                self.Memory[self.ROOT].MountOpKey('alinfo',Al13N.Modules.AlienInformation.Operate,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
            elif str(UI) in self.Memory[self.ROOT].REG:
                self.REGISTER = str(UI)
                self.Mode = '1:1'
            elif str(' ') in str(UI):
                TREE = UI.split(' ')
                if str(TREE[0]) in ['+','new','New','NEW']:
                    if len(TREE[1:]) == 2:
                        ID = TREE[1:][0]
                        LN = int('0x'+TREE[1:][1],16)
                        self.REGISTER = self.Memory[self.ROOT].new(ID,LN)
                        self.SEGMENT = []
                        for S in self.Memory[self.ROOT].REG[ID]: self.SEGMENT.append(S)
                        self.Mode='1:1'
                elif str(TREE[0]) in ['r','R','reg','Reg','REG']:
                    if TREE[1] in self.Memory[self.ROOT].REG:
                        for S in self.Memory[self.ROOT].REG[str(TREE[1])]: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) ('+str(self.ROOT)+') ('+str(TREE[1])+') > '+str(S)+' \t '+str(self.Memory[self.ROOT].REG[TREE[1]][S]))
                elif str(TREE[0]) in ['e','E','exe','Exe','EXE']:
                    if len(TREE[1:]) == 2:
                        if TREE[1] in self.Memory[self.ROOT].REG:
                            if TREE[2] in self.Memory[self.ROOT].REG[TREE[1]]:
                                Out = self.Memory[self.ROOT].execute(TREE[1],TREE[2])
                                self.Logger('HandleInput: '+str(Out)+' From '+str(UI))
                                if Out != None: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) Output > '+str(Out))
                    elif len(TREE[1:]) == 1:
                        if TREE[1:][0] in self.Memory[self.ROOT].REG:
                            Outputs = []
                            for Segment in self.Memory[self.ROOT].REG[TREE[1:][0]]:
                                Output = self.Memory[self.ROOT].execute(TREE[1:][0],Segment)
                                self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) ({}) ({}) > {}'.format(str(TREE[1:][0]),str(Segment)),str(Output))
                            self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) {}'.format(str(Outputs)))
                        else: raise self.ERROR('HandleInput: Expected A Valid Execution Tree')
        ###
        elif self.Mode == str('1:1'): # Targeted Segment Handler
            if len(UI) == 0:
                if self.SINDEX == len(self.SEGMENT)-1: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) Cannot Incriment At Segment Roof')
                else: self.SINDEX += 1
            elif str(UI) in ['q','Q','quit','Quit','QUIT']: self.Mode = '1:0'
            elif str(UI) in ['h','H','help','Help','HELP']: self.RaiseHelp(Command='1:1')
            elif str(UI) in ['r','R','reg','Reg','REG']   :
                for S in self.SEGMENT:
                    self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) {} |\t{}'.format(str(S),str(self.Memory[self.ROOT].REG[self.REGISTER][S])))
            elif str(UI) in ['e','E','exe','Exe','EXE']   :
                Out = self.Memory[self.ROOT].execute(self.REGISTER,self.SEGMENT[self.SINDEX])
                self.Logger('HandleInput: Out -> '+str(Out))
                if Out != None: self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) (Output) > '+str(Out))
            elif str(UI) in self.SEGMENT: self.SINDEX = self.SEGMENT.index(UI)
            elif str(' ') in str(UI):
                TREE = UI.split(' ')
                if str(TREE[0]) in self.Memory[self.ROOT].OKY:
                    if len(TREE[1:]) in self.Memory[self.ROOT].OKY[TREE[0]][1]:
                        TINDEX = 0
                        for I in TREE[1:]:
                            if I.isdigit() == True: TREE[1:][TINDEX]=int(I)
                            elif str(',') in str(I): TREE[1:][TINDEX]=I.split(',')
                            TINDEX += 1
                        self.Memory[self.ROOT].write(str(TREE[0]),self.REGISTER,self.SEGMENT[self.SINDEX],TREE[1:])
                        self.SINDEX += 1
                elif str(TREE[0]) in ['e','E','exe','Exe','EXE']: # Mulitple Location Execution
                    ValidExecLocations = []
                    Ignored            = []
                    for Location in TREE[1:]:
                        if str(Location) in self.SEGMENT: ValidExecLocations.append(str(Location))
                        else: Ignored.append(str(Location))
                    if len(Ignored) != 0: raise self.ERROR('HandleInput: Expected Multiple Locations For Executon Ignored: '+str(Ignored))
                    else:
                        Outputs = []
                        for Location in ValidExecLocations: Outputs.append( [Location,self.Memory[self.ROOT].execute(self.REGISTER,str(Location) )] )

                        for Output in Outputs:
                            if Output[1] != None:self.Display.Display('@/fw(@/frAl@/fg13@/frN 3.@/fy5@/fr.0@/fw) ({}) ({})'.format(str(Output[0]),str(Output[1])))
                elif str(TREE[0]) in ['if','If','IF']: # If Logical Operations
                    if len(TREE[1:]) == 5:
                        Location_To_Test = TREE[1]
                        Operand          = TREE[2]
                        Location_To_Pull = TREE[3]
                        Location_Exec_T  = TREE[4]
                        Location_Exec_F  = TREE[5]
                        if Location_To_Test in self.SEGMENT and Location_To_Pull in self.SEGMENT:
                            Value_Alpha  = self.Memory[self.ROOT].execute(self.REGISTER,str(Location_To_Test))
                            Value_Bravo  = self.Memory[self.ROOT].execute(self.REGISTER,str(Location_To_Pull))
                            if str(Operand) in ['==','isequal','IsEqual','ISEQUAL']:
                                if Value_Alpha == Value_Bravo:
                                    if Location_Exec_T not in ['null','Null','NULL']:
                                        if Location_Exec_T in self.SEGMENT:
                                            return self.Memory[self.ROOT].execute(self.REGISTER,str(Location_Exec_T))
                                        else: raise self.ERROR('HandleInput: (1:1) Logical Operation Catch: Recieved Invalid Segment Execution',str(Location_Exec_T))
                                    else: return None
                                else:
                                    if Location_Exec_F not in ['null','Null','NULL']:
                                        if Location_Exec_F in self.SEGMENT:
                                            return self.Memory[self.ROOT].execute(self.REGISTER,str(Location_Exec_F))
                                        else: raise self.ERROR('HandleInput: (1:1) Logical Operation Catch: Recieved Invalid Segment Execution',str(Location_Exec_F))
                                    else: return None
                            elif str(Operand) in ['!=','notequal','NotEqual','NOTEQUAL']:
                                if Value_Alpha != Value_Bravo:
                                    if Location_Exec_T not in ['null','Null','NULL']:
                                        if Location_Exec_T in self.SEGMENT:
                                            return self.Memory[self.ROOT].execute(self.REGISTER,str(Location_Exec_T))
                                        else: raise self.ERROR('HandleInput: (1:1) Logical Operation Catch: Recieved Invalid Segment Execution',str(Location_Exec_T))
                                    else: return None
                                else:
                                    if Location_Exec_F not in ['null','Null','NULL']:
                                        if Location_Exec_F in self.SEGMENT:
                                            return self.Memory[self.ROOT].execute(self.REGISTER,str(Location_Exec_F))
                                        else: raise self.ERROR('HandleInput: (1:1) Logical Operation Catch: Recieved Invalid Segment Execution',str(Location_Exec_F))
                                    else: return None
                    else: raise self.ERROR('HandleInput: Mode (1:1) Logical Operation Catch: Recieved Invalid Length','Check Inputs')
        ########################################################################
    # Pull Random Banner Depending On Level
    def RandomBanner(self,ShowAll=False,LowLevelOnly=False):
        self.Logger('RandomBanner: Got Action With {} | {} '.format(str(ShowAll),str(LowLevelOnly)))
        LowLevelOnly = self.IsTermux
        if self.BannerT != 'random':
            self.Display.Display('!/'+str(self.BannerT))
            return
        Banners_ID = []
        for Banners in self.Display.Message_Index:
            if str('Banner') in str(Banners):
                if LowLevelOnly == True and str('LowLevel') in str(Banners):
                    Banners_ID.append(Banners)
                elif LowLevelOnly == False: Banners_ID.append(Banners)
                if ShowAll == True: self.Display.Display('!/'+str(Banners))
        I          = Banners_ID[random.randint(0,len(Banners_ID)-1)]
        self.Display.Display('!/'+str(I))
    # Start While Loop Based Off self.Status
    # Pull From self.RaiseMode For Prompt And Sent input() To self.HandleInput
    def Start(self,Que=[]):
        self.Logger('Start: Starting Terminal @ '+str(time.asctime()))
        self.RandomBanner()
        self.Display.Display('!/Author\n!/Version')
        if len(Que) != 0:
            CMD_STR = ''
            for line in Que:
                if len(CMD_STR) == 0:CMD_STR=str(line)
                else: CMD_STR+=str(' ')+str(line)
            self.HandleInput(str(CMD_STR))
        if self.Status == True:
            self.Logger('Start: Interpreter Interally Set To True Going To WhileLoop...')
            while self.Status == True and self.Fails[0] < self.Fails[1]:
                try:
                    Prompt = self.RaiseMode()
                    self.Logger('Start:(Prompt) {}'.format(str(Prompt)))
                    UI     = input(str(Prompt))
                    if str('->') in str(UI):
                        TREE = UI.split('->')
                        for U in TREE:
                            self.Logger('Start:(User-Input) (Chain) {}'.format(str(U)))
                            self.HandleInput(U)
                    else:
                        self.Logger('Start:(User-Input) {}'.format(str(UI)))
                        self.HandleInput(UI)
                except EOFError  as EOF : self.ERROR(str('EOF'),'EOFERROR' ,str(EOF))
                except Exception as EXC : self.ERROR(str('EXP'),'EXCEPTION',str(EXC))
                except KeyboardInterrupt: self.ERROR(str('KEY'),'KeyboardInterrupt','')
    def Logger(self,MESG):
        self.Logs.append(str(MESG))
        if self.Debug == True: self.Display.Display('@/fg(@/fr@/bgAl13N@/b0 @/bg3.5.0@/b0@/fg) [@/fwDEBUGGING@/fg] > '+str(MESG))
    # For Errors And self.Fails
    def ERROR(self,UI,ERROR,REASON):
        self.Logger('ERROR: {}|{}|{}->ERROR'.format(str(UI),str(ERROR),str(REASON)))
        self.Fails[0] += 1
        if self.Fails[0] == self.Fails[1] // 2: self.HandleInput('h')
        if self.Fails[0] == self.Fails[1]:
            self.Display.Display('!/ERROR @/br@/fwExiting Due To Fail Count...')
            self.Status = False
        if self.Fails[2] == False:
            self.Display.Display('!/ERROR @/br@/fwExiting Due To FailSafe Being False...')
            self.Status = False
    # Mount Banner File
    def MountBannerFile(self,File):
        if os.path.isfile(str(File)) == True:
            Text = open(str(File)).read().split('\n')
            RECD = None
            LINE = {}
            CONV = {}
            # We Open A Banner Via [0] Being @ >> "@ BANNER_NAME" | RECD = str(BANNER_NAME),LINE[str(BANNER_NAME)=[]
            # We Catch Operand For Text Conversion Inside Of Parser Via '@' >> "@ CHR APPENDCOLOR" | CONV[str(CHR)]=str(APPENDCOLOR)
            # ^ Everything A Object Inside Of CONV Is Cought We Append CONV[CHR]
            # Lines Are Recorded In Via [0] ">" >> ">LINE..." | LINE[RECD].append(LINE)
            # We Close When We Hit @ END
            for line in Text:
                if len(str(line)) == 0: continue
                if str(line[0])   == str('@') and RECD == None:
                    if str(' ') in str(line):
                        line = line.split(' ')[1]
                        if len(line) != 0:
                            RECD = str(line)
                            LINE[str(line)] = []
                        else: continue
                    else: print('Ignored Line: {} Due To No Space'.format(str(line)));continue
                elif str(line[0]) == str('@') and RECD != None:
                    if str(' ') in line:
                        line = line.split(' ')
                        if len(line[1:]) == 2:
                            if len(line[1]) == 1: CONV[str(line[1])]=str(line[2])
                            elif len(line[1]) == 2 and line[1] == '%s': CONV[str(' ')]=str(line[2])
                            else: print('Ignored Line: {} Due To Length> or <1'.format(str(line)));continue
                        elif line[1] == str('END'):
                            RECD = None;CONV={}
                        else: print('Ignored Line: {} Due To Invalid Arugments'.format(str(line)));continue
                    else: print('Ignored Line: {} Due To No Space Implement'.format(str(line)));continue
                elif str(line[0]) == '>' and RECD != None:
                    line = str(line[1:])
                    for c in CONV:
                        if str(c) in str(line): line = line.replace(str(c),str(CONV[c]+str(c)))
                    LINE[str(RECD)].append(str(line))
            for Banner in LINE:
                Banner_Text = ''
                for L in LINE[Banner]: Banner_Text+='\n'+str(L)
                self.Display.Message_Index[str(Banner)]=str(Banner_Text)
################################################################################
def PreOps():
    if len(sys.argv[1:]) == 0:
        App = Application()
        App.Start()
    else:
        Flags = {'Debugging':False,'FailSafe':True,'Termux':False,'Execute':[],'Banner':'Banner_LowLevel_00'}
        Skip  = 0
        for Arg in sys.argv[1:]:
            if Skip != 0:
                Skip -= 1
                continue
            if Arg in ['d','D','debug','Debug']  : Flags['Debugging'] = True
            elif Arg in ['f','F','fail','Fail']    : Flags['FailSafe']  = True
            elif Arg in ['t','T','termux','Termux']: Flags['Termux']    = True
            elif Arg in ['b','B','banner','Banner']  :
                Flags['Banner']    = sys.argv[sys.argv[1:].index(Arg)+2]
                Skip = 2
                continue
            if Arg in ['e','E','execute','Execute']: Flags['Execute'] =sys.argv[sys.argv.index(Arg):];break
        for F in Flags:print('(Al13N 3.5.0) (Setting) {} | {}'.format(str(F),str(Flags[F])))
        App = Application(IsTermux=Flags['Termux'],BannerT=Flags['Banner'])
        App.Fails[2] = Flags['FailSafe']
        App.Debug    = Flags['Debugging']
        App.Start(Que=Flags['Execute'][1:])
if __name__ == '__main__':
    PreOps()
    sys.exit(1)
