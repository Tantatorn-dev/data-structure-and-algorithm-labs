import caesar_cipher as cc

myI = [1,2,3,4]

text=cc.encode("hello moto",myI)

print(text)

print(cc.decode(text,myI))