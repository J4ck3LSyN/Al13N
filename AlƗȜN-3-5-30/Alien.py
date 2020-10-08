#!/usr/bin/env python3
# Author: J4ck3LSyN {NO sys.argv COMPATABILITY}
#------------------------------------------------------------------------------#
import ColourFullDisplay as CFD_Mount
import sys,os,time,random,base64,hashlib,subprocess,socket,requests
#------------------------------------------------------------------------------#
###################################################################################################################################
#>>Register = Registry(K0=K0,K1=K1)
#>>For Register Handling
class Registry:
	def __init__(self,K0=str('0000000000000000'),K1=str('0000000000000000')):
		self.K0 = self.GenerateKey(K0);self.K1=self.GenerateKey(str(K1))
		self.RG = {};self.OpExec={}
		# K0 & K1 Are Signature Keys For Execution Validation
		# RG & OpExec Are For Execution And Memory Handling
	### For Executing Segments And Pages ###
	def Execute(self,SID,PID=None):
		if str(SID) in self.RG:
			if PID != None:
				if str(PID) in self.RG[str(SID)]:
					if len(self.RG[SID][PID]) != 0:
						Root_Operation = self.RG[SID][PID][0]
						Root_Arguments = self.RG[SID][PID][1]
						Root_Arg_Index = 0
						# Pasee Arguments
						for Arg in Root_Arguments:
							if str('@~') in str(Arg):
								if str('.') in str(Arg):
									Temp_Exec = str(Arg).strip('@~').split('.')
									if str(Temp_Exec[0]) not in self.RG:
										if str(Temp_Exec[0]) in ['$','home','Home','HOME']: Temp_Exec[0]=str(SID)
										else: raise self.RegistryException('Execute','Invalid Link Location Sent {} @ Location {} {}'.format(str(Temp_Exec[0]),str(SID),str(PID)))
									Segment = Temp_Exec[0]
									Page    = Temp_Exec[1]
									Return  = self.Execute(str(Segment),str(Page))
									if Return not in [None,'None']: Root_Arguments[Root_Arg_Index]=Return
									else: Root_Arguments[Root_Arg_Index]=''
							Root_Arg_Index += 1
						# Pull Operation Code And Execute
						OpKey = self.RG[SID][PID][0];OpArg = self.RG[SID][PID][1]
						Output = self.ExeOpKey(OpKey,OpArg)
						return Output
					else: return None
				else: raise self.RegistryException('Execute','Invalid PID {} For SID {}'.format(str(PID),str(SID)))
			else:
				Outputs = []
				for Page in self.RG[SID]: Outputs.append(self.Execute(SID,Page))
				return Outputs
		else: raise self.RegistryException('Execute','Invalid SID {} Sent Is Non-Existant'.format(str(SID)))

	### For Generating A New Segment ###
	def New(self,SID,SLN):
		if str(SID) not in self.RG:
			Valid_Hex = True
			for Character in str(SLN):
				if str(Character) not in 'abcdefABCDEF0123456789': Valid_Hex = False
			if Valid_Hex == True:
				self.RG[str(SID)] = {}
				if int('0x'+str(SLN),16)>0xffffffffffffffff: raise self.RegistryException('New','Invalid Page Limit Exceeds 0xffffffffffffffff')
				for Page in range(1,int('0x'+str(SLN),16)):
					Page_Hex = str(hex(Page)).strip('0x')
					if len(Page_Hex) < 17:
						Append_Length = 16-len(Page_Hex)
						Append_String = ''
						for A in range(0,Append_Length):Append_String+=str('0')
						Page_Hex = str(Append_String)+str(Page_Hex)
					self.RG[str(SID)][str(Page_Hex)]=[]
			else: raise self.RegistryException('New','Invalid Hex Value Sent For Length')
		else: raise self.RegistryException('New','Expected A Non-Existant ID Got {}'.format(str(SID)))
	### To Write A OpKey Arguement And Value Into A Segment ###
	def Write(self,SID,PID,OID,OAR):
		if str(SID) in self.RG:
			if str(PID) in self.RG[str(SID)]:
				if str(OID) in self.OpExec:
					if type(OAR) is list:
						if len(OAR) == self.OpExec[str(OID)][1] or self.OpExec[str(OID)][1] == str('*'): self.RG[str(SID)][str(PID)]=[str(OID),OAR]
						else: raise self.RegistryException('Write','Invalid Input Length Expected {} Got {}'.format(str(self.OpExec[OID][1]),str(len(OAR))))
					else: raise self.RegistryException('Write','Expected A list Type For Input Got {}'.format(str(type(OAR))))
				else: raise self.RegistryException('Write','Expected A Valid Operation Key')
			else: raise self.RegistryException('Write','Expected A Valid Page ID {} Is Non-Existant'.format(str(PID)))
		else: raise self.RegistryException('Write','Expected A Valid Segment ID {} Is Non-Existant'.format(str(SID)))
	### OpKey Execution (Post self.AddOpKey) ###
	def ExeOpKey(self,OpKey_ID,OpKey_IN):
		if str(OpKey_ID) in self.OpExec:
			if type(OpKey_IN) is list:
				if len(OpKey_IN) == self.OpExec[str(OpKey_ID)][1] or self.OpExec[str(OpKey_ID)][1] == str('*'): return self.OpExec[str(OpKey_ID)][2](OpKey_IN)
				else: raise self.RegistryException('ExeOpKey','Expected Valid Input Length {} Got {}'.format(str(self.OpExec[OpKey_ID][1]),str(len(OpKey_IN))))
			else: raise self.RegistryException('ExeOpKey','Expected A list Type Got {}'.format(str(type(OpKey_IN))))
		else: raise self.RegistryException('ExeOpKey','Expected A Valid ID {} Is Non-Existant'.format(str(OpKey_ID)))
	### AddOpKey For Appending To (self.OpExec) ###
	def AddOpKey(self,OpKey_ID,OpKey_Desc,OpKey_ArgLen,OpKey_Pipe):
		if str(OpKey_ID) not in self.OpExec:
			if type(OpKey_ArgLen) is int or str(OpKey_ArgLen) == '*':
				if str(type(OpKey_Pipe)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]:self.OpExec[str(OpKey_ID)]=[str(OpKey_Desc),OpKey_ArgLen,OpKey_Pipe]
				else: raise self.RegistryException('AddOpKey','Expected Valid Function/Method For Execution Pipe Got {}'.format(str(type(OpKey_Pipe))))
			else: raise self.RegistryException('AddOpKey','Expected A Int Value Or "*" Got {}'.format(str(OpKey_ArgLen)))
		else: raise self.RegistryException('AddOpKey','Expected A ID That Is Not Existant Got {}'.format(str(OpKey_ID)))
	### Key Generation ###
	def GenerateKey(self,Key):
		if len(str(Key)) == 16:
			### Seperate Every 2 Bytes ###
			# 00 00 00 00 00 00 00 00
			Flip = []
			Stat = False
			Temp = ''
			for Character in str(Key):
				if str(Character) not in str('abcdefABCDEF0123456789'): raise self.RegistryException('GenerateKey','Invalid Character {}'.format(str(Character)))
				if Stat == False:
					Temp = str(Character);Stat = True
				else:
					Flip.append(str(Temp+Character));Temp = '';Stat = False
			### Take And Convert From Hex Value To Int  ###
			Ints = []
			for HexValues in Flip:
				if str(HexValues) == '00': Ints.append(int(random.randint(1,255)))
				else: Ints.append( int( '0x'+HexValues,16 ) )
			### Pull Needed Key Values ###
			return str(hex( int(Ints[0]**Ints[1])^int(Ints[2]**Ints[3])^int(Ints[4]*Ints[5])^int(Ints[6]^Ints[7]) )).strip('0x')
		else: raise self.RegistryException('GenerateKey','Expected A Length Of 16 For Key ')
	def RegistryException(self,Root,Mesg):
		Message = 'Exception From ({}) With Error Message ({})'.format(str(Root),str(Mesg));raise Exception(Message)

###################################################################################################################################
###################################################################################################################################
#>> Alien_Mount = Alien.Alien(K0,K1)
#>> Both Keys Are For Registry().GenerateKey()
class Alien:
	def __init__(self,K0,K1,Debug=False,Logging=False,ExecLine=None,ExecFile=None,ProjectDIR=None,ExternalOpKey=None):
		self.Register = Registry(K0=str(K0),K1=str(K1))  # Register Functions
		self.Debug    = Debug # Debuging Boolean
		self.Logging  = Logging # Logging Boolean
		self.LogText  = [] # Log Output
		self.PreExec  = [ExecLine,ExecFile] # Execute Line and File
		self.External = ExternalOpKey # External Pythonic Operation Key File
		self.CmdLog   = [] # Command Log
		self.Project  = ProjectDIR # Project File For .aln Projects
		self.Fonts    = CFD_Mount.CFD.Fonts.FontStrings() # Fonts
		self.Display  = CFD_Mount.CFD.ColourPallet.Pallet() # Colours & Display
		###########################################################################
		self.Display.PalletKeys[2]['builtin.spacer']=str('[!fC!][!sB!]')+str('-')*120 # Spacer [?builtin.spacer?]
		self.Display.PalletKeys[2]['builtin.header']=str('[!fC!][!sN!]$[!fR!]:[!fG!]>[!fW!] ') # Header [?builtin.header?]
		###########################################################################
		self.SEGMENT_ID  = None # Current Segment
		self.PAGE_ID     = None # Current Page
		self.INC_ON_NULL = True # Current Inc Boolean (If True And ([self.SEGMENT_ID,self.PAGE_ID]!=None) Incriment)
		self.HEART_BEAT  = True # Current Status (Only Allow While Loop If True (self.Heart))
		self.SYMBOLIC    = {} # Symbolic Commands Links To Internal (Segment.Page)
		self.USAGE       = { # Usage Dictionary
			'q|Q|quit|Quit|QUIT|exit|Exit|EXIT':['Exits The Alien Interpreter'],
			'i|I|info|Info|INFO':[
				'info [ROOT] [ARG]',
				'\tUsed For Finding Information Regarding Internal Objects',
				'\tSegments:(s,S,segment,Segment,SEGMENTS)"info segment"/"i s"',
				'\t\tinfo segment              | Shows Basic Segment Information',
				'\t\tinfo segment <sid>        | Shows All Pages For That Segment ID',
				'\t\tinfo segment <sid> <pid>  | Shows Information For That Specific Page',
				'\t\tinfo segment *            | Shows All Pages And Page Values Inside Of All Segments Also Accepts (*,all,All,ALL)',
				'\t\tinfo segment TARGET_PAGE  | Shows Information Regarding One Specific Page In All Segments',
				'\tOperation Keys:(o,O,opkey,OpKey,OPKEY)"info opkey"/"i o"',
				'\t\tinfo opkey                | Shows Basic Operation Key Information',
				'\t\tinfo opkey <opkey>        | Shows Information For That Specific OpKey',
				'\t\tinfo opkey description    | Shows Operation Key Description Also Accepts (d,D,description,Description,DESCRIPTION)',
				'\t\tinfo opkey arglen         | Shows Amount Of Arguments For A Operation Key Also Accepts (l,L,arglen,ArgLen,ARGLEn)',
				'\t\tinfo opkey *              | Shows All Information For A Operation Key Also Accepts (*,all,All,ALL)',
				'\tLogging: (l,L,log,Log,LOG)"info log s/r" "i l s""i l r"',
				'\t\tinfo log read             | Read All Lines In Log Also Accepts (r,R,read,Read,READ)',
				'\t\tinfo log status           | Reads Current Status (s,S,status,Status,STATUS)',
				'\tBanners: (banners,Banners,BANNERS,banner,Banner,BANNER)',
				'\t\tinfo banners              | Displays All Banners Mounted Inside Of "self.Display.PalletKeys[2]"'
			],
			'c|C|config|Config|CONfig':[
				'config [SETTING] [ARG]',
				'\tUsed For Configuring Internal Functions',
				'\tconfig debug true/false',
				'\t\tInternal Debugging Flag (Also Accepts d,D,debug,Debug,DEBUG)',
				'\tconfig log true/false',
				'\t\tInternal Logging Flag (Also Accepts l,L,log,Log,LOG)',
				'\tconfig symbolic ID/SEGMENT.PAGE (Also Accepts s,S,symbolic,Symbolic,SYMBOLIC)',
				'\t\tCreates A Symbolic Link From Command To Segment Execution'
			],
		   'h|H|?|help|Help|HELP':[
		   		'help',
				'help ARG1 ARG2 ARG3',
				'\tUsed To Display This Help Screen...',
				'\tCan Also Take Arguments To Match Internally, If Any Match They Will Be Sent To "self.Display.Display()"'
		   ],
		   'Basic_Information|HowItWorks':[
		   		'[[!fR!] NOT A COMMAND [!fW!]]',
				'Documentation:',
				'\tAlien 3.5.30 is used as a enviroment to handle and execute pythonic objects in a structured manner,',
				'\tAlien uses a internal memory variable called "Registry()" this module allows us to:',
				'\t\t* Mount Pythonic Functions',
				'\t\t* Execute And Handle Functions In A Assembly Like Manner',
				'\t\t* Pipe Outputs And Inputs Between Functions',
				'\t\t* Read,Write, And Export Internal Segment Projects',
				'\t\t* Secure Projects With 2 Keys (Secure_Key,Author_Key) These Are Used To Obfuscate The Project',
				'\tThe Alien Interpreter is used to debug,handle, and build projects for usage use "h" or "help"',
				'',
				'\tHow The Registry Works:',
				'\t\tWe Hold Our Variables Inside Of A Dictionary Located At "self.Register.RG" From "Registry().RG",',
				'\t\tAlien will create "Builtin Operation Keys" via "self.Register.AddOpKey()",',
				'\t\t* These Operation Keys Can Be Called By The Alien Interpreter At Any Moment By Calling Its Name,',
				'\t\t* You Can See Operation Keys With Command "i o", Each Operation Key Takes X Amount Of Inputs',
				'\t\t! Example:"[!fG!]self.register.new test ff[!fW!]" Would Execute The Internal "self.builtin.new" Object',
				'\t\t^         Creating A Segment "test" With "ff" Values',
				'',
				'\t\tSegments are created under a segment ID (SID) inside of "Registry().RG" via "Registry().New(SID,LENGTH)"',
				'\t\t"LENGTH" being a hex value for page generation, this value cannot exceed 0xffffffffffffffff',
				'\t\t* This Operation Will Fail If SID Already Exists',
				'',
				'\t\tInternally Segments Can Be Written To Via "Registry().Write(SID,PID,OID,ORG)"',
				'\t\tSID Being The Segment ID, PID Being The Page ID, Operation Key ID,Operation Key Args',
				'\t\t* PID Must Exist Inside Of SID And OID Must Be A Valid Operation Key, With Valid A Valid Argument Lengths',
				'\t\tThis is written as a list to "Registry().RG[SID][PID]=[OID,ORG]"',
				'\t\t^ On execution it will execute on the the Operation Key with arguments from ORG via "Registry().ExeOpKey(OperationKey,OperationKeyArgs)"',
				'',
				'\tConfiguring From The Interpreter:',
				'\t\t* To Configure Internal Variables Like "Logging" & "Debugging" You Can Use: "c d true","c l true" Or "c d false","c l false"',
				'\t\t* You Can View Logs With "i l r"',
				'',
				'\tHow To Write To Segments And Pages:',
				'\t\t* You Can Create A New Segment With "new <sid> <hexlen>" Hex Length Be A Hex Byte Value (0/ffff...),',
				'\t\t* You Can Write To This Created Segment With "write <sid> <pid> <oid> <args....>" "pid" & "oid" Being "Page ID" & "OpKey ID"',
				'\t\t* You Can Find Pages Inside Of A Segment Via "i s <sid>" And Can Find A Specific Value Via "i s <sid> <pid>"',
				'\t\t* To Execute A Location Internally Use "@~<sid>.<pid>" This Can Also Be Supplied When Writing To A Pages OID Arguments ',
				'\t\t^ Example: "write example 0000000000000001 var.str 0 @~example.0000000000000002"',
				'\t\t^ This Can Also Be Replaced With //1 Or //2',
				'\t\t^ Example: "write example //1 var.str 0 @~example.//2"',
				'\t\t^ Executions Can Also Be Passed With Shortened Locations',
				'\t\t^ Example: "@~example.//2" Same As "@~example.0000000000000002"',
				'',
				'\tComments:',
				'\t\t* All Comments Are Found In The First 2 Character "@/"'
		   ]
		}
		self._Logger('__init__','Finished Setting Up Everything') # Tell Logger We Are Finished
	### Builtins ###
	## -- Internal Memory Functions -- #
	# For Creating New Segments
	def Builtin_Registry_New(self,IN):
		self._Logger('Builtin_Registry_New',str(IN))
		if len(IN) == 2: self.Register.New(str(IN[0]),str(IN[1]))
		else: raise self.AlienException('Builtin_Registry_New','Invalid Input By Arguement')
	# For Writing To Existing Segment Pages
	def Builtin_Registry_Write(self,IN):
		self._Logger('Builtin_Registry_Write',str(IN))
		if len(IN) >= 4:
			Target_SID    = IN[0]
			Target_Page   = IN[1]
			Target_OpCode = IN[2]
			#print(Target_SID,Target_Page,Target_OpCode)
			Target_Args = IN[3:]
			self.Register.Write(str(Target_SID),str(Target_Page),str(Target_OpCode),Target_Args)
		else: raise self.AlienException('Builtin_Registry_New','Invalid Length Sent Expected A Length Of 4')
	# For Logical Oprations
	def Builtin_Logic(self,IN):
		self._Logger('Builtin_Logic',str(IN))
		# [0] Operand
		# [1] Input_1 (SID.TARGET)
		# [2] Input_2 (SID.TARGET)
		# [3] Execute_True (SID.Target)
		# [4] Execute_False (SID.Target)
		if len(IN) == 5:
			Operand = str(IN[0])
			Targets = []
			Failed  = [False,None]
			for Location in IN[1:]:
				if str('.') in str(Location):
					Location = Location.split('.')
					if str(Location[0]) in self.Register.RG:
						if str(Location[1][:2]) == str('//'):Location[1] = str('0')*int(16-len(Location[1].strip('//')))+str(Location[1]).strip('//')
						if str(Location[1]) in self.Register.RG[str(Location[0])]: Targets.append(Location)
						else:
							Failed = [True,str(Location[1])];break
					else:
						Failed = [True,str(Location[0])];break
				else:
					Failed = [True,str(Location)];break
			if Failed[0] == False:
				if str(Operand) in ['==','is_equal']:
					Output_1 = self.Register.Execute(str(Targets[0][0]),str(Targets[0][1]))
					Output_2 = self.Register.Execute(str(Targets[1][0]),str(Targets[1][1]))
					if Output_1 == Output_2: return self.Register.Execute(str(Targets[2][0]),str(Targets[2][1]))
					else: return self.Register.Execute(str(Targets[3][0]),str(Targets[3][1]))
				else: self.Display.Display('[?builtin.header?] Invalid Operand Sent {}'.format(str(Operand)))
			else: self.Display.Display('[?builtin.header?] Operation Failed With Location {}'.format(str(Failed[1])))
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expected A Length Of 5')

	# For Executing Operation Codes
	def Builtin_Registry_ExeOpKey(self,IN):
		self._Logger('Builtin_Registry_ExeOpKey',str(IN))
		if len(IN) >= 2:
			Target_OpKey = IN[0]
			Target_OpArg = IN[1:]
			self.Register.ExeOpKey(Target_OpKey,Target_OpArg)
		else: raise self.AlienException('Builtin_Registry_ExeOpKey','Invalid Length Sent Expected A Length Of 2>')
	## -- Encoding & Hashing -- ##
	# For Encoding In Base64
	def Builtin_EncodeBase64(self,IN):
		self._Logger('Builtin_EncodeBase64',str(IN))
		Target_String = IN[0]
		for Line in IN[1:]:Target_String+=' '+str(Line)
		return base64.b64encode(bytes(str(Target_String),'utf-8')).decode('utf-8')
	# For Decoding In Base64
	def Builtin_DecodeBase64(self,IN):
		self._Logger('Builtin_DecodeBase64',str(IN))
		Target_String = IN[0]
		return base64.b64decode(bytes(str(Target_String),'utf-8')).decode('utf-8')
	# For Hashing Things
	def Builtin_HashLib(self,IN):
		self._Logger('Builtin_HashLib',str(IN))
		if len(IN) >= 3:
			Target_Hash_Type = IN[0]
			Target_Hash_Out  = IN[1]
			Target_Hash_Str  = IN[2]
			if len(IN[3:]) > 0:
				for Append_String in IN[3:]: Target_Hash_Str+=' '+str(Append_String)
			if Target_Hash_Type in hashlib.algorithms_available or Target_Hash_Type in hashlib.algorithms_guaranteed:
				Hash = hashlib.new(str(Target_Hash_Type))
				Hash.update(bytes(str(Target_Hash_Str),'utf-8'))
				if Target_Hash_Out in [0,'0','hex']: return Hash.hexdigest()
				elif Target_Hash_Out in [1,'1','digest']: return Hash.digest().decode('utf-8')
				else: raise self.AlienException('Builtin_HashLib','Invalid HashType For Output Expected [0,hex/1,digest]')
			else: raise self.AlienException('Builtin_HashLib','Invalid Hash Algorithm Sent')
		else: raise self.AlienException('Builtin_HashLib','Invalid Length Sent Expected A Length A 3>')
	## -- Variables  -- ##
	# For Handling Variables
	def Builtin_Var_String(self,IN): # Strings
		self._Logger('Builtin_Var_String',str(IN))
		if len(IN) >= 2:
			Operand = IN[0]
			Target  = IN[1]
			if str('@%n') in str(Target): Target=Target.replace('@%n','\n')
			elif str('@%t') in str(Target): Target=Target.replace('@%t','\t')
			Args    = IN[2:]
			# Parse String Functions
			if str(Operand) in [0,'0','r','R','return','Return','RETURN']:
				# Returns A String And Will Compile With Args
				for Arg in Args:
					if str('@%n') in str(Arg): Arg=Arg.replace('@%n','\n')
					elif str('@%t') in str(Arg): Arg=Arg.replace('@%t','\t')
					if len(Arg) > 0:Target += ' '+str(Arg)
				return str(Target)
			else: self.Display.Display('[?builtin.header?] Invalid Operand {} For String {}'.format(str(Operand),str(Target)))
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expected 2>')
	# For Handling Lists
	def Builtin_Var_List(self,IN): # Lists
		self._Logger('Builtin_Var_List',str(IN))
		if len(IN) >= 2:
			Operand = IN[0]
			Target  = IN[1]
			Args    = IN[2:]
			if type(Target) is not list:
				# Convert To List
				if str('|') in str(Target):Target = Target.split('|')
				else:
					self.Display.Display('[?builtin.header?] Expected A list Object Got Other... {}'.format(str(Target)))
			# Return List
			if str(Operand) in [0,'0','r','R','return','Return','RETURN']: return Target
			# Is In List
			elif str(Operand) in [1,'1','i','I','in','In','IN']:
				if len(Args) == 1:
					if str(Args[0]) in Target: return True
					else: return False
				else: self.Display.Display('[?builtin.header?] Expected 1 Args For {} '.format(str(Operand)))
			# Pull With Int
			elif str(Operand) in [2,'2','t','T','target','Target','TARGET']:
				if len(Args) == 1:
					if type(Args[0]) is int:
						if Args[0] <= len(Target)-1: return Target[Args[0]]
						else: self.Display.Display('[?builtin.header?] Args Index Target Is Out Of Range {} > {}'.format(str(Args[0]),str(len(Target)-1)))
					else: self.Display.Display('[?builtin.header?] Invalid Type Expected int Got {}'.format(str(type(Args[0]))))
				else: self.Display.Display('[?builtin.headear?] Invalid Length Sent Expected 1 Argument Got {}'.format(str(len(Args))))
			# Pull Target Range
			elif str(Operand) in [3,'3','x','X','range','Range','RANGE']:
				if len(Args) == 2:
					if int(Args[0]) < int(Args[1]):
						if int(Args[1]) < len(Target): return Target[int(Args[0]):int(Args[1])]
						else: self.Display.Display('[?builtin.header?] Invalid Argument For Scope {} Is Greater Than List Length {}'.format(str(Args[1]),str(len(Target))))
					else: self.Display.Display('[?builtin.header?] Invalid Argument For Scope {} Must Be Less Than {}'.format(str(Args[0]),str(Args[1])))
				else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expected 2 Arguments Got {}'.format(str(len(Args))))
			else: self.Display.Display('[?builtin.header?] Invalid Operand {} For List {}'.format(str(Operand),str(Target)))
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expected 2>')
	# For Handling Ints
	def Builtin_Var_Int(self,IN):
		self._Logger('Builtin_Var_Int',str(IN))
		if len(IN) >= 2:
			Operand = IN[0]
			Target  = IN[1]
			Args    = IN[2:]
			if Operand in [0,'0','r','R','return','Return','RETURN']:
				if type(Target) is int: return int(Target)
				else:
					IsInt = True
					for Character in str(Target):
						if str(Character) not in '0123456789': IsInt = False
					if IsInt == True:return int(Target)
					else: self.Display.Display('[?builtin.header?] Value Sent Is Not A "int" Type {}'.format(str(Target)))
			else: self.Display.Display('[?builtin.header?] Invalid Operand {} For int {}'.format(str(Operand),str(Target)))
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expected 2>')
	# For Handling Booleans #
	def Builtin_Var_Bool(self,IN):
		self._Logger('Builtin_Var_Bool',str(IN))
		if len(IN) >= 2:
			Operand = IN[0]
			Target  = IN[1]
			Args    = IN[2:]
			if Operand in [0,'0','r','r','return','Return','RETURN']:
				if str(Target) in [0,'0','f','F','false','False','FALSE']:return False
				elif str(Target) in [1,'1','t','T','true','True','TRUE']: return True
				else: self.Display.Display('[?builtin.header?] Invalid Input Sent Expected A Boolean Variable Got {}'.format(str(Target)))
			else: self.Display.Display('[?builtin.header?] Invalid Operand {} For bool {}'.format(str(Operand),str(Target)))
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Explected 2>')
	# For Finding Variable Types #
	def Builtin_Var_Type(self,IN):
		self._Logger('Builtin_Var_Type',str(IN[0]))
		if len(IN) == 1: return type(IN[0])
		else: self.Display.Display('[?builtin.header?] Invalid Length Sent Expeced 1')
	## -- Functions -- ##
	def Builtin_PageToPage(self,IN):
		self._Logger('Builtin_PageToPage',str(IN))
		if len(IN) == 3:
			SID = IN[0]
			OPG = IN[1]
			EPG = IN[2]
			if str(SID) in self.Register.RG:
				if str(OPG) in self.Register.RG[str(SID)] and str(EPG) in self.Register.RG[str(SID)]:
					Page_Index = []
					for Page in self.Register.RG[str(SID)]:Page_Index.append(str(Page))
					if Page_Index.index(OPG) < Page_Index.index(EPG):
						Pages = Page_Index[Page_Index.index(OPG):Page_Index.index(EPG)+1]
						Output = []
						for Page in Pages: Output.append(self.Register.Execute(str(SID),str(Page)))
						return Output
					else: self.Display.Display('[?builtin.header?] Invalid Index Values Expected {} To Be Lower Than {}'.format(str(OPG),str(EPG)))
				else: self.Display.Display('[?builtin.header?] Invalid Index Values By Existance {} And {} Do Not Exist Inside Of {}'.format(str(OPG),str(EPG),str(SID)))
			else: self.Display.Display('[?builtin.header?] Invalid SiD {} Is Non-Existant'.format(str(SID)))
		else: self.Dispaly.Display('[?builtin.header?] Invalid Length Expected 3')
	## -- Display -- ##
	# Send A String To Display
	def Builtin_TextToDisplay(self,IN):
		self._Logger('Builtin_TextToDisplay',str(IN))
		TTD = IN[0]
		for Line in IN[1:]:
			if type(Line) is not str:Line=str(Line)
			if len(Line) > 0:TTD+=' '+str(Line)
		self.Display.Display(str(TTD))
	# Append A New Header
	def Builtin_TextToHeader(self,IN):
		self._Logger('Builtin_TextToHeader',str(IN))
		if len(IN) > 1:
			Root = str(IN[0])
			Stem = IN[0:]
			Comp = ''
			for Line in Stem:
				if len(Comp) == 0:Comp = str(Line)
				else: Comp += ' '+str(Line)
			self.Display.PalletKeys[2][str(Root)]=str(Comp)
		else: raise self.AlienException('Builtin_TextToHeader','Invalid Length Expected 1>')
	# Fetch User Input (Passes Through Color And Messae Handler Prior)
	def Builtin_UserInput(self,IN):
		Prompt = ''
		for String in IN:
			if len(Prompt) == 0: Prompt = str(String)
			else: Prompt += ' {}'.format(str(String))
		Prompt = self.Display.FindMessage(str(Prompt));Prompt = self.Display.FindColours(str(Prompt));return input(str(Prompt))

	# Append A ASCII Art File
	def Builtin_TextToASCIIArt(self,IN):
		self._Logger('Builtin_TextToASCIIArt',str(IN))
		if len(IN) ==	1:
			if os.path.isfile(str(IN[0])) == True:
				Text = open(str(IN[0])).read().split('\n')
				Inside = False
				Target = None
				Append = {}
				for Line in Text:
					# All Input Are Caught With The First Two Characters Char[:2]
					# '//' Comment
					# '<# ID CHAR:OPEN:CLOSE ...' Opens A Header And Will Handle All Following Arguments In-Line For Replacment
					# '#>' Close
					if len(Line) > 0:
						if str(Line[:2]) == str('//'): continue
						elif str(Line[:2]) == str('<#'):
							Tree = str(Line).split(' ')
							Target = str(Tree[1])
							Inside = True
							Append[str(Target)]=[ Tree[2:],[] ]
						elif str(Line) == str('#>') or str(Line[:2]) == str('#>'):
							Target = None;Inside = False
						else:
							if Target != None and Inside == True and str(Line) != str('#>') or str(Line[:2]) != str('#>'):
								for Characters in Append[Target][0]:
									Characters = Characters.split(':')
									if str(Characters[0]) in str(Line):Line = Line.replace(str(Characters[0]),'{}{}{}'.format(str(Characters[1]),str(Characters[0]),str(Characters[2])))
								Append[Target][1].append(str(Line))
				# Appn Should Be Compiled
				self._Logger('Builtin_TextToASCIIArt','Preparing To Append Messages From File {} To Internal Headers {}'.format(str(IN[0]),str(Append)))
				for ID in Append:
					MS = ''
					for Line in Append[ID][1]:
						MS+=str(Line)+'\n'
					self.Display.PalletKeys[2][str(ID)]=str(MS)
					self._Logger('Builtin_TextToASCIIArt','Created Internal Message Header {}'.format(str(ID)))
			else: self.Display.Display('[?builtin.header?] Invalid File {} Is Non-Existant'.format(str(IN[0])))
		else: raise self.AlienException('Builtin_TextToASCIIArt','Invalid Length Expected 1')
	### Mounting Builtins ###
	def Mount_Builtin(self):
		self._Logger('Mount_Builtin')
		# Memory
		self.Register.AddOpKey('new','Appends New Segments Inside Of "self.Register" ["SID","HEXLEN"]',2,self.Builtin_Registry_New)
		self.Register.AddOpKey('write','Writes A OpCode Execution To A Target Inside Of "self.Register" ["SID","PID","OID","ARGS",...]','*',self.Builtin_Registry_Write)
		# Encoding & Hashing
		self.Register.AddOpKey('base64.encode','Encodes A Base64 String ["STRING","STRING"]','*',self.Builtin_EncodeBase64)
		self.Register.AddOpKey('base64.decode','Decodes A Base64 String["BASE64STRING"]','*',self.Builtin_DecodeBase64)
		self.Register.AddOpKey('hash','Hashes A String Based Off Your Desired Type. Args: [TYPE,MODE,STR1.....]','*',self.Builtin_HashLib)
		# Variables
		self.Register.AddOpKey('var.str','For Handling String Variables ["OPERAND","VARIABLE","ARGS"....] NOTE: @%n Is NewLine, @%t Is Tab','*',self.Builtin_Var_String)
		self.Register.AddOpKey('var.list','For Handling List Variables ["OPERAND","VARIABLE","ARGS"...]',"*",self.Builtin_Var_List)
		self.Register.AddOpKey('var.int','For Handling Integer Variables ["OPERAND","VARIABLE","ARGS"....]',"*",self.Builtin_Var_Int)
		self.Register.AddOpKey('var.bool','For Handling Boolean Variables ["OPERAND","VARIABLE","ARGS"....]',"*",self.Builtin_Var_Bool)
		self.Register.AddOpKey('var.type','To Identify A Variable Type ["VARIABLE"]',1,self.Builtin_Var_Type)
		# Functions
		self.Register.AddOpKey('func','For Executing Pages In A Specified Range ["LOWPAGE","HIGHPAGE"]',3,self.Builtin_PageToPage)
		# Display
		self.Register.AddOpKey('ttd.display','For Sending Text To The Display ["This","Is","A","String"]','*',self.Builtin_TextToDisplay)
		self.Register.AddOpKey('ttd.header','For Creating A Mounted Header Inside Of self.Display.PalletKeys[2] [<ID>,"string","to","send"]','*',self.Builtin_TextToHeader)
		self.Register.AddOpKey('ttd.asciiart','For Opening And Parsing ASCII Art Files',1,self.Builtin_TextToASCIIArt)
		# User Input
		self.Register.AddOpKey('sys.userinput','For Fetching User Input ["This","String","Can","Have","Colours"]',"*",self.Builtin_UserInput)
		# Logical
		self.Register.AddOpKey('logic','For Handling Logical Operations ["OPERAND","SID.LOC"...] TAKES 5 ARGUMENTS','*',self.Builtin_Logic)
	### Mounting External Module File ###
	def Mount_External(self,File):
		self._Logger('Mount_External','Input File: '+str(File))
		if os.path.isdir(str(File)) == True:
			File_Mount = __import__(str(File))
			try:
				Target_OpKeys = File_Mount.__OPKEY__
				Failed        = []
				for OKY in Target_OpKeys:
					if type(OKY) is list:
						if len(OKY) == 4: self.Register.AddOpKey(str(OKY[0]),str(OKY[1]),OKY[2],OKY[3])
						else: Failed.append([OKY,'len'])
					else: Failed.append([OKY,'type'])
				if len(Failed) > 0:
					for Failed_OpKey in Failed: self.Display.Display('[?builtin.header?] Invalid Operation Key {} With Error {}'.format(str(Failed_OpKey[0]),str(Failed_OpKey[1])))
			except Exception as e:
				self._Logger('Mount_External','Expected A Variable "__OPKEY__" For Mounting Of Operation Keys... Is Non-Existant');self._Logger('Mount_External','Exception:{}'.format(str(e)));self.Display.Display('[?builtin.header?] Invalid External Mount File By Variable... Breaking...');return
		else: raise self.AlienException('Mount_External','Invalid Directory Sent For import ')
	### Banner ###
	def RaiseBanner(self):
		self._Logger('RaiseBanner')
		Banner = '[!fG!][!sB!]'+str(self.Fonts.RandomFont('Alien'))+str('[?builtin.spacer?][?builtin.header?] Author :\t[!fC!]J[!fR!]4[!fC!]ck[!fB!]3[!fC!]LSyN\n[?builtin.header?] Version:\t[!fR!]3.5.30\n[?builtin.spacer?]')
		self.Display.Display(str(Banner))
	### Parse Input Level 0 ###
	def HandleInput(self,Input):
		self._Logger('HandleInput',str(Input))
		# Seperate For New Lines
		if str('->') in str(Input): Input = Input.split('->')
		else: Input = [str(Input)]
		# Parse Each Line
		for Line in Input:
			if len(Line) > 2:
				if str(Line[:2]) == str('@/'): continue
			if str(' ') in str(Line):
				Tree = Line.split(' ');TINX = 0
				for Possilbe_Location in Tree:
					if len(Possilbe_Location) > 2:
						if str(Possilbe_Location[:2]) == str('//'): Tree[TINX] = str('0')*int(16-len(Possilbe_Location.strip('//')))+str(Possilbe_Location).strip('//')
						elif str(Possilbe_Location[:2]) == str('@~'):
							Target_Location = Possilbe_Location.split('.')[1]
							if str(Target_Location[:2]) == str('//'):
								Compile_Location = str('0')*int(16-len(Target_Location.strip('//')))+str(Target_Location).strip("//")
								Compile_Location = str(Possilbe_Location.split('.')[0])+str('.')+str(Compile_Location)
								Tree[TINX]=str(Compile_Location);self._Logger('HandleInput','Replaced Execution Location {} With {}'.format(str(Possilbe_Location),str(Compile_Location)))
					TINX += 1
				if str(Tree[0]) in self.Register.OpExec:
					if self.Debug == True: self.Display.Display('[?builtin.header?] Executing Operation Key: {} With Args {}'.format(str(Tree[0]),str(Tree[1:])))
					OpExecArgs = Tree[1:];Output = self.Register.ExeOpKey(str(Tree[0]),OpExecArgs)
					if self.Debug == True: self.Display.Display('[?builtin.header?] Command({}) Output:{}'.format(str(Input),str(Output)))
				else:
					# Information Commands
					#:?>i
					if str(Tree[0]) in ['i','I','info','Info','INFO']:
						# Expect Args 1 Or Greater
						if len(Tree[1:]) >= 1:
							# Identify The Segment Information
							if str(Tree[1]) in ['s','S','segment','Segment','SEGMENT']:
								self.Display.Display('[?builtin.spacer?][?builtin.header?] Showing All Internal Segments {}'.format(str(len(self.Register.RG))))
								# Are We Working With A Segment?
								if len(Tree[2:]) >= 1:
									if str(Tree[2]) in self.Register.RG:
										#print(str(Tree))
										# Are We Going Down To The Page?
										if len(Tree[1:]) == 3:
											if str(Tree[3]) in self.Register.RG[str(Tree[2])]:
												self.Display.Display('[?builtin.header?] ([!fB!]info[!fW!]) Location: {}.{} \t {}'.format(str(Tree[2]),str(Tree[3]),str(self.Register.RG[Tree[2]][Tree[3]])));return
											else:
												self.Display.Display('[?builtin.header?] ([!fB!]info[!fW!]) Sent Location {} Is Non-Existant Inside Of {}'.format(str(Tree[3]),str(Tree[2])));return
										else:
											self.Display.Display('[?builtin.header?] ([!fB!]info[!fW!]) Segment: {}'.format(str(Tree[2])))
											for Page in self.Register.RG[str(Tree[2])]: self.Display.Display('[?builtin.header?] ([!fB!]info[!fW!]) {}.{} \t {}'.format(str(Tree[2]),str(Page),str(self.Register.RG[Tree[2]][Page])))
											return
								else:
									for SID in self.Register.RG:self.Display.Display('[?builtin.header?] ([!fR!]Segment[!fW!]) {} Has {} Pages'.format(str(SID),str(len(self.Register.RG[SID]))))
								# Display All Segments
								for Segments in self.Register.RG:
									self.Display.Display('[?builtin.header?] {} With {} Pages'.format(str(Segments),str(len(self.Register.RG[Segments]))))
									# Do We Want To Target A Page
									if len(Tree[1:]) == 2:
										# Display All Page IDs
										if str(Tree[2]) in ['*','all','All','ALL']:
											for Page in self.Register.RG[str(Segments)]: self.Display.Display('[?builtin.header?] {} {} {}'.format(str(Segments),str(Page),str(self.Register.RG[Segments][Page])))
										elif str(Tree[2]) in self.Register.RG[Segments]: self.Display.Display('[?builtin.header?] {} {} {}'.format(str(Segments),str(Tree[2]),str(self.Register.RG[Segments][Tree[2]])))
										else: self.Display.Display('[?builtin.header?] Invalid Argument For Command {} Expected "i s *" Or "i s TARGET_PAGE"'.format(str(Input)))
									else:
										if len(Tree) != 2:self.Display.Display('[?builtin.header?] Invalid Arguements By Length "info segment" Only Accepts 1 Following Argument');break
							# Identify The OpKey Information
							elif str(Tree[1]) in ['o','O','opkey','OpKey','OPKEY']:
								self.Display.Display('[?builtin.spacer?][?builtin.header?] Showing All Internal Operation Keys {}'.format(str(len(self.Register.OpExec))))
								if len(Tree) == 3:
									if str(Tree[2]) in self.Register.OpExec:
										self.Display.Display('[?builtin.header?] ([!fR!]info[!fW!]) Operation Key: {} // Description: {} // Argument Length: {}'.format(str(Tree[2]),str(self.Register.OpExec[Tree[2]][0]),str(self.Register.OpExec[Tree[2]][1])));return
								for OperationKeys in self.Register.OpExec:
									self.Display.Display('[?builtin.header?] OperationKey {} Takes {} Arguments'.format(str(OperationKeys),str(self.Register.OpExec[OperationKeys][1])))
									if len(Tree[1:]) == 2:
										# Read Description
										if str(Tree[2]) in ['d','D','description','Description','DESCRIPTION']: self.Display.Display('[?builtin.header?] {} \n[?builtin.header?]\t {} \n[?builtin.spacer?]'.format(str(OperationKeys),str(self.Register.OpExec[OperationKeys][0])))
										# Read Argument Length
										elif str(Tree[2]) in ['l','L','arglen','ArgLen','ARGLEN']: self.Display.Display('[?builtin.header?] {} // {}'.format(str(OperationKeys),str(self.Register.OpExec[OperationKeys][1])))
										# Read All Information
										elif str(Tree[2]) in ['*','all','All','ALL']: self.Display.Display('[?builtin.header?] OpKey({}) // Description({}) // ArgLen({})'.format(str(OperationKeys),str(self.Register.OpExec[OperationKeys][0]),str(self.Register.OpExec[OperationKeys][1])))
										else: self.Display.Display('[?builtin.header?] Invalid Argument for Command {} Expected "i o d","i o l","i o *"')
									else:
										if len(Tree) != 2:self.Display.Display('[?builtin.header?] Invalid Arguments By Length "info opkey" Only Accepts 1 Follow Argument');break
							# Read Log Information
							elif str(Tree[1]) in ['l','L','log','Log','LOG']:
								if len(Tree[1:]) == 1:
									if Tree[2] in ['s','S','status','Status','STATUS']: self.Display.Display('[?builtin.header?] Log Status: {}'.format(str(self.Logging)))
									elif Tree[2] in ['r','R','read','Read','READ']:
										Line_Count = 0
										for Line in self.LogText:
											self.Display.Display('Line ([!fR!]{}[!fW!]) > {}'.format(str(Line_Count),str(Line)))
											Line_Count += 1
									else: self.Display.Display('[?builtin.header?] Invalid Follow Up Argument {} For {}'.format(str(Tree[2]),str(Tree[1])))
								else:
									self.Display.Display('[?builtin.header?] Status : {}'.format(str(self.Logging)))
									Line_Count = 0
									for Line in self.LogText:
										self.Display.Display('Line ([!fR!]{}[!fW!]) > {}'.format(str(Line_Count),str(Line)))
										Line_Count += 1
							# Read Symbolic Information
							elif str(Tree[1]) in ['%','symbolic','Symbolic','SYMBOLIC']:
								if len(Tree) == 3:
									if str(Tree[2]) in ['*','all','All','ALL']:
										self.Display.Display('[?builtin.header?] Showing All Symbolic Links')
										for Syms in self.SYMBOLIC: self.Display.Display('[?builtin.header?] Symbolic Link([!fC!]{}[!fW!]) Execution([!sB!][!fG!]{}[!fW!].[!fG!]{}[!fW!][!sN!])'.format(str(Syms),str(self.SYMBOLIC[Syms][0]),str(self.SYMBOLIC[Syms][1])))
									elif str(Tree[2]) in self.SYMBOLIC: self.Display.Display('[?builtin.header?] Showing Information For Symbolic Link ([!fC!]{}[!fW!]) // Execution([!sB!][!fG!]{}[!fW!].[!fG!]{}[!fW!][!sN!])'.format(str(Tree[2]),str(self.SYMBOLIC[Tree[2]][0]),str(self.SYMBOLIC[Tree[2]][1])))
									else: self.Display.Display('[?builtin.header?] Invalid Argument {} For Command "info symbolic"'.format(str(Tree[2])))
								else: self.Display.Display('[?builtin.header?] Invalid Argument By Length "info symbolic <Action>"')
							# Read Banner Information
							elif str(Tree[1]) in ['banners','Banners','BANNERS','banner','Banner','BANNER']:
								for Banner in self.Display.PalletKeys[2]: self.Display.Display('[?builtin.header?] Banner ID:[!fC!]{}'.format(str(Banner)))
							# Invalid Followup For info
							else: self.Display.Display('[?builtin.header?] Invalid Follow Up Argument For "Info" {}'.format(str(Tree[1:])))
					# Usage Commands
					#:?>h
					elif str(Tree[0]) in ['h','H','?','help','Help','HELP']:
						Line_Out = []
						for Arg in Tree[1:]:
							for Command in self.USAGE:
								if str(Arg) in Command: Line_Out.append('[?builtin.header?] ([!fR!]{}[!fW!])'.format(str(Command)))
								for Lines in self.USAGE[Command]:
									if str(Arg) in str(Lines): Line_Out.append('[?builtin.header?] ([!fR!]{}[!fW!]) >> {}'.format(str(Command),str(Lines.replace(Arg,'[!fG!]{}[!fW!]'.format(str(Arg))))))
						for Line in Line_Out: self.Display.Display('[?builtin.header?] Usage Directed: {}'.format(str(Line)))
					# Configure Commands
					#:?>c
					elif str(Tree[0]) in ['c','C','config','Config','CONFIG']:
						if len(Tree[1:]) == 2:
							Target = Tree[1]
							SetTo  = Tree[2]
							if str(SetTo) in ['t','T','true','True']: SetTo = True
							elif str(SetTo) in ['f','F','false','False']: SetTo = False
							if str(Target) in ['d','D','debug','Debug','DEBUG']:
								if type(SetTo) is bool:
									self.Debug = SetTo;self.Display.Display('[?builtin.header?] Configured Internal Variable "Debug" To {} '.format(str(SetTo)))
								else: self.Display.Display('[?builtin.header?] Expected A Boolean Type For This Variable Got {}'.format(str(type(SetTo))))
							elif str(Target) in ['l','L','log','Log','LOG']:
								if type(SetTo) is bool:
									self.Logging = SetTo;self.Display.Display('[?builtin.header?] Configured Internal Variable "Log" To {}'.format(str(SetTo)))
								else: self.Display.Display('[?builtin.header?] Expected A Boolean Type For This Variable Got {}'.format(str(type(SetTo))))
							# Setting Symbolics
							elif str(Target) in ['s','S','symbolic','Symbolic','SYMBOLIC']:
								if str(':') in str(SetTo):
									SetTo_Tree = SetTo.split(':')
									if str('.') in str(SetTo_Tree[1]):
										SetTo_Stem = SetTo_Tree[1].split('.')
										if str(SetTo_Stem[0]) in self.Register.RG:
											#print(str(SetTo_Stem))
											if str(SetTo_Stem[1][:2]) == str('//'):
												SetTo_Stem[1] = str('0')*int(16-len(SetTo_Stem[1].strip('//')))+str(SetTo_Stem[1].strip('//'))
											if str(SetTo_Stem[1]) in self.Register.RG[SetTo_Stem[0]]:
												if str(SetTo_Tree[0]) not in self.SYMBOLIC:
													self.SYMBOLIC[str(SetTo_Tree[0])]=SetTo_Stem;self.Display.Display('[?builtin.header?] Configured A Symbolic Object {} With Pointer {}'.format(str(SetTo_Tree[0]),str(SetTo_Stem)))
												else: self.Display.Display('[?builtin.header?] SYMBOLIC_ID {} Is Existant'.format(str(SetTo_Tree[0])))
											else: self.Display.Display('[?builtin.header?] Target Page ID {} Is Non-Existant'.format(str(SetTo_Stem[1])))
										else: self.Display.Display('[?builtin.header?] Target Segment ID {} Is Non-Existant'.format(str(SetTo_Stem[0])))
									else: self.Display.Display('[?builtin.header?] Expected A Location Seperator "SYMBOLIC_ID/SEGMENT.PAGE" Failed To Find "."')
								else: self.Display.Display('[?builtin.header?] Expected A Name Seperator "SYMBOLIC_ID:SEGMENT.PAGE"')
							else: self.Display.Display('[?builtin.header?] Expected A Valid Target Configuration Got {}'.format(str(Target)))
						else: self.Display.Display('[?builtin.header?] Invalid Length Expected 2 Got {}'.format(str(len(Tree[1:]))))
					# Failed Commands
					else: self.Display.Display('[?builtin.header?] Invalid Command Tree: [!fR!]{}[!fW!] Raw Input [!fC!]{}[!fW!]'.format(str(Tree),str(Input)))

			else:
				if len(Line) > 2 and str(Line[:2]) == str('@~'):
					Line = Line.strip('@~')
					if str('.') in str(Line):
						Tree = Line.split('.')
						Root = Tree[0]
						Stem = Tree[1]
						if str(Stem[:2]) == str('//'):
							Stem = str('0')*int(16-len(Stem.strip('//')))+str(Stem).strip('//');self._Logger('HandleInput','Found Short Location In Execution {} Replaced With {}'.format(str(Line),str(Stem)))
						if  str(Root) in self.Register.RG:
							if str(Stem) in self.Register.RG[str(Root)]:
								Output = self.Register.Execute(str(Root),str(Stem));self.Display.Display('[?builtin.header?] Output {} From Location {}'.format(str(Output),str(Line)));return str(Output)
							else: self.Display.Display('[?builtin.header?] Invalid Stem Sent For SID {} | {}'.format(str(Root),str(Stem)))
						else: self.Display.Display('[?builtin.header?] Invalid SID Sent {}'.format(str(Root)))
					else:
						if str(Line) in self.Register.RG:
							Output = self.Register.Execute(Line);return Output
						else: self.Display.Display('[?builtin.header?] Invalid SID Sent For Execution {} Is Non-Existant'.format(str(Line)))
				elif str(Line) in ['q','Q','quit','Quit','QUIT','exit','Exit','EXIT']: self.HEART_BEAT = False
				elif str(Line) in ['h','H','?','help','Help','HELP']:
					for Command in self.USAGE:
						self.Display.Display('[?builtin.header?] (USAGE) {}'.format(str(Command).replace('|',', ')))
						for Line in self.USAGE[Command]:
							self.Display.Display('[?builtin.header?] {}'.format(str(Line)))
						self.Display.Display('[?builtin.spacer?]')
				elif str(Line) in self.SYMBOLIC:
					Output = self.Register.Execute(self.SYMBOLIC[Line][0],self.SYMBOLIC[Line][1]);self.Display.Display('[?builtin.header?] Symbolic Tag {} Returned {}'.format(str(Line),str(Output)));return Output
				elif len(Line) == 0: self.Display.Display('[?builtin.header?] Recieved No Input, Use "h","H","?" or just "help" For Help')
				else: self.Display.Display('[?builtin.header?] Invalid Command Sent: [!fR!]{}[!fW!]'.format(str(Line)))

	### Heart ###
	def Heart(self):
		self._Logger('Heart')
		if self.HEART_BEAT == True:
			self.RaiseBanner()
			Interrupt_Count = 0
			if self.Project != None:
				if os.path.isdir(str(self.Project)) == True:
					Target_Projects = os.listdir(str(self.Project))
					for Project in Target_Projects:
						self.Display.Display('[?builtin.header?] ([!fR!]Project[!fW!]) {} Opening...'.format(str(Project)))
						Target_Path = os.path.join(str(self.Project),str(Project))
						Target_Text = open(str(Target_Path)).read().split('\n')
						for Line in Target_Text: self.HandleInput(str(Line))
				else: self.Display.Display('[?builtin.header?] Attempted To Find {} But Is Non-Existant'.format(str(self.Project)))
			if self.PreExec[1] != None:
				if os.path.isfile(str(self.PreExec[1])) == True:
					File = open(str(self.PreExec[1])).read().split('\n')
					for Line in File:
						if len(Line) > 0: self.HandleInput(str(Line))
				else: raise self.AlienException('Heart','Recieved File Input {} But Is Non-Existant'.format(str(self.PreExec[1])))
			if self.PreExec[0] != None: self.HandleInput(str(self.PreExec[0]))
			if self.External != None: self.Mount_External(str(self.External))
			while self.HEART_BEAT == True:
				if Interrupt_Count >= 9: self.Display.Display('[?builtin.header?] [!fR!]Exiting Due To [!fB!]KeyboardInterrupt[!fR!]...');self.HEART_BEAT=False
				try:
					# Raise Prompt And Fetch User Input
					Prompt = self.Display.FindColours('[!fG!][!sB!]:[!fC!]?[!fR!]>[!fW!][!sN!] ')
					UserIn = input(str(Prompt));self.HandleInput(str(UserIn))
				# Handle Exceptions
				except KeyboardInterrupt:
					Interrupt_Count+=1;self.Display.Display('[?builtin.header?] KeyboardInterrupt ({})'.format(str(Interrupt_Count)))
				except Exception as E : self.Display.Display('[?builtin.header?] Exception : [!fR!]{}[!fW!] From [!fG!]{}'.format(str(E),str(UserIn)))
				except NameError as E : self.Display.Display('[?builtin.header?] NameError : [!fR!]{}[!fW!] From [!fG!]{}'.format(str(E),str(UserIn)))
				except TypeError as E : self.Display.Display('[?builtin.header?] TypeError : [!fR!]{}[!fW!] From [!fG!]{}'.format(str(E),str(UserIn)))
				except IndexError as E: self.Display.Display('[?builtin.header?] IndexError: [!fR!]{}[!fW!] From [!fG!]{}'.format(str(E),str(UserIn)))
				except ValueError as E: self.Display.Display('[?builtin.header?] ValueError: [!fR!]{}[!fW!] From [!fG!]{}'.format(str(E),str(UserIn)))
			self.Display.Display('[?builtin.spacer?][?builtin.header?] Exiting Alien 3.5.30...')
			sys.exit(1)
		else: raise self.AlienException('Heart','Expected Internal "self.HEART_BEAT" Variable To Be "True" Is "False"')
	### Logging Handler ###
	def _Logger(self,Root,Message=None):
		Message_Padding = 50
		if Message != None: Message_Padding -= len(Root)+len(Message)
		Message_Padding = str('-'*Message_Padding)
		if self.Logging == True:
			Log_Message = str(time.asctime())+'\tRoot({}){}Message({})'.format(str(Root),str(Message_Padding),str((Message)));self.LogText.append(str(Log_Message))
			if self.Debug == True: self.Display.Display('[?builtin.header?] ([!fR!]LOG-DEBUG[!fW!]) {}'.format(str(Log_Message)))
		else:
			if self.Debug == True: self.Display.Display('[?builtin.header?] ([!fR!]Raw-DEBUG[!fW!]) Root({}) {} Message({})'.format(str(Root),str(Message_Padding),str(Message)))
	### Exception Handler ###
	def AlienException(self,Root,Message):
		self._Logger('AlienException','Exception {} With Message {}'.format(str(Root),str(Message)))
		Message = str('Exception From: {} With Message {}'.format(str(Root),str(Message)));raise Exception(str(Message))


if __name__ == "__main__":
	if os.path.isfile(str('install.sh')) == True:
		print('[!] Have You Ran "install.sh" Via: "chmod +x install.sh && ./install.sh"?')
		userinput = input('(Y/N)>')
		if userinput in ['y','Y','yes','Yes','YES']:
			print('[!] Would You Like To Delete This File?')
			userinput_delete = input('(Y/N)>')
			if userinput_delete in ['y','Y','yes','Yes','YES']: print('[!] Deleting.....{}'.format(str(subprocess.Popen(['rm -f install.sh'],stdout=subprocess.PIPE,shell=True).stdout.read().decode('utf-8'))))
		else:
			print('[!] Would You Like To Install?')
			userinput = input('(Y/N)>')
			if userinput in ['y','Y','yes','Yes','YES']:
				print('[!] Installing.......{}'.format(str(subprocess.Popen(['chmod +x install.sh && ./install.sh'],stdout=subprocess.PIPE,shell=True).stdout.read().decode('utf-8'))));sys.exit(1)

	if len(sys.argv) == 1:
		A = Alien(str('0'*16),str('0'*16))
		A.Mount_Builtin()
		A.Heart()
	else:
		Config = {'NoMount_BI':False,'K0':str('0'*16),'K1':str('0'*16),'DB':False,'LG':False,'ExecLine':None,'ExecFile':None,'MountAllProjects':None,'ASCII_ART':None,'External':None}
		Arg_Counter = 0
		Read_To_ExecLine = False
		for Argument in sys.argv[1:]:
			if str(Argument) in ['-d','--debug']:
				print('[!] Set Debugging Flag To True');Config['DB']=True
			elif str(Argument) in ['-l','--logging']:
				print('[!] Set Logging Flag To True');Config['LG']=True
			elif str(Argument) in ['-nM','--no-mount']:
				print('[!] Set No Mount Builtin To True');Config['NoMount_BI']=True
			elif str(Argument) in ['-map','--mount-all-projects']:
				print('[!] Set Mount All Projects To True');Config['MountAllProjects']='AlienProjects'
			elif str(Argument) in ['-h','--help']:
				Usage = [
					'Alien 3.5.30',
					'Usage: python3 Alien.py [ARG] [ARG] [ARG] -e "string to execute"',
					'-'*120,
					'\t-h, --help    \n\t\tDisplays This Help Screen',
					'\t-d, --debug   \n\t\tSets Debuging Flag',
					'\t-l  --logging \n\t\tSets Logging Flag',
					'\t-map --mount-all-projects \n\t\tSets All Projects To Be Mounted',
					'\t-nM --no-mount\n\t\tSets Internal Builtin Mount To False',
					'\t-k0:KEY       \n\t\tSets Key Zero To Key (Must Be 16 Bits [8 Bytes])',
					'\t-k1:KEY       \n\t\tSets Key One To Key (Must Be 16 Bits [8 Bytes])',
					'\t-f:FILE       \n\t\tSets Execute File To Execute',
					'\t-E:FILE       \n\t\tSets Enternal Operation-Key Handler',
					'\t-e            \n\t\tSets Execute Line To All Following Arguments']
				for Line in Usage:print(str(Line))
				sys.exit(1)

			elif str(Argument) in ['-e','--execute']:
				# Reads All Following Inputs
				Read_To_ExecLine = True;break
			elif str(':') in str(Argument):
				Arg_Tree = Argument.split(':')
				if str(Arg_Tree[0]) in ['-k0','--key-zero']:
					if len(Arg_Tree[1]) == 16:
						print('[!] Set Key-Zero To {}'.format(str(Arg_Tree[1])));Config['K0']=str(Arg_Tree[1])
					else:
						print('[!] Invalid Key Length For {} Expected 16 For {}'.format(str(Arg_Tree[1])),str(len(Arg_Tree[1])));sys.exit(1)
				elif str(Arg_Tree[0]) in ['-k1','--key-one']:
					if len(Arg_Tree[1]) == 16:
						print('[!] Set Key-One To {}'.format(str(Arg_Tree[1])));Config['K1']=str(Arg_Tree[1])
					else:
						print('[!] Invalid Key Length For {} Expected 16 For {}'.format(str(Arg_Tree[1])),str(len(Arg_Tree[1])));sys.exit(1)
				elif str(Arg_Tree[0]) in ['-f','--exec-file']:
					if os.path.isfile(str(Arg_Tree[1])) == True:
						print('[!] Set Execute-File To {}'.format(str(Arg_Tree[1])));Config['ExecFile']=str(Arg_Tree[1])
					else:
						print('[!] Invalid File Sent {} Is Non-Existant'.format(str(Arg_Tree[1])));sys.exit(1)
				elif str(Arg_Tree[0]) in ['-aA','--ascii-art']:
					if os.path.isfile(str(Arg_Tree[1])) == True: Config['ASCII_ART'] = str(Arg_Tree[1])
					else: print('[!] Invalid File Sent {} Is Non-Existant'.format(str(Arg_Tree[1])));sys.exit(1)
				elif str(Arg_Tree[0]) in ['-E','--external']:
					if os.path.isdir(str(Arg_Tree[1])) == True: Config['External'] = str(Arg_Tree[1])
					else: print('[!] Invalid File Sent {} Is Non-Existant'.format(str(Arg_Tree[1])));sys.exit(1)

			Arg_Counter += 1
		if Read_To_ExecLine == True:
			Args_To_Exec = sys.argv[int(Arg_Counter)+2:]
			Args_String  = Args_To_Exec[0]
			for Arg in Args_To_Exec[1:]:Args_String+=' '+str(Arg)
			print('[!] Set Execute-Command To {}'.format(str(Args_String)));Config['ExecLine']=str(Args_String)
		A = Alien(str(Config['K0']),str(Config['K1']),Debug=Config['DB'],Logging=Config['LG'],ExecLine=Config['ExecLine'],ExecFile=Config['ExecFile'],ProjectDIR=Config['MountAllProjects'],ExternalOpKey=Config['External'])
		if Config['NoMount_BI'] == False: A.Mount_Builtin()
		A.Heart()
