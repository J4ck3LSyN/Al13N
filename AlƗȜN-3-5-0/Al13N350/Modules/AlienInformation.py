import os,sys,time,subprocess
# Current Working Directory
def CWD(): return str(os.getcwd())
# Current Time ASCII
def TIME(): return str(time.asctime())
# Current Interface Status
def IFACE():
    interface = subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE)
    interface = bytes.decode(interface.stdout.read(),'utf-8').split('\n')
    out       = []
    for line in interface:
        if len(line) == 0: continue
        else:
            if str(line[0]) != str(' '):
                out.append(line.split(':')[0])
    return out
# Read File As String
def READFILE(FILE):
    if os.path.isfile(str(FILE)) == True: return str(open(FILE).read())
    else: raise Exception('Invalid File Sent: '+str(FILE))
# Write File
def WRITEFILE(FILE,INPUT):
    if os.path.isfile(str(FILE)) == False:
        F = open(str(FILE),'w')
        F.write(str(INPUT))
        F.close()
    else: raise Exception('Cannot Operate On Existant File')

# Operations
def Operate(ARGS):
    if type(ARGS) is list or type(ARGS) is tuple:
        if ARGS[0] in ['c','C','cwd','Cwd','CWD']      : return CWD()
        if ARGS[0] in ['t','T','time','Time','TIME']   : return TIME()
        if ARGS[0] in ['i','I','iface','Iface','IFACE']: return IFACE()
        if ARGS[0] in ['r','R','read','Read','READ'] and len(ARGS[1:]) == 1: return str(READFILE(ARGS[1]))
        if ARGS[0] in ['w','W','write','Write','WRITE'] and len(ARGS[1:]) >= 2:
            FILENAME = ARGS[1]
            FILETEXT = ARGS[2:]
            WRITEFILE(str(FILENAME),str(FILETEXT))
            return None
