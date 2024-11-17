l=list(map(int,input().strip().split()))
arr=list(map(int,input().strip().split()))
n=l[0]
h=l[1]
count=0
for i in arr:
    if i>h:
        count=count+2
    else:
        count=count+1
print(count)
