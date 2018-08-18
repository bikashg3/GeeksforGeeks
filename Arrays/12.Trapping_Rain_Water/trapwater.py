#code
def trapwater(arr,n):
    largest=arr[n-1]
    left_largest=[0 for i in range(n)]
    right_largest=[0 for i in range(n)]
    water=0
    
    for i in range(n-1,0,-1):
        if largest<arr[i]:
            largest=arr[i]
        left_largest[i]=largest
    
    largest=arr[0]
    
    for i in range(n):
        if largest<arr[i]:
            largest=arr[i]
        right_largest[i]=largest
    
    
    for i in range(n):
        minimum=min(left_largest[i],right_largest[i])
        if minimum>arr[i]:
            water=water+minimum-arr[i]
    return water

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(trapwater(arr,n))
    t=t-1
