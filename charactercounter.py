word=str(input("enter any word"))
char=str(input("enter any character"))
M=0
count=0
while (M < len(word)):
    if (word[M]==char):
        count=count+1
    M=M+1
print("the character",char,"appears",count,"times in the word",word)
