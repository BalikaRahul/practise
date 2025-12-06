def sort (a,i=0):
    n =len(a)
    if i==n:
        return 
    key =a[i]
    j=i-1
    while(j>=0 and a[j]>key):
        a[j+1]= a[j]
        j-=1
    a[j+1]= key

    return sort (a,i+1)
a=[1,4,3,2,5]
result = sort(a)
print(a)