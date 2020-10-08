try:
    import colorama
    from   colorama import Fore   as F
    from   colorama import Back   as B
    from   colorama import Style  as S
    colorama.init(autoreset=True)
except ImportError as I: Exception('Need To Install Colorama Use "pip3 install colorama"')
################################################################################

class Pallet:
    def __init__(self):
        self.PalletKeys = [{

            # Colors
            'fG':F.GREEN   ,'bG':B.GREEN,
            'fB':F.BLUE    ,'bB':B.BLUE,
            'fY':F.YELLOW  ,'bY':B.YELLOW,
            'fM':F.MAGENTA ,'bM':B.MAGENTA,
            'fW':F.WHITE   ,'bW':B.WHITE,
            'fC':F.CYAN    ,'bC':B.CYAN,
            'f0':F.BLACK   ,'b0':B.BLACK,
            'fR':F.RED     ,'bR':B.RED,
            ####################################################################
            # Style
            'sB':S.BRIGHT  ,'sN':S.NORMAL,
            'sD':S.DIM     ,'sR':S.RESET_ALL,
            'f1':F.RESET   ,'b1':B.RESET
            },
            [
            '[!','!]',
            '[?','?]'
            # [0][0] Opening Key ( [1][0][0]+str(KEY)+[1][0][1] )
            ],
            {},
            # Message Index [2]
            {}
            # Character Conversion
            ]
        # [0] | Colour Pallet
        # [1] | [ str, str ]
        # [2] | Message Index
        # [3] | Character Conversion
        self.CCOD = False
        # Convert Characters On Display
    # Message Index Append
    def MessageIndex_Append(self,ID,Message):
        if str(ID) not in self.PalletKeys[2]: self.PalletKeys[2][str(ID)]=str(Message)
        else: raise self.PalletException('MessageIndex_Append(...)','Expected A Non-Existant ID')
    # Character Conversion Append
    def CharacterConversion_Append(self,Character,KEY_REPLACE):
        if len(str(Character)) == 1:
            if str(KEY_REPLACE) in self.PalletKeys[0]: self.PalletKeys[3][str(Character)]=self.PalletKeys[0][str(KEY_REPLACE)]
            else: raise self.PalletException('CharacterConversion_Append(...)','Invalid Key Sent For Replace')
        else: raise self.PalletException('CharacterConversion_Append(...)','Invalid Length For Replace Expected Length Of 1')
    # Discover Messages
    def FindMessage(self,Message):
        for Messages in self.PalletKeys[2]:
            HotKey = str(self.PalletKeys[1][2])+str(Messages)+str(self.PalletKeys[1][3])
            # ^ Compile Key
            if str(HotKey) in str(Message):Message = Message.replace(str(HotKey),str(self.PalletKeys[2][Messages]))
        return str(Message)
    # Replace Targeted Character
    def TargetConvertCharacter(self,Message,Character,Convert,Close):
        if str(Character) in str(Message):
            if type(Convert) is list and type(Close) is list:
                Valid = True
                for Item in Convert:
                    if str(Item) not in self.PalletKeys[0]: Valid = False
                for Item in Close:
                    if str(Item) not in self.PalletKeys[0]: Valid = False
                if Valid == True:
                    Open = ''
                    End  = ''
                    for Object in Convert:
                        if len(Open) == 0: Open = str(self.PalletKeys[1][0])+str(Object)+str(self.PalletKeys[1][1])
                        else: Open += str(self.PalletKeys[1][0])+str(Object)+str(self.PalletKeys[1][1])
                    for Object in Close:
                        if len(End) == 0: End = str(self.PalletKeys[1][0])+str(Object)+str(self.PalletKeys[1][1])
                        else: End = str(self.PalletKeys[1][0])+str(Object)+str(self.PalletKeys[1][1])

                    Message = Message.replace(str(Character),str(Open)+str(Character)+str(End))
                    return Message
                else: raise self.PalletException('TargetConvertCharacter(...)','Valid Trigger Failed Was Not Good Key')
            else: raise self.PalletException('TargetConvertCharacter(...)','Input Arguments Where Noto list')
        else: raise self.PalletException('TargetConvertCharacter(...)','Character Wanted Does Not Exist In Message')
    # Discover Character Conversion
    def FindConvertedCharacter(self,Message):
        if self.CCOD == False: raise self.PalletException('FindConvertedCharacter(...)','Internal Configuration CCOF Is False')
        for Characters in self.PalletKeys[3]:Message= Message.replace(str(Characters),self.PalletKeys[3][Characters])
        return str(Message)
    # Discover Color Keys
    def FindColours(self,Message):
        for Colours in self.PalletKeys[0]:
            HotKey = str(self.PalletKeys[1][0])+str(Colours)+str(self.PalletKeys[1][1])
            if str(HotKey) in str(Message):Message=Message.replace(str(HotKey),str(self.PalletKeys[0][Colours]))
        return str(Message)
    # Remove Colour Mounts
    def RemoveCCOD_ID(self,ID):
        if str(ID) in self.PalletKeys[3]: del(self.PalletKeys[3][str(ID)])
        else: raise self.PalletException('RemoveCCOD_ID(...)','Invalid ID Sent')
    # Remove Message Mounts
    def RemoveMESG_ID(self,ID):
        if str(ID) in self.PalletKeys[2]: del(self.PalletKeys[2][str(ID)])
        else: raise selt.PalletException('RemoveMESG_ID(...)','Invalid ID Sent')
    # Display Operations
    def Display(self,Message):
        Message = str(self.FindMessage(Message))
        Message = str(self.FindColours(Message))
        if self.CCOD == True: Message = str(self.FindConvertedCharacter(Message))
        print(str(Message))
    def PalletException(self,Root,ExceptionMessage):
        ExceptionMessage = '['+str(Root)+'] '+str(ExceptionMessage);raise Exception(str(ExceptionMessage))

#######################################################################################################################################################################################################
