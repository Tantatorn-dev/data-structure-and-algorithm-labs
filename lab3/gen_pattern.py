def createLine(chars,width):
    return '.'.join(chars).center(width,'.')

def gen_pattern(chars):
    myStr=""
    width  = 4*len(chars) -3
    for i in range(len(chars),0,-1):
        s = chars[i:len(chars):]
        if len(s) == 1:
            myStr+= createLine(s,width) + '\n'
        else:
            s = s+s[len(s)-2::-1]
            myStr+= createLine(s,width) + '\n'
    for i in range(0,len(chars)):
        s = chars[i:len(chars):]
        if len(s) == 1:
            myStr+= createLine(s,width) + '\n'
        else:
            s = s+s[len(s)-2::-1]
            myStr+= createLine(s,width) + '\n'
    myStr = myStr.split('\n',1)[1]
    return myStr

print(gen_pattern('zyxw'))