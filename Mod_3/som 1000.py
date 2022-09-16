total = 0
for i in range(1000):
  total += i + 50
  print(f'{i + 1} {total}')
  if total > 1000:
      break