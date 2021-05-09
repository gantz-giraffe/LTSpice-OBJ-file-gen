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

def coords(table, x, y, z):
    inStr =  getTxt(table)
    lineSize = valsPerLine(inStr)
    lines = inStr.split()[lineSize:]
    lines = list(map(str,lines))
    lineAmount = int(len(lines)/lineSize)
    outStr = ''
    for i in range(0,lineAmount):
        indx = i * lineSize
        outStr += 'v ' + lines[x + indx] + ' ' + lines[y + indx] + ' ' + lines[z + indx] + ' ' + '\n'
    for i in range (1,lineAmount - 1):
        outStr += 'l ' + str(i) + ' ' + str(i + 1) + '\n'
    with open(r'E:\3d\turtleslurp.obj', 'x') as f:
        f.write(outStr)
        

        
coords(r'C:\Users\Noah\Documents\LTspiceXVII\chaotic twin-t.txt', 3, 1, 2)
