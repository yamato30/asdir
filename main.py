idea = ("|_______________________________________________________________________________________________________________________________|")
import os
from treat import *
from decomp import *
#load function asdir start _______________________________________
from function.aff import aff
#load function asdir stop ________________________________________


print(idea)
print("bonjour choisisier un fichier .asdir dans le dossier project (vous n'avez pas besoin de mettre le .asdir)")
filepro = input("fichier : ")
filetot = "project/" + filepro + ".asdir"

def read(ter , fir):
    print(ter)
    print("chargement de :" , fir)
    fw = open(fir)
    print(ter)

    nll = fw.readlines()
    nlt = len(nll)
    nl = 0
    print(nlt)
    while nl < nlt:
        
        wl1 = nll[nl]
        treat(wl1)
        nl = nl + 1
       

    print("fin")

read(idea , filetot)

    




