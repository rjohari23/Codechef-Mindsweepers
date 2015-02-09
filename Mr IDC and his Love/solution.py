"""created by : rjohari23"""

t = int(raw_input())
while t:
    n,mod = map(int,raw_input().split())
    k = n%mod
    print mod*(mod-1)/2 * (n/mod) + k*(k+1)/2
	t -= 1