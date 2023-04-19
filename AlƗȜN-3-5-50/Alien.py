# Author: J4ck3LSyN
import os,time,sys,random,base64,hashlib,subprocess,socket,requests
try:
    import colorama;colorama.init()
except:
    print('Cannot Continue Without Colorama, Please Install Using: "pip3 install colorama"');exit(1)
#-----------------------------------------------------------------#
class Alien:
    def __init__(self,verboseBoolean=True,loggingBoolean=True,loggingOutPath='out/output.log',interpreterFailSafe=False,interpreterDeBug=False):
        if [type(verboseBoolean),type(loggingBoolean),type(loggingOutPath),type(interpreterFailSafe),type(interpreterDeBug)] == [bool,bool,str,bool,bool]:
            self.registry = {}
            self.configure = {
                'verboseStatus':verboseBoolean,
                'loggingStatus':loggingBoolean,
                'loggingOutPath':str(loggingOutPath),
                'loggingOutPipe':[],
                'interpreterFailSafe':interpreterFailSafe,
                'interpreterDeBug':interpreterDeBug,
                'interpreterHeartBeat':False,
                'signalCallTree':self._generate_signalTree()
            }
            self.registryOperations = self.registryHandle()
            self.textToDisplayOperatons = self.textToDisplay()

        else: raise self.alienException('__init__',f'Verify Inputs When Mounting Must Be The Type Specified\n\t* Verbose({verboseBoolean}),Logging({loggingBoolean}),loggingOutPath({loggingOutPath}),interpreterFailSafe({interpreterFailSafe}),interpreterDeBug({interpreterDeBug})')

    class builtinModules:
        class time:
            def __init__(self):
                self._alien_configure = {
                    'usage':{},
                    'inputKeys':{
                        'ctime':bool()
                    }
                }
            def _alien_handle(self,alienInput):
                if type(alienInput) is dict:
                    validKeys = True
                    for alienKey in alienInput:
                        if alienKey not in self._alien_configure['inputKeys']: validKeys = False
                    if validKeys == True:
                        if alienInput['ctime'] in [1,'true','True',True]: return time.ctime()
                else: self.timeException('_operate_alienModule',f'\n\t* Variable alienInput({alienInput}) Is Not dict Type')

            def timeException(self,root,message): raise Exception(f'time.{root} -> Exception: {message}')

    class textToDisplay:
        def __init__(self):
            self.config = {
                'F':{'BLACK': '\x1b[30m', 'BLUE': '\x1b[34m', 'CYAN': '\x1b[36m', 'GREEN': '\x1b[32m', 'LIGHTBLACK_EX': '\x1b[90m', 'LIGHTBLUE_EX': '\x1b[94m', 'LIGHTCYAN_EX': '\x1b[96m', 'LIGHTGREEN_EX': '\x1b[92m', 'LIGHTMAGENTA_EX': '\x1b[95m', 'LIGHTRED_EX': '\x1b[91m', 'LIGHTWHITE_EX': '\x1b[97m', 'LIGHTYELLOW_EX': '\x1b[93m', 'MAGENTA': '\x1b[35m', 'RED': '\x1b[31m', 'RESET': '\x1b[39m', 'WHITE': '\x1b[37m', 'YELLOW': '\x1b[33m'},
                'B':{'BLACK': '\x1b[40m', 'BLUE': '\x1b[44m', 'CYAN': '\x1b[46m', 'GREEN': '\x1b[42m', 'LIGHTBLACK_EX': '\x1b[100m', 'LIGHTBLUE_EX': '\x1b[104m', 'LIGHTCYAN_EX': '\x1b[106m', 'LIGHTGREEN_EX': '\x1b[102m', 'LIGHTMAGENTA_EX': '\x1b[105m', 'LIGHTRED_EX': '\x1b[101m', 'LIGHTWHITE_EX': '\x1b[107m', 'LIGHTYELLOW_EX': '\x1b[103m', 'MAGENTA': '\x1b[45m', 'RED': '\x1b[41m', 'RESET': '\x1b[49m', 'WHITE': '\x1b[47m', 'YELLOW': '\x1b[43m'},
                'S':{'BRIGHT': '\x1b[1m', 'DIM': '\x1b[2m', 'NORMAL': '\x1b[22m', 'RESET_ALL': '\x1b[0m'},
                'M':{
                    'Alien.header':f'@C-F.WHITE [@C-F.YELLOWAlien(3.5.5)@C-F.WHITE](@C-F.GREEN{os.getcwd()}@C-F.WHITE)@:>@C-F.LIGHTCYAN_EX',
                    'Alien.shortHeader':'@C-F.WHITE [@C-F.YELLOWAlien(3.5.5)@C-F.WHITE]@:>@C-F.LIGHTCYAN_EX',
                    'Alien.interpreterTerminate':'@C-F.RED[@C-F.WHITETerminate@C-F.RED] @C-F.WHITE>\t',
                    'Alien.banner':''

                },
                'colorKey':['@C-',''],
                'messageKey':['@M-','']
            }

        def _replace_colorKey(self,inputString,iterateInterval=3):
            '''
            Alien.textToDisplay._replace_colorKey(str,iterateInterval=int)
            * Replaces Colors In inputString From self.config
            * Returns str With Color Values

            {```
                for value in Alien.textToDisplay.config['F'...'S']:
                    Generate ColorID By Alien.textToDisplay.config['colorKey']
                    * [0] -> open
                    * [1] -> close
            ```}
            '''
            for iterate in range(0,int(iterateInterval)):
                for colorType in ['F','B','S']:
                    for colorKey in self.config[str(colorType)]:
                        colorKeyInternal = f'{self.config["colorKey"][0]}{colorType}.{colorKey}{self.config["colorKey"][1]}'
                        if str(colorKeyInternal) in str(inputString): inputString = inputString.replace(str(colorKeyInternal),self.config[str(colorType)][str(colorKey)])
            return inputString

        def _replace_messageKey(self,inputString):
            '''
            Alien.textToDisplay._replace_messageKey(str)
            * Replaces Messages In inputString From self.config
            * Returns str With Message Value
            {```
                for value in Alien.textToDisplay.confg['M']:
                    Generate Message By Alien.textToDisplay.config['messageKey']
            ```}
            '''
            for messageKey in self.config['M']:
                messageKeyInternal = f'{self.config["messageKey"][0]}{messageKey}{self.config["messageKey"][1]}'
                if str(messageKeyInternal) in str(inputString):
                    inputString = str(inputString).replace(str(messageKeyInternal),str(self.config['M'][str(messageKey)]))
            return inputString

        def _append_headerMessageKey(self,inputHead):
            return str(f'{self.config["messageKey"][0]}{str(inputHead)}{self.config["messageKey"][1]}')

        def _append_headerColorKey(self,inputColor):
            return str(f'{self.config["colorKey"][0]}{str(inputColor)}{self.config["colorKey"][1]}')

        def _generate_dictDisplay(self,inputDict,indentLevel=1):
            compileString = []
            for dictKey in inputDict:
                indentLevelStringHead = str('\t')*int(indentLevel-1)
                indentLevelStringMain = str('\t')*int(indentLevel)
                compileString.append(f'{indentLevelStringHead}Key: {dictKey} (')
                if type(inputDict[dictKey]) is dict:
                    returnString = self._generate_dictDisplay(inputDict[dictKey],indentLevel=int(indentLevel+1))
                    for returnLine in returnString: compileString.append(f'{indentLevelStringMain} {returnLine}')
                else: compileString.append(f'{indentLevelStringMain} {inputDict[dictKey]}')
            return compileString

        def _generate_userPrompt(self):
            prompt = self._replace_messageKey(str('@M-Alien.shortHeader'))
            prompt = self._replace_colorKey(str(prompt))
            return str(prompt)

        def displayDict(self,inputDict):
            compileLine = ''
            for displayLine in self._generate_dictDisplay(inputDict): compileLine+='\n'+str(displayLine)
            self.display(str(compileLine))

        def display(self,inputString,inputHead='Alien.header'):
            inputHead = self._append_headerMessageKey(str(inputHead))
            inputString=f'{inputHead} {inputString}'
            inputString=self._replace_messageKey(inputString)
            inputString=self._replace_colorKey(inputString)
            print(str(inputString))

        def textToDisplayException(self,root,message): raise Exception(f'Alien.appDisplayHandle.{root} -> Exception: {message}')

    class registryHandle:
        '''
        Alien.registryHandle()
        * Alien Registry Operations

        {
            root.{
                $_config.{
                    allowModules   : False
                    mountedModules : {}
                }
            }
        }

        '''
        def __init__(self):
            self.registerIndex={}

        ### Return Bool Functions
        def _retBool_verifyVarType(self,varInput,varType,varIterate=False):
            '''
            Alen.registryHandle()._retBool_verifyVarType((str,list,bool,dict,tuple,int,func),(int,str),varIterate=bool)
            * Returns True/False If varInput Is The Type Sent By varType

            varType:
                {```
                    if type(varInput) is varType
                        return True
                    else return False
                }```
                0 - str
                1 - int
                2 - list
                3 - bool
                4 - dict
                5 - tuple
                6 - func

            varIterate:
                {```
                    if type(varInput) is list and type(varType) is list and varIterate is True
                        if len(varInput) == len(varType)
                            if varInput[indexInterval] is type(varType[indexInterval]) continue
                            else return False
                        else rase Alien.registryHandle.registryHandleException
                    else raise Alien.registryHandle.registryHandleException
                ```}

            '''
            returnValue = True
            if varIterate == True:
                if isinstance(varInput,list) == True and isinstance(varType,list) and len(varInput) == len(varType):
                    for varIterateHandle in range(0,len(varInput)-1):
                        if self._retBool_verifyVarType(varInput[int(varIterateHandle)],varType[int(varIterateHandle)]) == False: returnValue = False
                    return returnValue
                else: self.registryHandleException('_retBool_verifyVarType',f'\n\t* With Variable varIterate({varIterate}) Is True\n\t* Variable varInput({varInput}) Or varType({varType}) Is Not List\n\t* Or len(varInput{len(varInput)}) Is Not Equal To len(varType({len(varType)}))')
            else:
                if varType in [0,'s','S','str','Str','STRING',str]: varType = str
                elif varType in [1,'i','I','int','Int','INT',int]: varType = int
                elif varType in [2,'l','L','list','List','LIST',list]: varType = list
                elif varType in [3,'b','B','bool','Bool','BOOL',bool]: varType = bool
                elif varType in [4,'d','D','dict','Dict','DICT',dict]: varType = dict
                elif varType in [5,'t','T','tuple','Tuple','TUPLE',tuple]: varType = tuple
                elif str(type(varInput)) in  ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]: return True
                else: self.registryHandleException('_retBool_verifyVarType',f'\n\t* Variable Input varInput({varInput}) In Not A Valid Type To Be Handled\n\t* Accepted Types: (str,int,list,bool,dict,tuple,dict,func)')
                return isinstance(varInput,varType)

        def _retBool_verifyKeyInDict(self,key,index):
            '''
            Alien.registryHandle()._retBool_verifyKeyInDict(str,dict)
            * Returns True/False If key In index
            '''
            if self._retBool_verifyVarType(index,4) == True:
                if str(key) in index: return True
                else: return False
            else: self.registryHandleException('_retBool_verifyKeyInDict',f'\n\t* Variable index({index}) Is Not dict Type')

        def _retBool_verifyStrInString(self,key,string):
            '''
            Alien.registryHandle()._retBool_verifyStrInString(str,str)
            * Returns True/False If key In string
            '''
            if self._retBool_verifyVarType(string,0) == True:
                if str(key) in str(string): return True
                else: return False
            else: self.registryHandleException('_retBool_verifyStrInString',f'\n\t* Variable string({string}) Is Not str Type')

        def _retBool_verifyExistInList(self,key,listIndex):
            '''
            Alien.registryHandle()._retBool_verifyExistInList((*),list)
            * Returns True/False If key In listIndex
            '''
            if self._retBool_verifyVarType(listIndex,2) == True:
                if key in listIndex: return True
                else: return False
            else: self.registryHandleException('_retBool_verifyExistInList',f'\n\t* Variable listIndex({listIndex}) Is Not list Type')

        def _retString_getDoubleQuotesInString(self,string):
            '''
            Alien.registryHandle()._retString_getDoubleQuotesInString(str)
            * Returns A list With Values Inside Double Quotes In A str

            {```
                if '"' in string
                    return [True,string,[SplitValueInternals]]
                else return [False, string]
            ```}
            '''
            if self._retBool_verifyVarType(string,0) == True:
                if str('"') in str(string):
                    returnValue = [True,string]
                    stringSeperated = string.split('"')
                    stringCollected = []
                    stringFlip = False
                    if len(stringSeperated) % 2 != 0:
                        for stringItem in stringSeperated:
                            if stringFlip == False:
                                stringFlip = True;continue
                            else:
                                stringCollected.append(str(stringItem));stringFlip = False
                        returnValue.append(stringCollected);return returnValue
                    else: self.registryHandleException('_retString_getDoubleQuotesInString',f'\n\t* Variable string({string}) Has A Un-Closed Double Quote By Length: {len(stringSeperated)}')
                else: return [False,string]
            else: self.registryHandleException('_retString_getDoubleQuotesInString',f'\n\t* Variable string({string}) Is Not str Type')

        def _retDict_getCurlyBracketInString(self,string):
            '''
            Alien.registerHandle()._retList_getCurlyBracketInString(str)
            * Returns A dict Wth Values Inside Of Curly Brackets In A str

            [NOTE]: Only Works With 1 Dimensonal Dictionaries
            '''
            if self._retBool_verifyVarType(string,0) == True:
                curlyDepth = 0
                for stringChar in string:
                    if stringChar == str('{'): curlyDepth += 1
                    elif stringChar == str('}'): curlyDepth -= 1
                    else: continue
                if curlyDepth == 0:
                    entryMap = {}
                    entryID  = None
                    recordEntry = False
                    IDCompile = ''
                    for charInterval in range(0,len(string)):
                        if recordEntry == False:
                            if string[charInterval] == str('{'):
                                entryID = str(IDCompile)
                                recordEntry = True
                                entryMap[entryID]=''
                            else: IDCompile += str(string[charInterval])
                        else:
                            if str(string[charInterval]) == str('}'):
                                entryID = None
                                recordEntry = False
                                IDCompile = ''
                            else:
                                entryMap[str(entryID)]+=str(string[charInterval])
                    return entryMap
                else: self.registryHandleException('_retDict_getCurlyBracketInString',f'Variable string({string}) Has Non-Closed Curly Brackets By Curly Depth: {curlyDepth}')
            else: self.registryHandleException('_retDict_getCurlyBracketInString',f'Variable string({string}) Is Not str Type/')

        def _retString_removeSpaces(self,string):
            '''
            Alien.registerHandle()._retString_removeSpaces(str)
            * Removes All Spaces Insde Of String
            '''
            returnString = ''
            for stringChar in str(string):
                if str(stringChar) == str(' '): continue
                else: returnString += str(stringChar)
            return returnString

        def _retList_getDictKeys(self,dictInput):
            '''
            Alien.registerHandle()._retList_getDictKeys(dict)
            * Returns All Keys Inside dict As List
            '''
            if self._retBool_verifyVarType(dictInput,4) == True:
                outputList = []
                for dictKey in dictInput: outputList.append(dictKey)
                return outputList
            else: self.registryHandleException('_retList_getDictKeys',f'\n\t* Variable dictInput({dictInput}) Is Not dict Type')

        def _retValue_conversionString(self,string):
            '''
            Alien.registerHandle()._retValue_conversionString(str)
            * Returns Conversion For string Variables
            '''
            if str('(') in str(string) and str(')') in str(string):
                stringType = string.split('(')[0]
                stringValue = string.split('(')[1].strip(')')
                if stringType in ['BOOL','0xb01']:
                    if stringValue in ['true','True','TRUE',1]: return True
                    elif stringValue in ['false','False','FALSE','0']: return False
                    else: self.registryHandleException('_retValue_conversionString',f'\n\t* Invalid Input For Type: {stringType}\n\t* Expected boolean Type')
                elif stringType in ['STR','0xb02']: return str(stringValue)
                elif stringType in ['INT','0xb03']:
                    digits = '0123456789'
                    digitsBool = True
                    for character in stringValue:
                        if str(character) not in digits:
                            digitsBool = False;break
                    if digitsBool == True: return int(stringValue)
                    else: self.registryHandleException('_retValue_conversionString',f'\n\t* Invalid Input For Type: {stringType}\n\t* Expected int Values For Else')
                else: self.registryHandleException('_retValue_conversionString',f'\n\t* Invalid Type For Operation: {stringType}')
            else: self.registryHandleException('_retValue_conversionString',f'\n\t* Variable string({string}) Does Not Carry Input Operands')


        ### Registry Functions

        def _retBool_verifyLocation(self,locationTree):
            '''
            Alien.registryHandle()._retBool_verifyLocation(str)
            * Returns True/False If locationTree Is A Valid Location

            locationTree:
                * Seperated By "."
                root
                root.stem
                root.stem.branch
                root.stem.branch.leaf
            '''
            if str('.') in str(locationTree):
                locationTreeSeperated = str(locationTree).split('.')
                if len(locationTreeSeperated) == 1: return self._retBool_verifyKeyInDict(str(locationTreeSeperated[0]),self.registerIndex) # Verify Root Exists 'root.'
                elif len(locationTreeSeperated) == 2: # Verify Stem Exists 'root.stem'
                    if self._retBool_verifyKeyInDict(str(locationTreeSeperated[0]),self.registerIndex) == True: return self._retBool_verifyKeyInDict(str(locationTreeSeperated[1]),self.registerIndex[str(locationTreeSeperated[0])])
                    else: return False
                elif len(locationTreeSeperated) == 3: # Verify Branch Exists 'root.stem.branch'
                    if self._retBool_verifyKeyInDict(str(locationTreeSeperated[0]),self.registerIndex) == True:
                        if self._retBool_verifyKeyInDict(str(locationTreeSeperated[1]),self.registerIndex[str(locationTreeSeperated[0])]) == True:
                            if self._retBool_verifyVarType(self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])],4) == True: return self._retBool_verifyKeyInDict(str(locationTreeSeperated[2]),self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])])
                            else: self.registryHandleException('_retBool_verifyLocation',f'\n\t* Got Branch: {str(locationTreeSeperated[2])} However Stem Is Not A Index: {str(locationTreeSeperated[1])} Inside Of Root: {str(locationTreeSeperated[0])}')
                        else: return False
                    else: return False
                elif len(locationTreeSeperated) == 4: # Verify Leaf Exists 'root.stem.branch.leaf'
                    if self._retBool_verifyLocation(str(f'{str(locationTreeSeperated[0])}.{str(locationTreeSeperated[1])}.{str(locationTreeSeperated[2])}')) == True:
                        if self._retBool_verifyVarType(self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])],4) == True: return self._retBool_verifyKeyInDict(str(locationTreeSeperated[3]),self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])])
                        else: self.registryHandleException('_retBool_verifyLocation',f'\n\t* Got Leaf: {ste(locationTreeSeperated[3])} However Branch Is Not A Index: {str(locationTreeSeperated[2])} Inside Of Branch: {str(locationTreeSeperated[1])} From Root: {str(locationTreeSeperated[0])}')
                else: self.registryHandleException('_retBool_verifyLocation',f'\n\t* Variable locationTree({locationTree}) Exceeded The Length For Regstery Locations ({len(locationTreeSeperated)}>4)')
            else: return self._retBool_verifyKeyInDict(str(locationTree),self.registerIndex)

        def _retValue_fromLocation(self,locationTree):
            '''
            Alien.registryHandle()._retValue_fromLocation(str)
            * Returns Value Of Registry Location
            '''
            if str('.') in str(locationTree):
                locationTreeSeperated = locationTree.split('.')
                if self._retBool_verifyLocation(str(locationTree)) == True:
                    if len(locationTreeSeperated) == 1: return self.registerIndex[str(locationTreeSeperated[0])]
                    elif len(locationTreeSeperated) == 2: return self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])]
                    elif len(locationTreeSeperated) == 3: return self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])]
                    elif len(locationTreeSeperated) == 4: return self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])][str(locationTreeSeperated[3])]
                    else: self.registryHandleException('_retValue_fromLocation',f'\n\t* Got locationTree({locationTree}) Exceeded The Length For Registery Locations ({len(locationTreeSeperated)}>4)')
                else: self.registryHandleException('_retValue_fromLocation',f'\n\t Locaton locationTree({locationTree}) Is Non-Existant')
            else:
                if self._retBool_verifyLocation(str(locationTree)) == True: return self.registerIndex[str(locationTree)]

        def _generate_stem(self,locationTree):
            '''
            Alien.registryHandle()._generate_stem(str)
            * Builds A Stem Inside Of Root Location
            '''
            if str('.') in str(locationTree):
                locationTreeSeperated = locationTree.split('.')
                if len(locationTreeSeperated) == 2:
                    if self._retBool_verifyKeyInDict(str(locationTreeSeperated[0]),self.registerIndex) == True: self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])]={}
                    else: self.registryHandleException('_generate_stem',f'\n\t* Location locationTree({locationTree}) Root: {locationTreeSeperated[0]} Is Non-Existant')
                else: self.registryHandleException('_generate_stem',f'\n\t* Variable locationTree({locationTree}) Was Expected Inside Of Root Index, Length Did Not Match: {len(locationTreeSeperated)}')
            else: self.registryHandleException('_generate_stem',f'\n\t* Variable locationTree({locationTree}) Did Not Contain Location Seperator "."')

        def _generate_branch(self,locationTree,branchRangeMin=random.randint(6666,999999),branchRangeMax=random.randint(999999,9999999999),padding=16):
            '''
            Alien.registryHandle()._generate_branch(str,branchRangeMin=int,branchRangeMax=int)
            * Buids leaf index Inside Of Branch Index
            '''
            if str('.') in str(locationTree):
                locationTreeSeperated = locationTree.split('.')
                if len(locationTreeSeperated) == 3:
                    if self._retBool_verifyVarType(branchRangeMin,1) == True and self._retBool_verifyVarType(branchRangeMax,1) == True:
                        branch = {}
                        if self._retBool_verifyKeyInDict(str(locationTreeSeperated[2]),self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])]) == False:
                            if int(branchRangeMin) < int(branchRangeMax):
                                for leaf in range(int(branchRangeMin),int(branchRangeMax)):
                                    leafHex = hex(int(leaf)).split('0x')[1]
                                    if len(leafHex) < padding:
                                        leafHex = str('0'*int(padding-len(leafHex)))+str(leafHex)
                                    branch[str(leafHex)]=['null']
                            else: self.registryHandleException('_generate_branch',f'\n\t* Variable branchRangeMin({branchRangeMin}) < branchRangeMax({branchRangeMax})')
                        self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])]=branch
                    else: self.registryHandleException('_generate_branch',f'\n\t* Variable branchRangeMin({branchRangeMin}) Or branchRangeMax({branchRangeMax}) Was Not int Type')
                else: self.registryHandleException('_generate_branch',f'\n\t* Variable locationTree({locationTree}) Was Excpected Inside Of Stem, Length Did Not Match: {len(locationTreeSeperated)}')
            else: self.registryHandleException('_generate_branch',f'\n\t* Variable locationTree({locationTree}) Did Not Contain Location Seperator "."')

        def _generate_register(self,root):
            '''
            Alien.registryHandle()._generate_register(str)
            * Builds A Root Index Inside Of self.registerIndex
            '''
            if self._retBool_verifyKeyInDict(str(root),self.registerIndex) == False:
                self.registerIndex[str(root)]={}
                self._generate_stem(f'{root}.$_config')
                self._generate_branch(f'{root}.$_config.modules',branchRangeMin=1,branchRangeMax=9)
            else: self.registryHandleException('_generate_register',f'\n\t* Root root({root}) Already Exists')

        def _write_registerLeaf(self,locationTree,value):
            '''
            Alien.registryHandle()._write_registerLeaf(str,tuple)
            * Appends value To Location Inside Of self.registerIndex
            '''
            if self._retBool_verifyLocation(str(locationTree)) == True:
                if self._retBool_verifyVarType(value,2) == True:
                    locationTreeSeperated=locationTree.split('.')
                    self.registerIndex[str(locationTreeSeperated[0])][str(locationTreeSeperated[1])][str(locationTreeSeperated[2])][str(locationTreeSeperated[3])]=value
                else: self.registryHandleException('_write_registerLeaf',f'Variable value({value}) Is Not tuple Type')
            else: self.registryHandleException('_write_registerLeaf',f'\n\t* Location locationTree({locationTree}) Is Non-Existant')

        def registryHandleException(self,root,message): raise Exception(f'\n* Alien.registryHandle.{root} -> Exception: {message}')
        ### END Alien.registryHandle()


    ### Generation Operations
    def _generate_register(self,root):
        '''
        Alien._generate_register(str)
        * Generates A registerHandle ID Inside Of self.registry By ID root
        '''
        if str(root) not in self.registry: self.registry[str(root)] = self.registryHandle()
        else: self.alienException('_generate_register',f'\n\t* Variable root({root}) Already Exists')

    def _generate_signalTree(self):
        '''
        Alien._generate_signalTree()
        * Generates A Signal Tree { 0x000...0xf00 { 0x000...0xfff } }
        '''
        signalTree = {}
        signalKeys = [hex(i) for i in range(0x000,0xfff)]
        for SKI in range(0,len(signalKeys)-1): # Filter For All Values To Be A Length Of 3
            signalKey = str(signalKeys[SKI])
            if len(signalKey.split('x')[1]) < 3:
                if len(signalKey.split('x')[1]) == 1: signalKeys[SKI]=f'0x00{signalKey.split("x")[1]}'
                elif len(signalKey.split('x')[1]) == 2: signalKeys[SKI]=f'0x0{signalKey.split("x")[1]}'
        signalTreeKeys = []
        recordEntry = ''
        for SKI in signalKeys: # Create Key Enries With Values
            targetValues = '0123456789ascbdef'
            if str(SKI[2]) in str(targetValues):
                if str(SKI[3:]) == str('00'):
                    recordEntry = str(SKI)
                    signalTree[str(SKI)]={}
                    signalTreeKeys.append(str(SKI))
                else: signalTree[str(recordEntry)][str(SKI)]=['NULL']
        return [signalTreeKeys,signalTree]

    def _generate_signalCall(self,signalCallID,signalCallFunction,signalRules={},signalCallOutputLocation=''):
        '''
        Alien._generate_signalCall(str,func,signalRules=list,signalCallOutputLocation=None/str)
        * Configures Alien.configure['signalCallTree'] Keys To Function Call Mounts

        signalCallID:
            Must Contain '.' For Seperation <signal>.<call>

        SIGCALL Structure:
            ['NULL'] -> None Configured Signal ID
            [
                <FUNC(func)>,
                <RULES(DICT)>,
                <OUTPUTPIPE(None/str)>
            ]

            FUNC:
                * Python Method/Function To Execute
                * Every Function Will Be 'Mounted' By Calling It As A Module IE: func()
                * To Execute Function Operations func()._operate_alienModule(list) To Execute
                * Return Output Will Be Sent To [2] And If Not None Than Register Location

            RULES:
                * Each Rule Is A String "<RULE>:<VALUE>"

        '''
        if self.registryOperations._retBool_verifyVarType([signalCallID,signalCallFunction,signalRules,signalCallOutputLocation],[0,6,4,0]) == True:
            if str('.') in str(signalCallID):
                SCT = signalCallID.split('.')
                if self.registryOperations._retBool_verifyKeyInDict(str(SCT[0]),self.configure['signalCallTree']) == True:
                    if self.registryOperations._retBool_verifyKeyInDict(str(SCT[1]),self.configure['signalCallTree'][str(SCT[0])]) == True:
                        SCT_value = self.configure['signalCallTree'][SCT[0]][SCT[1]]
                        if SCT_value == ['NULL']:
                            try:
                                moduleMount = signalCallFunction()
                                moduleConfig = moduleMount.configure
                                
                            except Exception as E: self.alienException('_generate_signalCall',f'\n\t* SIGCALL({signalCallID}) Failed Due To: {E}')
                        else: self.alienException('_generate_signalCall',f'\n\t* SIGCALL({signalCallID}) Is Already Configured To: {SCT_value}')
                    else: self.alienException('_generate_signalCall',f'\n\t* Call({SCT[1]}) Did Not Exist Inside Of Signal({SCT[0]}), Dirived From signalCallID({signalCallID})')
                else: self.alienException('_generate_signalCall',f'\n\t* Signal({SCT[0]}) Did Not Exist, Was Dirived From signalCallID({signalCallID})')
            else: self.alienException('_generate_signalCall',f'\n\t* Variable signalCallID(signalCallID) Did Not Contain Seperator "."')
        else: self.alienException('_generate_signalCall',f'\n\t* Variables Sent Are Invalid Type:\n\t\t* signalCallID({signalCallID}) | str\n\t\t* signalCallFunction({str(signalCallFunction)}) | func\n\t\t* signalRules({signalRules}) | dict\n\t\t* signalCallOutputLocation({signalCallOutputLocation}) | str')

    ### File Operations
    def _read_fileFromPath(self,filePath,encoding='utf-8'):
        '''
        Alien._read_fileFromPath(str,encoding=str)
        * Reads A File And Splits By New Line Returns list
        '''
        if os.path.isfile(str(filePath)) == True:
            fileText = []
            try:
                fileHandle=open(str(filePath),'r',encoding=str(encoding));fileText=fileHandle.read().split('\n');fileHandle.close()
            except Exception as E: self.alienException('_read_fileFromPath',f'\n\t* Operation Failed Due To {E} On File filePath({filePath})')
            return fileText
        else: self.alienException('_read_fileFromPath',f'\n\t* Variable filePath({filePath}) Is Not A Valid File Path')

    ### Pipe Operations
    def _pipe_verboseMessages(self,root,message):
        '''
        Alien._pipe_loggingMessages(str,str)
        * Pipes Message To Screen
        '''
        if self.configure['verboseBoolean'] == True:
            message = f'@C-F.RED(@C-F.GREEN{root}@C-F.RED)@C-F.WHITE {message}';self.textToDisplayOperatons.display(str(message))

    def _pipe_loggingMessages(self,root,message):
        '''
        Alien._pipe_loggingMessages(str,str)
        * Pipes Logging Messages
        '''
        if self.configure['loggingBoolean'] == True:
            timestamp = str(time.ctime())
            currentDir = str(os.getcwd())
            message = f'[LOG]\n\tTime: {timestamp}\n\tCurrent Directory: {currentDir}\n\tMessage: {message}'
            self.configure['loggingOutPipe'].append(str(message))
            if self.configure['interpreterDeBug'] == True: self.textToDisplayOperatons(str(message))

    def _pipe_VAndL(self,root,message):
        '''
        Alien._pipe_VAndL(str,str)
        * Pipe For Alien._pipe_verboseMessages And Alien._pipe_loggingMessages
        '''
        self._pipe_verboseMessages(str(root),str(message))
        self._pipe_loggingMessages(str(root),str(message))

    ### Return Operations
    def _retBool_areWeConfigured(self):
        '''
        Alien._retBool_areWeConfigured()
        * Returns True/False If Internals Are Configured
        '''
        if self.registryOperations._retBool_verifyKeyInDict(str('alienConfig'),self.registry) == True:
            returnValue = True
            if self.registry['alienConfig']._retBool_verifyLocation('Alien.Verbose.Boolean') == False: returnValue = False
            if self.registry['alienConfig']._retBool_verifyLocation('Alien.Logging.Boolean') == False: returnValue = False
            return returnValue
        else: return False

    def _retBool_verifyLocation(self,location):
        '''
        Alien._retBool_verifyLocation(str)
        * Returns True/False If location Exists
        '''
        if str('.') in str(location):
            locationTree = location.split('.')
            if self.registryOperations._retBool_verifyKeyInDict(str(locationTree[0]),self.registry):
                locationTarget = ''
                for locationIndex in locationTree[1:]: locationTarget += f'.{locationIndex}'
                return self.registry[str(locationTree[0])]._retBool_verifyLocation(str(locationTarget))
            else: return False
        else: return self.registryOperations._retBool_verifyKeyInDict(str(location),self.registry)

    def _retBool_verifySignalCall(self,signalCall):
        '''
        '''
        ...

    ### Interpreter Operations
    def _interpreter_handleSyntaxLine(self,syntaxLine):
        '''
        Alien._interpreter_handleSyntaxLine(str)
        * Handles Indivitual Alien Syntax
        '''
        ...

    def _interpreter_handleSyntaxList(self,syntaxList):
        '''
        Alien._interpreter_handleSyntaxList(list)
        * Initial Handle For Alien Script

        Removed Comments : '!/'
        Combines Line Seperated Inputs:
        ```
        foo {
            bar:foo,
            bar:foo
        }
        ```
        `foo {bar:foo,bar:foo}`
        '''
        if self.registryOperations._retBool_verifyVarType(syntaxList,2) == True:
            syntaxStage0 = []
            for syntaxLine in syntaxList:
                if str(syntaxLine[2:]) == str('!/'): continue
                if str(';') in str(syntaxLine):
                    syntaxLineTree = syntaxLine.split(';')
                    for syntaxSubLine in syntaxLineTree:
                        if str('!/') in str(syntaxSubLine): syntaxSubLine = str(syntaxSubLine).split('!/')[0]
                        syntaxStage0.append(str(syntaxSubLine))
                else:
                    if str('!/') in str(syntaxLine): syntaxLine = str(syntaxLine).split('!/')[0]
                    syntaxStage0.append(str(syntaxLine))
            syntaxStage1 = []
            record = [False,'',[]]
            for syntaxLine in syntaxStage0:
                if record[0] == False:
                    if str('{') in str(syntaxLine) and str('}') not in str(syntaxLine): record = [True,str(syntaxLine.split('{')[0]),[]]
                    else: syntaxStage1.append(str(syntaxLine))
                else:
                    if str('}') in str(syntaxLine):
                        syntaxLineCompiled = str(record[1])+str('{')
                        for subLine in record[2]:
                            syntaxLineCompiled += str(subLine)
                        syntaxLineCompiled += '}'
                        syntaxStage1.append(str(syntaxLineCompiled))
                    else: record[2].append(str(syntaxLine))
            syntaxStage2 = [syntaxLine for syntaxLine in syntaxStage1 if len(syntaxLine) != 0]
            syntaxOutputs = []
            for syntaxLine in syntaxStage2:
                syntaxOutput = self._interpreter_handleSyntaxLine(str(syntaxLine))
                syntaxOutputs.append(str(syntaxOutput))
                if syntaxOutput == '0xfff': break
            return syntaxOutputs
        else: self.alienException('_interpreter_handleSyntaxList',f'\n\t* Variable syntaxList({syntaxList}) Is Not list Type')

    def interpreter(self):
        if self.configure['interpreterHeartBeat'] == False: self.configure['interpreterHeartBeat'] = True
        promptAppend = ''
        self.textToDisplayOperatons.display('[!] Initialzing Alien Interpreter...')
        while self.configure['interpreterHeartBeat'] == True:
            try:
                if len(promptAppend) == 0:
                    userPrompt = self.textToDisplayOperatons._generate_userPrompt()+str(' (HOME) >')
                else:
                    userPrompt = self.textToDisplayOperatons._generate_userPrompt()+str(f' ({promptAppend}) >')
                userInput = input(str(userPrompt))
                if str(' ') in str(userInput):
                    ...
                else:
                    if str(userInput) in ['0xfff','terminate','Terminate','TERMINATE']:
                        self.textToDisplayOperatons.display('@M-Alien.interpreterTerminate Due To User Input');self.configure['interpreterHeartBeat']=False
            except Exception as E:
                if self.configure['interpreterFailSafe'] == False:
                    self.alienException('interpreter',f'\n\t* Failed Due To: {E}')
                else: continue
            except KeyboardInterrupt: continue

    def alienException(self,root,message): raise Exception(f'\n* Alien.{root} -> Exception: {message}')

if __name__ == '__main__':
    app = Alien()
    if len(sys.argv[1:]) == 0:
        # app.interpreter()
        print(app.configure)
    else:
        ...
