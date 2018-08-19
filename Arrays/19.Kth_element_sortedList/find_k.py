#code
def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def find_k(left_half,right_half,k):
    final_arr=merge(left_half,right_half)
    return(final_arr[k-1])

t=int(input())
while t>0:
    nmk=list(map(int,input().split()))
    n=nmk[0]
    m=nmk[1]
    k=nmk[2]
    left_half=list(map(int,input().split()))
    right_half=list(map(int,input().split()))
    print(find_k(left_half,right_half,k))
    t=t-1
