#code

def getmin(arr,n,k):
    arr.sort()
    arr_k = [-1 for i in range(int(n-k+1))]
    index=0
    cur_min=int(arr[n-1]-arr[0])
    for i in range(int(n-k+1)):
        arr_k[i]=arr[i+k-1]-arr[i]
        if arr_k[i]<cur_min:
            index=i
            cur_min=arr_k[i]
    #print(arr[index:index+k])
    print(cur_min)
    #print(index)

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    getmin(arr,n,k)
    t=t-1
    
   
