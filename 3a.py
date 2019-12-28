import fileinput

paths = fileinput.input()
a_path = paths[0].strip().split(',')
b_path = paths[1].strip().split(',')

def path_to_coords(path):
  cur = (0, 0)
  coords = set()
  coords.add(cur)
  for move in path:
    num = int(move[1:])
    if move[0] == 'U':
      for _ in range(num):
        cur = (cur[0], cur[1] + 1)
        coords.add(cur)
    elif move[0] == 'D':
      for _ in range(num):
        cur = (cur[0], cur[1] - 1)
        coords.add(cur)
    elif move[0] == 'L':
      for _ in range(num):
        cur = (cur[0] - 1, cur[1])
        coords.add(cur)
    elif move[0] == 'R':
      for _ in range(num):
        cur = (cur[0] + 1, cur[1])
        coords.add(cur)

  return coords

a_coords = path_to_coords(a_path)
b_coords = path_to_coords(b_path)
intersections = a_coords & b_coords
intersections.remove((0,0))

sorted_intersections = sorted(
  intersections, key=lambda item: abs(item[0]) + abs(item[1]))
print(abs(sorted_intersections[0][0]) + abs(sorted_intersections[0][1]))
