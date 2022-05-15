n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(m):
    x,y = map(int,input().split())
    union_parent(x,y)
for i in range(n):
    find_parent(i)
parents = []
for i in range(1,n+1):
    if find_parent(i) not in parents:
        parents.append(find_parent(i))
print(len(parents))
