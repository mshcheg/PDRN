#!/bin/python

########################################################################
###1. Match entries in MBSS data files by unique identifier (ID) 
### - make a dictionary key = ID, value = {columns 3: from MBSS R1 & R2 Site x Habitat.csv}
### - loop through MBSS R1 & R2 Benthic w FFG & Taxonomic Information.csv -- concatonate with correct entry from dictionary
###
### Output file only contains entries for rounds 1 and 2
### Crustacean genera: Branchiura, Musculium, Stygobromus - no cray fish 
### Shreders - Anything other than detritivors? 
###
###
###2. Extract shreders 
###3. Create Taxa by Site file for each year
###4. Create Env by Site file for each year
###
###5. Get shreder sequences from genbank - who submited, loc, seq 
########################################################################

import sys

def ROUND(x): #set round based on sampling year
    if x in range(92,98):
        return 1
    if x in range(1999,2005):
        return 2
    if x in range(2006,2012):
        return 3


ENVF = sys.argv[1]
TAXF = sys.argv[2]

ENVD = {}

with open(ENVF, "r") as eh: #open MBSS R1 & R2 Site x Habitat.csv
    ENVH = eh.readline()
    ENVH = ENVH.split(",")[3:] #extract column names to use later 
    for chute in eh:
        dook = chute.split(",")
        Key = dook[0]
        Value = dook[3:]
        ENVD[Key] = Value #create dictionary: key = ID, value = {columns 3: from MBSS R1 & R2 Site x Habitat.csv}

with open(TAXF, "r") as infile: #open MBSS R1 & R2 Benthic w FFG & Taxonomic Information.csv
    TAXH = infile.readline()
    TAXH = TAXH.strip("\n") #extract column names
    print "Round,%s,%s" %(TAXH, ",".join(ENVH).strip("\n")) #print combined column names
    for line in infile:
        LL = line.strip("\n").split(",")
        ID = LL[0]
        Year = LL[1].split("-")
        R = ROUND(int(Year[-1]))
        TaxEnv = ENVD[ID] #get env info for site id
        print "%s,%s,%s" %(R, ",".join(LL), ",".join(TaxEnv).strip("\n"))




