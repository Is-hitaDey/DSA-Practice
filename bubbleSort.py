def bubbleSort(a):
    n=len(a)
    for j in range(n-1):
        for i in range(n-1-j):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return(a)


arr=[98,88,78,65,45,25,10 ]
sortedArr=bubbleSort(arr)
print(sortedArr)
        