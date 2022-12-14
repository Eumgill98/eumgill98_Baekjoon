from collections import deque

#BFS 함수 정의
def bfs(graph, start, visited):
    #큐 구현을 위해서 deque 라이브러리 이용
    queue = deque([start])
    #현재 노드 망문 저리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐 에서 한의 원소를 뽑아서  출력

        v = queue.popleft()
        print(queue)
        #print(v, end=' ')
        #해당 원소와 연결된 , 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)