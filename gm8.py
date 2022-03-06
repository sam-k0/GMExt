
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


def printlisttofile(lines):
    f = open("test.txt", "w")
    for line in lines:
        if(len(line) != 1):
            f.write(line);
    f.close();



