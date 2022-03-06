
def readFileToList(filename):
    with open(filename) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        return lines;

def unsusLines(input):
    lines = input;
    newlines = []
    for j in range(len(lines)): # loop entries
        line = lines[j]
        tocut = 0
        
        if(len(line) == 1):
            continue
        

        for i in range(len(line)): # loop chars
            c = line[i]# getcurr

            if(c == ' '): # if whitespace, cut from string
                tocut = tocut + 1
            else:
                newlines.append(line[tocut:]) ## add to new list
                break;
    return newlines;

def getApiInitChunk(inlines):
    END_SECTION_KEYWORD = "#define API_Define_Styles"
    START_SECTION_KEYWORD = "#define API_Init"
    newlist = []
    started = False;
    for line in inlines:
        print(line)
        if(started == False and START_SECTION_KEYWORD in line):
            started = True
            print("started")
            continue
        if(started == True and END_SECTION_KEYWORD in line):
            print("end")
            newlist = newlist[1:]
            break
        
        if(started):
            newlist.append(line);
    return newlist;

def handleApiInit(lines):
    print(lines)
    functionsList = []

    for line in lines:
        step = 0;
        _dllname = ""
        _funcname = ""
        _calltype = ""
        _retType = ""
        _numArgs = ""
        argsTypeList = []
        finishDict = {}
        outerDict = {}

        for c in line:
            if(c == '('): # begin name read
                step = 1;
                continue
            elif(c == ',' and step == 1): # begin func read
                step = 2
                continue
            elif(c == ',' and step == 2): # begin calltype read
                step = 3
                continue
            elif(c == ',' and step == 3): # begin rettype read
                step = 4
                continue
            elif(c == ',' and step == 4): # begin argnum read
                step = 5
                continue
            elif(c == ',' and step == 5): # begin argstype read
                step = 6
                continue
            elif(c == ')' and step == 6):
                #done
                finishDict['name'] = _funcname
                finishDict['externalName'] = _funcname
                finishDict['kind'] = 11 # TODO: needs research
                finishDict['help'] = "sus"

                if("ty_real" in _retType):
                    finishDict['returnType'] = 1
                else:
                    finishDict['returnType'] = 2

                finishDict['argCount'] = int(_numArgs)
                # TODO Add args list
                # push to dict
                outerDict['function'] = finishDict
                functionsList.append(outerDict)
                 

            ## determine where to write
            if(step == 1):
                _dllname += c;

            elif(step == 2):
                _funcname += c;

            elif(step == 3):
                _calltype += c;

            elif(step == 4):
                _retType += c;

            elif(step == 5):
                _numArgs += c;
    #ret
    return functionsList;




                



def printlisttofile(lines):
    f = open("test.txt", "w")
    for line in lines:
        if(len(line) != 1):
            f.write(line);
    f.close();



