def selectionSort(a):
    n= len(a)
    for j in range(n-1): 
        minimum=j
        for i in range(j,n):
            if (a[minimum]>a[i]):
                minimum=i
        a[j],a[minimum]=a[minimum],a[j]
        
    print(a)
    return a

arr=[98,54,24,70,14,10]
selectionSort(arr)