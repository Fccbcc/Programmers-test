# 풀이

def solution(babbling):
    count = 0
    speak = [ "aya", "ye", "woo", "ma" ]
    for i in babbling:
        for j in speak:
            if j * 2 not in i:
                i = i.replace(j, ' ')
        if i.strip() == '':
            count += 1
    return count
  
  # 해설 
  # babbling과 입력갑(speak) 연속된 문자를 제외한 겹치는 문자를 for문으로 돌리며 지워나간다
