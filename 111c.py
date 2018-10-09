from collections import Counter

def f(n,v):
	a=Counter(v[0::2]).most_common()
	b=Counter(v[1::2]).most_common()
	
	a.append([0,0])
	b.append([0,0])
	
	if a[0][0]!=b[0][0]:
		return n-(a[0][1]+b[0][1])
	else:
		return min(n-(a[1][1]+b[0][1]),n-(a[0][1]+b[1][1]))

if __name__=="__main__":
	x=int(input())
	data=[int(i) for i in input().split()]
	print(f(x,data))