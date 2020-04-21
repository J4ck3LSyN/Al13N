NAME = 'Display Hanler'
import sys
try:
    import colorama
    from   colorama import Fore  as C_F
    from   colorama import Back  as C_B
    from   colorama import Style as C_S
    colorama.init(autoreset=True)
except NameError as N:
    print('[!] This Module Is Dependent On The colorama(python3) Module Use "pip3 install colorama" To Install')
    sys.exit(1)
except:
    print('[?] Unkown Error!!!!')
    sys.exit(1)

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

################################################################################
def Al13N_INFO(Version):
    return [ ['00','display','Display','DISPLAY'],['Used For TextToDisplay Functions'],'']
################################################################################
def Al13N_HooK(Version,*Args):
    print(Version,Args)
