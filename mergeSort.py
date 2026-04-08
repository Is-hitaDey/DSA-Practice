def Divide(arr,l,r):
    m=(l+r)//2
    if (l<r):
        Divide(arr,l,m)
        Divide(arr,m+1,r)
        Merge(arr,l,m,r)

def Merge(arr,l,m,r):
    s1=m-l+1
    s2=r-m
    L=[0]*s1
    R=[0]*s2
    for i in range(s1):
        L[i]=arr[l+i]
    for j in range(s2):
        R[j]=arr[m+1+j]

    i=j=0
    k=l

    while(i<s1 and j<s2):
        if(L[i]<R[j]):
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
    while(i<s1):
        arr[k]=L[i]
        i+=1
        k+=1
    
    while(j<s2):
        arr[k]=R[j]
        j+=1
        k+=1

arr=[98,54,47,12,63,85,10]
Divide(arr,0,len(arr)-1)
print(arr)
            