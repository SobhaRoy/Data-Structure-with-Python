l=[7,4,5,9,8,3,2]
length=len(l)
for i in range(0,length-1):
    for j in range(0,(length-i)-1):
        if l[j]>l[j+1]:
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print("Bubble sorts are:")
for i in l:
    print (i,end=" ")
