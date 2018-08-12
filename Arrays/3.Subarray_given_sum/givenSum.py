def givenSum(arr,n,reqsum):
    sum1=0
    flag=0
    start=0
    end=0
    
    while end<n:
        sum1=sum1+arr[end]
        if sum1>reqsum:
            start=start+1
            end=start
            sum1=0
        elif sum1==reqsum:
            flag=1
            break
        else:
            end=end+1
    if flag==1:
        print(start+1,end+1)
    else:
        print(-1)

t=int(input())
while t>0:
    ns=list(map(int,input().split()))
    n=ns[0]
    reqsum=ns[1]
    arr=list(map(int,input().split()))
    givenSum(arr,n,reqsum)
    t=t-1
