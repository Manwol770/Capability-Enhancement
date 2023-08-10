def reflection(n) :                             # 재귀 함수를 사용
    
    if n-1 >= len(memo) :                         # n 값이 1 또는 2면 반환값으로 1을 반환해줌
        memo.append(reflection(n-1) + reflection(n-2))
    return memo[n-1]                              # len이 다 채워주면 memo[n]을 출력

def dp (n) :                                    # dp 를 사용
    global dp_cnt                               # 횟수를 새주기 위해 글로벌 선언
    dp = [1,1]                                  # 초기값을 줌
    if n >= 2 :                                 # 인덱스 오류를 막기위해 n이 2 이상일때 선언
        for i in range (2,n) :                  # 시작 값을 2 이상으로 만듬
            dp_cnt += 1                         # dp를 한번 실행할때 마다 dp_cnt를 하나씩 올려줌
            dp.append(dp[i-1] + dp[i-2])        # dp 값 추가
    return None


N = int(input())                                # N 받아오기
dp_cnt = 0                                      # 글로벌 선언한 dp_cnt
dp(N)                                           # dp 실행
memo = [1,1]                                    # 메모이제이션 사용
print(reflection(N), dp_cnt)                    # 함수 실행 후 두 값 비교