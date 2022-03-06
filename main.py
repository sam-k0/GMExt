import string
from typing import Dict
import json, xmltodict

import gm8
from inputfile import EXTENSIONSTRING
import inputfile as inpf
import os
## OS
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTFILENAME = os.path.join(HERE, 'input.xml')
OUTPUTFILENAME = os.path.join(HERE, 'output.xml')
GM8EXFILENAME = os.path.join(HERE, 'extension.gml')
DEBUG = True

functionsDictList = []

## program main
def runmain():
    ## Make fucking xml crap actually readable / convert to json
    o = xmltodict.parse(EXTENSIONSTRING)
    jstr = json.dumps(o);
    extensionDict = json.loads(jstr); ## at this point we have the extension serialized to dict
    ## READ GM8 FILE HERE!
    lines = gm8.readFileToList(GM8EXFILENAME)
    #lines = ["   sussy baka", "     ", "we are sus!"]
    lines = gm8.unsusLines(lines)
    #for line in lines:
    #    print(line)
    initchunk = gm8.getApiInitChunk(lines)
    _readFuncs = gm8.handleApiInit(initchunk)    
    


    extensionDict['extension']['files']['file']['functions'] = _readFuncs;
    print(json.dumps(extensionDict, indent=4))

    ## RETURN TO MONKE / Unparse the json to xml and write to file
    xmstring = (xmltodict.unparse(extensionDict, pretty=True))
    f = open(OUTPUTFILENAME, "w")
    f.write(xmstring);
    f.close();
    
    


    

    

### runner
### This will just launch the program and catch any excepts
if(DEBUG):
    runmain()
else:
    try:
        print("launching...")
        runmain()
    except Exception as e:
        print("DURING EXECUTION, THE FOLLOWING ERROR HAS OCCURED:")
        print(e)