def knapsack01(k,n,w,v):
    result=list()
    result=[[0]*(k+1)]*(len(w)+1)
    for i in range(n+1):
        temp=[]
        for j in range(k+1):
            try:
                if(i==0 or j==0):
                    temp.append(0)
                elif(j>=w[i-1]):
                    temp.append(max([result[i-1][j],  result[i-1][j-w[i-1]]+ v[i-1]]))
                else:
                    temp.append(result[i-1][j])
            except:
                pass
        result.pop(i)
        result.insert(i,temp)
    return result[len(result)-1][len(result[len(result)-1])-1]



if __name__ == "__main__":
    n=int(input("No of elements to enter: "))
    values = list(map(int, input("Enter values: ").split()))
    weights = list(map(int, input("Enter weights: ").split()))
    size = int(input("Enter knapsack size: "))
    r = knapsack01(size,n, weights, values)
    print(r)