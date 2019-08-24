<Page@1>
================================================================================
                          :: Author   :: J4ck3LSyN ::
                          :: Version  :: 3.1.0     ::
                          "A Python Swiss Army Knife"
================================================================================
<Page@2>
                                 What Is Al13N?
  *--------------------------------------------------------------------------*
  Al13N is a Chain Based language written to be a interactive, dynamic and
  systematic shell. Al13N can be used to do normal programming operations
  while being able to interact with system operations and languages.

  You can use Al13N inside of your Python3 scripts and interact with the
  environment as you wish. Everything is open source and can be modified to
  fit what ever your needs may be.

<Page@3>
================================================================================
                                 Al13N Memory
  *--------------------------------------------------------------------------*
  Everything In Al13N_310 Is Stored Inside Of The Object:
   Al13N_310.Root.RooTUniverse
  This is handed with the object:
   Al13N_310.Root._RooTHandle_

  All galaxies are generated in a multi-layered dictionary:
   <Galaxy>
   --------<Dimension>
   -------------------<BiT>
   -------------------<BiT>...
   --------</>
   </>
<Page@4>
================================================================================
                          Al13N_310.Root._RooTHandle_
  *--------------------------------------------------------------------------*
  Takes 1 Input As list:
   Al13N_310.Root._RooTHandle_([])

  Takes 3 Entities:
   Al13N_310.Root._RooTHandle_([ str::Mode, list::Location, list::MDIO(ModeIO) ])

  Modes:
--------------------------------------------------------------------------------
    g-g, generategalaxy, GenerateGalaxy, GENERATEGALAXY
    Conditions:
     Location Must Contain 1 Entity And Cannot Exist
     MDIO If Empty Than It Will Default Else:
      MDIO Must Contain 3 int Types
       [0] - Low Value
       [1] - High Value
       [2] - Padding
      Low Value Must Be Less Than High Value, This Is The Dimension Generation
      Range, Each Value Inside The Range Will Be Hexed And Padded With
      'f'*Padding.

    Generation Conditions:
     Location { (for i in range(MDIO:0,MDIO:1)-Hex(i)+'f'*MDIO:2) : { ... } }
  ------------------------------------------------------------------------------
   v-l, validationlocation, ValidateLocation, VALIDATELOCATION
   Conditions:
    Location Can Contain 1-3 Entities And MDIO Will Be Ignored
    Will Return list Containing 2 Values [bool,list]
     [0] - Existance
     [1] - Tree
  ------------------------------------------------------------------------------
   g-sl, generatesymlink, GenerateSymLink, GENERATESYMLINK
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contain 1 Entity As str, This Will Be The Label For The Link
     [0] - Gets Mouned With Location[0].MDIO[0]

    Once Complete This Location Can Be Called Globally As That Single Address
    Instead Of Needing To Call:
     [ 'X','.x.','....x....' ] You Can Call ['X.ID']
  ------------------------------------------------------------------------------
   g-vs, variablesimple, VariableSimple, VARIABLESIMPLE
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contian 1 Entity As str,int,list,bool
     [0] - Value

    This Is Mounted Under Tag 'VR-S'
  ------------------------------------------------------------------------------
   g-va, variableadvanced, VariableAdvanced, VARIABLEADVANCED
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contain 1 Entity As dict,bytes
     [0] - Value

    This Is Mounted Under Tag 'VR-A'
  ------------------------------------------------------------------------------
   g-o, generateoutput, GenerateOutput, GENERATEOUTPUT
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Will Be Ignored

    This Is Used Specifically For Output From Other Operations,
    Mounted Under Tag 'G-O'
  ------------------------------------------------------------------------------
   g-f, generatefunction, GenerateFunction, GENERATEGALAXY
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contain 2 Entities
     [0] - Function
     [1] - Location (If Empty No Input)

     This Will Mount The Function As A Variable And Execute It Based Off [1]
     If [1] Is Empty Execute Without Input, Else Take Input From [1] And
     Put Inside Execute Variable.
  ------------------------------------------------------------------------------
   t-b, triggerbit, TriggerBiT, TRIGGERBIT
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    If MDIO Is Empty Than A Output Will Be Sent Back As list Containing
    3 Entities [0] Being The Tree, [1] Being The Entity Value, [2] Being
    The Output From The Operation.
    Else If MDIO Contains A Valid Location The Output Will Be Sent To The
    Address And IT Will Be Writen To 'G-O'

   This IS Mounted Under No_ID
  ------------------------------------------------------------------------------
  <Page@5>
  ==============================================================================
                              Programming Structure
                        Al13N_310.Root._ConvertStringToOp_
   *--------------------------------------------------------------------------*
   Used To Convert Strings Into Operations And Passes Them Through
    Al13N_310.Root._RooTHandle_(operation)

   Syntax:
  ------------------------------------------------------------------------------
    '+' Generates Galaxies (Takes 2/3 Position Inputs)
    ---- [1] Dimension Count
    ---- [2] Configuration
    ---- Same As [ 'g-g', [[1]], [[2]]]
    ---- However This Needs To Be Split Into 3 Sections Via /
    ---- <+Example::1/2/1||
    ---- [ 'g-g', ['Example'], [2]]
    ---- <+Example::||
    ---- [ 'g-g', ['Example'], [] ]
  ------------------------------------------------------------------------------
    '||' New Line Adjustment
  ------------------------------------------------------------------------------
    '::' Main Argument Separator
  ------------------------------------------------------------------------------
    ':-' Location Seperator
  ------------------------------------------------------------------------------
    '-' Writes Into BiTs (Takes 3 Positional Inputs And 1 BiT Target)
    ---- [0] Location ID
    ---- [1] Operation
    ---- [2] Inputs
    ---- <-Example:-0x0:-0000x0000::g-vs::True||
    ---- [ 'g-vs', ['Example','0x0','0000x0000'],[True]]
    ---- [2] Will Be Separated If ',' Exists And Is Parsed
    ---- <-Example:-0x0:-0000x0000::l-bl::X:-.X.:-....x....,...||
    ---- [ 'l-bl', ['Example','0x0','0000x0000'],[...,...]]
  ------------------------------------------------------------------------------
   '/' Comments
  ------------------------------------------------------------------------------
    ',' Seperates Into Lists For Handling
  ------------------------------------------------------------------------------
