string="(A+(B*C-(D/E^F)*G)*H)"
precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
operator=['+','-','*','/','^']
stack=[]
p=""
for ch in string:
    if ch=='(':
        stack.append(ch)
    elif ch.isalnum():
        p+=ch
    elif ch==')':
        while(stack[-1]!='('):
            e=stack.pop()
            p+=e
        stack.pop()
    elif ch in operator:
            while(stack[-1]!='(' and precedence[stack[-1]]>=precedence[ch]):
                t=stack.pop()
                p+=t
            stack.append(ch)
            
print(p)
