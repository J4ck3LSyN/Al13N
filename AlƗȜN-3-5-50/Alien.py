# Author: J4ck3LSyN
import os,time,sys,random,base64,hashlib,subprocess,socket,requests,json
if os.name == 'nt':
    try:
        import colorama;colorama.init()
    except:
        print('Cannot Continue Without Colorama, Please Install Using: "pip3 install colorama"');exit(1)
#-----------------------------------------------------------------#
class Alien:
    def __init__(self,verboseStatus=True,loggingStatus=True,loggingOutPath='output.log',interpreterFailSafe=False,interpreterDeBug=False,dumpLogOnExit=True,dumpRegistryOnExit=True):
        self.registry = {}
        self.config = {
            'verboseStatus':verboseStatus,
            'loggingStatus':loggingStatus,
            'loggingOutPath':str(loggingOutPath),
            'dumpLogOnExit':dumpLogOnExit,
            'dumpRegistryOnExit':dumpRegistryOnExit,
            'loggingOutPipe':[],
            'interpreterFailSafe':interpreterFailSafe,
            'interpreterDeBug':interpreterDeBug,
            'interpreterHeartBeat':False,
            'signalCallTree':None,
            'usageDict':{
                ### InLine
                '-h,--help':[
                    '(InLine) Displays This Help Message',
                    '',
                    '* Can Take 1 Argument As Query',
                    '`@C-F.GREEN-h:Message@C-F.WHITE`',
                    '^ Will Display Every String Containing The String "Message"'
                ],
                '-lS,--logStatus':[
                    '(InLine) Flips Current Log Status'
                ],
                '-vS,--verStatus':[
                    '(InLine) Flips Current Verbose Status'
                ],
                '-vD,--verDebug':[
                    '(InLine) Flips Current Debug Status'
                ],
                '-dLOE,--dumpLogOnExit':[
                    '(InLine) Flips Current dumpLogOnExit Status'
                ],
                '-dROE,--dumpRegistryOnExit':[
                    '(InLine) Flips Current dumpRegistryOnExit Status'
                ],
                '-cF,--configConfigFile':[
                    '(InLine) Takes 1 Input And Will OverRide: -lS -vS -vD'
                ],
                '-sI,--startInterpreter':[
                    '(InLine) Starts Alien.interpreter()'
                ],
                '-eI,--executeInterpreter':[
                    '(InLine) Takes 1 Input In "" And Will Execute',
                    '',
                    '[NOTE: If "-sI" Is Active It Will Execute Prior]'
                ],
                '-sF.--startFresh':[
                    '(InLine) If True Than All Files In "logs/" And "output/" Will Be Removed'
                ],
                '-cR,--configReset':[
                    '(InLine) If True Than src/alien.json Will Be Confgured Based Off Current Configuration'
                ],
                ### Interpreter
                f'0xfffa0,terminate,Terminate,TERMINATE,{str(int(0xfffa0))}':[
                    '(Interpreter) Terminates The Script'
                ],
                f'0xfffb0,usage,Usage,USAGE,{str(int(0xfffb0))}':[
                    '(Interpreter) Displays Usage'
                ],
                f'0xfffb1,displayRegistry,DisplayRegistry,DISPLAYREGISTRY,{str(int(0xfffb1))}':[
                    '(Interpreter) Displays All Registy Entries',
                    '',
                    'Can Take 1 Input For Location Inside Of Register'
                ]
            },
            'startInterpreterWithNoArg':True
        }
        self.config['signalCallTree']=self._generate_signalTree()
        self.registryOperations = self.registryHandle()
        self.textToDisplayOperations = self.textToDisplay()


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
                else: self.timeException('_alien_handle',f'\n\t* Variable alienInput({alienInput}) Is Not dict Type')

            def timeException(self,root,message): raise Exception(f'time.{root} -> Exception: {message}')
        class terminate:
            def __init__(self):
                self._alien_configure = {
                    'usage':{},
                    'inputKeys':{
                        'init':None
                    }
                }
            def _alien_handle(self,alienInput):
                if type(alienInput) is dict:
                    validKeys = True
                    for alienKey in alienInput:
                        if alienKey not in self._alien_configure['inputKeys']: validKeys = False
                    if validKeys == True:
                        if alienInput['init'] == None: exit(1)
                else: self.terminateException('_alien_handle',f'\n\t* Veriable alienInput({alienInput}) Is Not dict Type')

            def terminateException(self,root,message): raise Exception(f'terminate.{root} -> Exception: {message}')

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
                    'Alien.usageCommand':'@C-F.WHITE(Command) ',
                    'Alien.usageLine':'@C-F.GREEN\t',
                    'Alien.blank':'',
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

        def displayUsage(self,usageDict,query=None):
            if isinstance(usageDict,dict) == True:
                if query == None:
                    for command in usageDict: self.displayUsage(usageDict,query=str(command))
                else:
                    usageTree = {}
                    for command in usageDict:
                        if str(query) in str(command): usageTree[f'@C-F.YELLOW{command}@C-F.WHITE']=usageDict[command]
                        else:
                            for line in range(0,len(usageDict[str(command)])-1):
                                if str(query) in str(usageDict[str(command)][line]):
                                    usageDict[str(command)][line]=str(usageDict[str(command)][line]).replace(str(query),f'@C-F.YELLOW{query}@C-F.WHITE')
                                    usageTree[str(command)]=usageDict[str(command)]
                    if len(usageTree) > 0:
                        for command in usageTree:
                            self.display(str(command),inputHead='Alien.usageCommand')
                            for line in usageTree[command]:
                                self.display(str(line),inputHead='Alien.usageLine')
                        commandSeperator = str('*')*100
                        commandSeperator = f'@C-F.GREEN{commandSeperator}'
                        self.display(commandSeperator,inputHead='Alien.blank')
                    else: self.textToDisplayException('displayUsage',f'\n\t* Query String: {query} Does Not Exist Inside Of usageDict({usageDict})')
            else: self.textToDisplayException('displayUsage',f'\n\t* Variable usageDict({usageDict}) Is Not dict Type')

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
        self._pipe_loggingMessages(f'_generate_register({root})','Operating...')
        '''
        Alien._generate_register(str)
        * Generates A registerHandle ID Inside Of self.registry By ID root
        '''
        if str(root) not in self.registry: self.registry[str(root)] = self.registryHandle()
        else: self.alienException('_generate_register',f'\n\t* Variable root({root}) Already Exists')

    def _generate_signalTree(self):
        self._pipe_loggingMessages('_generate_signalTree()','Operating...')
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
        self._pipe_loggingMessages('_generate_signalTree()',f'Generated Signal Tree Keys And Dict: {signalTreeKeys} - {signalTree}')
        return [signalTreeKeys,signalTree]

    def _generate_signalCall(self,SIG_call,SIG_function,SIG_rules,SIG_outPipe=''):
        self._pipe_loggingMessages(f'_generate_signalCall({SIG_call},{str(SIG_function)},{SIG_rules},outPipe={outPipe})','Operating...')
        '''
        Alien._generate_signalCall(str,func,dict,outPipe=str)
        * Configures values inside of Alien.config['signalCallTree'] to modules

        SIG_call:
            This variable is a string containing the signal.call for operation,
            `0x000.0x001 == Alien.config['signalCallTree']['0x000']['0x001']`

        SIG_function:
            This is your module to execute, it will be set to a variable via SIG_function(),
            this module must contain two objects:
                '_alien_configure'
                    (dict) To Handle Operations By
                    ```
                    {
                        'usage':{
                            # Usage Dictionary
                        },
                        'inputKeys':{
                            'key':(bool,str,int,list,dict/None)
                            # Key will be a execution key and will verify the key input by the value
                            #
                        }

                    }
                    ```
                '_alien_handle(dict)'
                    (func) To Execute Operations
                    Must Take A Input With dict Type
                    ```
                    {
                        'inputArg':'inputValue'

                    }
                    ```

        SIG_rules:
            (dict) For Operations (_alien_configure Will Be Appended Here Under 'alienConfig')

        SIG_outPipe:
            (str) Location In A Register To Output Value To When Executed

        SIGCALL Values:
            If Not Configured Values Will Be:
                ['NULL']
            Else:
                [
                    functon_to_execute,
                    SIG_rules,
                    [
                        SIG_outPipe,
                        [
                            # Output From Execution Storage
                        ]
                    ]
                ]
        '''
        if self.registryOperations._retBool_verifyVarType([SIG_call,SIG_function,SIG_rules,SIG_outPipe],[0,6,4,0],varIterate=True) == True:
            try:
                if str('.') in str(SIG_call):
                    SIG_tree = str(SIG_call.split('.'))
                    if len(SIG_tree) == 2:
                        if self.registryOperations._retBool_verifyKeyInDict(str(SIG_tree[0]),self.config['signalCallTree']) == True:
                            if self.registryOperations._retBool_verifyKeyInDict(str(SIG_tree[1]),self.config['signalCallTree'][str(SIG_tree[0])]) == True:
                                SIG_currentValue = self.config['signalCallTree'][str(SIG_tree[0])][str(SIG_tree[1])]
                                if SIG_currentValue == ['NULL']:
                                    SIG_value = []
                                    alienModule = SIG_function()
                                    alienConfigure = alienModule._alien_configure
                                    SIG_value.append(alienModule)
                                    SIG_rules['alienConfig']=alienConfigure
                                    SIG_value.append(SIG_rules)
                                    SIG_value.append([str(SIG_outPipe),[]])
                                    self.config['signalCallTree'][str(SIG_tree[0])][str(SIG_tree[1])]=SIG_value
                                    self._pipe_loggingMessages(f'_generate_signalCall({SIG_call},{str(SIG_function)},{SIG_rules},outPupe={outPipe})',f'Configured SIGCALL({SIG_call}) To {SIG_value}')
                                else: self.alienException('_generate_signalCall',f'\n\t* Variable SIG_call Contains A Value: {SIG_currentValue}')
                            else: self.alienException('_generate_signalCall',f'\n\t* Call({SIG_tree[0]}) For Signal({SIG_tree[0]}) Is Non-Existant')
                        else: self.alienException('_generate_signalCall',f'\n\t* Signal({SIG_tree[0]}) Is Non-Existant')
                    else: self.alienException('_generate_signalCall',f'\n\t* Operation Failed Due To Length Of SIG_call({SIG_call}) {len(SIG_tree)}')
                else: self.alienException('_generate_signalCall',f'\n\t* Variable SIG_call({SIG_call}) Does Not Contain Seperator "."')
            except Exception as E: self.alienException('_generate_signalCall',f'\n\t* Exception: {E}')
        else: self.alienException('_generate_signalCall',f'\n\t* Invalid Variable In Arguments By Type:\n\t\t* SIG_call({SIG_call}) | str\n\t\t* SIG_function({SIG_function}) | func\n\t\t* SIG_rules({SIG_rules}) | dict\n\t\t* SIG_outPipe({SIG_outPipe}) | list')

    def _generate_sourceFiles(self,deleteIfExist=False):
        self._pipe_loggingMessages(f'_generate_sourceFiles(deleteIfExist={deleteIfExist})','Operating...')
        '''
        Alien._generate_sourceFiles(deleteIfExist=bool)
        * Builds src Directory
        '''
        CWD = os.getcwd()
        if os.path.isdir(str('src')) == False:
            CWD_src = CWD+str('\\src')
            CWD_log = CWD+str('\\logs')
            CWD_out = CWD+str('\\output')
            CWD_mod = CWD+str('\\modules')
            CWD_modInit = CWD_mod+str('\\__init__.py')
            os.mkdir(str(CWD_src))
            os.mkdir(str(CWD_mod))
            os.mkdir(str(CWD_log))
            os.mkdir(str(CWD_out))
            CWD_modInitFile = open(str(CWD_modInit),'x')
            CWD_modInitFile.write('# Alien External Module Port')
            CWD_modInitFile.close()
        else:
            if deleteIfExist == True:
                os.rmdir(str('src'))
                self._generate_sourceFiles()
            else: self.alienException('_generate_sourceFiles',f'\n\t* Path src Is Existant And Variable deleteIfExist({deleteIfExist}) Is False')

    def _generate_alienConfigurationFile(self,alienConfigurePath='alien.json'):
        self._pipe_loggingMessages(f'_generate_alienConfigurationFile(alienConfigurePath={alienConfigurePath})','Operating...')
        '''
        Alien._generate_alienConfigurationFile(dict,alienConfigurePath=str)
        * Generates A Configuration File Based Off Current Configuration
        '''
        if os.path.isdir('src') == True:
            configureTranslated = {}
            for confKey in self.config:
                if str(confKey) not in ['signalCallTree','loggingOutPipe']: configureTranslated[str(confKey)]=self.config[confKey]
            jsonConfig = {
                'alienConfig':configureTranslated,
                'textToDisplayConfig':self.textToDisplayOperations.config
            }
            if str('src/') not in str(alienConfigurePath): alienConfigurePath = f'src/{alienConfigurePath}'
            with open(str(alienConfigurePath),'w') as jsonConfigWrite: json.dump(jsonConfig,jsonConfigWrite,indent=2)
        else:
            self._generate_sourceFiles();self._generate_alienConfigurationFile(customConfigureDict,alienConfigurePath=str(alienConfigurePath))

    ### File Operations
    def _read_fileFromPath(self,filePath,encoding='utf-8'):
        self._pipe_loggingMessages(f'_read_fileFromPath({filePath},encoding={encoding})','Operating...')
        '''
        Alien._read_fileFromPath(str,encoding=str)
        * Reads A File And Splits By New Line Returns list
        '''
        if os.path.isfile(str(filePath)) == True:
            fileText = []
            try:
                fileHandle=open(str(filePath),'r',encoding=str(encoding));fileText=fileHandle.read().split('\n');fileHandle.close()
            except Exception as E: self.alienException('_read_fileFromPath',f'\n\t* Operation Failed Due To {E} On File filePath({filePath})')
            self._pipe_loggingMessages(f'_read_fileFromPath({filePath},encoding={encoding})',f'Output File Text: {fileText}')
            return fileText
        else: self.alienException('_read_fileFromPath',f'\n\t* Variable filePath({filePath}) Is Not A Valid File Path')

    def _read_jsonFromPath(self,jsonPath):
        self._pipe_loggingMessages(f'_read_jsonFromPath({jsonPath})','Operating...')
        '''
        Alien._read_jsonFromPath(str)
        * Returns dict From Json File
        '''
        if os.path.isfile(str(jsonPath)) == True:
            try:
                with open(str(jsonPath),"r") as jsonRead:
                    jsonData=json.load(jsonRead)
                self._pipe_loggingMessages(f'_read_jsonFromPath({jsonPath})',f'Read Json Data: {jsonData}')
                return jsonData
            except Exception as E: self.alienException('_read_jsonFromPath',f'\n\t* Operation Failed Due To: {E} From jsonPath({jsonPath})')
        else: self.alienException('_read_jsonFromPath',f'\n\t* Variable jsonPath({jsonPath}) Is Not A Valid File Path')

    def _write_jsonToPath(self,jsonPath,jsonData):
        self._pipe_loggingMessages(f'_write_jsonToPath({jsonPath},{jsonData})','Operating...')
        '''
        Alien._write_jsonToPath(str,dict)
        * Writes Json Data To File
        '''
        if self.registryOperations._retBool_verifyVarType(jsonData,4) == True:
            try:
                with open(jsonPath,'w') as jsonWrite:
                    json.dump(jsonData,jsonWrite)
            except Exception as E: self.alienException('_write_jsonToPath',f'\n\t* Operation Faled Due To: {E} From jsonPath({jsonPath}) With jsonData({jsonData})')
        else: self.alienException('_write_jsonToPath',f'\n\t* Variable jsonData({jsonData}) Is Not dict Type')

    def _write_dumpLog(self):
        self._pipe_loggingMessages('_write_dumpLog()','Operating...')
        '''
        Alien._write_dumpLog()
        * Dumps Everything In Log To File
        '''
        if os.path.isdir('logs') == False: os.mkdir('logs')
        logFileTitle = f"{'_'.join(str(time.ctime()).split(' ')[1:4]).replace(':','_')}_{self.config['loggingOutPath']}"
        logFilePath = 'logs/'+str(logFileTitle)
        logFileText = ''
        for logLine in self.config['loggingOutPipe']: logFileText = f'{logFileText}\n{logLine}'
        logFileWriter = open(logFilePath,'w',encoding='utf-8')
        logFileWriter.write(str(logFileText))
        logFileWriter.close()
        self._pipe_loggingMessages('_write_dumpLog()',f'Wrote File: {logFilePath} With {len(logFileText)} Bytes')

    def _write_dumpRegistry(self,registerID=None):
        '''
        Alien._write_dumpRegistry(registerID=None/str)
        * Writes A json File With The Value Of Alien.registry[registerID]
        * If registerID Is None, Dump Every ID
        '''
        self._pipe_loggingMessages(f'_write_dumpRegistry(registerID={str(registerID)})','Operating')
        if os.path.isdir(str('output')) == False: os.mkdir('output')
        if registerID == None:
            compiledRegisters = {}
            for register in self.registry:
                registerIndex = self.registry[register].registerIndex
                for root in registerIndex: compiledRegisters[str(f'{registerID}.{registerIndex}')] = registerIndex[root]
            outputTitle = f'output/{str("_".join(time.ctime().split(" ")[1:4])).replace(":","_")}_registry.json'
            with open(str(outputTitle),'w') as outputWrite: json.dump(compiledRegisters,outputWrite,indent=2)
            self._pipe_loggingMessages(f'_write_dumpRegistry(registerID={str(registerID)})',f'Wrote File: {outputTitle} With {len(str(compiledRegisters))} Bytes')
        else:
            if str(registerID) in self.registry:
                registerIndex = self.registry[registerID]
                compiledRegister = self.registry[registerID].registerIndex
                outputTitle = f'{str("_".join(time.ctime().split(" ")[1:4])).replace(":","_")}_{registerID}.json'
                with open(str(outputTitle),'w') as outputWrite: json.dump(compiledRegister,outputWrite,indent=2)
                self._pipe_loggingMessages(f'_write_dumpRegistry(registerID={registerID})',f'Wrote File: {outputTitle} With {len(str(compiledRegister))} Bytes')
            else: self.alienException('_write_dumpRegistry',f'Variable registerID({registerID}) Is Not A Valid ID And Is Not None')

    def _remove_unInstall(self):
        self._pipe_loggingMessages('_remove_unInstall()','Operating...')
        '''
        Alien._remove_unInstall()
        * Deletes src,log,out Directories
        '''
        if os.path.isdir(str('src')) == True: os.rmdir('src')
        if os.path.isdir(str('log')) == True: os.rmdir('log')
        if os.path.isdir(str('out')) == True: os.rmdir('out')

    def _remove_logFiles(self):
        self._pipe_loggingMessages('_remove_logFiles()','Operating...')
        '''
        Alien._remove_logFiles()
        * Removes All Files Inside Of "logs/"
        '''
        if os.path.isdir(str('logs')) == True:
            filesToRemove = [f'logs/{logFile}' for logFile in os.listdir('logs')]
            for file in filesToRemove: os.remove(str(file))
        else: self.alienException('_remove_logFiles','\n\t* "logs" Path Is Non-Existant')

    def _remove_outFiles(self):
        self._pipe_loggingMessages('_remove_outFiles()','Operating...')
        '''
        Alien._remove_outFiles()
        * Removes All Files Inside Of "output/"
        '''
        if os.path.isdir(str('output')) == True:
            filesToRemove = [f'output/{outFile}' for outFile in os.listdir('output')]
            for file in filesToRemove: os.remove(str(file))
        else: self.alienException('_remove_outFiles','\n\t* "out" Path Is Non-Existant')

    ### Pipe Operation
    def _pipe_verboseMessages(self,root,message):
        '''
        Alien._pipe_loggingMessages(str,str)
        * Pipes Message To Screen
        '''
        if self.config['verboseStatus'] == True:
            message = f'@C-F.RED(@C-F.GREEN{root}@C-F.RED)@C-F.WHITE {message}';self.textToDisplayOperations.display(str(message))

    def _pipe_loggingMessages(self,root,message):
        '''
        Alien._pipe_loggingMessages(str,str)
        * Pipes Logging Messages
        '''
        if self.config['loggingStatus'] == True:
            timestamp = str(time.ctime())
            currentDir = str(os.getcwd())
            message = f'[LOG]\n\tTime: {timestamp}\n\tCurrent Directory: {currentDir}\n\tRoot Function: {root}\n\tMessage: {message}'
            self.config['loggingOutPipe'].append(str(message))
            if self.config['interpreterDeBug'] == True: self.textToDisplayOperations.display(str(message))

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
        self._pipe_loggingMessages(f'_retBool_verifyLocation({location})','Operating...')
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
        self._pipe_loggingMessages(f'_retBool_verifySignalCall({signalCall})','Operating...')
        '''
        Alien._retBool_verifySignalCall(str)
        * Returns True/False Is signalCall Is Existant In alien.jsonigure['signalCallTree']
        '''
        if str('.') in str(signalCall):
            signalTree = signalCall.split('.')
            if len(signalTree) == 2:
                if str(signalTree[0]) in self.config['signalCallTree']:
                    if str(signalTree[1]) in ['NULL','']: return True
                    else:
                        if str(signalTree[1]) in self.config['signalCallTree'][str(signalTree[0])]: return True
                        else: return False
                else: return False
            else: self.alienException('_retBool_verifySignalCall',f'\n\t* Variable signalCall({signalCall}) Is Not A Length Of 2 Post Sepeartion: ({len(signalTree)})')
        else:
            if str(signalCall) in self.config['signalCallTree']: return True
            else: return False

    ### Interpreter Operations
    def _interpreter_updateConfigureFile(self,confPath='src/alien.json'):
        self._pipe_loggingMessages(f'_interpreter_updateConfigureFile(confPath={confPath})','Operating...')
        '''
        Alien._interpreter_updateConfigureFile(confPath=str)
        * Deletes And ReGenerates Configuration File
        '''
        if os.path.isfile(str(confPath)) == True:
            os.remove(str(confPath));self._generate_alienConfigurationFile()
            self._pipe_loggingMessages(f'_interpreter_updateConfigureFile(confPath={confPath})',f'Removed {confPath} And Generated New Configuration')
        else: self.alienException('_interpreter_updateConfigureFile',f'\n\t* Variable confPath({confPath}) Is Non-Existant')

    def _interpreter_handleConfigureFile(self,confPath='src/alien.json',generateIfNotExist=True):
        self._pipe_loggingMessages(f'_interpreter_handleConfigureFile(confPath={confPath},generateIfNotExist={generateIfNotExist})','Operating...')
        '''
        Alien._interpreter_handleConfigureFile(confPath=str,generateIfNotExist=bool)
        * Reads Or Writes Configure File: "src/alien.json"
        * If confPath Does Not Exist Generate Is generateIfNotExist Is True
        '''
        if os.path.isfile(str(confPath)) == True:
            alienConfig = self._read_jsonFromPath(str(confPath))
            validConfg = True
            for configKey in alienConfig:
                if str(configKey) in ['alienConfig','textToDisplayConfig']:
                    for configSubKey in alienConfig['alienConfig']:
                        if str(configSubKey) in self.config:
                            self.config[str(configSubKey)]=alienConfig['alienConfig'][configSubKey]
                            self._pipe_loggingMessages(f'_interpreter_handleConfigureFile(confPath={confPath},generateIfNotExist={generateIfNotExist})',f'Configuring Location: Alien.configure[{configKey}] To {alienConfig["alienConfig"][configSubKey]}')
                    for ttdConfigKey in alienConfig['textToDisplayConfig']:
                        if str(ttdConfigKey) in self.textToDisplayOperations.config:
                            self.textToDisplayOperations.config[str(ttdConfigKey)] = alienConfig['textToDisplayConfig'][str(ttdConfigKey)]
                            self._pipe_loggingMessages(f'_interpreter_handleConfigureFile(confPath={confPath},generateIfNotExist={generateIfNotExist})',f'Configuring Location: Alien.textToDisplayOperations.config[{configKey}] To {alienConfig["textToDisplayConfig"][ttdConfigKey]}')
        else:
            if generateIfNotExist == True:
                self._generate_alienConfigurationFile()
                self._pipe_loggingMessages(f'_interpreter_handleConfigureFile(confPath={confPath},generateIfNotExist={generateIfNotExist})',f'Generated New Configuration Due To generateIfNotExist')
            else: self.alienException('_interpreter_handleConfigureFile',f'\n\t* File Path Is Non-Existant And generateIfNotExist({generateIfNotExist}) Is False\n\t* confPath({confPath})')

    def _interpreter_handleSysArgv(self,argv=sys.argv[1:]):
        self._pipe_loggingMessages(f'_interpreter_handleSysArgv(argv={argv})','Operating...')
        '''
        Alien._interpreter_handleSysArgv(argv=list)
        * Handles Arguments From sys.argv
        '''
        if len(argv) == 0:
            self._pipe_loggingMessages(f'_interpreter_handleSysArgv(argv={argv})','Operating With No Arguments...')
            self._interpreter_handleConfigureFile()
            if self.config['startInterpreterWithNoArg'] == True:
                self.interpreter()
                self._write_dumpLog()
                exit(1)
            else:
                self.textToDisplayOperations.displayUsage(self.config['usageDict'],query='(InLine)')
                exit(1)
        else:
            self._pipe_loggingMessages(f'_interpreter_handleSysArgv(argv={argv})',f'Operating With Arguments: {argv}')
            argumentTree = {
                # Display Usage
                'display.usageInfo':[False,None],
                # Logging Configure
                'logging.status':self.config['loggingStatus'],
                'logging.output':self.config['loggingOutPath'],
                # Verbose Configure
                'verbose.status':self.config['verboseStatus'],
                'verbose.debug':self.config['interpreterDeBug'],
                # Interpreter Configuraton
                'interpreter.failsafe':self.config['interpreterFailSafe'],
                'interpreter.init':False,
                # Configuration File
                'config.file':None,
                # Pre Operation
                'preop.startFresh':False,
                'preop.resetConfig':False,
                # Dump Configuration
                'dump.logOnExit':self.config['dumpLogOnExit'],
                'dump.RegistryOnExit':self.config['dumpRegistryOnExit'],
                # Execution Confguration
                'execute.interpreter':None,
                'execute.syntax':None,
                'execute.alienPath':None
            }

            for arg in argv:
                if str(':') in str(arg):
                    argTree = arg.split(':')
                    if str(argTree[0]) in ['-h','--help']: argumentTree['display.usageInfo']=[True,str(argTree[1])]
                    elif str(argTree[0]) in ['-cC','--configConfigFile']: argumentTree['config.file']=str(argTree[1])
                    elif str(argTree[0]) in ['-eI','--executeInterpreter']: argumentTree['execute.interpreter']= str(argTree[1])
                else:
                    if str(arg) in ['-h','--help']: argumentTree['display.usageInfo']=[True,None]
                    elif str(arg) in ['-lS','--logStatus']: argumentTree['logging.status']=False
                    elif str(arg) in ['-vS','--verStatus']: argumentTree['verbose.status']=False
                    elif str(arg) in ['-vD','--verDebug']: argumentTree['verbose.debug']= True
                    elif str(arg) in ['-sF','--startFresh']: argumentTree['preop.startFresh']=True
                    elif str(arg) in ['-sI','--startInterpreter']: argumentTree['interpreter.init'] = True
                    elif str(arg) in ['-cR','--configReset']: argumentTree['preop.resetConfig'] = True

            if argumentTree['display.usageInfo'][0] == True:
                if argumentTree['display.usageInfo'][1] == None:
                    self.textToDisplayOperations.displayUsage(self.config['usageDict'])
                    exit(1)
                else:
                    self.textToDisplayOperations.displayUsage(self.config['usageDict'],query=str(argTree[1]))
                    exit(1)
            if argumentTree['config.file'] != None:
                self._interpreter_handleConfigureFile(confPath=str(argTree[1]))
            else:
                self.config['loggingStatus']=argumentTree['logging.status']
                self.config['loggingOutPath']=argumentTree['logging.output']
                self.config['verboseStatus']=argumentTree['verbose.status']
                self.config['interpreterDeBug']=argumentTree['verbose.debug']
                self.config['interpreterFailSafe']=argumentTree['interpreter.failsafe']
                self.config['dumpLogOnExit']=argumentTree['dump.logOnExit']
                self.config['dumpRegistryOnExit']=argumentTree['dump.RegistryOnExit']
            # Pre-Operations
            if argumentTree['preop.startFresh'] == True:
                self._remove_logFiles()
                self._remove_outFiles()
            if argumentTree['preop.resetConfig'] == True:
                if os.path.isfile(str('src/alien.json')) == False:
                    self._generate_alienConfigurationFile()
                else:
                    os.remove('src/alien.json')
                    self._generate_alienConfigurationFile()
            # Executions
            if argumentTree['execute.interpreter'] != None:
                returnCode = self._interpreter_handleUserInput(str(argumentTree['execute.interpreter']))
            # Interpreter
            if argumentTree['interpreter.init'] == True:
                self.interpreter()


    def _interpreter_handleSyntaxLine(self,syntaxLine):
        self._pipe_loggingMessages(f'_interpreter_handleSyntaxLine({syntaxLine})','Operating')
        '''
        Alien._interpreter_handleSyntaxLine(str)
        * Handles Indivitual Alien Syntax
        '''
        if str('{') in str(syntaxLine) and str('}') in str(syntaxLine):
            if str(' ') in str(syntaxLine):
                syntaxOperand = str(syntaxLine.split('{')[0])
                syntaxInput = self.registryOperations._retDict_getCurlyBracketInString(str(syntaxLine))[syntaxOperand]
                syntaxOperandTree = [syntaxOp for syntaxOp in syntaxOperand.split(' ') if len(syntaxOp) > 0]
                if len(syntaxInput) == 0: syntaxInput = []
                else:
                    if str(',') in str(syntaxInput): syntaxInput = syntaxInput.split(',')
                    else: syntaxInput = [str(syntaxInput)]
                self._pipe_loggingMessages(f'_interpreter_handleSyntaxLine({syntaxLine})',f'Execution Operation Variables: syntaxOperand({syntaxOperand}) | syntaxOperandTree({syntaxOperandTree}) | syntaxInput({syntaxInput})')
                if str(syntaxOperandTree[0]) in ['0xff101','register.new']:
                    if str(syntaxOperandTree[1]) not in self.registry:
                        self.registry[str(syntaxOperandTree[1])]=self.registryHandle()
                        if len(syntaxInput) != 0:
                            ...
                        else: return '0xfff90'
                    else: self.alienException('_interpreter_handleSyntaxLine',f'\n\t* Operand: {syntaxOperand}[{syntaxOperandTree[1]}] Is Existant')
                else: self.alienException('_interpreter_handleSyntaxLine',f'\n\t* Invalid Syntax: {syntaxLine} By OperandID')
            else: self.alienException('_interpreter_handleSyntaxLine',f'\n\t* Invalid Syntax: {syntaxLine} By Seperator " "')
        else:
            ...

    def _interpreter_handleSyntaxList(self,syntaxList):
        self._pipe_loggingMessages(f'_interpreter_handleSyntaxList({syntaxList})','Operating...')
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
            self._pipe_loggingMessages(f'_interpreter_handleSyntaxList({syntaxList})',f'Output From Operation: {syntaxOutput}')
            return syntaxOutputs
        else: self.alienException('_interpreter_handleSyntaxList',f'\n\t* Variable syntaxList({syntaxList}) Is Not list Type')

    def _interpreter_handleUserInput(self,userInput):
        self._pipe_loggingMessages(f'_interpreter_handleUserInput({userInput})','Operating')
        '''
        Alien._interpreter_handleUserInput(str)
        * Handle interpreter() Input
        '''
        returnValue = [None,None]
        interpreterShortCuts = {
            'terminate.interpreter':[
                '0xfffa0',str(int(0xfffa0)),
                'terminate','Terminate','TERMINATE',
            ],
            'display.usage.main':[
                '0xfffb0',str(int(0xfffb0)),
                'usage','Usage','USAGE'
            ],
            'display.info.registry':[
                '0xfffb1',str(int(0xfffb1)),
                'displayRegistry','DisplayRegistry','DISPLAYREGISTRY'
            ]
        }
        if len(userInput) > 0:
            if str(' ') in str(userInput):
                # Syntax Operations
                if str('{') in str(userInput):
                    if str('}') in str(userInput):
                        syntaxOutput = self._interpreter_handleSyntaxList([str(userInput)])
                else:
                    # Interpreter Operations
                    userInputTree = userInput.split(' ')
                    if userInputTree[0] in interpreterShortCuts['terminate.interpreter']:
                        returnValue[0]='0xfffa0';self._pipe_loggingMessages('_interpreter_handleUserInput({userInput})','Returning Termnate Signal: "0xfffa0"')

                    elif userInputTree[0] in interpreterShortCuts['display.usage.main']:
                        queryString = str(' '.join(userInputTree[1:]))
                        self.textToDisplayOperations.displayUsage(self.config['usageDict'],query=str(queryString))
                        returnValue[0]='0xfff90';self._pipe_loggingMessages('_interpreter_handleUserInput({userInput})','Returning Continue Signal: "0xfff90"')
                        
                    else:
                        if str('.') in str(userInputTree[0]):
                            ...
                        else:
                            ...

            else:
                if str(userInput) in interpreterShortCuts['terminate.interpreter']:
                    returnValue[0]='0xfffa0';self._pipe_loggingMessages('_interpreter_handleUserInput({userInput})','Returning Termnate Signal: "0xfffa0"')
                elif str(userInput) in interpreterShortCuts['display.usage.main']:
                    returnValue[0] = '0xfff90';self.textToDisplayOperations.displayUsage(self.config['usageDict'])
                    self._pipe_loggingMessages(f'_interpreter_handleUserInput({userInput})','Returning Continue Signal: "0xfff90"')
                elif userInputTree[0] in str(interpreterShortCuts['display.info.registry']):
                    for register in self.registry:
                        self.textToDisplayOperations.display(f'Register: {register}\n\n\t* Length: {len(self.registry[register].registerIndex)}');returnValue='0xfff90'
        return returnValue


    def interpreter(self):
        self._pipe_loggingMessages('interpreter()','Operating')
        if self.config['interpreterHeartBeat'] == False: self.config['interpreterHeartBeat'] = True
        promptAppend = ''
        self.textToDisplayOperations.display('[!] Initialzing Alien Interpreter...')
        while self.config['interpreterHeartBeat'] == True:
            try:
                if len(promptAppend) == 0:
                    userPrompt = self.textToDisplayOperations._generate_userPrompt()+str(' (HOME) >')
                else:
                    userPrompt = self.textToDisplayOperations._generate_userPrompt()+str(f' ({promptAppend}) >')
                userInput = input(str(userPrompt))
                self._pipe_loggingMessages('interpreter()',f'Processing UserInput: {userInput}')
                if str(';') in str(userInput):
                    userInputTree = userInput.split(';')
                    for userInputKey in range(0,len(userInputTree)-1):
                        self._pipe_loggingMessages('interpreter()',f'Recieved Line Seperator ";", Executing {len(userInputTree)} Lines')
                        userInputReturn = self._interpreter_handleUserInput(str(userInputTree[userInputKey]))
                        if userInputReturn[0] == '0xfffa0':
                            self.textToDisplayOperations.display('@M-Alien.interpreterTerminate Due To User Input');self.config['interpreterHeartBeat']=False
                        elif userInputReturn[0] == '0xfff90': continue
                returnOutput = self._interpreter_handleUserInput(str(userInput))
                if returnOutput[0] == '0xfffa0':  # Terinate
                    self.textToDisplayOperations.display('@M-Alien.interpreterTerminate Due To User Input');self.config['interpreterHeartBeat']=False
                elif returnOutput[0] == '0xfff90': continue # Continue
            except Exception as E:
                self._pipe_loggingMessages('interpreter()',f'Recieved Exception: {E}')
                if self.config['interpreterFailSafe'] == False:
                    self.alienException('interpreter',f'\n\t* Failed Due To: {E}')
                else: continue
            except KeyboardInterrupt: continue
        if self.config['dumpLogOnExit'] == True:
            self._write_dumpLog()
        if self.config['dumpRegistryOnExit'] == True:
            self._write_dumpRegistry()
        exit(1)

    def alienException(self,root,message): raise Exception(f'\n* Alien.{root} -> Exception: {message}')

if __name__ == '__main__':
    app = Alien()
    app._interpreter_handleSysArgv()
