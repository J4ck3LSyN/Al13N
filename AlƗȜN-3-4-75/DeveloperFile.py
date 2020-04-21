import Al13N3475 as Al13N
Brain   =Al13N.Al13N3475((0x6664,0x6,0xaf13d375,0x9999,0x9),(0x666,0x6,0xa13f573,0x999,0x9))
Display =Brain.Display()
Banner = '''
 .              +   .                .   . .     .  .    |       ~Author~
                   .                    .       .     *  |      J4ck3LSyN
  .       *                        . . . .  .   .  + .   |      ~Version~
            "You Are Here"            .   .  +  . . .    |         3.4.75
.                 |             .  .   .    .    . .     |---------------
                  |           .     .     . +.    +  .   | >> Kill All
                 \|/            .       .   . .          | >> Salute
        . .       V          .    * . . .  .  +   .      | -- No One
           +      .           .   .      +          . .  | >> Never
                            .       . +  .+. .      ...  | -- Forgive
  .                      .     . + .  . .     .      ..  | >> Never
           .      .    .     . .   . . .        ! /   +  | -- Forget
      *             .    . .  +    .  .       - O -      | >> We Are
          .     .    .  +   . .  *  .       . / |        |----Legion-----
               . + .  .  .  .. +  .                        .  . , *
.      .  .  .  *   .  *  . +..  .            *          .. ..         -
 .      .   . .   .   .   . .  +   .    .            +       .   *
-------------------------------------------------------------------------
█████╗ ██╗     ██╗██████╗ ███╗   ██╗    ██████╗ ██╗  ██╗███████╗███████╗
██╔══██╗██║    ███║╚════██╗████╗  ██║    ╚════██╗██║  ██║╚════██║██╔════╝
███████║██║    ╚██║ █████╔╝██╔██╗ ██║     █████╔╝███████║    ██╔╝███████╗
██╔══██║██║     ██║ ╚═══██╗██║╚██╗██║     ╚═══██╗╚════██║   ██╔╝ ╚════██║
██║  ██║███████╗██║██████╔╝██║ ╚████║    ██████╔╝██╗  ██║██╗██║  ███████║
╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚══════╝
-------------------------------------------------------------------------
                             (Developer File)
'''
NewBanner     = ''
for Character in str(Banner):
    if str(Character) in ['█']: Character = str('@/sb@/fg')+str(Character)
    #if str(Character) in [' ']: Character = str('@/sn@/bc')+str(Character)+str('@/b0')
    if str(Character) in ['-']: Character = str('@/sb@/fr')+str(Character)
    if str(Character) in ['|']: Character = str('@/sb@/fg')+str(Character)
    if str(Character) in ['.']: Character = str('@/sb@/fm')+str(Character)
    if str(Character) in ['+','*']: Character = str('@/sn@/fc')+str(Character)
    if str(Character) in ['/','0']: Character = str('@/sb@/fy')+str(Character)
    if str(Character) in ['3','4','7','5']: Character = str('@/fb')+str(Character)
    if str(Character) in ['~']: Character = str('@/fw')+str(Character)
    else: Character = str('@/fy@/sd')+str(Character)
    NewBanner+=str(Character)
print(NewBanner)
Display.Display(str(NewBanner))
def DisplayHandle(IN):
    return IN
print(str(Brain.OpKeys))
ID = Brain.new((0x3,0x4,0x5,0x6,0x7),0xff)
Brain.write(ID,'0000','(Al13N(3.4.75)',('s',0,'v','test',''))
Brain.write(ID,'0001','(Al13N(3.4.75)',('s',0,'+','@0000','!!!'))
TestOut = Brain.execute(ID,'0001')
print(str(TestOut))
#print(str(Brain.KEY))
#print(str(Brain.COF))
print(str(Brain.Registry))
'''
DO NOT DELETE 
'''
