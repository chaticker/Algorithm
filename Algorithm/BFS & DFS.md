그래프 탐색
그래프의 기본 개념

그래프의 각 정점을 방문하는 것을 탐색이라고 한다.

BFS (너비 우선 탐색)
개념
너비 우선 탐색(Breath First Search)이란 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 고려하여 방문하는 알고리즘이다. 쉽게 말하면 거리가 가까운 노드부터 탐색하는 알고리즘. 

그래프의 표현방법에 따라 구현하는 방법이 다르다. 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph)의 경우 인접 행렬보다 인접 리스트를 사용하는 것이 유리하다. 





특징
어떤 노드를 방문했었는지 여부를 반드시 검사해야한다.
자료구조 큐(Queue)를 이용해 선입선출 원칙으로 탐색한다.
재귀를 사용하지 않는다.
노드 사이의 최단 경로, 임의의 경로를 찾을 때 사용한다.
관련 : Prim,  Dijkstra

구현
인접 리스트
방법
변수 설정
graph 는 각 정점과 인접한 정점들을 dictionary 형태로 기록한다.
셋으로 한 이유: 중복 안되게 하려는 목적. 리스트로 구현이 안함! 
ex) graph = {1: {2, 3}, 2: {1, 5}, 3: {1, 4}, 4: {3, 5}, 5: {2, 4}}
길은 다른말로 ‘탐색을 아직 하지 않은 정점’으로, 탐색을 마친 후에는 해당 정점의 값을 0으로 변경해준다.

visited 는 각 지점까지 경로의 길이를 저장한다.

queue 에는 탐색이 남은 노드들을 저장한다. 처음엔 시작 정점의 위치를 저장하고, 해당 정점을 탐색할 땐 queue에서 뺀 다음, 인접한 정점들의 위치를 탐색한다.
과정
1. 큐에서 정점 하나를 꺼낸다.
2. 해당 정점과 인접한 정점들을 탐색한다.
3. 탐색하려는 정점이 아직 탐색되지 않았다면, 해당 정점까지의 방문여부를 기록한다. 해당 정점을 queue에 넣어준다.
5. 다음 루프로 돌아간다.

###팀노트
```python
graph, visited는 함수 밖에 생성한다. n은 정점의 개수

from collections import deque 

graph = {1: {2, 3}, 2: {1, 5}, 3: {1, 4}, 4: {3, 5}, 5: {2, 4}}
visited = [False] * (n+1)

def bfs(graph, start, visited): 
    queue = deque([start]) 
    visited[start] = True 
    while queue: 
        v = queue.popleft() 
        for i in graph[v]: 
            if not visited[i]: 
                queue.append(i) 
                visited[i] = True
```
코드 (백준 1260)
```python
import sys

from collections import defaultdict
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # i : v와 인접한 정점들을 하나씩 꺼낸다.
        for i in sorted(graph[v]): # graph[v]를 정렬해줘야한다. 
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n,m,v = map(int, sys.stdin.readline().split())

graph = defaultdict(set)
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].add(n2)
    graph[n2].add(n1)


visited = [False] * (n+1)
bfs(graph, v, visited)
```

시간복잡도
V는 접점, E는 간선의 수일 때, O(V + E)
인접 행렬
방법
변수 설정
graph 는 각 정점과 인접한 정점들을 N * N 배열로 기록한다.
visited 는 각 정점의 방문 여부를 저장한다.
queue 에는 탐색이 남은 정점들을 저장한다. 

과정
1. 큐에서 정점 하나를 꺼낸다.
2. 다른 모든 정점들을 탐색한다.
3. 탐색되지 않았고, 꺼낸 정점과 인접해있다면 인접한 정점의 방문여부를 체크한다. 해당 정점을 queue에 넣어준다.
5. 다음 루프로 돌아간다.

###팀노트
```python
from collections import deque


graph = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
visited = [0 for i in range(n+1)]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = 1
```
```python
코드 (백준 1260)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = 1
                
n,m,v = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1 
    graph[y][x] = 1

bfs(graph, v, visited)

```

시간복잡도
O(V^2) V는 정점의 개수

N*M 배열
방법
변수설정
graph 는 길 또는 벽으로 입력받는다. 
ex. graph = [[1,1,0,1],[0,1,1,1]] 
길은 다른말로 ‘탐색을 아직 하지 않은 정점’으로, 탐색을 마친 후에는 해당 정점의 값을 0으로 변경해준다.

visited 는 각 지점까지 경로의 길이를 저장한다.
    ex. visited = [[1,2,0,6],[0,3,4,5]]

queue 에는 탐색이 남은 노드들을 저장한다. 처음엔 시작 정점의 위치를 저장하고, 해당 정점을 탐색할 땐 queue에서 뺀 다음, 인접한 정점들의 위치를 탐색한다.

인접한 정점의 위치를 탐색하기 위해 dx, dy를 이용한다. 

과정
1. 큐에서 정점 하나를 꺼낸다.
2. 해당 정점을 기준으로 상하좌우를 탐색한다.
3. 탐색하려는 정점이 지정된 영역 밖이라면 넘어간다.
4. 탐색하려는 정점이 아직 탐색되지 않았다면, 해당 정점까지의 경로의 길이를 기록하고 해당 정점을 탐색했다고 체크한다. 해당 정점을 queue에 넣어준다.
5. 다음 루프로 돌아간다.


###팀노트
```python

#graph, visited는 함수 밖에 생성하고 입력인자로 넣어준다. 추가로 시작 위치의 좌표를 입력한다. n은 세로, m은 가로 

from collections import deque


graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(graph, start, visited):
    # graph의 시작 정점을 이미 탐색한 정점으로 설정
    graph[start[0]][start[[1]] = 0
    # visited의 시작 정점은 1 (경로의 길이 + 1)
    visited[start[0]][start[1]] = 1

    queue = deque()
    queue.append([start[0],start[[1]])



    # 네 방향으로 정의(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x,y = queue.popleft()
        # length는 시작 위치에서부터 경로의 길이 + 1
        length = visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위에서 벗어난 경우, 다음 방향
            if nx < 0 or ny < 0 or nx >= n or ny >= m: 
                continue
            # 길이 있는 경우
            if graph[nx][ny]:
                # 해당 위치까지 경로의 길이 기록
                visited[nx][ny] = length + 1
                # queue에 해당 위치 저장
                queue.append([nx,ny])
                # 지나간 지점은 0으로 표시
                graph[nx][ny] = 0

    return visited
    
```
