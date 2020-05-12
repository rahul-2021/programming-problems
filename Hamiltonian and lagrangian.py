n=int(input())
a=list(map(int,input().split()))
x=[]
for i in range(n):
    for j in range(i+1,n):
        if a[i]<a[j]:
            break
    else:
        x.append(str(a[i]))
print(' '.join(x))

