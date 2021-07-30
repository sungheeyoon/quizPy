from itertools import combinations
import sys
N,M = map(int,sys.stdin.readline().strip().split())
card_list=[int(i) for i in sys.stdin.readline().strip().split()[:N]]
card_combiantions = set([i for i in combinations(card_list,3)])
max =0

for i in card_combiantions:
    sum =0
    for unit in i:
        sum += unit
    if sum>=max and sum<=M:
        max=sum
print(max)