#code
def equilibriumPoint(arr,n):
    point=int(n/2)
    for i in range(n):
        leftSum=sum(arr[:point])
        rightSum=sum(arr[point+1:n])
        if rightSum-leftSum>0:
            point=point+1
        elif rightSum-leftSum<0:
            point=point-1
        else:
            return(point+1)
    return(-1)

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(equilibriumPoint(arr,n))
    t=t-1
