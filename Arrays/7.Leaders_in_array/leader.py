def leader(arr,n):
    max_element=arr[n-1]
    leader_list=[arr[n-1]]
    j=n-1
    while j>=0:
        if arr[j]>max_element:
            leader_list.insert(0,arr[j])
            max_element=arr[j]
            
        j=j-1
    print(*leader_list)

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    leader(arr,n)
    t=t-1
