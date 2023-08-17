n = int(input())
arr = [x+1 for x in range(n)]

queue = []

while len(arr) != 1:
    card1 = arr.pop(0)
    queue.append(card1)

    card2 = arr.pop(0)
    arr.append(card2)

queue.append(arr.pop())
for i in queue :
    print(i, end = ' ')