def sortedArray(arr,n):
    arrsort=[0 for i in range(n)]
    start=0
    end=n-1
    for i in range(n):
        if (arr[i]-1)>0:
            arrsort[end]=arr[i]
            end=end-1
        elif (arr[i]-1)<0:
            arrsort[start]=arr[i]
            start=start+1
    for i in range(start,end+1):
        arrsort[i]=1
    print(*arrsort)

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    sortedArray(arr,n)
    t=t-1
    
