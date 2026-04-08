def Max_Min_Difference(arr):
    s_arr=sorted(arr)
    n=len(arr)
    maxD=0
    minD=0

    i=0
    j=n-1
    k=0
    while i<=(n-1)//2:
        maxD+=abs(s_arr[i]-s_arr[j])
        i+=1
        j-=1

        minD+=abs(s_arr[k]-s_arr[k+1])
        k=k+2
    print("Max Difference between the two arrays is ",maxD)

    print("Min Difference betweent the two arrays is ",minD)




arr=[12,5,25,10,2,15,8,30]
Max_Min_Difference(arr)