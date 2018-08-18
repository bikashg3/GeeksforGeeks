#code

def find(arr,n):
    
    maxNo=arr[0]
    for i in range(1,n-1):
        if arr[i]>=maxNo:
            maxNo=arr[i]
            arr[i]=-arr[i]
    
    minNo=abs(arr[n-1])
    for i in range(n-2,0,-1):
        val=abs(arr[i])
        if val<=minNo:
            minNo=val
        if arr[i]<=0 and minNo<val:
            arr[i]=abs(arr[i])
    #print(*arr)
    for i in arr:
        if i<0:
            return(abs(i))
    
    return(-1)


t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(find(arr,n))
    t=t-1
        
