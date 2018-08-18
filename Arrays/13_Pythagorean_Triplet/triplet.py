#code

def triplet(arr,n):
    sq_num=0
    sq_arr=[]
    for i in range(n):
        sq_num=pow(arr[i],2)
        sq_arr.append(sq_num)
    flag="No"
    
    for i in range(n):
        if flag=="Yes":
            break
        for j in range(i+1,n):
            side_sums=sq_arr[i]+sq_arr[j]
            if side_sums in sq_arr:
                flag="Yes"
                break
    return(flag)


t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(triplet(arr,n))
    t=t-1
    
