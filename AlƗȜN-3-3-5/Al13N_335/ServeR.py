import Al13N_335.Exceptions as Exceptions
import Al13N_335.RegeX      as RegeX
import Al13N_335.Graphical  as Graphics
import Al13N_335.ThreadR    as Threads
import os, time, sys
import subprocess, scapy, socket

class Tramition:
    def __init__(self):
        self.Sockets = {}
        self.HostIP  = '0.0.0.0'
        self.Port    = 0
        
