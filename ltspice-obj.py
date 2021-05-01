from  pathlib import Path

def getTxt(textfile):
    f = open(textfile.replace('\\','/'))
    text = f.read()
    f.close()
    return text

def valsPerLine(lines):
    firstLine = lines.splitlines()[1]
    return len(firstLine.split())
    

def numLines(lines):
    return len(lines.split('\n'))

def coords(inFile, outFile, x, y, z):
    inStr =  getTxt(table)
    lineAmount = numLines(inStr)
    lineSize = valsPerLine(inStr)
    lines = inStr[inStr.find('\n')+1:]
    lines = lines.split()
 #   lines = list(map(float,lines))
#    s = sum(lines); lines = [float(i)/s for i in lines]
    lines = list(map(str,lines))
    outStr = ''

    for i in range(0,lineAmount):
        indx = i * lineSize
        outStr += 'v ' + lines[x + indx] + ' ' + lines[y + indx] + ' ' + lines[z + indx] + ' ' + '\n'

    for i in range (1,lineAmount - 1):
        outStr += 'l ' + str(i) + ' ' + str(i + 1) + '\n'

    with open(outFile.replace('\\','/'), 'x') as f:
        f.write(outStr)

        
coords(r'C:\Users\Noah\Documents\LTspiceXVII\Chuas Circuit.txt', r'E:\3d\turtleslurp.obj, 0, 1, 2)
