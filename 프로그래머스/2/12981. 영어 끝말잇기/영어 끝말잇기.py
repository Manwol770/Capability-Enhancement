def solution(n, words):
    answer = [0, 0]

    people = 0
    remember_word = [words[0]]
    order = 0
    lenth = len(words)
    
    for i in range(1, lenth):
        people += 1
        if not people % n :
            people = 0
            order += 1
        if words[i] in remember_word :
            answer = [people + 1, order + 1]
            break
        elif words[i-1][-1] != words[i][0]:
            answer = [people + 1, order + 1]
            break
        else:
            remember_word.append(words[i])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)
    print(remember_word)

    return answer