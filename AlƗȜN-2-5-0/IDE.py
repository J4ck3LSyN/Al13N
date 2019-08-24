import os,sys,time,threading,subprocess
#######################################
import Al13N
import colorama
from   colorama import Fore   as F
from   colorama import Back   as B
from   colorama import Style  as S
colorama.init(autoreset=True)
#######################################
Al13NImport = False
Al13NReason = None
try:
    import Al13N
    Al13NImport = True
except Exception as e:
    Al13NReason = str(e)
finally:
    if Al13NImport == False:
        raise Exception(str(e)+' On Al13N Importation Check File Or Existance')
        exit(1)
    else:
        pass
#######################################
Color_Index = { # For Colorizing Messages By Code
    'F.W':F.WHITE,
    'B.W':B.WHITE,
    # White
    'F.R':F.RED,
    'B.R':B.RED,
    # Red
    'F.G':F.GREEN,
    'B.G':B.GREEN,
    # GREEN
    'F.M':F.MAGENTA,
    'B.M':F.MAGENTA,
    # Magenta
    'F.C':F.CYAN,
    'B.C':B.CYAN,
    # Cyan
    'F.B':F.BLUE,
    'B.B':B.BLUE,
    # Blue
    'F.Z':F.BLACK,
    'B.Z':B.BLACK,
    # Black
    'F.X':F.RESET,
    'B.X':B.RESET,
    # Brightness
    'S.B':S.BRIGHT,
    'S.N':S.NORMAL,
    'S.D':S.DIM,
    # RESET ALL
    'S.X':S.RESET_ALL
}
#####################################
def Colorize(String):
    global Color_Index
    for Color in Color_Index:
        CKey = str('{'+str(Color)+'}')
        if str(CKey) in str(String):
            String = String.replace(str(CKey),Color_Index[str(Color)])
        else:
            pass
    return String
######################################
def Display_Out(String):
    print(str(String))
######################################
def Display_In(String):
    return str(input(String))
######################################
Running = False
Root    = Al13N.Root()
UEntry  = '{F.G}{S.B}[{F.W}'+str(os.getcwd())+'{F.G}]{F.R}--> {S.N}{F.W}'
