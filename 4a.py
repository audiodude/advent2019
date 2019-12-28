from collections import defaultdict

def has_doubles(n):
  digits = defaultdict(list)
  for j, d in enumerate(str(n)):
    digits[d].append(j)

  for d, appearances in digits.items():
    for i, a in enumerate(appearances):
      if i == len(appearances) - 1:
        break

      if appearances[i+1] - appearances[i] == 1:
        return True

def always_increasing(n):
  string = str(n)
  for j, _ in enumerate(string):
    if j == len(string) - 1:
      break

    if int(string[j+1]) < int(string[j]):
      return False

  return True

def include(start, end):
  for i in range(start, end+1):
    if has_doubles(i) and always_increasing(i):
      yield i

print(len(list(include(402328, 864247))))
