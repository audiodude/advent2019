import fileinput

WIDTH = 25
HEIGHT = 6
LAYER_LEN = WIDTH * HEIGHT

for line in fileinput.input():
  pixels = line.strip()

layers = []
for i in range(len(pixels) // LAYER_LEN):
  layers.append(pixels[LAYER_LEN*i:LAYER_LEN*(i+1)])

for l in layers:
  assert len(l) == LAYER_LEN

def resolve(x, y):
  for l in layers:
    dominate = l[y * WIDTH + x]
    if dominate == '1' or dominate == '0':
      return dominate

image = [-1] * LAYER_LEN
for y in range(HEIGHT):
  for x in range(WIDTH):
    image[y * WIDTH + x] = resolve(x, y)

for y in range(HEIGHT):
  for x in range(WIDTH):
    print('□' if image[y * WIDTH + x] == '1' else '■', end='')
  print()
