def coinChange(arr,total):
    n=len(arr)
    arr.sort()
    count=0
    i=n-1

    while total>0 and i>=0:
        while arr[i]<=total:
            count+=1
            total-=arr[i]
        i-=1
    
    print("Minimum denominations required:",count)

arr=[1,2,5,10,20,50,100,200,500]
money=1024
coinChange(arr,money)