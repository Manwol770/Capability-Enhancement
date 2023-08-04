import sys
case = int(sys.stdin.readline())
for _ in range(case):

    n, m = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    index = [i for i in range(n)]
    count = 0
    
    while True:

        if priority[0] == max(priority):
            count += 1

            if index[0] == m:
                print(count)
                break

            else:
                del priority[0]
                del index[0]

        else:
            priority.append(priority[0])
            del priority[0]
            index.append(index[0])
            del index[0]