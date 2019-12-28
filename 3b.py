from collections import defaultdict
import fileinput

paths = fileinput.input()
a_path = paths[0].strip().split(',')
b_path = paths[1].strip().split(',')

def path_to_coords(path):
  cur = (0, 0)
  coords = defaultdict(list)
  coords[cur].append(cur)
  total_steps = 0
  for move in path:
    num = int(move[1:])
    if move[0] == 'U':
      for _ in range(num):
        cur = (cur[0], cur[1] + 1)
        total_steps += 1
        coords[cur].append(total_steps)
    elif move[0] == 'D':
      for _ in range(num):
        cur = (cur[0], cur[1] - 1)
        total_steps += 1
        coords[cur].append(total_steps)
    elif move[0] == 'L':
      for _ in range(num):
        cur = (cur[0] - 1, cur[1])
        total_steps += 1
        coords[cur].append(total_steps)
    elif move[0] == 'R':
      for _ in range(num):
        cur = (cur[0] + 1, cur[1])
        total_steps += 1
        coords[cur].append(total_steps)

  return coords

a_coords = path_to_coords(a_path)
b_coords = path_to_coords(b_path)
intersections = set(a_coords.keys()) & set(b_coords.keys())
intersections.remove((0,0))

a_steps = dict((inter, steps[0]) for inter, steps in a_coords.items()
           if inter in intersections)
b_steps = dict((inter, steps[0]) for inter, steps in b_coords.items()
           if inter in intersections)

total_steps = [a_steps[inter] + b_steps[inter] for inter in intersections]
print(min(total_steps))
