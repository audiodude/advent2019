from collections import defaultdict
import fileinput

raw = []
for line in fileinput.input():
  raw.append(line.strip())

orbits = defaultdict(list)
for o in raw:
  obj1, obj2 = o.split(')')
  orbits[obj1].append(obj2)
  orbits[obj2].append(obj1)

unvisited = set(orbits.keys())
previous = dict((obj, None) for obj in orbits.keys())
distance = dict((obj, None) for obj in orbits.keys())
distance['YOU'] = 0

while len(unvisited) != 0:
  u = None
  min_dist = None
  for vertex in unvisited:
    if min_dist is None:
      if distance[vertex] is None:
        continue
      else:
        u = vertex
        min_dist = distance[vertex]
    else:
      if distance[vertex] is None:
        continue
      elif distance[vertex] < min_dist:
        u = vertex
        min_dist = distance[vertex]

  unvisited.remove(u)
  if u == 'SAN':
    break

  for v in orbits[u]:
    alt = distance[u] + 1  # Edge weights are always 1
    if distance[v] is None or alt < distance[v]:
      distance[v] = alt
      previous[v] = u

num = -1
next_obj = previous['SAN']
while next_obj != 'YOU':
  num += 1
  next_obj = previous[next_obj]

print(num)
