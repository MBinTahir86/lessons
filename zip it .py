list_1=[1,2,3]
list_2=['a','b','c']
zipped=zip(list_1,list_2)
print(list(zipped))


list3=[2,4,6,8]
list4=['d','e','f','g']
for i ,j in zip(list3,list4[::-1]):
    print(i,j)

