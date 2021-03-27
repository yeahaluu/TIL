# Stack1

## 인접 행렬/ 인접 리스트

모델링한 그래프의 연결관계를 나타내기 위한 방법

<input>

7 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6

### 1. 인접 행렬

그래프의 연결 관계를 이차원 배열로 나타낸다.

```python
# V : 정점의 수
# E : 간선의 수
V, E = map(int, input().split())

# V * V 크기의 0으로 초기화된 2차원 리스트 선언.
adj_arr = [[0]*V for_in range(V)]

for i in range(E):
    A, B = map(int, input().split())
   
	adj_arr[A][B] = 1
    adj_arr[B][A] = 1  # 유향이면 생략
    
for i in adj_arr:
    print(*i)
```

<output>

0 1 1 0 0 0 0
1 0 0 1 1 0 0
1 0 0 0 1 0 0
0 1 0 0 0 1 0
0 1 1 0 0 1 0
0 0 0 1 1 0 1
0 0 0 0 0 1 0

- 무향 그래프의 경우, 대각성분을 기준으로 대칭



### 2. 인접 리스트

그래프의 연결 관계를 vector의 배열로 나타내는 방식

```python
# V : 정점의 수
# E : 간선의 수
V, E = map(int, input().split())

adj_lst = [[] for _ in range(V)]

for i in range(E):
    A, B = map(int, input().split())
    
    adj_lst[A].append(B)
    adj_lst[B].append(A)  # 유향이면 생략
    
for i in adj_lst:
    print(*i)
```

<output>

1 2 
0 3 4 
0 4
1 5
1 2 5
3 4 6
5



### 3. 장단점

#### 장점

인접행렬: 구현이 쉽다.

인접리스트: 실제로 연결된 노드들에 대한 정보만 저장해서, 모든 벡터들의 원소의 개수 합이 간선의 개수와 같다. 즉, _간선의 개수에 비례하는 메모리만 차지._

#### 단점

인접행렬: 연결된 모든 노드들에 방문해보고 싶은 경우 시간이 많이 걸린다

인접 리스트: i와 j가 연결되어 있는지 알고 싶을때 인접행렬의 경우 adj\[i][j] 로 보면 되지만 인접리스트 경우 다 봐야한다



## Stack



