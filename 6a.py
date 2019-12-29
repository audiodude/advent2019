import fileinput

raw = []
for line in fileinput.input():
  raw.append(line.strip())

orbits = {}
for o in raw:
  value, key = o.split(')')
  orbits[key] = value

num = 0
seen = set()
for key, value in orbits.items():
  num += 1  
  while value != 'COM':
    key = value
    value = orbits[key]
    num += 1
    

print(num)
