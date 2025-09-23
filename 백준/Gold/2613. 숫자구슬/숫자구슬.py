def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 0     # 최종 그룹합의 최대값
    group = []  # 각 그룹을 구성하는 구슬의 갯수
    start = max(nums)   # 그룹합의 하한
    end = sum(nums)     # 그룹합의 상한
    while start <= end:
        mid = (start + end) // 2    # 현재 그룹합의 최대값 기준

        group_cnt = 0   # 이번에 만들어진 그룹의 갯수

        idx = 0
        group = []
        while idx < N:
            sub_sum = 0     # 특정 그룹의 합
            sub_count = 0   # 특정 그룹을 구성하는 구슬의 갯수
            while idx < N and sub_sum + nums[idx] <= mid:   # 각 그룹의 합이 mid보다 작도록 구슬 넣기
                sub_sum += nums[idx]
                sub_count += 1
                idx += 1
                if M - group_cnt == N - (idx - 1):  # 남은 그룹의 갯수와 남은 구슬의 갯수가 같은 경우, 한 그룹에 하나의 구슬만 넣기 위해 break
                    break
            group_cnt += 1  # 만들어진 그룹 수 증가
            group.append(sub_count) # 각 그룹의 구슬 갯수 리스트에 추가

        if group_cnt <= M:  # 그룹이 M개보다 적거나 같은 경우, mid를 작게 만들어 더 잘게 쪼갤 수 있도록, 또는 최대값이 최소가 되도록 함
            end -= 1
        else:               # 그룹이 M개보다 큰 경우, mid를 키워 더 많은 구슬을 한 그룹에 담을 수 있도록 함
            start += 1
        ans = mid

    print(ans)
    print(*group)


if __name__ == "__main__":
    main()