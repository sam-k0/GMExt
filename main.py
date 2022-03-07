import string
from typing import Dict
import json, xmltodict
import ctypes
import gm8
from inputfile import EXTENSIONSTRING, checkFileExists
import inputfile as inpf
import os
import shutil
## OS
HERE = os.path.dirname(os.path.abspath(__file__))

EXTENSIONNAME = input("Extension Name: ")
DLLFILENAME = input("DLL file name (Include the .dll ending!): ")
INPUTFILENAME = os.path.join(HERE, 'input.xml')
OUTPUTFILENAME = os.path.join(HERE, 'output\\{name}\\{name}.extension.gmx'.format(name=EXTENSIONNAME))
YYMANIFESTFILENAME = os.path.join(HERE, 'output\\{name}\\yymanifest.xml'.format(name=EXTENSIONNAME))
DLLDESTPATH = os.path.join(HERE, 'output\\{name}\\{name}'.format(name=EXTENSIONNAME))
GM8EXFILENAME = os.path.join(HERE, EXTENSIONNAME+'.gml')
OUTPUTDIRECTORY = os.path.join(HERE, 'output\\{name}'.format(name=EXTENSIONNAME))
DLLFILEPATH = os.path.join(HERE, DLLFILENAME)
DEBUG = True

# check if dll path is valid
if(checkFileExists(DLLFILEPATH) == False):
    print(ctypes.windll.user32.MessageBoxW(0, """The DLL file you specified could not be found.\n
Please make sure to place it in the same directory as this script.""", "Error", 0))
    exit()

# copy DLL file to destination folder
__path = os.path.join(HERE + os.sep + "output", EXTENSIONNAME)
try:
    os.makedirs(os.path.join(__path, EXTENSIONNAME))
except:
    print("[OK] Folder already created")
shutil.copyfile(DLLFILEPATH, DLLDESTPATH+ os.sep+DLLFILENAME)


functionsDictList = []

## program main
def runmain():
    ## Make fucking xml crap actually readable / convert to json
    o = xmltodict.parse(EXTENSIONSTRING)
    jstr = json.dumps(o);
    extensionDict = json.loads(jstr); ## at this point we have the extension serialized to dict
    ## READ GM8 FILE HERE!
    lines = gm8.readFileToList(GM8EXFILENAME)
    lines = gm8.unsusLines(lines)

    initchunk = gm8.getApiInitChunk(lines)
    _readFuncs = gm8.handleApiInit(initchunk)    

    # manipulate dict
    # set the extensions name
    extensionDict['extension']['name'] = EXTENSIONNAME
    #set the extension filename
    extensionDict['extension']['files']['file']['filename'] = DLLFILENAME
    extensionDict['extension']['files']['file']['origname'] = "extensions\\"+DLLFILENAME
    #set the description
    extensionDict['extension']['description'] = "This was auto-generated using GMEX."
    #set the functions
    extensionDict['extension']['files']['file']['functions']['function'] = _readFuncs;
    print(json.dumps(extensionDict, indent=4))

    ## RETURN TO MONKE / Unparse the json to xml and write to file
    xmstring = (xmltodict.unparse(extensionDict, pretty=True))
    f = open(OUTPUTFILENAME, "w")
    f.write(xmstring);
    f.close();
    # generate zipfile
    shutil.make_archive(os.path.join(HERE, "output"+os.sep+EXTENSIONNAME), 'zip', OUTPUTDIRECTORY )
    #rename to GMEZ
    try:
        os.rename(os.path.join(HERE, "output"+os.sep+EXTENSIONNAME+".zip"),os.path.join(HERE, "output"+os.sep+EXTENSIONNAME+".gmez"))
    except:
        print("[ERR] File already exists.")

    

    

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