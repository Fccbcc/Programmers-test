## 풀이

def solution(order):
    answer = 0
    
    for i in str(order):
        if int(i)!=0 and int(i)%3==0:
            answer += 1
    return answer

# 해설
# 배수에서 주의해야하는 부분.. 0을 나누면 0이다

# 다른 해설

def solution(order):
    result = 0

    for i in range(3, 10, 3):
        result += str(order).count(str(i))

    return result
#369 게임에서 369만 쓰면 되는 것!
