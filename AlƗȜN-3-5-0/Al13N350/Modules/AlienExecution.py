import os,sys,time,subprocess,threading
import base64,random

def Shell(CommandString):
    if type(CommandString) is str:
        if str(' ') in str(CommandString):CommandString = CommandString.split(' ')
        else: CommandString = [str(CommandString)]
        Output      = subprocess.Popen(CommandString,stdout=subprocess.PIPE)
        Output_Text = bytes.decode(Output.stdout.read(),'utf-8')
        return str(Output_Text)
    else: raise AlienExecutionException('Shell(...)','Expected A String')



def Operate(Operand):
    if type(Operand) is list or type(Operand) is tuple:
        if len(Operand) >= 2:
            Trigger  = Operand[0]
            ExecuteT = Operand[1:]
            Execute  = ''
            for C in ExecuteT:
                if len(Execute) == 0: Execute=str(C)
                else: Execute+=str(' ')+str(C)
            if Trigger in [0,'s','S','shell','Shell','SHELL']:
                return str(Shell(Execute))
            else: raise AlienExecutionException('Operate(...)','Invalid Operand Sent')
        else: raise AlienExecutionException('Operate(...)','Expected At Least 2 Values')
    else: raise AlienExecutionException('Opeation(type)','Expected A list With 2> Values')

def AlienExecutionException(Root,Mesg): raise Exception('AlienExecution.'+str(Root)+' -> '+str(Mesg))
