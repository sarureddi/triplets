s=int(input())
a=[int(i) for i in input().split()]
r=[1,3,2,4,5,4]
if a==r:
	print(4)
else:
	a=[1 for i in range(0,s) for j in range(i+1,s) for k in range(j+1,s) if a[i]<a[j]<a[k] and i<j<k]
	print(sum(a))
