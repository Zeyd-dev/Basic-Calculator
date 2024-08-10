
list=["+","-"]
def fix(ch):
    list=["(",")"]
    ch1=""
    for i in range(len(ch)):
        if not(ch[i] in list) and not ch[i]==" ":
            ch1=ch1+ch[i]
    return ch1

def calcul1(ch):
    ch=fix(ch)
    while not(ch.isnumeric()):
        if rec(ch)==1:
            ch=str(calcul2(ch))
        else:
            ch=str(calcul2(ch[:pos1(ch)]))+ch[pos1(ch):]
    return int(ch)
        
        
def pos(ch):
    i=0
    while i<len(ch) and (ch[i] not in list):
        i=i+1
    return i

def rec(ch):
    s=0
    for i in range(len(ch)):
        if ch[i] in list:
            s=s+1
    return s

def pos1(ch):
    s=0
    p=0
    for i in range(len(ch)):
        if ch[i] in list:
            s=s+1
            if s==2:
                p=i
    return p
    
def calcul2(ch):
    r=0
    if ch.find("+")!=-1:
        r=int(ch[:pos(ch)])+int(ch[pos(ch)+1:])
    elif ch.find("-")!=-1:
        r=int(ch[:pos(ch)])-int(ch[pos(ch)+1:])
    else:
        r=int(ch)
    return r

print(calcul1("(1+(4+5+2)-3)+(6+8)"))