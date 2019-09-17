import Al13N_330.Exceptions as Exceptions
import os     # For Handling OS Based Operations
import sys    # For Handling System Based Operations
import random # For Randomness

class Translate:
    def __init__(self,GenerateOnStart=True):
        self.Character_Set = {}
        self.Character_Max = 500
        self.Character_Sep = '.../...'
        self.Character_ID  = '...@...'
        self.Character_Fle = '/../...'
        self.Character_Dir = '/..@...'
        self.Character_Sft = 1
        if GenerateOnStart == True:
            self.GenerateCharacterMap()
    #########################################################################################################################################
    def GenerateCharacterMap(self):
        for c in range(0,self.Character_Max+1):
            i = hex(c*self.Character_Sft)
            self.Character_Set[str(i)] = chr(c)
        return self.Character_Set
    #########################################################################################################################################
