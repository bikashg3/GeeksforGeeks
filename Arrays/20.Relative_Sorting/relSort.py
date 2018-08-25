#code
def relSort(a1,a2,m,n):
    count=[0 for i in range(n)]
    not_inlist=[]
    final_list=[]
    for i in a1:
        try:
            a=a2.index(i)
            count[a]+=1
        except ValueError:
            not_inlist.append(i)
    
    length_notlist=len(not_inlist)
    
    for i in range(len(count)):
        b=count[i]
        while b>0:
            final_list.append(a2[i])
            b-=1
    
    final_list = final_list + sorted(not_inlist)
    print(*final_list)


t=int(input())
while t>0:
    mn=list(map(int,input().split()))
    m=mn[0]
    n=mn[1]
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    relSort(a1,a2,m,n)
    t=t-1
