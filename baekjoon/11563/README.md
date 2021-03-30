연돌이와 고잠녀
============
|시간 제한|메모리 제한|
|:---:|:---:|
|7초|256MB|

## 문제
-------
연돌이와 고잠녀는 유치원 시절부터 친한 친구였다.</br>
하지만 한 순간의 잘못된 선택으로 인해 서로 만나기 힘들게 되었다.</br>
신촌에서 안암으로 갈 수 없기 때문이다.</br>
이를 딱하게 여긴 국토교통부 장관은 도로를 하나 놓아주기로 했다.</br>
하지만 재정상의 문제로 도로의 길이는 가능한 한 짧아야 한다.</br>

2차원 평면 위에 신촌에 연결된 직선도로들의 정보와 안암에 연결된 직선도로들의 정보가 주어진다.</br>
연돌이는 도로 위를 통해서만 이동할 수 있고, 두 도로가 만나는 지점에서 도로를 갈아탈 수 있다.</br>
신촌에서 안암으로 갈 수 있도록 새로 설치할 도로의 최소 길이를 알려주자.</br>

## 입력
-------
첫 줄에는 신촌에 연결된 도로의 개수 n과 안암에 연결된 도로의 개수 m(1 ≤ n, m ≤ 2,000)이 주어진다.</br>

이어지는 n줄에 걸쳐 xs, ys, xe, ye가 주어진다. (-10,000 ≤ xs, ys, xe, ye ≤ 10,000)</br>
이는 신촌에 연결된 도로의 양 끝점의 좌표가 (xs, ys), (xe, ye)임을 의미한다.</br>
이어지는 m줄에 걸쳐 xs, ys, xe, ye가 주어진다. (-50,000 ≤ xs, ys, xe, ye ≤ 50,000)</br>
이는 안암에 연결된 도로의 양 끝점의 좌표가 (xs, ys), (xe, ye)임을 의미한다.</br>
모든 좌표는 소수점 아래 최대 20자리까지 주어진다.</br>

신촌에 연결된 임의의 두 도로에 대해 한 도로에서 출발해서 다른 도로에 도착하는 것이 가능하고,</br>
안암에 연결된 임의의 두 도로에 대해서도 마찬가지이다.</br>
새로 도로를 놓기 전에는 신촌에 연결된 도로에서 출발해서 안암에 연결된 도로에 도착할 수 없다.</br>

## 출력
-------
신촌에서 안암으로 가기 위해 새로 놓아야 하는 최소 도로의 길이를 출력한다.</br>
실제 답과의 절대 혹은 상대오차가 1e-6 미만이면 정답으로 인정한다.</br>

## 예제 1
-------
### 입력
```
2 1
-1.0 0.0 1.0 0.0
-1.0 1.0 1.0 -1.0
2.0 1.0 5.0 8.0
```
### 출력
```
1.4142135623730951
```