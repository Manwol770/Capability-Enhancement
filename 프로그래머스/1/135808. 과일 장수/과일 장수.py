def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    
    l = len(score)
    for i in range(m-1, l, m):
        answer += score[i] * m
    return answer