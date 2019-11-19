from math import log2
from math import floor

def print90(h,i,max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h,(i*2)+2,max_i)
        print('   '*indent,h[i])
        print90(h,(i*2)+1,max_i)

def insertMinHeap(h,i):
    print('insert',h[i],'at index',i,end='    ')
    print(h)
    insertEle = h[i]
    fi = (i-1)//2
    while i > 0 and insertEle < h[fi]:
        h[i] = h[fi]
        i=fi
        fi = (i-1)//2
    h[i] = insertEle

h = [30,85,97,100,200]
for i in range(1,len(h)):
    insertMinHeap(h,i)
    print(h)
    print90(h,0,i)
    print('------------------------\n')

def delMin(h,last):
    print('delete min ',h[0],' last index= ',last,end='     ')
    print(h)
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2 +1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        minVal = ls if h[ls] < h[rs] else rs
        if h[minVal] < insertEle:
            h[hole] = h[minVal]
            hole = minVal
            ls = hole*2 + 1
        else:
            found = True
    h[hole] = insertEle

h= [1,4,2,3,8,7]
for last in range(len(h)-1,-1,-1):
    delMin(h,last)
    print(h)
    print90(h,0,last)
    print('-------------------\n')