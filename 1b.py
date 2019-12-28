import fileinput

def fuel_for(n):
  req = n // 3 - 2
  if req < 1:
    return 0
  else:
    return req + fuel_for(req)

result = 0
for line in fileinput.input():
  n = int(line.strip())
  result += fuel_for(n)

print(result)
