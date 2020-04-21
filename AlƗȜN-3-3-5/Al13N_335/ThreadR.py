# For Threading Things
import Al13N_335.RegeX        as RegeX
import Al13N_335.Exceptions   as Exceptions
import threading              as ThrdH

class ThreadR:
    def __init__(self):
        self.Memory = {}
        self.Count  = 0
    #########################################################################################################################################
    def SpawnThread(self,Target,Args):
        ObjectID    = self.Count
        try:
            ThreadObject = ThrdH.Thread(target=Target,args=Args)
            self.Memory[str(ObjectID)] = ThreadObject
            self.Count += 1
        except Exception as e:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.ThreadR.ThreadR.SpawnThread','E',str(e)+str(' From Operation: SpawnThread('+str(Target)+','+str(Args)+')')))
    #########################################################################################################################################
    def Status(self,ID):
        if str(ID) in self.Memory:
            return self.Memory[str(ID)].isAlive()
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.ThreadR.ThreadR.Status','V',str(ID)+' Is Non-Existant'))
    #########################################################################################################################################
    def RawName(self,ID):
        if str(ID) in self.Memory:
            return self.Memory[str(ID)].name
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.ThreadR.ThreadR.RawName','V',str(ID)+' Is Non-Existant'))
    #########################################################################################################################################
    def RunThread(self,ID):
        if str(ID) in self.Memory:
            self.Memory[str(ID)].run()
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.ThreadR.ThreadR.RunThread','V',str(ID)+' Is Non-Existant'))
    #########################################################################################################################################
    def JoinThread(self,ID,TimeOutInt):
        if str(ID) in self.Memory and type(TimeOutInt) is float:
            self.Memory[str(ID)].join(timeout=int(TimeOutInt))
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.ThreadR.ThreadR.JoinThread','V',str(ID)+' Is Non-Existant Or '+str(TimeOutInt)+' Is Not Float'))
            
