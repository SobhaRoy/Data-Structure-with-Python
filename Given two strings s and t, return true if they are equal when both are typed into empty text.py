s="ab#c"
s1=""
s1=list(s1)
for i in s:
    if i!='#':
        s1+=i
    else:
        if s1!=[]:
            del s1[len(s1)-1]
print(''.join(s1))
result1=''.join(s1)

t="ad#c"
t1=""
t1=list(t1)
for i in t:
    if i!='#':
        t1+=i
    else:
        if t1!=[]:
            del t1[len(t1)-1]
result2=''.join(t1)
print(''.join(t1))

if result1==result2:
    print("True")
else:
   print("False") 


        
