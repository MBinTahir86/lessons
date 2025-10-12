num01=[1,2,3]
num02=[4,5,6]
result=map(lambda x,y:x+y,num01,num02)
print(list(result))

newnums=[1,2,3,4,5,6]

def sq(n):  
    return n*n

square =list(map(sq,newnums))
print(square)