import sys 
import heapq 
input = sys.stdin.readline 
INF = sys.maxsize 
V, E = map(int, input().split()) 

K = int(input()) 

dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    #����ġ ���̺��� ���� ������ �ش��ϴ� ����ġ�� 0���� �ʱ�ȭ
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    #���� ���Ұ� ���� �� ���� �ݺ�.
    while heap:
        wei, now = heapq.heappop(heap)

        #���� ���̺�� ���Ͽ� ���ʿ���(�� ����ġ�� ū) Ʃ���̸� ����.
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            #���� ���� ������ ����ġ wei + ���� �������� ���� ����(next_node)������ ����ġ W
            # = ���� �������� ����ġ(next_wei)
            next_wei = w + wei
            #���� �������� ����ġ(next_wei)�� ���� ��ϵ� �� ���� ������ ���� ����.
            if next_wei < dp[next_node]:
                #����ߴ� next_wei�� ����ġ ���̺� ������Ʈ.
                dp[next_node] = next_wei
                #���� �� ������ ����ġ�� ���� ���� ���� ������ Ʃ�÷� ���� �ּ� ���� ����.
                heapq.heappush(heap,(next_wei,next_node))

#�ʱ�ȭ
for _ in range(E):
    u, v, w = map(int, input().split())
    #(����ġ, ������ ���) ���·� ����
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])
