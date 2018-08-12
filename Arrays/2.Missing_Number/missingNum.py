def missingNum(arr,n):
    totalsum = int(n*(n+1)/2)
    req_num = totalsum - sum(arr)
    return req_num

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(missingNum(arr,n))
    t=t-1
