def pellandrome(r):
    var1 = len(r)-1
    s=0
    while (s < var1):
        if r [s]!= r [var1]:
            return False
        s += 1
        var1 -= 1
    return True
r=(1,2,3,3,2,4)
if pellandrome(r):
    print("it is pellandrome")
else:
    print("it is not pellandrome")

