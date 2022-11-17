## 풀이

def solution(numbers, direction):
    answer = []

    if direction == 'right' :
        answer.append(numbers[-1])

        for i in numbers[0:-1] :
            answer.append(i)
    else :
        for i in numbers[1:] :
            answer.append(i)

        answer.append(numbers[0])

    return answer
# 리스트 인덱싱에 대해서 잘 알고 있어야 한다.
  
  
# 다른 풀이

def solution(numbers, direction):
    from collections import deque
    numbers_deque = deque(numbers)
    if direction == "right":
        numbers_deque.rotate(1)
    elif direction == "left":
        numbers_deque.rotate(-1)
    return list(numbers_deque)

#deque.rotate(양수의 숫자) 이면 시계방향으로 숫자만큼 돈다. 즉, 오른쪽으로 숫자만큼 회전한다.
#deque.rotate(음수의 숫자) 이면 반시계방향으로 숫자만큼 돈다. 즉, 왼쪽으로 숫자만큼 회전한다.

