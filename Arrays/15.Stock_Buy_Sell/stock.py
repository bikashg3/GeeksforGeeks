#code
def stock(arr,n):
    curr_min=9999
    curr_max=-9999
    curr_st=-9999
    curr_end=-9999
    flag=0
    
    for i in range(n):
        if arr[i]<curr_min or arr[i]<curr_max:
            if curr_end>curr_st:
                print("({0} {1})".format(curr_st,curr_end),end=' ')
                flag=1
            curr_st=i
            curr_end=i
            curr_min=arr[i]
            curr_max=arr[i]
        elif arr[i]>curr_max:
            curr_end=i
            curr_max=arr[i]
    if curr_end>curr_st:
        flag=1
        print("({0} {1})".format(curr_st,curr_end),end=' ')
    if flag!=1:
        print("No Profit",end='')
    print()

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    stock(arr,n)
    t=t-1
    
