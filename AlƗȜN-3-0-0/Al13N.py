### Verion 3.0.0
import os,time,sys
import hashlib
import subprocess
# Author  :: J4ck3lSyN
############################################################################
#                               Root    Object                             #
#$>----------------------------------------------------------------------<$#
#  Object                       |    Type    |                      Usage  #
#--------------------------------------------------------------------------#
# > __init__()                  |    func    | Triggered On Mount          #
# - self.Universe(dict)         |  variable  | Used For Central Memory     #
# - self.BiTMaP(list)           |  variable  | Used When Creating Galaxies #
# - self.SymUniverse            |  variable  | Used To Tie Entities        #
#--------------------------------------------------------------------------#
# > _ValidateLocation()         |    func    | For Validating Locations    #
# -                             |  --------  | Takes 1 Input As list(IO)   #
# -                             |  --------  | Expects 1 Entry As str      #
# -                             |  --------  | ([str]) Will Return         #
# -                             |  --------  | list:                       #
# -                             |  --------  | [0] - bool (Existance)      #
# -                             |  --------  | [1] - str  (Location)       #
# -                             |  --------  | [2] - list (Tree For Handle)#
# -                             |  --------  | --------------------------- #
# > _GenerateGalaxy_            |    func    | For Generating Galaxies     #
# -                             |  --------  | Takes 1 Input As list(IO)   #
# -                             |  --------  | Expects 2 Entries As str,int#
# -                             |  --------  | ([str,int]) If str Exists   #
# -                             |  --------  | Than It Will Fail If Not    #
# -                             |  --------  | A Galaxy Will Be Generated  #
# -                             |  --------  | Inside Of:                  #
# -                             |  --------  |  self.Universe              #
# -                             |  --------  | int Will Be The Amount Of   #
# -                             |  --------  | Dimensions That Will Be     #
# -                             |  --------  | Generated All With BiTMaPs  #
# -                             |  --------  | s = str                     #
# -                             |  --------  | for i in range(0,int)       #
# -                             |  --------  |  i Gets Ran Through hex(int)#
# -                             |  --------  |  Generates i Inside Of      #
# -                             |  --------  |   self.Universe[str]        #
# -                             |  --------  |   for b in self.BiTMaP      #
# -                             |  --------  |    Generates b Inside Of    #
# -                             |  --------  |    self.Universe[str][i]    #
# -                             |  --------  |    As list.                 #
# -                             |  --------  | --------------------------- #
# > _WriteToBiT_                |    func    | For Writing To Generated    #
# -                             |  --------  | Galaxies                    #
# -                             |  --------  | Takes 1 Input As list(IO)   #
# -                             |  --------  | Expects 3 Entites As str,str#
# -                             |  --------  | ,list. [0] Being The        #
# -                             |  --------  | Target Location Split By '.'#
# -                             |  --------  | Must Be Valid By            #
# -                             |  --------  | self._ValidateLocation_     #
# -                             |  --------  | [1] Being The Type To Write #
# -                             |  --------  | [2] Being The Inputs For [1]#
# -                             |  --------  | --------------------------- #
# > _GenerateSymTie_            |    func    | For Generating Symbloic Ties#
# -                             |  --------  | Takes 1 Input As list(IO)   #
# -                             |  --------  | Expects 2 Entities As str,  #
# -                             |  --------  | str.                        #
# -                             |  --------  | [0] Being The Tie String    #
# -                             |  --------  | [1] Being The Target        #
# -                             |  --------  | Location                    #
# -                             |  --------  | --------------------------- #
# > _HandleBiT_                 |    func    | For Handling BiTs           #
# -                             |  --------  | Takes 1 Input As list       #
# -                             |  --------  | Expects 1 Entity As str     #
# -                             |  --------  | [0] Being The BiT Location  #
# -                             |  --------  | --------------------------- #
class Root:
    def __init__(self,WithGalaxies=None):
        # Configure Memory
        self.Universe    = {}
        # Configure Symbolic Ties
        self.SymUniverse = {}
        # ASCII Handling
        self.PipeHandle  = {
            'SpawnGalaxy':'>>',    # When Spawning A Galaxy
            'WriteBiT'   :'->',    # For Writing To A Location
            'CloseLine'  :'||',    # For Closing A Line Off
            'Seperator'  :'|>',    # For Seperating Things
            'TagBitToSym':'!>',    # For Tagging Existing BiTs To Symbolic Links
            'OpenRecord' :'|/',    # For Recording Mutliple Lines
            'NewIndent'  :'- ',    # For Handling Input As A Record
            'CloseRecord':'/|',    # For Closing The Record
            'CommentLine':'//'     # For Catching Comments
        }
        # Usage Index
        self.UsageIndex  = {
            '__init__':[
                'Description:',
                '----------------------------------------------------------',
                '> Called On Creation Takes 1 Argument',
                '- Al13N.Root()',
                '- Al13N.Root(WithGalaxies=[[str,int],...])',
                '----------------------------------------------------------',
                'Variables:',
                '----------------------------------------------------------',
                '+ self.Universe    dit                     Central Memory ',
                '+ self.SymUniverse dict                   Symbolic Memory ',
                '+ self.UsageIndex  dict                      Usage Memory ',
                '+ self.BiTMaP      list                     BiTMaP Memory ',
                '----------------------------------------------------------'
            ],
            '_GenerateGalaxy_':[
                'Description: For Generating Galaxies',
                '----------------------------------------------------------',
                '> Class Object Takes 1 Argument As list',
                '- Root._GenerateGalaxy_([str,int])',
                '----------------------------------------------------------',
                'Variables:',
                '----------------------------------------------------------',
                '< self.Universe[str](for hex(i) in range(0,int))(BiT)',
                '----------------------------------------------------------',
                'Memo:',
                '- [0] // ID For Mounting The Galaxy Under',
                '- [1] // Dimension Count',
                '----------------------------------------------------------'
            ],
            '_WriteToBiT_':[
                'Description: For Writing to BiTs Inside Of Galaxies',
                '----------------------------------------------------------',
                '> Class Object Takes 1 Argument As list',
                '- Root._WriteToBiT_([str,str,list])',
                '----------------------------------------------------------',
                'Variables:',
                '< self.Universe[str][hex(str[1])][str[2]]=[str,[value]]',
                '----------------------------------------------------------',
                'Memo:',
                '- [0] // ID For Writing To GALAXY.DIMENSION.BIT',
                '- [1] // Function To Write Under',
                '-- Functions:',
                '--  var_string,Var_String,VAR_STRING,v-s',
                '^-  String Variables [str]',
                '--  var_integer,Var_Integer,VAR_INTEGER,v-s',
                '^-  Integer Variable [int]',
                '--  var_list,Var_List,VAR_LIST,v-l',
                '^-  List Variable    [list]',
                '--  var_out,Var_Out,VAR_OUT,v-o',
                '^-  Output Variable  []',
                '--  fun_shl_surface,Fun_Shl_Surface,FUN_SHL_SURFACE,f-s-s',
                '^-  Surface Based Shell Actions [str] NOOUT',
                '--  fun_shl_subliminal,Fun_Shl_Subliminal,FUN_SHL_SUBLIMINAL,f-s-u',
                '^-  Subliminal Based Shell Actions [str] OUTPUT',
                '- [2] // Input For Functions',
                '----------------------------------------------------------'
            ],
            '_ValidateLocation_':[
                'Description: For Validating BiTMaP Locations',
                '----------------------------------------------------------',
                '> Class Objects Takes 1 Argument As list',
                '- Root._ValidateLocation_([str])',
                '----------------------------------------------------------',
                'Variables:',
                '< self.Universe[...]',
                '----------------------------------------------------------',
                'Memo:',
                '- [0] // Location To Find Seperates Based Off "."',
                '-- Returns A list [location,Tree,]'
            ]
        }
        # Configure Index
        self.BiTMaP      = [ # BitLen 37
            '00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000',
            '10000000', '10000001', '10000010', '10000100', '10001000', '10010000', '10100000',
            '11000000', '11000001', '11000010', '11000100', '11001000', '11010000',
            '11100000', '11100001', '11100010', '11100100', '11101000',
            '11110000', '11110001', '11110010', '11110100',
            '11111000', '11111001', '11111010',
            '11111100', '11111101',
            '11111110', '11111111' ]
        # Validate Galaxy Call
        if WithGalaxies != None:
            if type(WithGalaxies) is list:
                for Item in WithGalaxies:
                    if type(Item) is list:
                        if len(Item) is 2:
                            if type(Item[0]) is str and type(Item[1]) is int:
                                self._GenerateGalaxy_(Item)
                            else:
                                raise TypeError(str(type(Item[0]))+'/'+str(type(Item[1]))+' Expected str,int')
                        else:
                            raise ValueError(str(len(Item))+' Expected 2 Entities ')
                    else:
                        raise TypeError(str(type(Item))+' Expected list')
            else:
                raise TypeError(str(type(Item))+' Expected NoneType Or list')
    ############################################################################
    # Takes IO As list
    # [0] - str (Location)
    def _ValidateLocation_(self,IO):
        if type(IO) is list:
            Location = str(IO[0])
            if str('.') in str(Location):
                Tree = Location.split('.')
                if len(Tree) == 2:
                    if str(Tree[0]) in self.Universe:
                        if str(Tree[1]) in self.Universe[str(Tree[0])]:
                            return [True,Location,Tree]
                        else:
                            return [False,Location,Tree[1]]
                    else:
                        return [False,Location,Tree[0]]
                elif len(Tree) == 3:
                    if str(Tree[0]) in self.Universe:
                        if str(Tree[1]) in self.Universe[str(Tree[0])]:
                            if str(Tree[2]) in self.BiTMaP:
                                if str(Tree[2]) in self.Universe[str(Tree[0])][str(Tree[1])]:
                                    return [True,Location,Tree]
                                else:
                                    return [False,Location,Tree[2]]
                            else:
                                return [False,Location,self.BiTMaP]
                        else:
                            return [False,Location,Tree[1]]
                    else:
                        return [False,Location,Tree[0]]
                else:
                    return [False,Location,str(len(Tree))]
            else:
                if str(Location) in self.Universe:
                    return [True,Location,Location]
                else:
                    return [False,Location,Location]
        else:
            raise TypeError(str(type(IO))+' Expected list')
    ############################################################################
    # Takes IO As list
    # [0] - str (Location)
    # [1] - int (Dimension Count)
    def _GenerateGalaxy_(self,IO):
        if type(IO) is list:
            if len(IO) == 2:
                if type(IO[0]) is str and type(IO[1]) is int:
                    if self._ValidateLocation_([str(IO[0])])[0] == False:
                        if int(IO[1]) != 0 and int(IO[1]) < int(11111111):
                            self.Universe[str(IO[0])] = {}
                            for i in range(0,int(IO[1])):
                                h = str(hex(i))
                                self.Universe[str(IO[0])][str(h)] = {}
                                for b in self.BiTMaP:
                                    self.Universe[str(IO[0])][str(h)][str(b)]=[]
                        else:
                            raise ValueError(str(int(IO[1]))+' Got 0 For > 11111111')
                    else:
                        raise ValueError(str(IO[0])+' Exists')
                else:
                    raise TypeError(str(type(IO[0]))+'/'+str(type(IO[1]))+' Expected str/int')
            else:
                raise ValueError(str(len(IO))+' Expected 2 Entries')
        else:
            raise TypeError(str(type(IO))+' Expected list')
    ############################################################################
    # Takes IO As list
    # [0] - str TieEntity
    # [1] - str TargetLocation
    def _GenerateSymTie_(self,IO):
        if type(IO) is list:
            if len(IO) == 2:
                Identity = str(IO[0])
                Location = str(IO[1])
                if str(Identity) not in self.SimUniverse:
                    if self._ValidateLocation_([str(Location)])[0] == True:
                        Tree = self._ValidateLocation_([str(Location)])[2]
                        self.SimUniverse[str(Identity)] = [str(Location),Tree]
                    else:
                        raise ValueError(str(Location)+" Does'nt Exist")
                else:
                    raise ValueError(str(Identity)+' Already Exists As A Tie')
            else:
                raise ValueError(str(len(IO))+' Expected 2 Entities')
        else:
            raise TypeError(str(type(IO))+' Expected list')
    ############################################################################
    # Takes IO As list
    # [0] - str Location
    # [1] - str Type
    # [2] - list Type-Inputs
    def _WriteToBiT_(self,IO):
        # Validation
        if type(IO) is list:
            if len(IO) == 3:
                if type(IO[0]) is str and type(IO[1]) is str and type(IO[2]) is list:
                    # SimTie Capture
                    if str(IO[0]) in self.SymUniverse:
                        IO[0] = str(self.SymUniverse[IO[0]][0])
                    if self._ValidateLocation_([str(IO[0])])[0] == True:
                        # Capture Tree
                        Tree = self._ValidateLocation_([str(IO[0])])[2]
                        ### Variable Handling ###
                        if str(IO[1]) in ['var_string','Var_String','VAR_STRING','v-s']:
                            # Variable String
                            if len(IO[2]) == 1:
                                if type(IO[2][0]) is str:
                                    self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VARSTR',str(IO[2][0])]
                                    # Write String Variable To Bit
                                else:
                                    raise ValueError(str(type(IO[2]))+' Expected str')
                            else:
                                raise ValueError(str(len(IO[2]))+' Expected 1 Entity')
                        elif str(IO[1]) in ['var_integer','Var_Integer','VAR_INTEGER','v-i']:
                            # Variable Integer
                            if len(IO[2]) == 1:
                                if type(IO[2][0]) is int or str(IO[2][0]).isdigit() == True:
                                    self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VARINT',int(IO[2][0])]
                                    # Write Integer Variable To Bit
                                else:
                                    raise ValueError(str(type(IO[2]))+' Expected int')
                        elif str(IO[1]) in ['var_list','Var_List','VAR_LIST','v-l']:
                            # Variable List
                            if len(IO[2]) == 1:
                                if type(IO[2][0]) is list:
                                    self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VARLST',IO[2][0]]
                                    # Write List Variable To BiT
                                else:
                                    raise TypeError(str(type(IO[0][2]))+' Expected list')
                        elif str(IO[1]) in ['var_out','Var_Out','VAR_OUT','v-o']:
                            # Variable OUTPUT
                            if len(IO[2]) == 0:
                                self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['VAROUT',None]
                            else:
                                raise ValueError(str(len(IO[2]))+' Expected 0 Entites')
                        ### Shell Based Handling ###
                        elif str(IO[1]) in ['fun_shl_surface','Fun_Shl_Surface','FUN_SHL_SURFACE','f-s-s']:
                            # os.system Operation
                            if len(IO[2]) == 1:
                                if type(IO[2][0]) is str:
                                    self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['FUNSHL_Surface',str(IO[2][0])]
                                else:
                                    raise TypeError(str(IO[2][0])+' Expected str')
                            else:
                                raise ValueError(str(len(IO[2]))+' Expected 1 Entry')
                        elif str(IO[1]) in ['fun_shl_subliminal','Fun_Shl_Subliminal','FUN_SHL_SUBLIMINAL','f-s-u']:
                            # subprocess.Popen Operation
                            if len(IO[2]) == 1:
                                if type(IO[2][0]) is str:
                                    self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]=['FUNSHL_Subliminal',str(IO[2][0])]
                                else:
                                    raise TypeError(str(IO[2][0])+' Expected str')
                            else:
                                raise ValueError(str(len(IO[2]))+' Expected 1 Entry')
                        ### Logic Handling ###
                        else:
                            raise ValueError(str(IO[1])+' Expected Valid Entity')
                    else:
                        raise ValueError(str(IO[0])+' Invalid Location')
                else:
                    raise TypeError(str(IO)+' Expected str,str,list')
            else:
                raise ValueError(str(len(IO))+' Expected 3 Entities')
        else:
            raise TypeError(str(type(IO))+' Expected list')
    ############################################################################
    # Takes IO As list
    # [0] - str   // Location
    # Returns 4 Entries
    # [0] - Location
    # [1] - Tree
    # [2] - Stem
    # [3] - Value//Message
    def _HandleBiT_(self,IO):
        # Validate
        if type(IO) is list:
            if len(IO) == 1:
                Location      = str(IO[0])
                if str(Location) in self.SymUniverse:
                    Location = str(self.SymUniverse[Location][0])
                if self._ValidateLocation_([str(Location)])[0] == True:
                    # Vapture Tree And Stem
                    Tree = self._ValidateLocation_([str(Location)])[2]
                    Stem = self.Universe[str(Tree[0])][str(Tree[1])][str(Tree[2])]
                    if len(Stem) == 0:
                        # Not Configured BiT
                        return [str(Location),str(Tree),str(Valu),'Not-Configured']
                    else:
                        if str(Stem[0]) in ['VARSTR','VARINT','VARLST','VAROUT']:
                            # Variable BiT
                            return [str(Location),str(Tree),str(Stem),Stem[1]]
                        elif str(Stem[0]) == str('FUNSHL_Surface'):
                            # Shell Function Script os.system
                            Script = str(Stem[1])
                            Failed = False
                            Reason = None
                            try:
                                os.system(str(Script))
                            except Exception as e:
                                Failed = True
                                Reason = str(e)
                            finally:
                                if Failed == True:
                                    raise Exception(str(Reason)+' From '+str(Location))
                                else:
                                    return None
                        elif str(Stem[0]) == str('FUNSHL_Subliminal'):
                            # Shell Funtion Script subprocess.Popen
                            # Returns Output Value
                            Script = str(Stem[1])
                            Failed = False
                            Reason = None
                            Output = None
                            if str(' ') in str(Script):
                                STree = Script.split(' ')
                            else:
                                STree = [str(Script)]
                            try:
                                Output = subprocess.Popen(STree,stdout=subprocess.PIPE,shell=True)
                                Output = str(Output.stdout.read().decode('utf-8'))
                            except Exception as e:
                                Failed = True
                                Reason = str(e)
                            finally:
                                if Failed == True:
                                    raise Exception(str(e)+' From '+str(Location))
                                else:
                                    return Output
                        else:
                            raise ValueError(str(Stem[0])+' Invalid Operand')
                else:
                    raise ValueError(str(Location)+" Does'nt Exist")
            else:
                raise ValueError(str(len(IO))+' Expected 1 Entity')
        else:
            raise TypeError(str(type(IO))+' Expected list')
    ############################################################################
    ############################################################################
    # Takes IO As list
    # [0] - str  // Mode
    # [1] - list // Mode Input
    class ToolBox:
        Alpha   = ['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        Reverse = ['zyxwvutsrqponmlkjihgfedcba','ZYXWVUTSRQPONMLKJIHGFEDCBA']
        Digit   = ['0123456789'                ,'9876543210']
        Special = ['~`!@#$%^&*()_+-={}[]:"";<>,.?/|']
        def __init__(self,IO):
            if type(IO) is list:
                if len(IO) == 2:
                    if type(IO[0]) is str and type(IO[1]) is list:
                        Mode = str(IO[0])
                        Args = IO[1]
                        if str(Mode) in ['convert-to-byte','Convert-To-Byte','CONVERT-TO-BYTE','c-t-b']:
                            if len(Args) == 1:
                                if type(Args[0]) is str:
                                    Byte_Object = self.ConvertToByte(str(Args[0]))
                                    return Byte_Object
                                else:
                                    raise TypeError(str(Args[0])+' Expected str')
                            else:
                                raise ValueError(str(len(Args))+' Expected 1 Entity')
                        elif str(Mode) in ['convert-from-byte','Convert-From-Byte','CONVERT-FROM-BYTE','c-f-b']:
                            if len(Args) == 1:
                                if type(Args[0]) is bytes:
                                    String_Object = self.ConvertFromByte(Args[0])
                                    return str(String_Object)
                                else:
                                    raise TypeError(str(type(Args[0]))+' Expected bytes')
                            else:
                                raise ValueError(str(len(Args))+'::'+str(Args)+' Expected 1 Entity')
                        else:
                            raise KeyError(str(Mode)+' Invalid Argument Sent')
                    else:
                        raise TypeError(str(IO[0])+'/'+str(IO[1])+' Expected str,list')
                else:
                    raise ValueError(str(len(IO))+' Expected 2 Entities')
            else:
                raise TypeError(str(type(IO))+' Expected list')
        ########################################################################
        # Takes 1 Input As str
        # Convert str Into bytes('') Object As utf-8
        def ConvertToByte(self,TargetString):
            if type(TargetString) is str:
                return bytes(str(TargetString),'utf-8')
            else:
                raise TypeError(str(type(TargetString))+' Expected str')
        ########################################################################
        # Takes 1 Input As bytes
        # Converts bytes Into str bytes(str,'utf-8').decode('utf-8')
        def ConvertFromByte(self,TargetByte):
            if type(TargetByte) is bytes:
                return str(TargetByte.decode('utf-8'))
            else:
                raise TypeError(str(type(TargetByte))+' Expected bytes')
        ########################################################################
    ############################################################################
    # Takes IO As list
    # [0] - str  // Target Help Option // If NONE Print All
    # [1] - bool // If False Return String Else Print
    def _Usage_(self,IO):
        if type(IO) is list:
            if len(IO) == 2:
                Home = IO[0]
                Verb = IO[1]
                if Home == None:
                    Mesg = ''
                    for item in self.UsageIndex:
                        for line in self.UsageIndex[str(item)]:
                            Mesg += str('{} '+str(line)+str('\n')).format(str(item))
                    if Verb == True:
                        print(str(Mesg))
                    else:
                        return str(Mesg)
                else:
                    if str(Home) in self.UsageIndex:
                        Mesg = ''
                        for Item in self.UsageIndex[str(Home)]:
                            Mesg += str('{} '+str(Item)+str('\n')).format(str(Home))
                        if Verb == True:
                            print(str(Mesg))
                        else:
                            return str(Mesg)
                    else:
                        raise KeyError(str(Home)+' Entity Is NonExistant')
            else:
                raise ValueError(str(len(IO))+' Expected 2 Entities')
        else:
            raise TypeError(str(type(IO))+' Expected list')
################
