num2=[1,2,3,4]
num1=[2,4]
ans=[]
for i in num1:
    for j in num2:
        if i==j:
            loc=j
            flag=0
            for k in range(loc+1,len(num2)):
                if i<num2[k]:
                    flag=1
            if flag==0:
                ans.append(-1)
            else:
                ans.append(num2[j])
print(ans)
                
