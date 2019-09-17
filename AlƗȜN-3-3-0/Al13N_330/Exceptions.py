FailSafe = False
def RaiseToUser(RootFunction,Type,Message):
    Message = str(RootFunction)+str(' >> ')+str(Message)
    if FailSafe == True:
        return Message
    if   str(Type) in ['I','ImportError','importerror','IMPORTERROR']:
        raise ImportError(str(Message))
    elif str(Type) in ['V','ValueError','valueerror','VALUEERROR']:
        raise ValueError(str(Message))
    elif str(Type) in ['K','KeyError','keyerror','KEYERROR']:
        raise KeyError(str(Message))
    elif str(Type) in ['N','NameError','nameerror','NAMEERROR']:
        raise NameError(str(Message))
    elif str(Type) in ['T','TypeError','typerror','TYPERROR']:
        raise TypeError(str(Message))
    elif str(Type) in ['E','Exception','exception','EXCEPTION']:
        raise Exception(str(Message))
    else:
        Message += str(' (Invalid Type sent ')+str(Type)+str(')')
        raise Exception(str(Message))
