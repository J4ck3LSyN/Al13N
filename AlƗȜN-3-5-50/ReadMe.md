# Alien (3.5.50)
#### Author: J4ck3LSyN | http://github.com/J4ck3LSyN

#### Index:

1. [Description](#Description)
2. [Interpreter](#Interpreter)
3. [Syntax](#Syntax)
4. [Signal Calls](#Signal-Calls)

# Description
Alien is a dynamic tool to assist in general programming automation and cyber CyberSecurity Operations.

## Requirements
Python Module: `colorama` Install Via `pip3 install colorama`   

# Interpreter

## Commands:

### 0xfffa0 (Terminate)
Terminates the interpreter
`0xfffa0 1048480 terminate Terminate TERMINATE`

### 0xfffb0 (Usage)
Displays Help Usage
`0xfffb0 104898 usage Usage USAGE`

Can take a argument to act as query for internal Alien.config['usageDict']
`0xfffb0 query`

# Syntax

## Syntax Flow

# Signal-Calls

## What Are Signal Calls

SIGCALLS(Signal Calls) are functions that are set inside of a dictionary to be executed with arguments to return a output, this is generated on initialization of `Alien()` to `Alien.configure['signalCallTree']`,
this is returned from `Alien._generate_signalTree()` as a list: [0] is the signal keys, [1] is the dictionary of signal calls. When generating each hex value is appended by character index IE:
```python
hexKeys = ['0x000','0x001','0x100','0x101']
hexTree = {}
for Key in range(0,len(hexKeys)-1):
  if str(hexKeys[Key])[2] in validCharacter and str(hexKeys[Key][3:]) == str('00'):
    # Create Key In hexTree And Configure To Record All Non Entries Inside Until New Value Occurs
```
The `Signal` is the key inside of the signalTree while `Call` is the value inside of that location:
```python
signalCall = '0x000.0x001'
signal = signalCall.split('.')[0]
call   = signalCall.split('.')[1]
signalCallValue =hexTree[signal][call]
```
## Signal Call Values
After generation of a signalTree each calls value is set to `['NULL']` this is a non-configured value and will do nothing if called, if the value is configured it will be a list containing 3 values: `[<func>,<rules>,<outputLocaton>]`,
`<func>` must be a python method to call when the SIGCALL is executed. `<rules>` Are operation rules for execution, this tells the execution valid arguments and internal function operations, `<outputLocaton>` is where we wish to send
the returned output to, this must be a valid register inside of `Alien.registry`, all outputs are recorded into the values third value.
## Mounting Signal Call Modules (Alien Modules)
Each module must contain a structure like so:
```python
class moduleName:
  def __init__(self):
    self._alien_configure = {}
  def _alien_handle(self,alienInput):
    if type(alienInput) is dict:
      ...
    else: raise self.moduleNameException(...)
  def moduleNameException(...):
    ...
```

### _alien_configure (Description)
This is the configurations to handle the function under, this allows for more control over argument types and length, logging and verbosity, and registry operations.

### _alien_configure (Keys)

### _alien_handle (Description)
When a SIGCALL is executed the inputs and configurations are executed via the `_alien_handle` function through the variable `alienInput` as a dictionary.

### _alien_handle (Keys)
```python
alienInput = {
  'moduleCommand':'commandValue'
}
```

#### Developer Notes
