def quicksort(a,l,r):
    if(l<r):
        p=quick(a,l,r)
        quicksort(a,l,p-1)
        quicksort(a,p+1,r)
def quick(a,l,r):
    p=l
    left=l+1
    right=r
    while(True):
        while(a[p]<=a[right] and right>=left):
            right=right-1
            
        if(a[p]>a[right]):
            a[p],a[right]=a[right],a[p]
            p=left
            right=right-1
            
        if(right<left):
            return p
        
        while(a[p]>=a[left] and right>=left):
            left=left+1
        if(a[p]>=a[left]):
            a[p],a[left]=a[left],a[p]
            p=left
            left=left+1
        if(right<left):
            return p
l=[9,4,12,7,1]
p=len(l)-1
quicksort(l,0,p)

print(l)

