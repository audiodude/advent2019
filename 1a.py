import fileinput

result = 0
for line in fileinput.input():
  n = int(line.strip())
  result += n // 3 - 2

print(result)
