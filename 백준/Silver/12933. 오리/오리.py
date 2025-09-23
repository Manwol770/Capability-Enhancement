import sys
input = sys.stdin.readline

duck_list = [[] for _ in range(500)]
min_num = 0
sound = input().strip()
for i in sound:
  for j in range(500):
    if i == 'q' and not duck_list[j]:
      duck_list[j].append(i)
      break
    elif i == 'u' and len(duck_list[j]) == 1:
      duck_list[j].append(i)
      break
    elif i == 'a' and len(duck_list[j]) == 2:
      duck_list[j].append(i)
      break
    elif i == 'c' and len(duck_list[j]) == 3:
      duck_list[j].append(i)
      break
    elif i == 'k' and len(duck_list[j]) == 4:
      duck_list[j] = []
      min_num = max(min_num, j + 1)
      break
  else:
    min_num = -1
    break

for i in range(500):
  if duck_list[i]:
    min_num = -1
    break

print(min_num)