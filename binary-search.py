def binary_search(L,x):
	
	l=L.sort()
	left,right=0,len(l)-1
	while left<right:
		m=(left+right)//2
		if l[m]==x:
			return m
		if l[m]<x:
			right=m-1
		if l[m]>x:
			left=m+1
	return -1
L=[24,12,34,234,71,19,82,16,35,29,84,86,75,16,17,13]
position=binary_search(L,84)
print(position)