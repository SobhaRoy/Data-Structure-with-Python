l=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    a=int(input("Enter element for a["+str(i)+"]:"))
    l.append(a)
item=int(input("Enter the item value:"))
flag=0
for i in range(0,len(l)):
    if(l[i]>item):
        loc=i
        flag=1
        break
if(flag==1):
    l.insert(loc,item)
else: l.insert(len(l),item)
print(l)
