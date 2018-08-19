#code
def zigzag(arr,n):
    flag=-1
    for i in range(n-1):
        if flag!=1 and arr[i]>arr[i+1]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
        if flag==1 and arr[i]<arr[i+1]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
        flag=-flag
    print(*arr)

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    zigzag(arr,n)
    t=t-1
