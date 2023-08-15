import sys
input = sys.stdin.readline

k = list()
N, M = map(int, input().split())
D = set()
S = set()
for i in range (N) :
    D.add(input().rstrip())

for i in range (M) :
    S.add(input().rstrip())

D_S = sorted(list(D & S))
print(len(D_S))
for i in D_S :
    print(i)