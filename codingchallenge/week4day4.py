def seearch(lst,l,r,x):
    if r>=l:
        mid = l + (r - l) // 2
        if lst[mid]==x:
            return 1
        else:
            if lst[mid]>x:
                return seearch(lst,1,mid-1,x)
            else:
                return seearch(lst,mid+1,r,x)
    else:
        return -1
T=int(input())
for i in range(T):
    N,x=map(int,input().split())
    lst=list(map(int,input().split()))[:N]
    mid=N//2
    ans=seearch(lst,0,N,x)
    print(ans)
