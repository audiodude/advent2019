import fileinput
from itertools import permutations

class IntCodeComputer:
  def __init__(self, codes, inputs):
    self.codes = codes
    self.inputs = inputs
    self.input_idx = 0
    self.outputs = []

  def compute(self):
    ptr = 0
    while self.codes[ptr] != 99:
      code_str = str(self.codes[ptr])[::-1]

      opcode = int(code_str[0])
      modes = [-1]
      for m in code_str[2:]:
        modes.append(m)

      if opcode in (1,2,5,6,7,8):
        if len(modes) < 2 or modes[1] == '0':
          p1 = self.codes[self.codes[ptr+1]]
        else:
          p1 = self.codes[ptr+1]

        if len(modes) < 3 or modes[2] == '0':
          p2 = self.codes[self.codes[ptr+2]]
        else:
          p2 = self.codes[ptr+2]

        out_pos = self.codes[ptr + 3]
        adv = 4
      elif opcode == 3 or opcode == 4:
        if len(modes) < 2 or modes[1] == '0':
          out_pos = self.codes[ptr+1]
        else:
          out_pos = ptr+1
        adv = 2

      if opcode == 1:
        self.codes[out_pos] =  p1 + p2
      elif opcode == 2:
        self.codes[out_pos] = p1 * p2
      elif opcode == 3:
        self.codes[out_pos] = self.inputs[self.input_idx]
        self.input_idx += 1
      elif opcode == 4:
        out_value = self.codes[out_pos]
        self.outputs.append(out_value)
      elif opcode == 5:
          adv = p2 - ptr if p1 != 0 else 3
      elif opcode == 6:
          adv = p2 - ptr if p1 == 0 else 3
      elif opcode == 7:
        self.codes[out_pos] = 1 if p1 < p2 else 0
      elif opcode == 8:
        self.codes[out_pos] = 1 if p1 == p2 else 0

      ptr += adv


init_codes = [int(c) for c in fileinput.input()[0].strip().split(',')]
guesses = (0, 1, 2, 3, 4)

max_ = -1
for guess in permutations(guesses):
  last = None
  for i in range(5):
    last = IntCodeComputer(
      init_codes[:], (guess[i], 0 if last is None else last.outputs[0]))
    last.compute()

  if last.outputs[0] > max_:
    max_ = last.outputs[0]

print(max_)
