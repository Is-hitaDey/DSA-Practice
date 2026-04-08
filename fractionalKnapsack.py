def Fractional_knapsack(items_wt,price,capacity):
    n= len(items_wt)

    # items = [(24,3,7),(12,4,3),(10,5,2)]

    items=[ [price[i], items_wt[i],price[i]/items_wt[i]] for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if items[i][2]>items[j][2]:
                items[i][2],items[j][2]=items[j][2],items[i][2]

    profit =0.0

    for price,weight,perKGPrice in items:
        if(capacity>=weight):
            capacity-=weight
            profit+=price
        else:
            profit=profit +perKGPrice * capacity
    print("Total Profit = ",profit)


price=[24,21,12,10]
item_wt=[7,3,4,5]
capacity=20
Fractional_knapsack(item_wt,price,capacity)

