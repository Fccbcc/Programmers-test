## 풀이

def solution(my_string, num1, num2):
    str_list = list(my_string)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    return ''.join(str_list)
  
#list()로 리스트 생성하고 ''.join()로 다시 리스트를 문자열로 변환한다

# 다른 풀이

def solution(my_string, num1, num2):
    answer = ''
    a, b = my_string[num1], my_string[num2]
    
    for i in range(len(my_string)):
        if i == num1:
            answer += b
        elif i == num2:
            answer += a
        else: answer += my_string[i]
    return answer
