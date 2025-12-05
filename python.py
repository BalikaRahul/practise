def sort(a):
    if(len(a)>1):
        mid=len(a)//2
        left =a[:mid]
        right=a[mid:]
        sort(left)
        sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1

    return a

a=[1,2,4,3,6,5,8,0]
result = sort(a)
print(result)