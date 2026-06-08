def heapify(a,i,n):
    l=2*i+1
    r=2*i+2
    lar=i
    if(r<n and a[r]>a[lar]):
        lar=r
    if(l<n and a[l]>a[lar]):
        lar=l
    if(i==lar):
        return
    a[i],a[lar]=a[lar],a[i]
    heapify(a,lar,n)

def max_heap(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        heapify(a,i,n)

    

def heap_sort(a):
    n=len(a)
    while n>0:
        a[0],a[n-1]=a[n-1],a[0]
        n=n-1
        heapify(a,0,n)

a=[40,30,50,60,35,49,65,55,25,28]
n=len(a)
max_heap(a)
print(a)
heap_sort(a)
print(a)




