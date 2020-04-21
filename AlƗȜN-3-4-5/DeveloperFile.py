import Al13N345
import UFO
import random
################################################################################
Banner = '''                                   *     .....
               *                |  *  .              ......
                     *          .     |             .......
                          *        - -+- -     *    .....
         .                      .     |   *        .. ...
         .                      ;     .           ..  ....
         :                  - --+- -             ..     ...
         !           .          !         .     ....    ....
         |        .         *   .         |    ......   ....
        _|_         +             *    - -+- -  ....   ....
      ,` | `.                  .          |      .... ....
--- --+-<#>-+- ---  --  -      |    *     .     ........
      `._|_,'               - -+- -   .        ......
         T                   . |.     |        .....
         |                  .    . - -+- -      ....
         !                .  . .      |     *    ...
         :         . :  .             .  *        ...
         .       *                                ...
---------------------------------------------------------------------|
 █████╗ ██╗     ██╗██████╗ ███╗   ██╗    ██████╗ ██╗  ██╗   ███████╗ |
██╔══██╗██║    ███║╚════██╗████╗  ██║    ╚════██╗██║  ██║   ██╔════╝ |
███████║██║    ╚██║ █████╔╝██╔██╗ ██║     █████╔╝███████║   ███████╗ |
██╔══██║██║     ██║ ╚═══██╗██║╚██╗██║     ╚═══██╗╚════██║   ╚════██║ |
██║  ██║███████╗██║██████╔╝██║ ╚████║    ██████╔╝██╗  ██║██╗███████║ |
╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝ |
---------------------------------------------------------------------|
'''
DisplayHandle = UFO.Display()
NewBanner     = ''
for I in Banner:
    if str(I) == str('█'):NewBanner += '@/fg@/sb'+str(I)
    elif str(I) in ['-','|',',']: NewBanner += '@/fw@/sn'+str(I)
    elif str(I) in ['*','.']:
        RandomColors = ['@/fy','@/fb','@/fr','@/fc','@/fm']
        RandomC      = RandomColors[random.randint(0,len(RandomColors)-1)]
        I = str(RandomC)+'@/sb'+str(I)
        NewBanner += str(I)
    else:
        if str(NewBanner) == ' ':NewBanner += str(I)
        else:NewBanner += '@/fy@/sb'+str(I)

#print(NewBanner)
DisplayHandle.Display(str(NewBanner))
print(DisplayHandle.RainbowString(1,'<!> Attempting To Mount Registry, If Success Will Display Locations....'))
###
Brain  = Al13N345.Brain(verbosity=False)
Brain.append(0x1,0x2,0xf,0x4,0x5)
# Attempting To Write A String Into Buffer '00'
Brain.write('401','00','0000000000000002.0000','Example String')
# Attempting To Write A String As Integer Into Buffer '01'
Brain.write('401','01','0000000000000002.0001','Example String')
# Attempting To Write A Function To Area
def Test(FunctionIN):
    print(str(FunctionIN))
Brain.write('401','02','0000000000000004.0000',[Test,{'FetchValues':['00','01']}])
Brain.execute('401',Target_Segment='02')
print(Brain.execute('401'))
# Send Message
def Display():
    Message = ''
    for Registry in Brain.Registry:
        Message += '!/BUILTIN.MESSAGE_HEAD @/fw@/sn>> '+str(Registry)
        for Segment in Brain.Registry[str(Registry)]:
            Message += '\n!/BUILTIN.MESSAGE_HEAD @/fw@/sn>> \t'+str(Segment)+' :: @/sb'+str(Brain.Registry[Registry][Segment])
    DisplayHandle.Display(Message)
#Display()
