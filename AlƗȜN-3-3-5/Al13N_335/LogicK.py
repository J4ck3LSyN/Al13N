import Al13N_335.Exceptions as Exceptions
import os, sys, time, random
### Version 3.3.5 Remastered
class RegeX:
    def __init__(self,CharacterCount=500,Displace=1,UseHex=False):
        self.Memory = {}
        if type(CharacterCount) is int and type(Displace) is int:
            for CharacterIndex in range(0,int(CharacterCount)):
                CharacterObject = chr(int(CharacterIndex))
                if Displace not in [0,1]:
                    CharacterIndex = int(CharacterIndex)**int(Displace)
                if UseHex == True:
                    CharacterIndex = hex(int(CharacterIndex))
                self.Memory[str(CharacterIndex)]=str(CharacterObject)
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.RegeX.__init__','V',str(CharacterCount)+'/'+str(Displace)+' Is Not int'))
    #########################################################################################################################################
    class Logic:
        def __init__(self):
            pass

        # Basic Logic #
        def IsEqual(self,Target,Variable):
            if Target == Variable:
                return True
            else:
                return False

        def IsNotEqual(self,Target,Variable):
            if Target != Variable:
                return True
            else:
                return False

        def IsIn(self,Target,Variable):
            if Target in Variable:
                return True
            else:
                return False

        def IsNotIn(self,Target,Variable):
            if Target not in Variable:
                return True
            else:
                return False
        # Seperation And Striping #
        def SplitToList(self,Target,Variable):
            if self.IsIn(Target,Variable) == True:
                return str(Target).split(str(Variable))
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.RegeX.Logic.SplitToList','V',str(Target)+','+str(Variable)+' No Entity Found'))

        def StripFrom(self,Target,Variable):
            if self.IsIn(Target,Variable) == True:
                return str(Target).strip(str(Variable))
            else:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.RegeX.Logic.SplitToList','V',str(Target)+','+str(Variable)+' No Entity Found'))

        # Identify #
        def FetchType(self,Variable):
            return type(Variable)

        def IsDigit(self,Variable):
            return str(Variable).isdigit()

        def Length(self,Variable):
            return len(Variable)

        def IsFile(self,Variable):
            if os.path.isfile(str(Variable)) == True:
                return True
            else:
                return False

        def IsPath(self,Variable):
            if os.path.isdir(str(Variable)) == True:
                return True
            else:
                return False
    #########################################################################################################################################
    #########################################################################################################################################
    def ConvertRooT(self,TargetString,Seperator):
        Output_String = ''
        TargetString  = str(TargetString) # Just In Case
        for Character in TargetString:
            for Index in self.Memory:
                if str(self.Memory[Index]) == str(Character):
                    Output_String += str(Index)+str(Seperator)
        return Output_String

    def ConvertRevR(self,TargetString,Seperator):
        Output_String = ''
        TargetString  = str(TargetString) # Just In Case
        Logic         = self.Logic()
        if Logic.IsIn(str(TargetString),str(Variable)) == True:
            Tree = Logic.SplitToList(str(TargetString),str(Variable))
            for Object in Tree:
                if Object in self.Memory:
                    Output_String += str(self.Memory[Object])
            return Output_String
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.RegeX.ConvertRevR','V',str(Output_String)+' Doe Not Contain '+str(Variable)))
################################################################################################################################################
'''
^ Al13N_335.LogicK.GenerateRandomDisplacer(int,int,Displace=int)
- int[0] must be lower than int[1], if Displace is 0,1 than no operation will be acted on,
- else: it will be displaced to a exponent.
> import Al13N_335
> Crypt= Al13N_335.LogicK.RegeX(Displace=int(Al13N_335.LogicK.GenerateRandomDisplacer(int,int)))
'''
def GenerateRandomDisplacer(Lower,Higher,Displace=1):
    if type(Lower) is int and type(Higher) is int and type(Displace) is int:
        if int(Lower) < int(Higher):
            RandomDisplace = random.randint(int(Lower),int(Higher))
            if Displace not in [0,1]:
                RandomDisplace = int(RandomDisplace)**int(Displace)
            return RandomDisplace
        else:
            raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.GenerateRandomDisplacer','V',str(Lower)+' Is Not Less Than '+str(Higher)))
    else:
        raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.GenerateRandomDisplacer','T',str(type(Lower))+'/'+str(type(Higher))+'/'+str(type(Displace))+' Expected All int'))

################################################################################################################################################
'''
^ Al13N_335.LogicK.RegeX_Memory_Complex(Complexs=[[]])
- Every Item Inside Of Complexes Is Given 2-3 Values
- [0] int  Being The CharacterCoung
- [1] int  Being The Displacement
- [2] bool Being The Hex Boolean
- Used Purely For Saving Multiple Operations
- Each Item Is Appended Based Off The Time Of Generation
- 1 - [0], 2 - [1], 3 - [2]....
> import Al13N_335
> Crypt= Al13N_335.LogicK.RegeX_Memory_Complex(Complex=[[500,1],[500,5,True]])
> Obj_1= RegeX(CharacterCount=500,Displace=1)             | Crypt.ComplexMemory[0]
> Obj_2= RegeX(CharacterCount=500,Displace=1,UseHex=True) | Crypt.ComplexMemory[1]
'''
class RegeX_Memory_Complex:
    def __init__(self,Complex=[]):
        self.ComplexMemory = []
        if len(Complex) > 0:
            Failed = False
            Reason = None
            for Item in Complex:
                if type(Item) is list:
                    if len(Item) == 2:
                        if type(Item[0]) is int and type(Item[1]) is int:
                            self.ComplexMemory.append(RegeX(CharacterCount=Item[0],Displace=Item[1]))
                        else:
                            Failed = True
                            Reason = str(type(Item[0]))+'/'+str(type(Item[1]))+' Expected int'
                            break
                    elif len(Item) == 3:
                        if type(Item[0]) is int and type(Item[1]) is int and type(Item[2]) is bool:
                            self.ComplexMemory.append(RegeX(CharacterCount=Item[0],Displace=Item[1],UseHex=Item[2]))
                        else:
                            Failed = True
                            Reason = str(type(Item[9]))+'/'+str(type(Item[1]))+'/'+str(type(Item[2]))+' Expected int,int,bool'
                            break
                    else:
                        Failed = True
                        Reason = str(len(Item))+'/'+str(Item)+' Expected 2 Or 3 Entities'
                        break
                else:
                    Failed = True
                    Reason = str(type(Item))+'/'+str(Item)+' Expected A list'
                    break
            if Failed == True:
                raise Exception(Exceptions.RaiseToUser('Al13N_335.LogicK.RegeX_Memory_Complex.__init__','E',str(Reason)))
################################################################################################################################################
