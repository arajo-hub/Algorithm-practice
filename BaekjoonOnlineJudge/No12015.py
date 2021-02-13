from bisect import bisect_left
import sys

n=int(sys.stdin.readline())

a=list(map(int, sys.stdin.readline().split()))

dp=[]

for i in a:
    k=bisect_left(dp, i)
    if len(dp)<=k:
        dp.append(i)
    else:
        dp[k]=i

print(len(dp))

# def bisect_left(a: Sequence[_T], x: _T, lo: int=..., hi: int=...)
# Return the index where to insert item x in list a, assuming a is sorted.

# The return value i is such that all e in a[:i] have e < x, and all e in a[i:] have e >= x. So if x already appears in the list, a.insert(x) will insert just before the leftmost x already there.

# Optional args lo (default 0) and hi (default len(a)) bound the slice of a to be searched.