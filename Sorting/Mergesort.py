def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    left=merge_sort(lefthalf)
    right=merge_sort(righthalf)

    return merge(left,right)

def merge(left,right):
    i=j=0
    result=[]
    while(len(left)>i and len(right)>j):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[5,2,1,9,10,7,0,-1,-6]
l=merge_sort(arr)
print(l)
l
