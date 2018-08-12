def maxSum(arr,n):
    sum_arr = [arr[i] for i in range(n)]
    maximum = sum_arr[0]
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and sum_arr[i]< sum_arr[j]+arr[i]:
                sum_arr[i]=sum_arr[j]+arr[i]
        maximum=max(maximum,sum_arr[i])
    return(maximum)    

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxSum(arr,n))
    t=t-1
