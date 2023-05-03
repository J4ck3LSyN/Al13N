# Author: J4ck3LSyN  | Github : https://www.github.com/J4ck3LSyN
# version 3.6.33
import os,time,sys,random,base64,string,threading,subprocess,json

class ExceptionHandler:
    def __init__(self,title,log=True,display=False,fail=False,rootOp=None):
        self.title =  str(title)

        self.log     = [ log, [] ]
        self.display = display
        self.fail    = fail

        self.rootOp  = rootOp


    def _pipe_log(self,m):
        if self.log[0] == True: self.log[1].append(str(m))

    def _pipe_display(self,prompt):
        if self.display == True:
            print(str(prompt))

    def _pipe_prompt(self,r,m):
        prompt = f'\n\t'.join([ f'Root Function: {self.title}.{r}',f'Time Stamp: {time.asctime()}',f'Current Working Directory: {os.getcwd()}',f'Message: {str(m)}' ])

        return str(prompt)


    def raiseException(self,r,m):
        prompt = self._pipe_prompt(r,m)

        if self.rootOp != None:
            prompt = str(self.rootOp._pipe_prompt(f'raise({r},{m})',f'Exception Message: {m}'))+str(f'\n\t^ {prompt}')

            self._pipe_log(str(prompt))
            self._pipe_display(str(prompt))

            self.rootOp._pipe_log(str(prompt))
            self.rootOp._pipe_display(str(prompt))

            if self.fail == False:
                if self.rootOp.fail == False:
                    raise self.rootOp.raiseException(f'{self.title}.{r}',str(prompt))
        else:
            self._pipe_log(str(prompt))
            self._pipe_display(str(prompt))

            if self.fail == False:
                raise Exception(str(prompt))

class DisplayHandler:
    def __init__(self,rootPathPrompt=os.getcwd()):
        if str('\\') in str(rootPathPrompt): rootPathPrompt = rootPathPrompt.replace('\\','/')

        self.rootPathPrompt = rootPathPrompt

        self.displayConfig = {
            'F':{'BLACK': '\x1b[30m', 'BLUE': '\x1b[34m', 'CYAN': '\x1b[36m', 'GREEN': '\x1b[32m', 'LIGHTBLACK_EX': '\x1b[90m', 'LIGHTBLUE_EX': '\x1b[94m', 'LIGHTCYAN_EX': '\x1b[96m', 'LIGHTGREEN_EX': '\x1b[92m', 'LIGHTMAGENTA_EX': '\x1b[95m', 'LIGHTRED_EX': '\x1b[91m', 'LIGHTWHITE_EX': '\x1b[97m', 'LIGHTYELLOW_EX': '\x1b[93m', 'MAGENTA': '\x1b[35m', 'RED': '\x1b[31m', 'RESET': '\x1b[39m', 'WHITE': '\x1b[37m', 'YELLOW': '\x1b[33m'},
            'B':{'BLACK': '\x1b[40m', 'BLUE': '\x1b[44m', 'CYAN': '\x1b[46m', 'GREEN': '\x1b[42m', 'LIGHTBLACK_EX': '\x1b[100m', 'LIGHTBLUE_EX': '\x1b[104m', 'LIGHTCYAN_EX': '\x1b[106m', 'LIGHTGREEN_EX': '\x1b[102m', 'LIGHTMAGENTA_EX': '\x1b[105m', 'LIGHTRED_EX': '\x1b[101m', 'LIGHTWHITE_EX': '\x1b[107m', 'LIGHTYELLOW_EX': '\x1b[103m', 'MAGENTA': '\x1b[45m', 'RED': '\x1b[41m', 'RESET': '\x1b[49m', 'WHITE': '\x1b[47m', 'YELLOW': '\x1b[43m'},
            'S':{'BRIGHT': '\x1b[1m', 'DIM': '\x1b[2m', 'NORMAL': '\x1b[22m', 'RESET_ALL': '\x1b[0m'},
            'M':{
                'Alien.headerMain':'@C-F.GREEN[@C-F.WHITEAlien(@C-F.RED3.6.33@C-F.WHITE)@C-F.GREEN]\n@:>@C-F.YELLOW ',
                'Alien.promptHead':f'@C-F.GREEN(@C-F.WHITE~/{str(self.rootPathPrompt).split("/")[len(self.rootPathPrompt.split("/"))-1]}/@C-F.GREEN) @ (@C-F.WHITEAlien(3.6.33)@C-F.GREEN)',
                'Alien.promptFoot':'\n@C-F.YELLOW@:>>>@C-F.WHITE '
            },
            'colorKey':['@C-',''],
            'messageKey':['@M-','']
        }

        self.displayHandlerException = ExceptionHandler('DisplayHandler')

        self.alienConfig = {}

        if os.name == "nt":
            try:
                import colorama
                colorama.init()
            except Exception as E:
                self.exception(f'__init__.py',f'(Windows) Required Colorama Module Use: "pip3 install colorama" To Continue:{E}')

    def _message_replaceColors(self,message):
        colorKeys = ['F','B','S']
        for cK in colorKeys:
            for subKey in self.displayConfig[str(cK)]:
                messageKeyTarget = f'{self.displayConfig["colorKey"][0]}{cK}.{subKey}{self.displayConfig["colorKey"][1]}'
                if str(messageKeyTarget) in str(message):
                    message = message.replace(str(messageKeyTarget),self.displayConfig[cK][subKey])
        return message

    def _message_replaceMessages(self,message):
        for messageKey in self.displayConfig['M']:
            messageKeyTarget = f'{self.displayConfig["messageKey"][0]}{messageKey}{self.displayConfig["messageKey"][1]}'
            if str(messageKeyTarget) in str(message):
                message = message.replace(str(messageKeyTarget),str(self.displayConfig["M"][str(messageKey)]))
        return message

    def _message_pipe(self,message):
        message = self._message_replaceMessages(str(message))
        message = self._message_replaceColors(str(message))
        return str(message)

    def displayText(self,message,header='@M-Alien.headerMain'):
        message = f'{message}@C-S.RESET_ALL'
        print(self._message_pipe(str(f'{header}{message}')))

    def returnPrompt(self):
        return [ self._message_replaceColors(self._message_replaceMessages('@M-Alien.promptHead')),self._message_replaceColors(self._message_replaceMessages('@M-Alien.promptFoot')) ]

    def alienOperator(self,operand):
        ...

    def exception(self,r,m):
        self.displayHandlerException.raiseException(str(r),str(m))

class RegistryHandler:
    def __init__(self):
        self.registryHandlerException = ExceptionHandler('RegistryHandler')
        self.registryVariableHandle   = VariableHandler()
        self.registryFileHandle       = FileHandler()

        self.registry = {}

        self.alienConfig = {}
    # Generation And Write Operations
    def new(self,registerID,minimumRange,maximumRange,offset,padding):
        if str(registerID) not in self.registry:
            if self.registryVariableHandle.isType([minimumRange,maximumRange,offset,padding],['01','01','01','01']) == True:
                register = {
                    'info':{
                        'minimumRange':minimumRange,
                        'maximumRange':maximumRange,
                        'offset':offset,
                        'padding':padding
                    },
                    'keymap':{},
                    'segment':{},
                    'pageIndex':[]
                }
                if minimumRange < maximumRange:
                    for segment in range(minimumRange,maximumRange):
                        segmentHex = self.registryVariableHandle.appendZeroBytes(self.registryVariableHandle.intToHex(segment),padding).split('0x')[1]
                        register['segment'][str(segmentHex)]=[]
                        register['pageIndex'].append(str(segmentHex))
                    self.registryVariableHandle.newKeyMap(minimumRange,maximumRange,offset,padding);register['keymap']=self.registryVariableHandle.keymap;self.registryVariableHandle.keymap = {}
                    self.registry[str(registerID)]=register
                else: self.exception(f'new({registerID},{minimumRange},{maximumRange},{offset},{padding})',f'minimumRange({minimumRange}) Is Less Than maximumRange({maximumRange})')
            else: self.exception(f'new({registerID},{minimumRange},{maximumRange},{offset},{padding})',f'Input Variables Are Not Required Type ')
        else: self.exception(f'new({registerID},{minimumRange},{maximumRange},{offset},{padding})',f'registerID({registerID}) Is Existant')


    def write(self,registerID,pageID,pageType,pageValue):
        if str(registerID) in self.registry:
            register = self.regsitry[str(registerID)]
            try:
                pageID = self._register_pageIDIdentity(pageID,register)

                if pageType in ['a0','var(str)']:

                    pageValue = self.registryVariableHandle.encodeKeyMap(pageValue,keymap=register['keymap'])
                    pageHead  = f'a0{pageValue[0][2:]}'
                    pageFoot  = f'a1{pageValue[0][len(pageValue)-1]}'

                    pageValue[0] = str(pageHead)
                    pageValue[len(pageValue)-1] = pageFoot

                    register['segment'][str(pageID)] = pageValue

                    self.registry[str(registerID)]=register

                else: raise Exception(f'pageType({pageType}) Is Invalid')
            except Exception as e:
                self.exception(f'write({registerID},{pageID},{pageType},{pageValue})',f'Exception: {e}')

    # Register Operations
    def _register_pageIDIdentity(self,pageID,register):
        if str(pageID[:2]) == str('i:'):
            pageHex = str(pageID[2:])
            if self.registryVariableHandle.isType(pageHex,'08') == True:
                pageInt = self.registryVariableHandle.hexToInt(pageHex)
                if pageInt < len(register['pageIndex']):
                    return register['pageIndex'][pageInt]
                else: self.exception(f'_register_pageIDIdentity({pageID},{register})',f'pageID({pageID}) Int({pageInt}) Is Not Inside Of pageIndex Scope({len(register["pageIndex"])})')
            else: self.exception(f'_register_pageIDIdentity({pageID},{register})',f'pageID({pageID}) Does Not Contain A Hexadecimal Value')
        elif str(pageID[:2]) == str('p:'):
            pageTarget = str(pageID[2:])
            if str(pageTarget) in register['pageIndex']:
                return pageTarget
            else: self.exception(f'_register_pageIDIdentity({pageID},{register})',f'pageID({pageID}) pageTarget({pageTarget}) Is Not A Valid Path')
        else: self.exception(f'_register_pageIDIdentity({pageID},{register})',f'pageID({pageID}) Is A Invalid Input <index/page>:<value>')

    # Json Load And Dump Operations
    def load(self,path):
        ...

    def dump(self,path):
        ...

    # Packing/Unpacking Operations
    def pack(self,registerID,pageID=None):
        ...

    def unpack(self,data):
        ...

    def alienOperator(self,operand):
        if self.registryVariableHandle.isType(operand,'02') == True:
            operator=operand[0];operatorArg=operand[1:]

        else: self.exception(f'alienOperator({operand})',f'Operand Input Is Not list')

    def exception(self,r,m):
        self.registryHandlerException.raiseException(str(r),str(m))

class VariableHandler:
    def __init__(self):
        self.variableHandlerException = ExceptionHandler('VariableHandler')

        self.variables   = {}

        self.keymap      = {}

        self.alienConfig = {}

    # Boolean Operations
    def flipBoolean(self,varIN):
        if self.isType(varIN,'04') == True:
            if varIN == False: return True
            else: return False
        else: self.exception(f'flipBoolean({varIN})',f'varIN({varIN}) Is Not Bool(04) Type')

    # Information Operations
    def getLen(self,varIN):
        return len(varIN)

    def getType(self,varIN,alien=False):
        if alien == False:
            if type(varIN) == str:
                return '00'
            elif type(varIN) == int:
                return '01'
            elif type(varIN) == list:
                return '02'
            elif type(varIN) == dict:
                return '03'
            elif type(varIN) == bool:
                return '04'
            elif str(type(varIN)) == str("<class 'bytes'>"):
                return '05'
            elif str(type(varIN)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]:
                return '06'
            elif type(varIN) == tuple:
                return '07'
            elif self.hexOnlyChar(str(varIN)) == True:
                return '08'
        else:
            ...

    def isType(self,varIN,varType,varIter=False):
        if varIter == True:
            if [self.isType(varIN,'02'),self.isType(varType,'02')] == [True,True]:
                if self.getLen(varIN) == self.getLen(varType):
                    returnOut = []
                    for i in range(0,len(varIN)):
                        returnOut.append(self.isType(varIN[i],varType[i]))
                    return returnOut
                else: self.exception(f'isType({varIN},{varType},varIter={varIter})',f'varIN({varIN}) And varType({varType}) Are Not Equal Lengths')
            else: self.exception(f'isType({varIN},{varType},varIter={varIter})',f'varIN({varIN}) Or varType({varType}) Are Not list(02) Types')
        else:
            varTypeConfig = None
            if varType in ['00','s','S','str','Str','STR',0]:
                varTypeConfig = str
            elif varType in ['01','i','I','int','Int','INT',1]:
                varTypeConfig = int
            elif varType in ['02','l','L','list','List','LIST',2]:
                varTypeConfig = list
            elif varType in ['03','d','D','dict','Dict','DICT',3]:
                varTypeConfig = dict
            elif varType in ['04','b','B','bool','Bool','BOOL',4]:
                varTypeConfig = bool
            elif varType in ['05','x','X','byte','Byte','BYTE',5]:
                if str(type(varIN)) == str("<class 'bytes'>"): return True
            elif varType in ['06','f','F','func','Func','FUNC',6]:
                if str(type(varIN)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]: return True
            elif varType in ['07','t','T','tuple','Tuple','TUPLE',7]:
                varTypeConfig = tuple
            elif varType in ['08','h','H','hex','Hex','HEX',8]:
                if str(varIN[:2]) == str('0x'):
                    if self.hexOnlyChar(str(varIN)) == True: return True
            if varTypeConfig != None:
                return isinstance(varIN,varTypeConfig)
            else: return False

    # Hex Operations
    def intToHex(self,varIN):
        if self.isType(varIN,'01') == True:
            return str(hex(varIN))
        else: self.exception(f'intToHex({varIN})',f'varIN({varIN}) Is Not int(01) Type')

    def hexToInt(self,varIN):
        if str(varIN[:2]) == str('0x'):
            return int(varIN,16)
        else: self.exception(f'hexToInt({varIN})',f'varIN({varIN}) Is Not hex Type')

    def hexOnlyChar(self,varIN):
        validChars = '0123456789abcdefABCDEF'
        returnBool = True
        if str(varIN[:2]) == '0x': varIN = str(varIN[2:])
        for char in str(varIN):
            if str(char) not in validChars:
                returnBool = False;break
        return returnBool

    def appendZeroBytes(self,varIN,varPad):
        if str(varIN[:2]) == str('0x'): varIN = str(varIN).strip('0x')
        if len(varIN) < varPad:
            return str('0x')+str('0'*int(varPad-len(varIN)))+str(varIN)
        else: return f'0x{varIN}'

    def stripBytes(self,varIN,varBuffer):
        if str(varIN[:2]) == str('0x'): varIN = str(varIN).strip('0x')
        record = [ False, '', [] ]
        for char in str(varIN):
            if record[0] == False:
                record[0] = True
                record[1] = str(char)
            else:
                record[1] = f'{record[1]}{char}'
                if len(record[1]) == int(varBuffer):
                    record[2].append(str(record[1]))
                    record[0] = False
                    record[1] = ''
        return record[2]

    # Keymap Operations
    def newKeyMap(self,minimumRange,maximumRange,offset,padding):
        if minimumRange < maximumRange:
            keymap = {}
            for char in range(minimumRange,maximumRange):
                charKey = chr(char)
                charHex = self.appendZeroBytes(self.intToHex(int(char+offset)),padding).split('0x')[1]
                keymap[str(charKey)] = str(charHex)
            self.keymap = keymap
            return keymap
        else: self.exception(f'newKeyMap({minimumRange},{maximumRange},{offset},{padding})',f'minimumRange({minimumRange}) Is Not Less Tha maximumRange({maximumRange})')

    def encodeKeyMap(self,varIN,keymap=None):
        if keymap == None: keymap = self.keymap
        encoded = []
        for char in str(varIN):
            if str(char) in keymap:
                encoded.append(keymap[char])
        return encoded

    def decodeKeyMap(self,varIN,padding,keymap=None):
        if keymap == None: keymap = self.keymap
        decoded = []
        varINTree = self.stripBytes(varIN,padding)
        for char in varINTree:
            for key in keymap:
                if str(char) == str(keymap[key]): decoded.append(str(key))
        return decoded

    # Alien Operator
    def alienOperator(self,operand):
        ...

    def exception(self,r,m):
        self.variableHandlerException.raiseException(str(r),str(m))


class FileHandler:
    def __init__(self):
        self.fileHandlerException = ExceptionHandler('FileHandler')
        self.fileHandlerVariable = VariableHandler()

        self.alienConfig = {}

    # File Existance
    def existFile(self,path):
        return os.path.isfile(str(path))

    def existPath(self,path):
        return os.path.isdir(str(path))
    # Read Operations
    def readText(self,path,encoding='utf-8'):
        if self.existFile(path) == True:
            fileData = ''
            with open(str(path),'r',encoding=encoding) as fileRead:
                fileData = fileRead.read()
            return fileData
        else: self.exception(f'readText({path})',f'path({path}) Is Invalid')

    def readJson(self,path):
        if self.existFile(path) == True:
            jsonData = None
            with open(str(path),'r') as jsonRead:
                jsonData = json.load(jsonRead)
            return jsonData
        else: self.exception(f'readJson({path})',f'path({path}) Is Invalid')

    def readData(self,path):
        ...

    def readDir(self,path):
        if self.existPath(str(path)) == True:
            return os.listdir(str(path))
        else: self.exception(f'readDir({path})',f'path({path}) Is Non-Existant')

    # Write Operations
    def writeJson(self,path,data,indent=2):
        try:
            with open(str(path),'w') as jsonPath:
                json.dump(data,jsonPath,indent=2)
        except Exception as E: self.exception(f'writeJson({path},{data},indent={indent})',f'Exception: {E}')

    def writeText(self,path,data,encoding='utf-8'):
        with open(str(path),'w',encoding=encoding) as textPath:
            textPath.write(str(data))

    def writeData(self,path,data):
        ...

    def writeDirectory(self,path,dname):
        if self.existPath(str(path)) == True:
            if str(dname) not in self.readDir(str(path)):
                os.mkdir(str(f'{path}/{dname}'))
            else: self.exception(f'writeDirectory({path},{dname})',f'dname({dname}) Is Existant')
        else: self.exception(f'writeDirectory({path},{dname})',f'path({path}) Is Non-Existant')

    def removeItemsInPath(self,path):
        if self.existPath(str(path)) == True:
            pathList = self.readDir(str(path))
            for pathItem in pathList:
                delPath = f'{path}/{pathItem}'
                os.remove(str(delPath))
        else: self.exception(f'removeItemsInPath({path})',f'path({path}) Is Non-Existant')

    def removeFile(self,path):
        if self.existFile(str(path)) == True:
            os.remove(str(path))
        else: self.exception(f'removeFile({path})',f'path({path}) Is Non-Existant Or Is Not File')

    # Alien Operator
    def alienOperator(self,operand):
        ...

    def exception(self,r,m):
        self.fileHandlerException.raiseException(str(r),str(m))

class Alien:
    def __init__(self,rootPath=os.getcwd(),install=False):
        if str('\\') in str(rootPath): rootPath = str(rootPath).replace('\\','/')
        self.rootConfig = {
            'root':{
                'path':rootPath,
                'conf':'alienConfig.json',
                'installStatus':install,
                'installTemplate':None,
                'modExternal':None,
                'exceptFailSafe':False,
                'startInterpreterNoInput':False
            },
            'info':{
                'timeStamp':str(time.asctime())
            },
            'float':{
                'interpreter.registry.root':[],
                'interpreter.project.root':{},
                'interpreter.status':False,
                'interpreter.errorMax':0x5,
                'interpreter.errorCount':0x0

            },
            'logging':{
                'status':False,
                'pipe':[],
                'path':'logs/$_alien(3-6-33).log',
                'dumpOnExit':True
            },
            'verbose':{
                'status':True,
                'level':1,
                'pipe':[]
            },
            'init':{
                'execute.stdin':[],
                'execute.path':None
            },
            'registry':{
                'mimimalSegmentLength':0x1111,
                'maximumSegmentLength':0xffff,
                'segmentOffset':0x3e7,
                'padding':0x4
            },
            'encoding':{
                'keymap':{},
                'minimumRange':0x1f,
                'maximumRange':0x80,
                'offset':0x3e7,
                'padding':0x4
            },
            'projects':{
                'lastEdited':None
            }
        }

        self.universe = {}
        self.signalTree = {}

        self.alienException = ExceptionHandler('Alien')
        self.alienRegistry  = RegistryHandler()
        self.alienRegistry.registryHandlerException.rootOp = self.alienException
        self.alienVariable  = VariableHandler()
        self.alienVariable.variableHandlerException.rootOp = self.alienException
        self.alienFile      = FileHandler()
        self.alienFile.fileHandlerException.rootOp = self.alienException
        self.alienDisplay   = DisplayHandler()
        self.alienDisplay.displayHandlerException.rootOp = self.alienException


    # signalTree Operations
    def _signalTree_new(self,operatorID,operatorFunction):
        self._pipe_logging(f'_signalTree_new({operatorID},{operatorFunction})','Operating...')
        if str(operatorID) not in self.signalTree:
            if self.alienVariable.isType(operatorFunction,'06') == True:
                try:
                    alienOperatorMount   = operatorFunction()
                    alienOperatorConfig  = alienOperatorMount.alienConfig
                    alienOperatorExecute = alienOperatorMount.alienOperator

                except Exception as e:
                    self.exception(f'_signalTree_new({operatorID},{str(operatorFunction)})',f'Opreation Failed Due To: {e}')
            else: self.exception(f'_signalTree_new({operatorID},{str(operatorFunction)})',f'operatorFunction({str(operatorFunction)}) Is Not func(06) Type')
        else: self.exception(f'_signalTree_new({operatorID},{str(operatorFunction)})',f'operatorID({operatorID}) Is Existant')

    def _signalTree_operate(self,operatorID,operand):
        self._pipe_logging(f'_signalTree_operate({operatorID},{operand})','Operating...')
        ...

    # Syntax Operations
    def _syntax_dataHandle(self,syntaxData):
        self._pipe_logging(f'_syntax_init({syntaxData})','Operating...')
        if self.alienVariable.isType(syntaxData,'03') == True:
            operatorTree = []
            for operatorKey in syntaxData:
                ...

        else: self.exception(f'_syntax_init({syntaxData})',f'syntaxData({syntaxData}) Is Not dict(03) Type')

    def _syntax_textHandle(self,syntaxText):
        return json.loads(json.dumps(str(syntaxText)))

    # Initialization
    def _init_handleSysArgv(self,argvTreeConfig=None):
        self._pipe_logging('_init_handleSysArgv()','Operating...')
        if len(sys.argv[1:]) == 0:
            if self.rootConfig['root']['startInterpreterNoInput'] == True:
                self._pipe_logging('_init_handleSysArgv()',f'[Internal] - root.startInterpreterNoInput:{self.rootConfig["root"]["startInterpreterNoInput"]} | True\n[!] Starting Interpreter Functions...')
                self.interpreter()
        else:
            configureTree = self.rootConfig

            argvTree = {
                'startFresh':False,
                'startInterpreter':False,
                'updateConfig':False,
                'developerExecute':False,
                'developerConsole':False,
            }


            for arg in sys.argv[1:]:
                if str(arg) in ['a001','-sF','--startFresh']:
                    argvTree['startFresh'] = self.alienVariable.flipBoolean(argvTree['startFresh'])
                elif str(arg) in ['a002','-sI','--startInterpreter']:
                    argvTree['startInterpreter'] = self.alienVariable.flipBoolean(argvTree['startInterpreter'])
                elif str(arg) in ['a011','-uC','--updateConfig']:
                    argvTree['updateConfig'] = self.alienVariable.flipBoolean(argvTree['updateConfig'])
                elif str(arg) in ['ad01','-dE','--developerExecute']:
                    argvTree['developerExecute'] = self.alienVariable.flipBoolean(argvTree['developerExecute'])
                elif str(arg) in ['ad02','-dC','--developerConsole']:
                    argvTree['developerConsole'] = self.alienVariable.flipBoolean(argvTree['developerConsole'])

            # a001
            if argvTree['startFresh'] == True:
                self.alienFile.removeItemsInPath(f'{self.rootConfig["root"]["path"]}/logs/')

            self._pipe_logging('_init_handleSysArgv()',f'Current Configuration Tree:\n{json.dumps(configureTree,indent=3)}\nArgV Tree:\n{json.dumps(argvTree,indent=3)}')

            # Update Log (Second To Last For Pare And Execute)
            # a011
            if argvTree['updateConfig'] == True:
                self.alienFile.removeFile(f'{configureTree["root"]["path"]}/src/{configureTree["root"]["conf"]}')
                self.alienFile.writeJson(f'{configureTree["root"]["path"]}/src/{configureTree["root"]["conf"]}',configureTree)

            self.rootConfig = configureTree
            # Developer Function Call (For Testing Internal Functions Alien._init_developerExecute())
            # ad01
            if argvTree['developerExecute'] == True:
                # ad02
                if argvTree['developerConsole'] == True:
                    self._init_developerExecute(devConsole=True)
                else:
                    self._init_developerExecute()
            # ad02
            if argvTree['developerConsole'] == True:
                self._init_developerExecute(devConsole=True)
            # Interpreter (Last To Parse And Execute)
            # a002
            if argvTree['startInterpreter'] == True:
                self.interpreter()

    def _init_developerExecute(self,devConsole=False):
        if devConsole == False:
            self._universe_newSolar('Alien-Example')
        else:
            ...


    def init(self):
        self._pipe_logging('init()','Operating...')
        rootPath = self.rootConfig['root']['path']
        if self.alienFile.existPath(f'{rootPath}/src') == False:
            self.alienFile.writeDirectory(rootPath,'src')
            self._pipe_logging('init()',f'Wrote Directory: {rootPath}/src')
        if self.alienFile.existFile(f'{rootPath}/src/{self.rootConfig["root"]["conf"]}') == False:
            self._pipe_logging('init()',f'Wrote File: {rootPath}/src/{self.rootConfig["root"]["conf"]}')
            self.rootConfig['info']['timeStamp'] = ''
            self.alienFile.writeJson(f'{rootPath}/src/{self.rootConfig["root"]["conf"]}',self.rootConfig)

        self.rootConfig = self.alienFile.readJson(f'{rootPath}/src/{self.rootConfig["root"]["conf"]}')
        self.rootConfig['info']['timeStamp'] = str(time.asctime())

        self._pipe_logging('init()',f'Configured rootConfig To {rootPath}/src/{self.rootConfig["root"]["conf"]} |\n{json.dumps(self.rootConfig,indent=3)}\n')

        if self.alienFile.existPath(f'{rootPath}/src/mod') == False:
            self.alienFile.writeDirectory(rootPath,'/src/mod')
            self._pipe_logging('init()',f'Wrote Direcotry: {rootPath}/src/mod')
        if self.alienFile.existPath(f'{rootPath}/src/lib') == False:
            self.alienFile.writeDirectory(rootPath,'/src/lib')
            self._pipe_logging('init()',f'Wrote Direcotry: {rootPath}/src/lib')
        if self.alienFile.existFile(f'{rootPath}/src/lib/alienLibraries.json') == False:
            self.alienFile.writeJson(f'{rootPath}/src/lib/alienLibraries.json',{})
            self._pipe_logging('init()',f'Wrote File: {rootPath}/src/lib/alienLibraries.json')
        if self.alienFile.existFile(f'{rootPath}/src/mod/alienModule.json') == False:
            self.alienFile.writeJson(f'{rootPath}/src/mod/alienModule.json',{})
            self._pipe_logging('init()',f'Write File: {rootPath}/src/mod/alienModule.json')
        if self.alienFile.existPath(f'{rootPath}/src/mod/__init__.py') == False:
            self.alienFile.writeText(f'{rootPath}/src/mod/__init__.py','# Module Init File For Alien(3.6.33) | J4ck3LSyN')
            self._pipe_logging('init()',f'Wrote File: {rootPath}/src/mod/__init__.py ')
        if self.alienFile.existPath(f'{rootPath}/projects') == False:
            self.alienFile.writeDirectory(rootPath,'projects')
            self._pipe_logging('init()',f'Wrote Directory: {rootPath}/projects')

        self._pipe_logging('init()',f'Passing To Alien._init_handleSysArgv()')
        operator = self._init_handleSysArgv()

        self.alienVariable.newKeyMap(self.rootConfig['encoding']['minimumRange'],self.rootConfig['encoding']['maximumRange'],self.rootConfig['encoding']['offset'],self.rootConfig['encoding']['padding'])

        if self.rootConfig['logging']['dumpOnExit'] == True:
            self._pipe_dumpLog()

    # Pipe Operations
    def _pipe_display(self,message,messageHead=None):
        if self.rootConfig['verbose']['status'] == True:
            self.rootConfig['verbose']['pipe'].append(str(message))
            if messageHead == None:
                self.alienDisplay.displayText(str(message))
            else:
                self.alienDisplay.displayText(str(message),header=str(messageHead))

    def _pipe_logging(self,root,message):
        if self.rootConfig['logging']['status'] == True:
            timestamp = self.rootConfig['info']['timeStamp']
            currentWorkingDir = self.rootConfig['root']['path']
            message = f'Alien(3.6.33)[LOG]\n\t* Started Time: {timestamp}\n\t* Log Time: {time.asctime()}\n\t* Current Working Directory: {currentWorkingDir}\n\t* Root Function: {root}\n\t* Message: {message}'
            self.rootConfig['logging']['pipe'].append(str(message))
            if self.rootConfig['verbose']['level'] == 2:
                self._pipe_display(str(message))

    def _pipe_dumpLog(self):
        logPath = self.rootConfig['logging']['path']
        logPath = logPath.replace('$',str('_'.join(time.asctime().split(' ')[1:5])).replace(':','-'))
        logText = []
        for line in self.rootConfig['logging']['pipe']:
            logText.append(f'[LOG]\n\t{line}')
        for line in self.rootConfig['verbose']['pipe']:
            logText.append(f'[VER]\n\t{line}')

        if len(self.alienException.log[1]) > 0:
            for line in self.alienException.log[1]:
                logText.append(f'[EXP]\n\t{line}')

        self.alienFile.writeText(str(logPath),str('\n'.join(logText)))

    def _pipe_dumpConfig(self):
        rootPath = self.rootConfig['root']['path']
        alienConfigPath = f'{rootPath}/src/{self.rootConfig["root"]["conf"]}'
        self.alienFile.writeJson(str(alienConfigPath),self.rootConfig)

    # Configuration
    def _configure_flipFailSafeGlobalStatus(self):
        if self.alienRegistry.registryHandlerException.fail == False: self.alienRegistry.registryHandlerException.fail = True
        else: self.alienRegistry.registryHandlerException.fail = False
        if self.alienVariable.variableHandlerException.fail == False: self.alienVariable.variableHandlerException.fail = True
        else: self.alienVariable.variableHandlerException = False
        if self.alienFile.fileHandlerException.fail == False: self.alienFile.fileHandlerException.fail = True
        else: self.alienFile.fileHandlerException.fail = False
        if self.alienDisplay.displayHandlerException.fail == False: self.alienDisplay.displayHandlerException.fail = True
        else: self.alienDisplay.displayHandlerException.fail = False
        if self.alienException.fail == False: self.alienException.fail = True
        else: self.alienException.fail = True

    def _configure_checkFailSafe(self):
        return self.alienException.fail

    def _configure_verifyExternal(self):
        if self.alienFile.existFile(f'{self.rootConfig["root"]["path"]}/src/alienConfig.json') == False:
            return False
        else: return True


    # Interpreter
    def interpreter(self,consoleType='interpreterRoot'):
        self._pipe_logging('interpreter()','Operating...')
        if self.rootConfig['float']['interpreter.status'] == False: self.rootConfig['float']['interpreter.status'] = True
        self._pipe_display('Beging Alien Interpreter...')
        dependantStatus = True
        consoleStack    = [consoleType]
        consoleCurrent  = consoleType
        consoleRestart  = False
        while self.rootConfig['float']['interpreter.status'] == True and dependantStatus == True:
            try:
                prompt = self.alienDisplay.returnPrompt()
                append = []
                if len(self.rootConfig['float']['interpreter.registry.root']) != 0:
                    ...
                if len(self.rootConfig['float']['interpreter.project.root']) != 0:
                    ...
                if len(append) == 0:
                    userInput = input(f'{prompt[0]}(Console:{consoleCurrent}){prompt[1]}')
                    self._pipe_logging('interpreter()',f'User Input: {userInput}')
                # Global Console Commands
                if userInput in ['ff01','interpreter.terminate']:
                    if len(consoleStack) == 1:
                        self.rootConfig['float']['interpreter.status'] = False
                    else:
                        consolePrior = consoleStack[len(consoleStack)-1]
                        consoleCurrent = consolePrior
                        consoleStack = consoleStack[:len(consoleStack)-1]

                    # interpreterRoot Commands
                    if consoleCurrent == 'interpreterRoot':
                        ...
                    # developerConsole Commands
                    elif consoleCurrent == 'developerConsole':
                        ...
                    # projectConsole Commands
                    elif consoleCurrent == 'projectConsole':
                        ...
                    # libraryConsole Commands
                    elif consoleCurrent == 'libraryConsole':
                        ...
                    # externalConsole Commands
                    elif consoleCurrent == 'externalConsole':
                        ...

            except Exception as E:
                if self.rootConfig['root']['exceptFailSafe'] == True:
                    self._pipe_logging('interpreter()',f'Exception: {E}')
                else: self.exception('interpreter()',f'Exception: {E}')
            except KeyboardInterrupt:
                errorCount = self.rootConfig['float']['interpreter.errorCount']
                maxCount   = self.rootConfig['float']['interpreter.errorMax']
                if self.rootConfig['float']['interpreter.errorCount'] >= self.rootConfig['float']['interpreter.errorMax']:
                    self._pipe_logging('interpreter()','Exiting Due To KeyboardInterrupt')
                    self._pipe_display('[!] Terminating Alien Due To KeyboardInterrupt...')
                    dependantStatus = False
                else:
                    self._pipe_logging('interpreter()','Recieved KeyboardInterrupt Interupt')
                    self.rootConfig['float']['interpreter.errorCount'] += 1

        if consoleRestart == True:
            self.rootConfig['float']['interpreter.status'] = True
            self.interpreter()
        else:
            return


    # Registry Operations
    def _universe_convertID(self,ID,keymap):
        IDGen = self.alienVariable.encodeKeyMap(str(solarID),keymap=solarKeymap)
        IDGen = self.alienVariable.hexToInt(f'0x{"".join(solarKey)}')
        return [ ID,IDGen ]

    def _universe_newSolar(self,solarID):
        encoding = self.rootConfig['encoding']
        solarKeymap = self.alienVariable.newKeyMap(encoding['minimumRange'],encoding['maximumRange'],encoding['offset'],encoding['padding'])
        solarKeyID = self._universe_convertID(str(solarID),solarKeyHex)
        self.universe[str(solarKeyHex)] = {
            '':{}
        }

    def _universe_newPlanet(self,solarID,planetID):
        ...

    # Module Operations /src/mod
    def _module_readModules(self):
        ...

    def _module_config(self):
        if self.alienFile.existFile(f'{self.rootConfig["root"]["path"]}/src/mod/alienModule.json') == True:
            ...
        else:
            ...

    def _module_writeRawConfig(self):
        ...

    def _module_updateConfig(self):
        ...

    # Library Operations /src/lib
    def _library_readLibrary(self):
        ...

    def _library_config(self):
        if self.alienFile.existFile(f'{self.rootConfig["root"]["path"]}/src/mod/alienLibraries.json') == True:
            ...
        else:
            ...

    def _library_writeRawConfig(self):
        ...

    def _library_updateConfig(self):
        ...

    # Exceptions
    def exception(self,r,m):
        if self.rootConfig['root']['exceptFailSafe'] == True:
            self._pipe_logging(f'exception({r},{m})',f'Exception:\n\t* {r}\n\t* {m}')
        else:
            self.alienException.raiseException(str(r),str(m))

def INIT():
    alienApp = Alien()

    alienApp.init()
if __name__ == "__main__":
    INIT()
