# Finding minimum and maximum elements by divide and conquer
def minMax(arr,start,end):
    if(start==end):
        return arr[start],arr[end]
    if (end ==start+1):
        if (arr[start]<arr[end]):
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]
    m=(start+end)//2
    min1,max1=minMax(arr,start,m)
    min2,max2=minMax(arr,m+1,end)

    return min(min1,min2),max(max1,max2)

    
arr=[54,12,45,98,63,54,10,25]
min,max=minMax(arr,0,len(arr)-1)
print("The minimum value is: ",min)
print("The minimum value is: ",max)