'''
Alien External Pythonic File
-----------------------------
* Used Not Only For Examples Of External Project Operations
* But Also For External Pythonic Operation Keys For Alien From J4ck3LSyN
'''
import os,time,subprocess

class SYSTEM:
    def CWD(IN): return str(os.getcwd())
    def TIME(IN): return str(time.asctime())
    def GUID(IN): return str(os.getuid())
    def SPPIPE(IN):
        Command = ''
        for String in IN:
            if len(Command) == 0:Command=str(String)
            else: Command+=' {}'.format(str(String))
        return str( subprocess.Popen([Command],stdout=subprocess.PIPE).stdout.read().decode('utf-8') )

__OPKEY__ = [
    ['sys.cwd', 'Pulls Current Working Directory (NOTE:Carries Some Errors On NoArg Input)','*',SYSTEM.CWD],
    ['sys.time','Pulls Current Time In ASCII (NOTE:Carries Some Errors On NoArg Input)','*',SYSTEM.TIME],
    ['sys.guid','Pulls Current UID','*',SYSTEM.GUID],
    ['sys.pipe','Pipes Input As String Into A Shell Command And Fetches The Output','*',SYSTEM.SPPIPE]
]
