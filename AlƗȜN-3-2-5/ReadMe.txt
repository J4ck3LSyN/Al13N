<Title@1>
================================================================================
                          :: Author   :: {F.G}J{F.R}4{F.G}ck{F.R}3{F.G}LSyN{F.W} ::
                          :: Version  :: 3.2.5     ::
                          "A Python Swiss Army Knife"
================================================================================
<Description@2>
                                 What Is Al13N?
  *--------------------------------------------------------------------------*
  Al13N is a Chain Based language written to be a interactive, dynamic and
  systematic shell. Al13N can be used to do normal programming operations
  while being able to interact with system operations and languages.

  You can use Al13N inside of your Python3 scripts and interact with the
  environment as you wish. Everything is open source and can be modified to
  fit what ever your needs may be.

<Memory Information@3>
================================================================================
                                 Al13N Memory
  *--------------------------------------------------------------------------*
  Everything In Al13N_325 Is Stored Inside Of The Object:
   Al13N_325.Root.RooTUniverse
  This is handed with the object:
   Al13N_325.Root._RooTHandle_

  All galaxies are generated in a multi-layered dictionary:
   <Galaxy>
   --------<Dimension>
   -------------------<BiT>
   -------------------<BiT>...
   --------</>
   </>
<_RooTHandle_@4>
================================================================================
                          Al13N_325.Root._RooTHandle_
  *--------------------------------------------------------------------------*
  Takes 1 Input As list:
   Al13N_325.Root._RooTHandle_([])

  Takes 3 Entities:
   Al13N_325.Root._RooTHandle_([ str::Mode, list::Location, list::MDIO(ModeIO) ])

  Modes:
--------------------------------------------------------------------------------
<_RooTHandle_@4.1>
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
<_RooTHandle_@4.2>
  ------------------------------------------------------------------------------
   v-l, validationlocation, ValidateLocation, VALIDATELOCATION
   Conditions:
    Location Can Contain 1-3 Entities And MDIO Will Be Ignored
    Will Return list Containing 2 Values [bool,list]
     [0] - Existance
     [1] - Tree
<_RooTHandle_@4.3>
  ------------------------------------------------------------------------------
   g-sl, generatesymlink, GenerateSymLink, GENERATESYMLINK
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contain 1 Entity As str, This Will Be The Label For The Link
     [0] - Gets Mouned With Location[0].MDIO[0]

    Once Complete This Location Can Be Called Globally As That Single Address
    Instead Of Needing To Call:
     [ 'X','.x.','....x....' ] You Can Call ['X.ID']
<_RooTHandle_@4.4>
  ------------------------------------------------------------------------------
   g-vs, variablesimple, VariableSimple, VARIABLESIMPLE
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contian 1 Entity As str,int,list,bool
     [0] - Value

    This Is Mounted Under Tag 'VR-S'
<_RooTHandle_@4.5>
  ------------------------------------------------------------------------------
   g-va, variableadvanced, VariableAdvanced, VARIABLEADVANCED
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Must Contain 1 Entity As dict,bytes
     [0] - Value

    This Is Mounted Under Tag 'VR-A'
<_RooTHandle_@4.6>
  ------------------------------------------------------------------------------
   g-o, generateoutput, GenerateOutput, GENERATEOUTPUT
   Conditions:
    Location Must Be A Valid Entity And Must Exist
    MDIO Will Be Ignored

    This Is Used Specifically For Output From Other Operations,
    Mounted Under Tag 'G-O'
<_RooTHandle_@4.7>
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
<_RooTHandle_@4.8>
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
<_RooTHandle_@4.9>
  ------------------------------------------------------------------------------
  l-bl, logicbool, LogicBool, LOGICBOOL
  Conditions:
   Location Must Be Valid Entity And Must Exist
    [0] - Variable To Test
    [1] - Variable To Test
   If [0] == [1] Than True / Else False
<_RooTHandle_@4.10>
  ------------------------------------------------------------------------------
  g-tb, toolbox, ToolBox, TOOLBOX
  Conditions:
   Location Must Be Valid Entity And Must Exist
    [0] - Trigger For ToolBox
    [1] - Input For Action
<_RooTHandle_@4.11>
  ------------------------------------------------------------------------------
  c-ap, compileappend, CompileAppend, COMPILEAPPEND
  Conditions:
   Location Must Be Valid Entity and Must Exist
    [0] - Location 1
    [1] - Location 2
  If The Types Of [0] And [1] Are A Match Append Values
<_RooTHandle_@4.12>
  ------------------------------------------------------------------------------
  s-t, shelltrigger, ShellTrigger, SHELLTRIGGER
  Conditions:
   Location Must Be Valid Entity And Must Exist
    [0] - List Of Commands
   Will Return Output As String
  ------------------------------------------------------------------------------
<Interpreter@5>
================================================================================
                                Al13N Interpreter
                                 Interpreter()
  *-------------------------------------------------------------------------*
  Used For Interpreting ASCII Commands And Translating Into Root()
  Command Structure:
   OP::Galaxy:-Dimension:-BiT::OP::IO....||

   ::   -> Spacing
   :-   -> Locations If Len Is 2 Than Capture SymLink If 3 Than Location
   ||   -> Must Include As Seperator
   ,    -> Capture List Entries
   @    -> Captures A Locations Value

   IO Can Take Locations As Well
   OP::Galaxy:-Dimension:-BiT::OP::Galaxy:-Dimension:-BiT||

   OPs:
    '+,new,New,NEW'       - Generates New Galaxy Must Be Followed By 3 Inputs
      ::Name::null/int,int,int||
      Name Being The Galaxy Title
      If null Than Configure Default Else Confiure Under Dimension Levels
      See: _RooTHandle_@4.1 For More Info
    '-,write,Write,WRITE' - Write To Given Location
      ::Galaxy:-Dimension:-BiT::Trigger::IO||
      Trigger Must Be A Valid Action For Root._RooTHandle_
      IO Must Pass For MDIO
    '/,comment,Comment,COMMENT' - Comments
      ::This Is A Comment||
<Handling_ReadMe@6>
================================================================================
                               ReadMe Handling
                      Interpreter._ChapterFileHandle_(File,Page)
  *-------------------------------------------------------------------------*
  Used To Channel ReadMe Files And Indexing Them By Pages.
  Pages Are Marked In These Files Via:
   <TITLE@NUMBER>
  This Can Be Triggered Via Interpreter._ChapterFileHandle_(File,Chapter)
  If Chapter Is None Than Send All
  If Chapter Is '...' Than Send all Pages
  Else Chapter Must Exist As A Page, And Can Be Called Via:
   TITLE
   NUMBER
   TITLE@NUMBER
  All Items Follow The Color Index
  ---------------------------------------------------------------------------
<Handling_Colour@7>
================================================================================
                               Color Handling
                       Interpreter._PipeColor_(string)
  *--------------------------------------------------------------------------*
  Used To Highlight Strings With Colours.
  These Are Interpreted Via {TYPE.COLOUR}
   {F.G} - ForeGround Green    F.G
   {B.G} - BackGround Green    B.G
   {F.B} - ForeGround Blue     F.B
   {B.B} - BackGround Blue     B.B
   {F.R} - ForeGround Red      F.R
   {B.R} - BackGround Red      B.R
   {F.M} - ForeGround Magenta  F.M
   {B.M} - BackGround Magenta  B.M
   {F.C} - ForeGround Cyan     F.C
   {B.C} - BackGRound Cyan     B.C
   {F.W} - ForeGround White    F.W
   {B.W} - BackGround White    B.W
   {F.Y} - ForeGround Yellow   F.Y
   {B.Y} - BackGround Yellow   B.Y
   {F.X} - ForeGround Black    F.X
   {B.X} - BackGround Black    B.X
   {F.0} - ForeGround Reset    F.0
   {B.0} - BackGround Reset    B.0
   {S.B} - Style Bright        S.B
   {S.N} - Style Normal        S.N
   {S.D} - Style Dim           S.D
   {S.0} - Style RESET_ALL     S.0
  ---------------------------------------------------------------------------
<Handling_ToolBox@8>
================================================================================
                            ToolBox Handling
                           Al13N_325.ToolBox()
  *--------------------------------------------------------------------------*
  Used For Extend Functionality And Is Used Via:
    -::B:-.x.:-....x....::g-tb::Function.inputs
