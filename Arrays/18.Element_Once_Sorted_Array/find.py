#code
def find_element(arr,n):
    total_sum=0
    for i in range(n):
        total_sum=total_sum+arr[i]
    return(2*sum(set(arr))-total_sum)

def find(arr,n):
    for i in range(1,n-1):
        if arr[i+1]-arr[i]>0 and arr[i]-arr[i-1]>0:
            return(arr[i])
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(find(arr,n))
    t=t-1
