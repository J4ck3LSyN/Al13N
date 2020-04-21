import Al13N3475 as Brain
import os,sys,time,random
import readline

class Circuit:
    def __init__(self,KEY=(0x66,0x6,0x123456789,0x99,0x9),COF=(0x66,0x6,0x987654321,0x99,0x9),HEADER='Headers.aln',PREOP=[],LOGGING=False,DEBUGGING=False,FAILSAFE=True):
        self.Mode               = 0                           # Interpreter Mode
        self.Stat               = True                        # Current Status
        self.Que                = PREOP                       # Current Operation Que
        self.Brain_Memory       = Brain.Al13N3475(KEY,COF)    # Current Brain Handler
        self.Usage              = {
                                    'h|H|help|Help|HELP':['Displays This Help Message'],
                                    'q|Q|quit|Quit|QUIT':['Exits UFO 1.0.0'],
                                    's|S|sett|Sett|SETT':['Configures Internal Settings',
                                                          '----------------------------------------------------------',
                                                          'Takes 2 Arguments: s TARGET VALUE',
                                                          'Targets:',
                                                          '    lg  t/f          | Logging Operation',
                                                          '    db  t/f          | Debugging Operaion',
                                                          '    fs  t/f          | Fail Safe Operation',
                                                          '    sg  str          | Configures SegmentID To str'],
                                    'i|I|info|Info|INFO':['Fetches Info In Internal Settings',
                                                          '----------------------------------------------------------',
                                                          'Takes 1 Arguments As Seperated Values <Location>-<Target>',
                                                          'Locations-Targets:',
                                                          '    m-k              | Memory Key',
                                                          '    m-c              | Memory CoF',
                                                          '    m-r              | Memory Registers',
                                                          '    m-rs             | Memory Register Segments',
                                                          '    d-m              | Display Message Keys',
                                                          '    d-h              | Display Current Header',
                                                          '    s-l              | Current Logs And Logging Setting'],
                                    '@|EXECUTE'         :['Executing Locations',
                                                          '----------------------------------------------------------',
                                                          '<Register>@<Segment> Outputs Value',
                                                          '<Register>@<*/---->  Executes Entire Register'],
                                    'Al13N.Neuro|Module-Al13N':[
                                                            'Internal Writing And Handling For Operations...',
                                                            'After Using "new" OpKeys Can Be Called Directly One Being',
                                                            '(Al13N(3.4.75)',
                                                            '(Al13N(3.4.75) SIGNAL MODE IN IN ...',
                                                            '----------------------------------------------------------',
                                                            'OpKey: Al13N.Neuro',
                                                            'Neuro.OpMount(Arguments) -> For Signal Handling',
                                                            '  [0]                  -> Root',
                                                            '  [1:]                 -> Args',
                                                            '  Roots:',
                                                            '      0,l,L,logic MODE OPERAND INPUT VALUE',
                                                            '          Operand',
                                                            '          -------',
                                                            '          ==',
                                                            '          !=',
                                                            '          >',
                                                            '          <',
                                                            '          !',
                                                            '          $',
                                                            '      1,t,Y,type  MODE INPUT VALUE',
                                                            '           Input',
                                                            '          -------',
                                                            '          i',
                                                            '          s',
                                                            '          l',
                                                            '          b',
                                                            '          d',
                                                            '          f',
                                                            '          t',
                                                            '      2,s,S,string MODE OPERAND INPUT VALUE',
                                                            '          /',
                                                            '          ;',
                                                            '          +',
                                                            '          v',
                                                            '      3,i,I,integer MODE OPERAND INPUT VALUE',
                                                            '          +',
                                                            '          -',
                                                            '          /',
                                                            '          @',
                                                            '          ^',
                                                            '          v',
                                                            '      --------------------------------------',
                                                            '      4,~,list MODE OPERAND INPUT VALUE',
                                                            '          +',
                                                            '          %',
                                                            '          ^',
                                                            '          $',
                                                            '          v',
                                                            'Neuro.Logic (Logical Operations)',
                                                            'Neuro.Logic.Operate(Mode,Operator,Input,Value)',
                                                            'Mode: (0:Single,1:Multiple(Input Must Be Tuple))',
                                                            'Operator:',
                                                            '      ==  -> Equal To     (I==V       :True)',
                                                            '      !=  -> Not Equal    (I!=V       :True)',
                                                            '      <   -> Less Than    (I<V        :True)',
                                                            '      >   -> Greater Than (I>V        :True)',
                                                            '      !   -> In           (I in V     :True)',
                                                            '      $   -> Not In       (I not in V :True)',
                                                            '      --------------------------------------',
                                                            'Neuro.Type.Operate(Mode,Input,Value)',
                                                            '      Mode: (0:Single,1:Multiple(I Must Be Tuple))',
                                                            '      Operands:',
                                                            '          i   -> int',
                                                            '          s   -> str',
                                                            '          l   -> list',
                                                            '          b   -> bool',
                                                            '          f   -> function',
                                                            '          d   -> dict',
                                                            '          t   -> tuple',
                                                            '          --------------------------------------',
                                                            'Neuro.Variables',
                                                            'Neuro.Variables.String.Operate(Mode,Operand,I,V)',
                                                            '          Mode: (0:single,1:multiple(I Must Be Tuple))',
                                                            '          Operands:',
                                                            '              / -> split',
                                                            '              ; -> strip',
                                                            '              + -> append',
                                                            '              v -> value',
                                                            '              ----------------------------------',
                                                            'Neuro.Variables.Integer.Operate(Mode,Operand,I,V)',
                                                            '          Mode: (0:single,1:multiple(I Must Be Tuple))',
                                                            '          Operands:',
                                                            '              + -> add',
                                                            '              - -> sub',
                                                            '              / -> div',
                                                            '              @ -> exp',
                                                            '              ^ -> xor',
                                                            '              v -> value',
                                                            '              ----------------------------------',
                                                            'Neuro.Variables.List.Operate(Mode,Operand,I,V)',
                                                            '          Mode: (0:single,1:multiple(V Must Be Tuple))',
                                                            '          Operands:',
                                                            '              + -> append',
                                                            '              % -> index',
                                                            '              ^ -> add',
                                                            '              $ -> pull (V Must Be Tuple With 2 Ints [int:int])',
                                                            '              v -> value',
                                                            '              ----------------------------------']}
        ########################################################################
        self.Brain_Display      = Brain.Al13N3475.Display()   # Current Display Handler
        self.Brain_Display.__readFile__(str(HEADER))          # Current Configuration For Displays
        self.Brain_Display_MSG  = '@/fw(Al@/fg13@/fwN @/fy3@/fw.@/fr4@/fw.@/fm7@/fc5@/fw) @/fg->@/fw@/sb ' # Interpreter Internal Header Display
        self.Brain_Display_ERR  = str(self.Brain_Display_MSG)+str('[@/brERROR@/b0] -> ')                   # Interpreter Internal Error Display
        self.Brain_Display_UIN  = '(Al13N 3.4.75 ) ->'        # Interpreter Internal User-Input Display
        self.Brain_Display_HDR  = str(self.Brain_Display_MSG)
        ### If Our Internal Values Are Set To "Headers.aln" Than We Are Going To Append Our Header To One From There ###
        if HEADER == str('Headers.aln'): self.Brain_Display_HDR = '!/Conf.Banner_Advanced_Basic'
        ########################################################################
        self.Logging            = [LOGGING,[]]
        self.Debugging          = DEBUGGING
        self.FailSafe           = FAILSAFE
        self.Fails              = [0,10]
        self.Targets            = ['',[],0]
        ########################################################################
        self.Brain_Display.Display(str(self.Brain_Display_MSG)+' Logging: {} Debugging: {} FailSafe: {}'.format(str(self.Logging),str(self.Debugging),str(self.FailSafe)))
        ExitStatus              = self.Start()
    ############################################################################
    # Logging
    def __pipe__(self,Operation,Message):
        MessageToAppend = str('[DEBUGGER] Al13N 3.4.75 (UFO 1.0.0 ( Circuit.__pipe__({},{}) ) ) @ {}').format(str(Operation),str(Message),str(time.asctime()))
        if self.Logging[0] == True: self.Logging[1].append(str(MessageToAppend))
        if self.Debugging  == True: self.Brain_Display.Display(str(self.Brain_Display_MSG)+str(MessageToAppend))
    ############################################################################
    # Loop0
    def Start(self):
        self.__pipe__('Start()','Triggered To Start While Loop Off Internal "self.Stat" & "self."')
        self.Brain_Display.Display(str(self.Brain_Display_HDR))
        while self.Stat == True and self.Fails[0] < self.Fails[1]:
            # Handle Que If Need Be
            if len(self.Que) != 0:
                for Command in self.Que: self.Process(str(Command))
                self.Que      = []
            # If We Are Mode 0 {
            try:
                if self.Mode        == 0:
                    Prompt           = str(self.Brain_Display_UIN)+' (Command-Control) ({}:{}) -> '.format(str(self.Fails[0]),str(self.Fails[1]))
                    User_Input       = str(input(Prompt))
                    self.__pipe__('Start()','User-Input: '+str(User_Input))
                    if len(User_Input) == 0:
                        self.Brain_Display.Display(str(self.Brain_Display_ERR)+' Expected A Value On Input Got None Use @/frhelp@/fw For Help')
                        self.Fails[0] += 1
                    else: self.Process(str(User_Input))
                elif self.Mode      == 1:
                    Prompt           = str(self.Brain_Display_UIN)+' (Memory-Handling) ({}:{}) [{}:{}]'.format(str(self.Fails[0]),str(self.Fails[1]),str(self.Targets[0]),str(self.Targets[1][self.Targets[2]]))
                    Prompt          += str(' -> ')
                    User_Input       = str(input(Prompt))
                    if len(User_Input) == 0:
                        if self.Targets[1][self.Targets[2]] >= self.Targets[1][len(self.Targets[1])-1]: self.Brain_Display.Display(str(self.Brain_Display_ERR)+' Hit Max Of Registry Scope')
                        else: self.Targets[2]+=1
                    else: self.Process(str(User_Input))
            except KeyboardInterrupt:
                if self.Mode in [1]:
                    self.Mode -= 1
                    continue
                self.Brain_Display.Display(str(self.Brain_Display_ERR)+' KeyboardInterrupt')
                self.Fails[0] += 1
                if self.FailSafe == False: break
            except EOFError:
                self.Brain_Display.Display(str(self.Brain_Display_ERR)+' EOF-ERROR')
                self.Fails[0] += 1
                if self.FailSafe == False: break
            except Exception as E:
                self.Brain_Display.Display(str(self.Brain_Display_ERR)+' Exception: '+str(E))
                self.Fails[0] += 1
                if self.FailSafe == False: break
        # }
        # If We Exited With Fail Errors Print For User Info
        if self.Fails[0] >= self.Fails[1] or self.FailSafe == False:
            self.Brain_Display.Display(str(self.Brain_Display_ERR)+'Broke Due To Amount Of Fails.. Or FailSafe Is False')
            return 0
    ############################################################################
    # Command Handler
    def Process(self,Command):
        # Seperate Command Via ;
        if str(';') in str(Command):Command_Tree = Command.split(';')
        else:Command_Tree = [str(Command)]
        self.__pipe__('Process('+str(Command)+')',"Called To Execute Command Converted To "+str(Command_Tree))
        ### Global Command Calls ###
        for CMD in Command_Tree:
            # 1 Step Commands (Global)
            if str(CMD) in ['h','H','help','Help','HELP']: self.ShowUsage()
            elif str(CMD) in ['q','Q','quit','Quit','QUIT']: self.Stat = False
            elif str(CMD) in self.Brain_Memory.Registry:
                self.Brain_Memory.execute(CMD)
            elif str('@') in str(CMD) and str(' ') not in str(CMD):
                Tree = CMD.split('@')
                if str(Tree[0]) in self.Brain_Memory.Registry:
                    if str(Tree[1]) in self.Brain_Memory.Registry[Tree[0]]:
                        Output = self.Brain_Memory.execute(Tree[0],SegmentID=Tree[1])
                        self.Brain_Display.Display(str(self.Brain_Display_MSG)+'@/fgOutput From Operation@/fr '+str(CMD)+' @/fw->@/fy '+str(Output))
                    elif str(Tree[1]) in ['*','----']:
                        Output = self.Brain_Memory.execute(Tree[0])
                        for Line in Output: self.Brain_Display.Display(str(self.Brain_Display_MSG)+' ('+str(CMD)+') -> '+str(Line))
            # Multi Step Commands (Global)
            elif str(' ') in str(CMD):
                CMD_Tree = CMD.split(' ')
                # <help> <Command>
                if str(CMD_Tree[0]) in ['h','H','help','Help','HELP']                              : self.ShowUsage(Key=str(CMD_Tree[1]))
                # <Mode 1 Input For Writing Operations >
                elif str(CMD_Tree[0]) in self.Brain_Memory.OpKeys and self.Mode == 1:
                    Index = 1
                    for C in CMD_Tree[1:]:
                        if str(',') in str(C): CMD_Tree[Index]=C.split(',')
                        Index += 1
                    self.Brain_Memory.write(str(self.Targets[0]),str(self.Targets[1][self.Targets[2]]),CMD_Tree[0],CMD_Tree[1:])
                    self.Targets[2] += 1
                # <Sett> <Target> <Value>
                elif str(CMD_Tree[0]) in ['s','S','sett','Sett','SETT','setting','Setting','SETTING']:
                    if len(CMD_Tree[1:]) == 2:
                        # DB
                        if CMD_Tree[1]   in ['db','DB','debugging']:
                            if CMD_Tree[2] in ['0','t','T','true','True']    : self.Debugging  = True
                            elif CMD_Tree[2] in ['1','f','F','false','False']: self.Debugging  = False
                        # LG
                        elif CMD_Tree[1] in ['lg','LG','logging']:
                            if CMD_Tree[2] in ['0','t','T','true','True']    : self.Logging[0] = True
                            elif CMD_Tree[2] in ['1','f','F','false','False']: self.Logging[0] = False
                        # FS
                        elif CMD_Tree[1] in ['fs','FS','failsafe','FailSafe']:
                            if CMD_Tree[2] in ['0','t','T','true','True']    : self.FailSafe   = True
                            elif CMD_Tree[2] in ['1','f','F','false','False']: self.FailSafe   = False
                        # SG
                        elif CMD_Tree[1] in ['sg','SG','segment','Segment'] and self.Targets[0] != str('') and str(CMD_Tree[2]) in self.Targets[1]: self.Targets[2] = self.Targets[1].index(CMD_Tree[2])
                        else:
                            self.Brain_Display.Display(str(self.Brain_Display_ERR)+' Invalid Operand "'+str(CMD_Tree[2])+'" For "'+str(CMD_Tree[1])+'"')
                            self.Fails[0] += 1
                # <info> <target>
                elif str(CMD_Tree[0]) in ['i','I','info','Info','INFO','information','Information','INFORMATION']:
                    if len(CMD_Tree[1:]) >= 1:
                        # Memory Key
                        if CMD_Tree[1] in ['m-k','M-K','memory-key', 'Memory-Key'] : self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(Key) : '+str(self.Brain_Memory.KEY))
                        # Memory Register
                        elif CMD_Tree[1] in ['m-r','M-R','memory-reg','Memory-Reg']:
                            if len(self.Brain_Memory.Registry) != 0:
                                for RegisterID in self.Brain_Memory.Registry: self.Brain_Display.Display(str(self.Brain_Display_MSG)+'Registry ID  : '+str(RegisterID)+' With Length '+str(len(self.Brain_Memory.Registry[RegisterID])))
                            else: self.Brain_Display.Display(str(self.Brain_Display_MSG)+' No Items Exist In Memory')
                        # Memory Register Segments
                        elif CMD_Tree[1] in ['m-rs','M-RS','memory-regsegments','Memory-RegSegments']:
                            if len(CMD_Tree[1:]) == 2:
                                if str(CMD_Tree[2]) in self.Brain_Memory.Registry:
                                    self.Brain_Display.Display(str(self.Brain_Display_MSG)+'Showing @/frSegments@/fw For @/fg'+str(CMD_Tree[2]))
                                    for Segment in self.Brain_Memory.Registry[CMD_Tree[2]]:
                                        Message  = str('@/fr\t')+str(Segment)
                                        Message += str('@/fw\t')+str(self.Brain_Memory.Registry[CMD_Tree[2]][Segment])
                                        self.Brain_Display.Display(str(Message))
                            # [NOTE: Need To Build Fail Catch...]
                        # Memory CoF
                        elif CMD_Tree[1] in ['m-c','M-C','memory-cof', 'Memory-CoF'] : self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(CoF) : '+str(self.Brain_Memory.COF))
                        # Display Message
                        elif CMD_Tree[1] in ['d-m','D-M','display-msg','Display-MSG']:
                            for MID in self.Brain_Display.Message_Index: self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(Message_Index) : '+str(MID))
                        # Display Header
                        elif CMD_Tree[1] in ['d-h','D-H','display-hdr','Display-HDR']: self.Brain_Display.Display(str(self.Brain_Display_HDR))
                        # Logging Configuration
                        elif CMD_Tree[1] in ['s-l','S-L','setting-log','Setting-LOG']:
                            self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(Setting) Log: '+str(self.Logging[0]))
                            if len(self.Logging[1]) != 0:
                                for Line in self.Logging[1]: self.Brain_Display.Display(str(self.Brain_Display_MSG)+' (MSG) : '+str(Line))
                        # Current Mode
                        elif CMD_Tree[1] in ['s-m','S-M','setting-mode','Setting-MODE']: self.Brain_Display.Display(str(self.Brain_Display_MSG)+' Current Mode '+str(self.Mode))
                    else:
                        self.Brain_Display.Brain(str(self.Brain_Display_ERR)+' Invalid Operand "'+str(CMD[1])+'"')
                        self.Fails[0] += 1
                elif str(CMD_Tree[0]) in ['+','n','N','new','New','NEW'] and len(CMD_Tree[1:]) == 6:
                    try:
                        Conversion = []
                        for Command in CMD_Tree[1:]:
                            Conversion.append(int(str('0x'+Command),16))
                        self.Targets[0]    = self.Brain_Memory.new((Conversion[0],Conversion[1],Conversion[2],Conversion[3],Conversion[4]),Conversion[5])
                        for Segments in self.Brain_Memory.Registry[self.Targets[0]]: self.Targets[1].append(Segments)
                        self.Targets[2]    = 0
                        self.Brain_Display.Display(str(self.Brain_Display_MSG)+' Generated Register With ID @/fr'+str(self.Targets[0])+str('@/fw With ')+str(len(self.Targets[1])))
                        self.Brain_Display.Display(str(self.Brain_Display_MSG)+' Converting Mode To 1 For Writing And Further Handling... Level 0 Operations Will Still Work')
                        self.Mode       = 1
                    except Exception as e:
                        self.Fails[0]+=1
                        self.Brain_Display.Display(str(self.Brain_Display_MSG)+' Exception: '+str(e))
    ############################################################################
    # Usage Handler
    def ShowUsage(self,Key=None):
        self.__pipe__('ShowUsage('+str(Key)+')',"For Showing Command Information, If None Than Sort Through Them All")
        if Key == None:
            for Key in self.Usage: self.ShowUsage(str(Key))
        else:
            Targets = []
            for Keys in self.Usage:
                if str(Key) in Keys.split('|') or str(Key) == str(Keys): Targets.append(Keys)
            for Keys in Targets:
                self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(@/fgUsage@/fw) Command: @/fw'+str(Keys.replace('|',', '))+str(' {'))
                for line in self.Usage[Keys]: self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(@/fbUsage@/fw) Command: @/fg'+str(line))
                self.Brain_Display.Display(str(self.Brain_Display_MSG)+'(@/fgUsage@/fw)         }')

def DisplayUsage():
    print('''
>> Al13N 3.4.75 (UFO 1.0.0)
>> h, --help                  Displays This Help Message
>> d, --header                Takes 1 Arg For Header Configuration File
>> l, --logging               Configures Internal Logging
>> v, --debugging             Configures Debugging Information Display
>> k, --key                   Takes 5 Args As hex Values Without "00"
--                            "0f" -> "0x0f" | 00 00 00 00 00
>> f, --failsafe              Sets Internal FailSafe Flag To False
>> c, --characteroffset       Same Operations As k
>> e, --execute               Takes Every Following Command For PreExecution
>> -------------------------------------------------------------------------
>> Usage: python3 UFO100.py [ARG] [ARG] [ARG] ...
>> Usage: python3 UFO100.py v l f e + 03 04 05 06 07 0f
.. Above Sets Configurations: debugging -> True, Logging -> True,
.. FailSafe -> False, Execute -> '+ 03 04 05 06 07 0f'
.. [NOTE: e Must Be The Last Argument Since All Following Args Are Sent]
>> -------------------------------------------------------------------------
''')
def Run():
    flags = {'headers':'Headers.aln','execute':[],'key':(0x66,0x6,0x123456789,0x99,0x9),'cof':(0x66,0x6,0x987654321,0x99,0x9),'v':False,'l':False,'f':True}
    Skip  = False
    Stage = 0
    for Arguments in sys.argv:
        # If True We Continue
        if Skip == True:
            Skip = False
            continue
        # If We Are Above 0 Continue Until We Hit 0
        if Stage != 0:
            while Stage != 0:
                Stage = Stage - 1
                Skip = True
        # Display Usage
        if Arguments in ['h','--help']  :
            DisplayUsage()
            sys.exit(1)
        # Header Configuration File
        if Arguments in ['d','--header']:
            try:
                if os.path.isfile(str(sys.argv[sys.argv.index(Arguments)+1])) == True:
                    flags['headers'] = str(sys.argv[sys.argv.index(Arguments)+1])
                    Skip = True
                else:
                    print('[ERROR] Expected Valid File For Input On Arugment '+str(sys.argv[sys.argv.index(Arguments)+1]))
            except:
                print('[ERROR] Expected Following Entry On "d, --header" Input '+str(sys.argv))
                Skip = True
                continue
        # Key Handling
        if Arguments in ['k','--key'] and len(sys.argv[sys.argv.index(Arguments)+1:]) >= 5:
            Args = sys.argv[sys.argv.index(Arguments)+1:sys.argv.index(Arguments)+6]
            Stage = 5
            Conv = []
            for A in Args:
                try: Conv.append(int(str('0x'+A),16))
                except:
                    print('[ERROR] Expected A Valid Hex() Conversion... Failed...'+str(Conv))
                    break
            if len(Conv) == 5: flags['key']=(Conv[0],Conv[1],Conv[2],Conv[3],Conv[4])
            else: print('[ERROR] Bounce Out Of Operation...')
        # cof Handling
        if Arguments in ['cof','--characteroffset'] and len(sys.argv[sys.argv.index(Arguments)+1:]) >= 5:
            Args = sys.argv[sys.argv.index(Arguments)+1:sys.argv.index(Arguments)+6]
            Stage = 5
            Conv = []
            for A in Args:
                try: Conv.append(int(str('0x'+A),16))
                except:
                    print('[ERROR] Expected A Valid Hex() Conversion... Failed...'+str(Conv))
                    break
            if len(Conv) == 5: flags['cof']=(Conv[0],Conv[1],Conv[2],Conv[3],Conv[4])
            else: print('[ERROR] Bounce Out Of Operation...')
        # debugging Handling
        if Arguments in ['v','--debugging']: flags['v'] = True
        # Logging Handling
        if Arguments in ['l','--logging']  :flags['l']  = True
        # FailSafe Handling
        if Arguments in ['f','--failsafe'] :flags['f']  = False
        # interpreter Commands
        if Arguments in ['e','--execute']  :
            Extended_Commands = sys.argv[sys.argv.index(Arguments)+1:]
            Commands          = ''
            for C in Extended_Commands:
                if len(Commands) == 0: Commands = C
                else: Commands += str(' ')+str(C)
            flags['execute'] = [str(Commands)]
            ### We Capture Everything Post This Call So We Break ###
            break
    for Flag in flags: print('(Al13N 3.4.75 ) -> '+str(time.asctime())+' Setting ({}) = ({})'.format(str(Flag),str(flags[Flag])))
    Interpreter = Circuit(KEY=flags['key'],COF=flags['cof'],HEADER=flags['headers'],PREOP=flags['execute'],LOGGING=flags['l'],DEBUGGING=flags['v'],FAILSAFE=flags['f'])
    if Interpreter == 0: sys.exit(1)
    if Interpreter == 1:
        Interpreter.Stat = True
        Interpreter.Run()
if __name__ == '__main__':
    print('Starting Al13N 3.4.75 Interpreter Functions (UFO 1.0.0) @ '+str(time.asctime()))
    print('Current Working Directory: '+str(os.getcwd()))
    Run()
