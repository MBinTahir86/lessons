a=[1,2,3,4,5]
b=[1,2,3,4,5,6,7,]
if b in a:
    print("true")
else: 
    print("false")

if a is b:
    print("false")
else:
    print("true")

c=[2,1,3,4,9,6]
d=[1,2,3,4,5,6,7,8,9,0]

if c not in d:
    print("true")
else:
    print("false")

if c is not d:
    print("true")
else:
    print("false")