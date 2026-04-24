string="5 6 2 + * 12 4 / -"
string=string.split()
operator=['+','-','*','/']
stack=[]
for ch in string:
    if ch.isalnum():
        stack.append(ch)
    elif ch in operator:
        if ch=='+':
            x=int(stack[-2]) + int(stack[-1])
        elif ch=='-':
            x=int(stack[-2]) - int(stack[-1])
        elif ch=='*':
            x=int(stack[-2]) * int(stack[-1])
        elif ch=='/':
            x=int(stack[-2]) / int(stack[-1])
        stack.pop()
        stack.pop()
        stack.append(x)
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
        
