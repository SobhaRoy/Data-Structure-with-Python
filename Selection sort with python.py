l=[7,4,5,9,8,3,2]
length=len(l)
for i in range(0,(length-1)):
    loc=i
    min=l[i]
    for j in range(loc+1,length):
        if min>l[j]:
            min=l[j]
            loc=j
    if min!=l[i]:
        c=l[i]
        l[i]=l[loc]
        l[loc]=c
print("Selection sorts are:")
for i in l:
    print (i,end=" ")
