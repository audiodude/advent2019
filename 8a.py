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

def num_digit(l, digit_str):
  num = 0
  for d in l:
    if d == digit_str:
      num += 1
  return num

zeros_per_layer = []
for l in layers:
  zeros_per_layer.append(num_digit(l, '0'))

idx = 0
min_ = zeros_per_layer[idx]
for i, z in enumerate(zeros_per_layer):
  if z < min_:
    min_ = z
    idx = i

print(num_digit(layers[idx], '1') * num_digit(layers[idx], '2'))


