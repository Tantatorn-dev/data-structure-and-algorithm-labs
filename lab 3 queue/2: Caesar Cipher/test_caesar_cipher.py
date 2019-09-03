import caesar_cipher as cc

myI = [1,1,1,1]
text=cc.encode("Zeta Zeza Mario",myI)

print(text)

print(cc.decode(text,myI))