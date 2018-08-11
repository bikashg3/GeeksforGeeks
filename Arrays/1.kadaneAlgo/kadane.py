def kadane(arr,n):
    gmax=arr[0]
    curmax=arr[0]
    for i in range(1,n):
        curmax=max(arr[i],arr[i]+curmax)
        gmax=max(curmax,gmax)
    return gmax

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(kadane(arr,n))
    t=t-1
