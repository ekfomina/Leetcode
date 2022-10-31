n=9
k=2678
import itertools
import time
start_time = time.time()
lst=[i for i in range(1, n+1)]
a=[]
for i in itertools.permutations(lst):
    res=''
    for j in i:
        res+=str(j)
    a.append(int(res))
a.sort()
print(str(a[k-1]))
print("--- %s seconds ---" % (time.time() - start_time))