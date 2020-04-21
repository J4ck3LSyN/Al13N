import Al13N_340 as Root
import os
RG = Root._Graphics()
PM = Root.Project('Example','whirlpool')
print(str(PM.Map))
PM._GenerateMemoryMap(PM.Signature,'Example','Example',['hex',1,2,2],['bin',32,2,2])
PM._ConfigureMemoryByte(PM.Signature,'Example',['Example','0x2','0b10'],'root.var',['test'])
PM._ConfigureMemoryByte(PM.Signature,'Example',['Example','0x2','0b110'],'root.fmnt',[ ['Example','0x2','0b101101011'],[]])
RG._ParseAndDisplayProject(PM.Map,PM.Register)
#PM.WritePureDataFile(PM.Signature,'utf-16',os.getcwd(),'example-nopad','data')
#PM.WritePureDataFile(PM.Signature,'utf-16',os.getcwd(),'example-padding','data',Padding=RP)
print(str(PM.Map))
