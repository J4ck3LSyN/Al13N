# Module For Memory Handling (Al13N3450)
################################################################################
import random,hashlib
################################################################################
class KeyGeneration:
    def Al13N3475_KEY( LowOpen,LowPost,Seed,HighOpen,HighPost ):
        if [type(LowOpen),type(LowPost),type(Seed),type(HighOpen),type(HighPost)] == [int,int,int,int,int]:
            if LowOpen  == 0: LowOpen  = random.randint(999,9999);
            if LowPost  == 0: LowPost  = random.randint(9999,99999999)
            if Seed     == 0: Seed     = random.randint(99999999,9999999999999999)
            if HighOpen == 0: HighOpen = random.randint(9999,99999999)
            if HighPost == 0: HighPost = random.randint(9999999999999999,999999999999999999999999)
            KEY = int( int(LowOpen) ** int(LowPost) // int(Seed) ) * int( int(HighOpen) ** int(HighPost) ) // int(Seed)
            if len(str(KEY)) == 0: KEY = KeyGeneration.Al13N3475_KEY(0,99,Seed,0,999)
            return str(hex(KEY)).strip('0x')
        else: raise KeyGeneration.KeyGenerationException('Al13N3475_KEY','Expected Ints')
    def Al13N350_KEY( LowOpen, LowMid, LowPost, SeedA, SeedB, HighOpen, HighMid, HighPost ):
        if [type(LowOpen),type(LowMid),type(LowPost),type(SeedA),type(SeedB),type(HighOpen),type(HighMid),type(HighPost)] == [int,int,int,int,int,int,int,int]:
            if LowOpen  == 0: LowOpen  = random.randint(999,9999)
            if LowMid   == 0: LowMid   = random.randint(9999,99999)
            if LowPost  == 0: LowPost  = random.randint(9999,99999999)
            if SeedA    == 0: SeedA    = random.randint(99999999,9999999999999999)
            if SeedB    == 0: SeedB    = random.randint(99999999,9999999999999999)
            if HighOpen == 0: HighOpen = random.randint(9999,99999999)
            if HighMid  == 0: HighMid  = random.randint(99999,9999999999)
            if HighPost == 0: HighPost = random.randint(9999999999999999,999999999999999999999999)
            KEY = int( int(LowOpen)  * int(LowMid)  ** int(LowPost)  ) * int( SeedA * SeedB ** int(LowOpen * HighOpen) )
            # (X * X ** X)//(X*XX//(X*X))
            KEY = int(KEY) ^ int( int(HighOpen) * int(HighMid) ** int(HighPost) ) * int( SeedA ^ int( SeedB ^ int(LowMid  * HighMid )) )
            # (K)^(X*X**X)//(X^(X^(X*X)))
            if len(str(KEY)) == 0: KEY = KeyGeneration.Al13N350_KEY(0,666,9,666,999,0,666,9)
            return str(hex(KEY)).strip('0x')
    def ConvertToHash(HashType,StringToHash):
        if str(HashType) in hashlib.algorithms_available or str(HashType) in hashlib.algorithms_guaranteed:
            Hashed = hashlib.new(str(HashType))
            Hashed.update(bytes(str(StringToHash),'utf-16'))
            return [Hashed,Hashed.hexdigest(),Hashed.digest()]
        else: raise KeyGeneration.KeyGenerationException('ConvertToHash(...)','Expected Valid HashType')
    def Operate(Input):
        return str(KeyGeneration.ConvertToHash(Input[0],Input[1])[1])
    def KeyGenerationException(Root,Mesg): raise Exception('KeyGeneration.'+str(Root)+' -> '+str(Mesg))

class Registry:
    def __init__(self,AuthorKey,COF):
        if len(AuthorKey) != 8 or len(COF) != 8: raise self.RegistryException('__init__(...)','Expected 8 Values For Keys')
        self.KEY = KeyGeneration.Al13N350_KEY(AuthorKey[0],AuthorKey[1],AuthorKey[2],AuthorKey[3],AuthorKey[4],AuthorKey[5],AuthorKey[6],AuthorKey[7])
        self.COF = KeyGeneration.Al13N350_KEY(COF[0],COF[1],COF[2],COF[3],COF[4],COF[5],COF[6],COF[7])
        self.REG = {}
        self.OKY = {}
        self.SEC = ''
    def UpdateSEC(self): self.SEC = str(KeyGeneration.ConvertToHash('whirlpool',str(self.REG)+str(self.OKY)+str(self.KEY)+str(self.COF))[1])
    def MountOpKey(self,OpKey,Function,Inputs):
        if str(type(Function)) in ["<class 'function'>","<class 'class'>","<class 'builtin_function_or_method'>","<class 'method'>"]: self.OKY[str(OpKey)]=(Function,Inputs)
        else: raise self.RegistryException('MountOpKey(...)','Invalid Function Sent...')
    def new(self, ID, Length ):
        if str(ID) not in self.REG and type(Length) is int:
            if Length == 0: Length  = 0xffffffff
            self.REG[str(ID)] = {}
            for Segment in range(1,int(Length)):
                HEXID = str(hex(Segment)).strip('0x')
                if len(HEXID) == 1: HEXID = '000'+str(HEXID)
                if len(HEXID) == 2: HEXID = '00' +str(HEXID)
                if len(HEXID) == 3: HEXID = '0'  +str(HEXID)
                self.REG[str(ID)][str(HEXID)]=()
            self.UpdateSEC()
            return str(ID)
        else: raise self.RegistryException('new(...)','Expected A Non-Existant ID Or A Integer')
    def write(self,OpKey,Register,Segment,Input):
        if type(Input) is list or type(Input) is tuple and str(Opkey) in self.OKY:
            if str(Register) in self.REG:
                if str(Segment) in self.REG[Register]:
                    if len(Input) in self.OKY[OpKey][1]: self.REG[Register][Segment]=(str(OpKey),Input)
                    else: raise self.RegistryException('write('+str(Input)+')','Expected Matching Values For OpKey '+str(self.OKY[OpKey][1]))
                else: raise self.RegistryException('write('+str(Segment)+')','Expected A Valid Segment For {}'.format(str(Register)))
            else: raise self.RegistryException('write('+str(Register)+')','Expected A Valid Register')
        else: raise self.RegistryException('write({},{},{})'.format(str(OpKey),str(Input)),'Expected A Valid OpKey Or A tuple/list')
    # Execution
    def execute(self,Register,Segment):
        if Register in self.REG:
            if Segment in self.REG[Register]:
                # Pull Value And Test Length
                Functions = self.REG[Register][Segment]
                if len(Functions) == 0: return None
                else:
                    # Pull OpKey
                    if Functions[0] in self.OKY:
                        OperationKey = self.OKY[Functions[0]]
                        if len(Functions[1]) in OperationKey[1]:
                            # Mount Function From OpKey
                            Exec = OperationKey[0]
                            # Execute And Recieve Output
                            if OperationKey[1][0] == 0: Out = Exec()
                            else:
                                CINDEX = 0
                                for EXECV in Functions[1]:
                                    if type(EXECV) is str:
                                        if len(EXECV) == 0: continue
                                        if str(EXECV[0]) == '~':
                                            if str(EXECV[1:]) in self.REG[Register]: Functions[1][CINDEX]=self.execute(Register,str(EXECV[1:]))
                                    CINDEX += 1
                                Out  = Exec(Functions[1])
                            # Return Output
                            return Out
            else: raise self.RegistryException('execute('+str(Segment)+')','Expected Valid Segment ID {}'.format(str(Segment)))
        else: raise self.RegistryException('execute('+str(Register)+')','Expected Valid Register ID {}'.format(str(Register)))
    def RegistryException(self,Root,Mesg): raise Exception('Registry.'+str(Root)+' -> '+str(Mesg))
