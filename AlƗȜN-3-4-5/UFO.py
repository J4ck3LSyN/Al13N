import Al13N345
import sys
import time
import random
import os
import readline
import subprocess
###
import colorama
from   colorama import Fore  as C_F
from   colorama import Back  as C_B
from   colorama import Style as C_S
colorama.init(autoreset=True)
###
class Display:
    def __init__(self):
        self.Message_Index = {
            'BUILTIN.MESSAGE_HEAD'  :'@/sb@/fg<@/fy?@/fg>@/fw Message: @/sn@/fw',
            'BUILTIN.EXCEPTION'     :'@/sb@/fr<!> Exception Caught @/br@/fw',
            'BUILTIN.HEADER_BRIGHT' :'''
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb;@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb:@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn-@/fy@/sb @/fw@/sn-@/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb!@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb!@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb_@/fw@/sn|@/fy@/sb_@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb+@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn,@/fy@/sb`@/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb`@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fy@/sb @/fw@/sn-@/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb<@/fy@/sb#@/fy@/sb>@/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fw@/sn-@/fw@/sn-@/fy@/sb @/fy@/sb @/fw@/sn-@/fw@/sn-@/fy@/sb @/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb`@/fc@/sb.@/fy@/sb_@/fw@/sn|@/fy@/sb_@/fw@/sn,@/fy@/sb'@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sbT@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fw@/sn|@/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb+@/fw@/sn-@/fy@/sb @/fw@/sn-@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb!@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fw@/sn|@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb:@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb:@/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb*@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fc@/sb.@/fc@/sb.@/fc@/sb.@/fy@/sb
@/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb
@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb
@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb╚@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb╝@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb╝@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb
@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb╚@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb
@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb╝@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb╚@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb╔@/fy@/sb╝@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fy@/sb @/fy@/sb @/fg@/sb█@/fg@/sb█@/fy@/sb║@/fg@/sb█@/fg@/sb█@/fy@/sb╗@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fg@/sb█@/fy@/sb║@/fy@/sb
@/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb @/fy@/sb @/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb╚@/fy@/sb═@/fy@/sb╝@/fy@/sb╚@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb═@/fy@/sb╝@/fy@/sb
@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fw@/sn-@/fy@/sb
'''
        }
        self.Color_Index   = {
            'fg':C_F.GREEN,   'bg':C_B.GREEN,
            'fb':C_F.BLUE,    'bb':C_B.BLUE,
            'fc':C_F.CYAN,    'bc':C_B.CYAN,
            'fm':C_F.MAGENTA, 'bm':C_B.MAGENTA,
            'fw':C_F.WHITE,   'bw':C_B.WHITE,
            'fr':C_F.RED,     'br':C_B.RED,
            'fy':C_F.YELLOW,  'by':C_B.YELLOW,
            'f0':C_F.RESET,   'b0':C_B.RESET,
            #################################
            'sb':C_S.BRIGHT,
            'sn':C_S.NORMAL,
            'sd':C_S.DIM,
            's0':C_S.RESET_ALL}
            ##################################
        self.HotKey = {'C':'@/','M':'!/'}
    def FindColor(self,Message):
        for Color in self.Color_Index:
            CID = str(self.HotKey['C'])+str(Color)
            if str(CID) in str(Message):Message = Message.replace(str(CID),self.Color_Index[Color])
        return Message
    def FindMessage(self,Message):
        for MesgI in self.Message_Index:
            MID = str(self.HotKey['M'])+str(MesgI)
            if str(MID) in str(Message):Message = Message.replace(str(MID),self.Message_Index[MesgI])
        return Message
    def RainbowString(self,Mode,Message):
        if Mode == 0:
            TempMessage = str(Message)
            Message     = ''
            for Character in str(TempMessage):
                Fore         = []
                Back         = []
                Style        = []
                for Color in self.Color_Index:
                    if str('f') in str(Color): Fore.append(Color)
                    if str('b') in str(Color): Back.append(Color)
                    if str('s') in str(Color) and str('0') not in Color: Style.append(Color)
                Fore_Rand    = Fore[random.randint(0,len(Fore)-1)]
                Back_Rand    = Back[random.randint(0,len(Back)-1)]
                Style_Rand   = Style[random.randint(0,len(Style)-1)]
                Message += str(self.Color_Index[Fore_Rand])+str(self.Color_Index[Back_Rand])+str(self.Color_Index[Style_Rand])+str(Character)
            return str(Message)
        elif Mode == 1:
            Fores   = []
            for Color in self.Color_Index:
                if str('f') in str(Color): Fores.append(self.Color_Index[Color])
            Output  = ''
            for Character in str(Message):
                RandomColor = random.randint(0,len(Fores)-1)
                Output     += str(Fores[RandomColor])+str(Character)
            return str(Output)
        elif Mode == 2:
            Backs   = []
            for Color in self.Color_Index:
                if str('b') in str(Color): Backs.append(str(self.Color_Index[Color]))
            Output  = ''
            for Character in str(Message):
                RandomColor = random.randint(0,len(Backs)-1)
                Output     += str(Backs[RandomColor])+str(Character)
            return str(Output)
        elif Mode == 3:
            Styles   = []
            for Style in self.Color_Index:
                if str('s') in str(Style): Styles.append(str(self.Color_Index[Style]))
            Output = ''
            for Character in str(Message):
                RandomStyle = random.randint(0,len(Styles)-1)
                Output     += str(Styles[RandomStyle])+str(Character)
            return str(Output)
    def Display(self,Message):
        Message = str(self.FindMessage(Message))
        Message = str(self.FindColor(Message))
        print(str(Message))
#################################################################################
class Al13N345_Interpreter:
    def __init__(self,**Handles):
        DBVerbose                 = False
        if str('DBVerbose') in Handles:
            if type(Handles['DBVerbose']) is bool: DBVerbose = Handles['DBVerbose']
        # Configure Brain With Verbose If DBVerbose Is Sent With A Boolean Configure
        self.Brain              = Al13N345.Brain(verbosity=DBVerbose)
        self.Home               = self.Brain.append(0x60,0x70,0xfff,0x70,0x60)
        # [0] Is Our Internal Handing ID And [1] Is Our Length For The Registry
        self.TextToDisplay      = Display()
        # Mount Display
        self.Running            = True
        # Current Status
        self.Configure          = {
            'Logs':[True,[]],
            # Logging
            'Que' :[],
            # Commands To Execute
            'CRID':'',
            'CRCF':True,
            # Current Register ID & Configure When Generating A Object
            'CSID':[],
            # Current Segment List For Register CRID
            'TINX':0,
            'TINC':True,
            # Current Register Index Value For Handling & And Step When No Input Is Sent
            'KARG':{},
            # Current Commands That Have Been Modulized
            # [0] Is Your Target Function
            # [1] Is You KeyArgs For UI
            # [2] Is You Input Length And Types [ 's/i/l/b/d/f',.... ] s(str),i(int),l(list),d(dict),b(bool),f(function/method/class/builtin_function_or_method)
            # Your Key Is Sperated Via '|' And The Inputs Are Caught Via Your Inputs Inside Of [2]
            'FAIL':[0,10],
            # Fail Information [0] Being The Current Count And [1] Being Our Max If We Hit [1]//[0] Display Help And If [0]>=[1] self.Kill()
            'FSFE':True,
            # If We Have Any Excpetions Dont Exit (If self.Configure['Fail'][0] Hits Max Than We Will self.Kill())
            'UAPP':{}
            # DisplayUsage Appending For Generating Messages Every Key Must Conatina '|' And The Value Must Be A List With String Values
         }
        # Trigger Loop0
        self.TextToDisplay.Display('!/BUILTIN.HEADER_BRIGHT')
        self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD @/sb@/fg'+str('-'*140))
        self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD @/sb@/fb'+str('Current Directory:@/fy\t')+str(os.getcwd()))
        self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD @/sb@/fb'+str('Current Time     :@/fy\t')+str(time.asctime()))
        self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD @/sb@/fg'+str('Current Home     :@/fw\t')+str(self.Home))
        self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD @/sb@/fr'+str('Log Status       :@/fw\t')+str(self.Configure['Logs'][0]))
        # Catch Pre Execution Commands
        if str('Execute') in Handles: self.HandleUI(str(Handles['Execute']))
        self.QueOps()
    # Loop0
    def QueOps(self):
        if self.Running == True:
            if len(self.Configure['Que']) == 0:
                # ^ Compile UserPrompt
                while self.Running == True:
                    try:
                        ### Fail Catch ###
                        if self.Configure['FAIL'][0] >= self.Configure['FAIL'][1]:
                            self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD!/BUILTIN.EXCEPTION@/fw@/b0 Exceeded Fail Threshold...{} >= {}'.format(str(self.Configure['FAIL'][0]),str(self.Configure['FAIL'][1])))
                            self.Kill()
                        if self.Configure['FAIL'][0 ] == int(self.Configure['FAIL'][1]//2):
                            self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD!/BUILTIN.EXCEPTION@/fw@/b0 Fail Threshold Hit On A Floor Division ||  {} // 2 == {}'.format(str(self.Configure['FAIL'][1]),str(self.Configure['FAIL'][0])))
                            self.TextToDisplay.Display('!/BUILTIN.MESSAGE_HEAD!/BUILTIN.EXCEPTION@/fw@/b0 Raising Help Information.....')
                            self.DisplayUsage()
                        ##################
                        UserPrompt = str(self.Prompt())
                        UserInput = input(str(UserPrompt))
                        ExitStatus = self.HandleUI(str(UserInput))
                        if ExitStatus == 'EXIT': self.Kill()
                        if ExitStatus == 'REST': self.Kill(Restart=True)
                    # Exception And Fail Catch
                    except KeyboardInterrupt:
                        self.TextToDisplay.Display('!/BUILTIN.EXCEPTION@/fw (@/fgKeyboardInterrupt@/fw)')
                        self.Configure['FAIL'][0] = self.Configure['FAIL'][0]+1
                        if self.Configure['FSFE'] == False:
                            self.TextToDisplay.Display('!/BUILTIN.EXCEPTION@/fr@/b0 Exiting Terminal... Flag{FSFE} Is False')
                            self.Kill()
                    except Exception as E:
                        self.TextToDisplay.Display('!/BUILTIN.EXCEPTION@/fw (@/fg'+str(E)+'@/fw)')
                        self.Configure['FAIL'][0] = self.Configure['FAIL'][0]+1
                        if self.Configure['FSFE'] == False:
                            self.TextToDisplay.Display('!/BUILTIN.EXCEPTION@/fr@/b0 Exiting Terminal... Flag{FSFE} Is False')
                            self.Kill()
            else:
                Failed = [False]
                for Command in self.Configure['Que']:
                    ExitStatus = self.UserInput(str(Command))
                    if ExitStatus == 'EXIT':
                        Failed = [True,Command,'EXIT']
                        break
                self.Configure['Que'] = []
                if Failed[0] == False: self.QueOps()
                else: raise self.Al13N345_InterpreterException('QueOps(...)','Failed Operations: '+str(Failed))
    # GeneratePrompt
    def Prompt(self):
        UserPrompt = str('> Al13N 3.4.5 ('+str(self.Configure['CRID'])+')')
        if len(self.Configure['CSID']) == 0: UserPrompt += str(' ()')
        else: UserPrompt += ' ('+str(self.Configure['CSID'][int(self.Configure['TINX'])])+')'
        UserPrompt += ' :> '
        return str(UserPrompt)
    # HandleUI
    def HandleUI(self,Command,**ExtendedHandle):
        if str(';') in str(Command):Command = Command.split(';')
        else: Command = [str(Command)]
        for CMD in Command:
            if len(CMD) == 0 and self.Configure['CRID'] != '' and self.Configure['TINC'] == True:
                Inc = self.Configure['TINX']+1
                if int(Inc) <= int(len(self.Configure['CSID'])-1): self.Configure['TINX'] = Inc
                else: raise self.Al13N345_InterpreterException('HandleUI(...)','Got No Value Inside Of Registry However We Cannot Escape Range...')
            if len(CMD) == 0 and self.Configure['CRID'] == '':
                self.TextToDisplay.Display('!/BUILTIN.EXCEPTION@/fw Expected A Input...')
                self.Configure['FAIL'][0] = self.Configure['FAIL'][0]+1
                # ^ Does Not Exit Since It Is Not A Major Invalid Input
            # Internal Interpreter Functions { Level 0
            if str(CMD) in ['exit','Exit','EXIT','quit','Quit','QUIT','q','Q']: self.Kill()
            if str(CMD) in ['help','Help','HELP']                     : self.DisplayUsage()
            # } Internal Interpreter Fucntons { Level 1 (' ')
            if str(' ') in str(CMD):
                CT        = CMD.split(' ')
                if str(CT[0]) in ['help','Help','HELP']: self.DisplayUsage(Command=str(CT[1]))
                if str(CT[0]) in ['rid','RID','RegisterID'] and CT[1] in self.Brain.Registry:
                    self.Configure['CRID'] = str(CT[1])
                    Segments = []
                    for Name in self.Brain.Registry[CT[1]]: Segments.append(str(Name))
                    self.Configure['CSID'] = Segments
                if str(CT[0]) in ['sid','SID','SegmentID'] and self.Configure['CRID'] != str('') and CT[1] in self.Configure['CSID']: self.Configure['TINX'] = self.Configure['CSID'].index(CT[1])
                # Target Register And Segment For Input
                # Takes Command As CRID@CSID Command (For Handling On Area Use '->' Instead Of ';' For Handling Internal Stepped Commands)
                if str('@') in str(CT[0]) and len(CT[1:]) != 0:
                    if str(CT[0]).split('@')[0] in self.Brain.Registry:
                        if str(CT[0].split('@')[1]) in self.Brain.Registry[CT[0].split('@')[0]]:
                            ReturnHome  = [self.Configure['CRID'],self.Configure['CSID'],self.Configure['TINX']]
                            self.HandleUI('rid '+str(CT[0]).split('@')[0]+';sid '+str(CT[0].split('@')[1]))
                            HandeAction   = CT[1:]
                            CompileAction = ''
                            print(ReturnHome)
                            for Operand in HandeAction:
                                if len(CompileAction) == 0: CompileAction = str(Operand)
                                else: CompileAction += ' '+str(Operand)
                            if str('->') in str(CompileAction): CompileAction = CompileAction.replace('->',';')
                            self.HandleUI(str(CompileAction))
                            if ReturnHome[0] != 0 and len(ReturnHome[1]) != 0: self.HandleUI('rid '+str(ReturnHome[0])+';sid '+str(ReturnHome[1][ReturnHome[2]]))
                            else:
                                self.Configure['CRID'] = ''
                                self.Configure['CSID'] = []
                                self.Configure['TINX'] = 0
                # Generate Register Catch
                if str(CT[0][0]) == str('+') and len(CT[1:]) == 5:
                    InValidateInformaton = [False]
                    for Value in CT[1:]:
                        for Char in str(Value):
                            if str(Char) not in 'abcdef0123456789': InValidateInformaton = [True,Char]
                    if InValidateInformaton[0] == False:
                        Values                  = []
                        for Conversion in CT[1:]: Values.append(int(str('0x'+Conversion),16))
                        Info = self.Brain.append(Values[0],Values[1],Values[2],Values[3],Values[4])
                        if self.Configure['CRCF'] == True: self.HandleUI('rid '+str(Info[0])+';sid 00')
                # Write Signature Values Into Segments If We Have A Register And Segment Set
                if str(CT[0][0]) == str('>') and self.Configure['CRID'] != str('') and len(CT[1:]) > 1:
                    Signature = CT[1]
                    Values    = CT[2:]
                    if len(Values) == 1: Values = Values[0]
                    OutputValue = self.Brain.write(str(self.Configure['CRID']),str(self.Configure['CSID'][self.Configure['TINX']]),str(Signature),Values)
            # }
            # Keyword Arg {
            TargetArg = ''
            for Arg in self.Configure['KARG']:
                if str(Command) == str(Arg) or str(Command) in str(Arg).split('|'): TargetArg = str(Arg)
            if len(TargetArg) != 0:
                Object = self.Configure['KARG'][str(TargetArg)]
                ### BUILD!!
            # }
    # Kill
    def Kill(self,Restart=False):
        if Restart == False:
            self.Running = False
        else:
            self.Running = False
            self.Running = True
            self.QueOps()
    # DisplayUsage
    def DisplayUsage(self,Command=None):
        Message = {
            'exit|Exit|EXIT|quit|Quit|QUIT|q|Q':['Exits This UFO Terminal...'],
            'help|Help|HELP'                   :['Displays This Help Message',
                                                 'Can Also Take 1 Args As A ',
                                                 'Command For Targeted Info..'],
            'rid|RID|RegisterID'               :['Configures Scope To Register ID',
                                                 'rid <RID>'],
            'sid|SID|SegmentID'                :['rid Must Be Configured',
                                                 'Configures Scope Inside Of RID',
                                                 'sid <SID>'],
            'rid@sid|@|r@s'                    :['Configures Scope To A Targeted',
                                                 'Register Or Segment Outside Of',
                                                 'Current Register'],
            '+|generate_register'              :['Use "+" Takes 5 Following Args',
                                                 'Each Args Is A Hex Value Sent',
                                                 'Without "0x" IE: @/fr03@/fw == @/fg0x03@/fw',
                                                 'This Is Sent 5 Time In A Argument',
                                                 'IE:@/fg"+ @/fyXX XX@/fm XX@/fc XX XX',
                                                 '@/fyYellow(Opening Generation Key)',
                                                 '@/fmMegenta(Registery Count)',
                                                 '@/fcCyan(Ending Key)',
                                                 '[@/fw@/brNOTE@/b0@/fw] Check Al13N345.py For',
                                                 '       Information Regarding Registry Key Generation...',
                                                 '[@/fb@/brNOTE@/b0@/fw] @/frDO@/fb NOT@/fr GENERATE@/fy EXTENSIVE@/fw KEYS']}
        # Append self.Configure['UAPP']
        if len(self.Configure['UAPP']) != 0:
            for MessageHead in self.Configure['UAPP']:
                if str(MessageHead) not in Message and str('|') in str(MessageHead): Message[str(MessageHead)] = self.Configure['UAPP'][str(MessageHead)]
        # Check For Command Arg If Is Default(None) Than Send Every Arg
        if Command == None:
            for Mesg in Message: self.DisplayUsage(Command=str(Mesg))
        else:
            Target = ''
            for MESG in Message:
                if str(Command) == str(MESG) or str(Command) in str(MESG).split('|'): Target = str(MESG)
            if len(Target) != 0:
                Output = '!/BUILTIN.MESSAGE_HEAD@/sb'+str(Target).replace('|',', ')+str('\t{')
                for Line in Message[Target]: Output += str('\n!/BUILTIN.MESSAGE_HEAD @/sb@/fw\t|@/fg')+str(Line)
                Output += str('\n!/BUILTIN.MESSAGE_HEAD @/sb@/fw}')
                self.TextToDisplay.Display(str(Output))
    # SysExit
    def SysExit(self): sys.exit(1)
    # Exceptions
    def Al13N345_InterpreterException(self,Root,Mesg):
        Mesg = 'Al13N345(UFO) (Al13N345_Interpreter.'+str(Root)+')'+' | '+str(Mesg)
        raise Exception(Mesg)
if __name__ == '__main__':
    if len(sys.argv[1:]) == 0: Al13N345_Interpreter(DBVerbose=True)
