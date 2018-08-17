#code
#using circular arrays
def max_k(arr,n,k):
    sub_array=[arr[i] for i in range(k)]
    max_list=[max(sub_array)]
    for i in range(k,n):
        j=i%k
        sub_array[j]=arr[i]
        max_list.append(max(sub_array))
    print(*max_list)

t=int(input())
while t>0:
    nk=list(map(int,input().split()))
    n=nk[0]
    k=nk[1]
    arr=list(map(int,input().split()))
    max_k(arr,n,k)
    t=t-1
