# Alien(3.6.40)
# Author: J4ck3LSyN
# Github: https://www.github.com/J4ck3LSyN

import os,time,socket,threading,subprocess,sys,random,json,sjcl,string

class exceptionHandler:
    def __init__(self,title):
        self.alienConfig = {}
        self.title = str(title)
        self.exceptionLog = [ True, [] ]
        self.failsafe = False
        self.rootOp = None
        self.display = False

    def _exceptionLog_pipe(self,stringVar):
        if self.exceptionLog[0] == True:
            self.exceptionLog[1].append(str(stringVar))

    def _display_display(self,stringVar):
        if self.display == True:
            print(str(stringVar))

    def _display_prompt(self,r,m):
        timestamp = str(time.asctime())
        currentWorkingDir = os.getcwd()
        ostype = sys.platform
        message = f'(exceptionHandler)\n\t* Time Stamp: {timestamp}\n\t* Current Working Directory: {currentWorkingDir}\n\t* Operating System: {ostype}\n\t* Root: '
        if self.rootOp != None:
            message = message+str(f'{self.rootOp.title}.{self.title}.{r}\n\t\t* ')
        else:
            message = message+str(f'{self.title}.{r}\n\t* ')
        message = message+str(f'Message: {m}')
        return str(message)

    def raiseException(self,r,m,prior=None):
        prompt = self._display_prompt(str(r),str(m))
        if prior != None:
            prior = str(prior).replace('\n\t','\n\t\t')
            prompt = str(prompt)+f'\n{prior}'
        if self.rootOp == None:
            self._exceptionLog_pipe(str(prompt))
            self._display_display(str(prompt))
            if self.failsafe == False:
                raise Exception(str(prompt))
        else:
            if self.rootOp.display == True:
                self.rootOp._exceptionLog_pipe(str(prompt))
                self.rootOp._display_display(str(prompt))
            if self.rootOp.failsafe == False:
                raise self.rootOp.raiseException(str(r),str(m),prior=str(prompt))


class toolBelt:
    def __init__(self):
        self.belt = {}

        self.alienConfig = {
            'alien.root.title':'toolBelt',
            'alien.root.version':'0.1',
            'alien.root.author':'J4ck3LSyN'
        }

        self.toolBeltException = exceptionHandler('toolBelt')

    # File Operations
    def _file_existPath(self,path):
        return os.path.isdir(str(path))

    def _file_existFile(self,path):
        return os.path.isfile(str(path))

    def _file_readDirectory(self,path):
        if self._file_existPath(str(path)) == True:
            return os.listdir()
        else:
            self.exception(str(f'_file_readDirectory({path})'),f'path({path}) Is Non-Existant')

    def _file_readText(self,path,encoding='utf-8'):
        if self._file_existFile(path) == True:
            fileText = ''
            fileLength = 0
            with open(str(path),'r',encoding=str(encoding)) as fileRead:
                fileText = fileRead.read()
                fileLength = len(fileText)
            return [ str(path),str(fileText),int(fileLength) ]
        else:
            self.exception(f'_file_readText({path},encoding={encoding})',f'path({path}) Is Non-Existant')


    def _file_readJsonData(self,path):
        if self._file_existPath(str(path)) == True:
            try:
                jsonData = None
                with open(str(path),'r') as jsonRead:
                    jsonData = json.load(jsonRead)
                return jsonData
            except Exception as E:
                self.exception(f'_file_readJsonData({path})',f'Operation Failed Due To: {E}')

    def _file_readDirectoryTree(self,path):
        if self._file_existPath(str(path)) == True:
            directoryTree  = {}
            directoryList  = self._file_readDirectory(str(path))
            for key in directoryList:
                if self._file_existPath(str(f'{path}/{key}')) == True:
                    directoryTree[str(f'd-{key}')]=self._file_readDirectory(str(f'{path}/{key}'))
                else:
                    directoryTree[str(f'f-{key}')]=str(key)
            return directoryTree
        else:
            self.exception(f'_file_readDirectoryTree({path})',f'path({path}) Is Non-Existant')

    def _file_writeText(self,path,text,encoding='utf-8'):
        if self._file_existFile(str(path)) == False and self._file_existPath(str(path)) == False:
            if self._variable_isType(text,'f0a3') == True:
                text = '\n'.join(text)
            else:
                text = str(text)
            try:
                with open(str(path),'w',encoding=str(encoding)) as fileWrite:
                    fileWrite.write(str(text))
            except Exception as E:
                self.exception(f'_file_writeJson({path},{text},encoding={encoding})',f'Exception: {E}')
        else:
            self.exception(f'_file_writeText({path},{text})',f'path({path},encoding={encoding}) Is Existant Use "toolBelt._file_appendText({path},{text})"')

    def _file_writeJson(self,path,jdata,encoding='utf-8'):
        if self._file_existFile(str(path)) == False and self._file_existPath(str(path)) == False:
            if self._variable_isType(jdata,'f0a5') == True:
                try:
                    with open(str(path),'w',encoding=str(encoding)) as jsonWrite:
                        json.dump(jdata,jsonWrite,indent=3)
                except Exception as E:
                    self.exception(f'_file_writeJson({path},{jdata},encodng={encoding})',f'Exception: {E}')
            else:
                self.exception(f'_file_writeJson({path},{jdata},encoding={encoding})',f'jdata({jdata}) Is Not dict(f0a5) Type')
        else:
            self.exception(f'_file_writeJson({path},{jdata},encodng={encoding})',f'path({path}) Is Existant Use "toolBelt._file_appendJson({path},{jdata})"')

    def _file_writeDirectory(self,path):
        if self._file_existPath(str(path)) == False:
            os.mkdir(str(path))
        else:
            self.exception(f'_file_writeDirectory({path})',f'path({path}) Is Existant')

    def _file_removeFile(self,path):
        if self._file_existFile(str(path)) == True:
            try:
                os.remove(str(path))
            except Exception as E:
                M = f'[Exception({E})]\n\t* File {path} Is Most Likely In Use On Another Service'
                self.exception(str(f'_file_removeFile({path})',str(M)))
        else:
            self.exception(str(f'_file_removeFile({path})',f'Path: {path} Is Non-Existant'))

    def _file_removeDirectory(self,path):
        if self._file_existPath(str(path)) == True:
            try:
                os.rmdir(str(path))
            except Exception as E:
                self.exception(f'_file_removeDirectory({path})',f'Exception: {E}')
        else:
            self.exception(f'_file_removeDirectory({path})',f'path({path}) Is Non-Existant')



    def _file_appendText(self,path,text):
        ...

    def _file_appendJson(self,path,jdata):
        ...

    # Variable Operations
    def _variable_isType(self,v1,v2,iT=False):
        '''
        toolBelt._variable_isType(v1,v2,iT=bool)

        Variable Type:
            f0a1 (str)
            f0a2 (int)
            f0a3 (list)
            f0a4 (bool)
            f0a5 (dict)
            f0a6 (tuple)

            f0aa (func/method)
            f0ab (byte)
            f0ac (hex)
        '''
        if iT == True:
            if [ self._variable_isType(v1,'f0a3')[0],self._variable_isType(v2,'f0a3')[0] ] == [ True,True ]:
                if self._variable_getLen(v1) == self._variable_getLen(v2):
                    rV = []
                    for vI in range(0,len(v1)-1):
                        rV.append(self._variable_isType(v1[vI],v2[vI]))
                    return rV
                else: self.exception(f'_variable_isType({v1},{v2},iT={iT})',f'v1{v1} And v2{v2} Are Not The Same Length: {len(v1)} != {len(v2)}')
            else: self.exception(f'_variable_isType({v1},{v2},iT={iT})',f'v1{v1} Or v2{v2} Are Not List(f0a3) Types For Iteration')
        else:
            vTC = [ [],None ]
            # str,int,list,bool,dict,tuple
            if v2 in [ 0xf0a1, 'f0a1', 'str', 'Str','STR' ]: vTC = [ [ 0xf0a1,'f0a1' ],str ]
            elif v2 in [ 0xf0a2, 'f0a2', 'int', 'Int','INT' ]: vTC = [ [ 0xf0a2,'f0a2' ],int ]
            elif v2 in [ 0xf0a3, 'f0a3', 'list', 'List', 'LIST']: vTC = [ [ 0xf0a3, 'f0a3' ],list ]
            elif v2 in [ 0xf0a4, 'f0a4', 'bool', 'Bool', 'BOOL' ]: vTC = [ [ 0xf0a4,'f0a4' ],bool ]
            elif v2 in [ 0xf0a5, 'f0a5', 'dict', 'Dict', 'DICT' ]: vTC = [ [ 0xf0a5, 'f0a5' ],dict ]
            elif v2 in [ 0xf0a6, 'f0a6', 'tuple', 'Tuple', 'TUPLE' ]: vTC = [ [ 0xf0a6, 'f0a6' ],tuple ]
             # function,method,hex,bytes
            elif v2 in [ 0xf0aa, 'f0aa', 'func', 'Func', 'FUNC', 'method', 'Method','METHOD' ]:
                if str(type(v1)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]: return [ True,[ 0xf0aa,'f0aa' ] ]
                else: return [ False,[ 0xf0aa, 'f0aa' ] ]
            elif v2 in [ 0xf0ab, 'f0ab', 'byte', 'Byte', 'BYTE' ]:
                if str(type(v1)) == str("<class 'bytes'>"): return [ True,[ 0xf0ab, 'f0ab' ] ]
                else: return [ False,[ 0xf0ab, 'f0ab' ] ]
            elif v2 in [ 0xf0ac, 'f0ac', 'hex', 'Hex', 'HEX' ]:
                if len(v1) >= 3:
                    if str(v1[:2]) == str('0x'): return [ True,[ 0xf0ac, 'f0ac' ] ]
                    else: return [ False,[ 0xf0ac, 'f0ac' ] ]
                else: return [ False,[ 0xf0ac, 'f0ac' ] ]
            if vTC[1] == None:
                return [ [ 0xf0af,'f0af' ],'f0af' ]
            else:
                return isinstance(v1,vTC[1]);return [ vTCV,vTC[0] ]

    def _variable_getType(self,v1):
        keyTranslate = {
            'str':[ str,'f0a1' ],
            'int':[ int,'f0a2' ],
            'list':[ list,'f0a3' ],
            'bool':[ bool,'f0a4' ],
            'dict':[ dict,'f0a5' ],
            'tuple':[ tuple,'f0a6'],
            'func':[ ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"],'f0aa' ],
            'byte':[ ["<class 'byte'>"],'f0ab' ],
            'hex':[ [],'f0ac' ]
        }
        returnValue = None
        for key in keyTranslate:
            if str(key) == 'func':
                if self._variable_isType(v1,'f0aa') == True:
                    returnValue = str('f0aa');break
            elif str(key) == 'hex':
                if self._variable_isType(v1,'f0ac') == True:
                    returnValue = str('f0ac');break
            elif str(key) == 'byte':
                if self._variable_isType(v1,'f0ab') == True:
                    returnValue = str(f'f0ab');break
            else:
                if self._variable_isType(v1,keyTranslate[key][0]) == True:
                    returnValue = keyTranslate[key][1];break
        if returnValue == None:
            return 'f0af'
        else:
            return returnValue

    def _variable_getLen(self,v1):
        return len(v1)

    def _variable_appendByte(self,v1,bL=8):
        if self._variable_isType(str(v1),'f0ac')[0] == True:
            v1 = str(v1[2:])
            v1 = str('0'*int(8-len(v1)))+str(v1)
            return str(v1)
        else:
            self.exception(f'_variable_appendByte({v1},bL={bL})',f'v1({v1}) Is Not hex(f0ab) Type')


    def _variable_seperateByte(self,v1,bL=8):
        if len(v1)%bL == 0:
            record = [ False, '', [] ]
            for character in str(v1):
                if record[0] == False:
                    record[0] = True;record[1] = str(character)
                else:
                    record[1] = f'{record[1]}{character}'
                    if len(record[1]) == bL:
                        record[2].append(str(record[1]));record[1] = '';record[0] = False
            return record[2]
        else: self.exception(f'_variable_seperateByte({v1},bL={bL})',f'Invalid Amount Of Bytes To Seperate By Modulus: v1(len({len(v1)}))%{bL}={len(v1)%bL}')

    def _variable_getShellEvalProcess(self,executeString):
        if str(' ') in str(executeString):
            executeTree = executeString.split(' ')
        else:
            executeTree = [str(executeString)]
        try:
            shellEvalProcess = subprocess.Popen(executeTree,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            print(type(shellEvalProcess))
        except Exception as E:
            self.exception(f'_variable_getShellEval({executeString})',f'Exception: {E}')

    # Convert int To hex
    def _variable_f0a2Tof0ab(self,v1):
        if self._variable_isType(v1,'f0a2') == True:
            return hex(int(v1))
        else:
            self.exception(f'_variable_f0a2Tof0ab({v1})',f'v1({v1}) Is Not int(f0a2) Type')

    # Validate Only Hexadecimal Characters
    def _variable_onlyf0abChars(self,v1):
        if str(v1[:2]) == str('0x'): v1 = v1[2:]
        validChars = string.hexdigits
        isHex = True
        for char in str(v1):
            if str(char) not in str(validChars):
                isHex = False;break
        return isHex

    # Convert hex To int
    def _variable_f0abTof0a2(self,v1):
        if str(v1[:2]) != str('0x'): v1 = f'0x{v1}'
        if self._variable_onlyf0abChars(str(v1)) == True:
            return int(v1,16)
        else:
            self.exception(f'_variable_f0abTof0a2({v1})',f'v1({v1}) Carries Non-Hex Characters')

    def _variable_getTime(self):
        return str('_'.join([ i for i in str(time.asctime()).split(' ')[1:5] if i]).replace(':','-'))

    def _variable_encodeB64(self,stringVar,encoding='utf-8'):
        return self._variable_f0abTof0a1(base64.b64encode(str(stringVar),encoding=encoding),encoding=encoding)

    def _variable_decodeB64(self,stringVar,encoding='utf-8'):
        return self._variable_f0abTof0a1(base64.b64decode(self._variable_f0a1Tof0ab(str(strng),encoding=encodng),encoding=encoding),encoding=encoding)

    # Convert str To bytes
    def _variable_f0a1Tof0ab(self,stringVar,encoding='utf-8'):
        return bytes(str(stringVar),encoding=encoding)

    # Convert bytes To str
    def _variable_f0abTof0a1(self,byteVar,encoding='utf-8'):
        if self._variable_isType(byteVar,'f0ab') == True:
            return str(byteVar.decode(encocing=encoding))
    # Exception
    def exception(self,r,m): self.toolBeltException.raiseException(str(r),str(m))

class Alien:
    def __init__(self):
        self.toolBelt = toolBelt()
        self.alienException = exceptionHandler('Alien(3.6.40)')
        self.toolBelt.toolBeltException.rootOp = self.alienException

        self.loggIndex = {}
        self.verbIndex = {}

        self.config    = self._config_build()

        self._install_verify()
        self._install_readConfig()

        self.registry  = self._registry_build('Alien-Registry')


        self._display_configureToWindows()

    # Installation Operations
    def _install_fetchGitHubConfig(self):
        ...

    def _install_fetchGitHubUpdate(self):
        ...

    def _install_readConfig(self,confPath=None, allowExitScope=False):
        self._logging_pipe(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})','...')
        if self.config:
            c = self.config
            rP = c['alien.root.path']
            if confPath == None:
                rP_S_C = f'{rP}/{c["alien.root.source"]}/{c["alien.root.source.config"]}'
            else:
                rP_S_C = str(confPath)
            if allowExitScope != True:
                if str(rP) not in str(rP_S_C):
                    self.exception(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})',f'allowExitScope({allowExitScope}) Is False While Attempted To Read Configure File Outside Of Scope: {rP}')
                else:
                    pass

            if self.toolBelt._file_existFile(str(rP_S_C)) == True:
                self._logging_pipe(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})',f'\n\t* Reading: {rP_S_C}')
                jsonData = self.toolBelt._file_readJsonData(str(rP_S_C))
                self._logging_pipe(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})',f'\n\t* File: {rP_S_C}\n\t Data Length: {len(str(jsonData))}')
                jsonConfigData = self._config_build(config=jsonData)
                self._logging_pipe(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})',f'\n\t* File: {rP_S_C}\n\t Data Length: {len(str(jsonData))}\n\t* Alien.config Is Set To:\n{json.dumps(jsonConfigData,indent=3)}\n')
                self.config = jsonConfigData
            else:
                self.exception(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})',f'path({rP_S_C}) Is Non-Existant')
        else:
            self.exception(f'_install_readConfig(confPath={confPath},allowExitScope={allowExitScope})','Alien Is Not Configured, Use "Alien._config_build()"')

    def _install_updateConfig(self,config=None):
        if self.config:
            if config == None: config = self.config
            rP = config['alien.root.path']
            rP_S_C = f'{rP}/{config["alien.root.source.config"]}'
            if self.toolBelt._file_existFile(str(rP_S_C)) == True:
                self.toolBelt._file_removeFile(str(rP_S_C))
            self.toolBelt._file_writeJson(str(rP_S_C),config)
        else:
            self.exception(f'_install_updateConfig(config={config})','Alien Is Not Configured, Use "Alien._config_build()"')

    def _install_verify(self):
        self._logging_pipe('_install_verify()','...')
        if self.config:
            c        = self.config
            rP       = str(c['alien.root.path'])
            self._logging_pipe('_install_verify()',f'\n\t* Config:\n{json.dumps(c,indent=2)}\n\t* rP: {rP}')
            if self.toolBelt._file_existPath(str(rP)) == True:
                mm_H     = [
                    '# Author: `J4ck3LSyN`',
                    '# Version: 3.6.40',
                    '### Manager Object ###'
                ]
                mm_C     = {}
                rP_S     = f'{rP}/{c["alien.root.source"]}'

                rP_S_M   = f'{rP_S}/{c["alien.root.source.modules"]}'
                rP_S_MC  = f'{rP_S_M}/{c["alien.root.source.modules.config"]}'
                rP_S_MM  = f'{rP_S_M}/{c["alien.root.source.modules.manager"]}'

                rP_S_L   = f'{rP_S}/{c["alien.root.source.library"]}'
                rP_S_LC  = f'{rP_S_L}/{c["alien.root.source.library.config"]}'
                rP_S_LM  = f'{rP_S_L}/{c["alien.root.source.library.manager"]}'

                rP_S_T   = f'{rP_S}/{c["alien.root.source.template"]}'
                rP_S_TC  = f'{rP_S_T}/{c["alien.root.source.template.config"]}'
                rP_S_TM  = f'{rP_S_T}/{c["alien.root.source.template.manager"]}'

                rP_S_C   = f'{rP_S}/{c["alien.root.source.config"]}'

                rP_L     = f'{rP}/{c["alien.root.logging"]}'
                rP_P     = f'{rP}/{c["alien.root.projects"]}'
                self._logging_pipe('_install_verify()',f'''\n\t* rP_S: {rP_S}\n\t* rP_S_M: {rP_S_M}\n\t* rP_S_MC: {rP_S_MC}\n\t* rP_S_MM: {rP_S_MM}\n\t* rP_S_L: {rP_S_L}\n\t* rP_S_LC\n\t* rP_S_LM: {rP_S_LM}\n\t* rP_S_T: {rP_S_T}\n\t* rP_S_TC: {rP_S_TC}\n\t* rP_S_TM: {rP_S_TM}\n\t* rP_S_C: {rP_S_C}\n\t* rP_L: {rP_L}\n\t* rP_P: {rP_P}''')
                # Create Directory
                if self.toolBelt._file_existPath(str(rP_S)) == False:
                    self.toolBelt._file_writeDirectory(str(rP_S))
                if self.toolBelt._file_existPath(str(rP_S_M)) == False:
                    self.toolBelt._file_writeDirectory(str(rP_S_M))
                if self.toolBelt._file_existPath(str(rP_S_L)) == False:
                    self.toolBelt._file_writeDirectory(str(rP_S_L))
                if self.toolBelt._file_existPath(str(rP_S_T)) == False:
                    self.toolBelt._file_writeDirectory(str(rP_S_T))
                if self.toolBelt._file_existPath(str(rP_L)) == False:
                    self.toolBelt._file_writeDirectory(str(rP_L))
                if self.toolBelt._file_existPath(rP_P) == False:
                    self.toolBelt._file_writeDirectory(str(rP_P))
                # Create Files (Modules)
                if self.toolBelt._file_existFile(rP_S_MM) == False:
                    self.toolBelt._file_writeText(str(rP_S_MM),mm_H)
                if self.toolBelt._file_existFile(rP_S_MC) == False:
                    self.toolBelt._file_writeJson(str(rP_S_MC),mm_C)
                # Create Files (Library)
                if self.toolBelt._file_existFile(rP_S_LC) == False:
                    self.toolBelt._file_writeJson(str(rP_S_LC),mm_C)
                if self.toolBelt._file_existFile(rP_S_LM) == False:
                    self.toolBelt._file_writeText(str(rP_S_LM),mm_H)
                # Create Files (Template)
                if self.toolBelt._file_existFile(rP_S_TC) == False:
                    self.toolBelt._file_writeJson(str(rP_S_TC),mm_C)
                if self.toolBelt._file_existFile(rP_S_TM) == False:
                    self.toolBelt._file_writeText(str(rP_S_TM),mm_H)
                # Create Config (source)
                if self.toolBelt._file_existFile(rP_S_C) == False:
                    self.toolBelt._file_writeJson(str(rP_S_C),c)

            else:
                self.exception(f'_install_verify()',f'rootPath: {rP} Is Nont-Existant')
        else:
            self.exception(f'_install_verify()',f'Alien Is Not Configured, Use "Alien._config_build( )"')

    # Configure Operations
    def _config_build(self,config=None):
        configRaw = {
            # Threads
            'alien.processes':{},
            # Path Configuration
            'alien.root.path':[ os.getcwd().replace('\\','/') if str('win') in sys.platform else os.getcwd() ][0],
            'alien.root.source':'src',
            # Module
            'alien.root.source.modules':'mod',
            'alien.root.source.modules.config':'alienModuleConfig.json',
            'alien.root.source.modules.manager':'alienModuleManager.py',
            # Library
            'alien.root.source.library':'lib',
            'alien.root.source.library.config':'alienLibraryConfig.json',
            'alien.root.source.library.manager':'alienLibraryManager.py',
            # Templates
            'alien.root.source.template':'templates',
            'alien.root.source.template.config':'alienTemplateConfig.json',
            'alien.root.source.template.manager':'alienTemplateManager.py',
            # Config, Logs, And Projects
            'alien.root.source.config':'alienConfig.json',
            'alien.root.logging':'logs',
            'alien.root.logging.path':'$_alien(3.6.40).log',
            'alien.root.logging.status':True,
            'alien.root.logging.verbose':True,
            'alien.root.logging.display':True,
            'alien.root.logging.dumpOnExit':False,
            'alien.root.projects':'projects',
            'alien.root.failsafe.status':False,
            # Interpreter Filters
            'alien.interpreter.filter.alien':False,
            'alien.interpreter.filter.developer':False,
            'alien.interpreter.filter.shell':False,
            # Floating Values
            'alien.float.interpreter.inline.status':False,
            'alien.float.interpreter.inline.stack':[],
            'alien.float.interpreter.inline.errorMax':5,
            'alien.float.interpreter.inline.KeyboardInterrupt-Count':5,
            'alien.float.interpreter.inline.project-Path':'NULL',
            'alien.float.interpreter.inline.process-Current':'NULL',
            # Registry Values
            'alien.registry.minimumRange':0x1111,
            'alien.registry.maximumRange':0xffff,
            'alien.registry.offset':0x3e7,
            'alien.registry.padding':0x8,
            'alien.registry.filter':'alien',
            'alien.registry.keymap':self._keymap_build(0x11,0x80,0x3e7,0x8),
            'alien.registry.bytemap':self._bytemap_build('byteMapTemplate',{})
        }
        if config == None: return configRaw
        else:
            for key in config:
                if str(key) in configRaw:
                    if isinstance(config[key],type(configRaw[key])) == True:
                        configRaw[key]=config[key]
            return configRaw

    # Console Operations
    def _console_build(self,template,rootFunc,config):
        ...

    def _console_readTemplateFile(self,path):
        ...

    def _console_filter(self):
        ...

    def _console_alien(self,operand):
        ...

    def _console_developer(self,operand):
        ...

    def _console_shell(self,operand):
        ...

    # Server Operations
    def _server_build(self):
        ...

    # Client Operations
    def _client_build(self):
        ...

    # Process Operations
    def _process_build(self):
        ...

    # Registry Operations
    def _registry_build(self,title,config=None,packRegister=False):
        if config == None: config = self.config
        minimumRange = config['alien.registry.minimumRange']
        maximumRange = config['alien.registry.maximumRange']
        offset       = config['alien.registry.offset']
        padding      = config['alien.registry.padding']
        filter       = config['alien.registry.filter']
        keymap       = config['alien.registry.keymap']
        register = [
            [
                minimumRange,
                maximumRange,
                offset,
                padding,
                filter
            ],
            []
        ]
        if int(minimumRange) < int(maximumRange):
            titleEncoded = self._keymap_encode(str(title))
            titleKey     = self._keymap_genKey(str(title))
            for segment in range(int(minimumRange),int(maximumRange)):
                segmentKey = str( self.toolBelt._variable_appendByte( str( self.toolBelt._variable_f0a2Tof0ab( segment+offset ) ),bL=padding ) ) # Need To Transfer To self._registry_getTitleKey
                register[1].append(str(segmentKey))
            if packRegister == False:
                self.registry[str(titleKey)]=register
                self._logging_pipe(f'_registry_build({title},config={config},packRegister={packRegister})',f'\n\t* Title: {title},\n\t* Key: {titleKey}\n\t* Register Length: {len(register)}\n\t* Packed: {packRegister}')
            else:
                packedRegister = self._registry_packOrUnpackRegister(register)
                self.registry[str(titleKey)]=packedRegister
                self._logging_pipe(f'_registry_build({title},config={config},packRegister={packRegister})',f'\n\t* Title: {title},\n\t* Key: {titleKey}\n\t* Register Length: {len(packedRegister)}\n\t* Packed: {packRegister}')
        else:
            self.exception(f'_registry_build({title},config={config},packRegister={packRegister})',f'minimumRange({minimumRange}) Is Not Less Than maximumRange({maximumRange})')

    def _registry_getTitleKey(self,title,register):
        if self._registry_isRegister(register) == [True,False]:
            return str( self.toolBelt._variable_appendByte( str( self.toolBelt._variable_f0a2Tof0ab( segment+offset ) ),bL=padding ) )
        elif self._registry_isRegister(register) == [True,True]:
            ...
        else:
            self.exception(f'_registry_getTitleKey({title},{register})',f'register({register}) Is Not Valid ')

    def _registry_isRegister(self,register):
        # Returns Boolean [0] - Is Alien Register Object // [1] - Is Alien
        if self._variable_isType(register,'f0a3') == True:
            if self._variable_getLen(register) == 2:
                if [ self._variable_isType(register[0],'f0a3'),self._variable_isType(register[0],'f0a3') ] == [ True,False ]:
                    return [False,False]
                else:
                    return [False,False]
            else:
                return [False,False]
        elif self._variable_isType(register,'f0ab'):
            # For Packed Alien Bytes
            ...
        else:
            return [False,False]

    def _registry_packOrUnpackRegister(self,register,packRegister=True):
        ...

    def _registry_getPackedStatusRegister(self,register):
        ...

    def _registry_packOrUnpackRegistry(self,packRegistry=False):
        ...

    def _registry_writeToPage(self,register,pageAddress,pageVariable):
        ...

    def _registry_convertPageVariableToAlienRegisterType(self,pageVariable):
        ...

    def _registry_clearPage(self,register,pageAddress):
        ...

    # byemap Operations
    def _bytemap_build(self,byteTemplate):
        ...

    # template Operations
    def _template_build(self):
        ...

    # Keymap Operations
    def _keymap_build(self,minimumRange,maximumRange,offset,padding):
        keymap = {}
        if minimumRange < maximumRange:
            for character in range(int(minimumRange),int(maximumRange)):
                characterKey = str(chr(character))
                characterHex = str( self.toolBelt._variable_appendByte( str( self.toolBelt._variable_f0a2Tof0ab( int( character + offset ) ) ), bL=padding ) )
                keymap[str(characterKey)]=str(characterHex)
            return keymap
        else:
            self.exception(f'_keymap_build({minimumRange},{maximumRange},{offset},{padding})',f'minimumRange({minimumRange}) Is Not Less Than maximumRange({maximumRange})')

    def _keymap_genKey(self,stringVar):
        self._logging_pipe(f'_keymap_genKey({stringVar})','...')
        if self.toolBelt._variable_onlyf0abChars(stringVar) == True:
            return int(f'0x{stringVar}',16)
        else:
            self.exception(f'_keymap_genKey({stringVar})',f'stringVar({stringVar}) Is Not A Valid Hexadecimal Value By Characters')

    def _keymap_encode(self,stringVar,keymap=None):
        self._logging_pipe(f'_keymap_encode({stringVar},keymap={keymap})','...')
        if self.config:
            if keymap == None: keymap = self.config['alien.registry.keymap']
            if self.toolBelt._variable_isType(keymap,'f0a5') == True:
                encoded = []
                for char in str(stringVar):
                    if str(char) in keymap:
                        encoded.append(str(keymap[char]))
                return ''.join(encoded)
            else:
                self.exception(f'_keymap_encode({stringVar},keymap={keymap})',f'keymap({keymap}) Is Not Dict(f0a4) Type')
        else:
            self.exception(f'_keymap_encode({stringVar},keymap={keymap})','Alien Is Not Configured, Use "Alien._config_build()"')

    def _keymap_decode(self,stringVar,keymap=None):
        self._logging_pipe(f'_keymap_decode({stringVar},keymap={keymap})','...')
        if self.config:
            if keymap == None: keymap = self.config['alien.registry.keymap']
            decoded = []
            encodedTree = self.toolBelt._variable_seperateByte(str(stringVar),bL=self.config['alien.registry.padding'])
            for key in encodedTree:
                for char in keymap:
                    if str(key) == str(keymap[char]):
                        decoded.append(str(char))
            return ''.join(decoded)

        else:
            self.exception(f'_keymap_decode({stringVar},keymap={keymap})','Alien Is Not Configured, Use "Alien._config_build()"')


    # Display Operations
    def _display_findColors(self,stringVar):
        self._logging_pipe(f'_display_findColors({stringVar})','...')
        for colorKey in self.config['alien.display.colorAndStyle']:
            for colorSubKey in self.config['alien.display.colorAndStyle'][str(colorSubKey)]:
                colorTargetKey = f'{self.config["alien.display.replace"]["colorKey"][0]}{colorKey}.{colorSubKey}{self.config["alien.display.replace"]["colorKey"][1]}'
                if str(colorTargetKey) in str(stringVar):
                    stringVar = str(stringVar.replace(str(colorTargetKey),self.config['alien.display.colorAndStyle'][colorKey][colorSubKey]))
        return stringVar

    def _display_findMessages(self,stringVar):
        self._logging_pipe(f'_display_findMessages({stringVar})','...')
        for messageKey in self.config['alien.display.replace']['M']:
            messageTargetKey = f'{self.config["alien.display.replace"]["messageKey"][0]}{messageKey}{self.config["alien.display.replace"]["messageKey"][1]}'
            if str(messageTargetKey) in str(stringVar):
                stringVar = stringVar.replace(str(messageTargetKey),self.config['alien.display.replace']['M'][str(messageKey)])
        return str(stringVar)

    def _display_pipe(self,stringVar):
        self._logging_pipe(f'_display_pipe({stringVar})','...')
        if self.config['alien.root.logging.verbose'] == True:
            timestamp = self.toolBelt._variable_getTime()
            self.verbIndex[str(timeStamp)]=str(stringVar)
            self._display_textToDisplay(str(stringVar))

    def _display_textToDisplay(self,stringVar):
        if self.config['alien.root.logging.verbose'] == True:
            stringVarPrompt = self._display_findMessages(str(stringVar))
            stringVarPrompt = self._display_findColors(str(stringVar))
            print(str(stringVarPrompt))

    def _display_configureToWindows(self):
        self._logging_pipe(f'_display_configureToWindows()','...')
        if str('win') in str(sys.platform):
            try:
                import colorama
                colorama.init()
                self.config['alien.display.configureWindows'] = True
            except Exception as E:
                self.exception('_display_configureToWindows()',f'Exception: {E}')

    def _display_appendMessage(self,messageID,messageString):
        self._logging_pipe(f'_display_appendMessage({messageID},{messageString})','...')
        if str(messageID) not in self.config['alien.display.replace']['M']:
            self.config['alien.display.replace']['M'][str(messageID)] = str(messageString)
    # Logging Operations
    def _logging_pipe(self,root,stringVar):
        '''
        Alien._logging_pipe(str(<root-function-name>),str(<message>))
        self._logging_pipe('example','this message')
        '''
        if self.config["alien.root.logging.status"] == True:
            message = f'RootFunction: {root}\n\t* RootPath: {self.config["alien.root.path"]}\n\t* Message: {stringVar}'
            self.loggIndex[str(self.toolBelt._variable_getTime())]=str(message)
            if self.config["alien.root.logging.display"] == True:
                print(f'\n\t* Log Verbosity: \n{message}\n')

    def exception(self,r,m):
        if self.config["alien.root.failsafe.status"] == False:
            self.alienException.raiseException(str(r),str(m))
        else:
            self._display_textToDisplay(f'\n\t* Root: {r}\n\t* Alien Root Exception: {m}')


def appInit():
    alienApp = Alien()

    alienEncoded = alienApp._keymap_encode('this stringVar')
    print(alienEncoded)
    print(alienApp._keymap_decode(alienEncoded))

    alienApp.toolBelt._variable_getShellEvalProcess('dir')

if __name__ == "__main__":
    appInit()
