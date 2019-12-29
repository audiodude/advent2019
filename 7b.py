import fileinput
from itertools import permutations

class IntCodeComputer:
  def __init__(self, codes, phase):
    self.codes = codes
    self.phase = phase
    self.inputs = [phase]
    self.ptr = 0
    self.halted = False

  def get_output(self, input_):
    self.inputs.append(input_)
    return self.compute()

  def compute(self):
    if self.halted:
      return None

    while self.codes[self.ptr] != 99:
      code_str = str(self.codes[self.ptr])[::-1]

      opcode = int(code_str[0])
      modes = [-1]
      for m in code_str[2:]:
        modes.append(m)

      if opcode in (1,2,5,6,7,8):
        if len(modes) < 2 or modes[1] == '0':
          p1 = self.codes[self.codes[self.ptr+1]]
        else:
          p1 = self.codes[self.ptr+1]

        if len(modes) < 3 or modes[2] == '0':
          p2 = self.codes[self.codes[self.ptr+2]]
        else:
          p2 = self.codes[self.ptr+2]

        out_pos = self.codes[self.ptr + 3]
        adv = 4
      elif opcode == 3 or opcode == 4:
        if len(modes) < 2 or modes[1] == '0':
          out_pos = self.codes[self.ptr+1]
        else:
          out_pos = self.ptr+1
        adv = 2

      if opcode == 1:
        self.codes[out_pos] =  p1 + p2
      elif opcode == 2:
        self.codes[out_pos] = p1 * p2
      elif opcode == 3:
        self.codes[out_pos] = self.inputs.pop(0)
      elif opcode == 4:
        out_value = self.codes[out_pos]
        self.ptr += adv
        return out_value
      elif opcode == 5:
          adv = p2 - self.ptr if p1 != 0 else 3
      elif opcode == 6:
          adv = p2 - self.ptr if p1 == 0 else 3
      elif opcode == 7:
        self.codes[out_pos] = 1 if p1 < p2 else 0
      elif opcode == 8:
        self.codes[out_pos] = 1 if p1 == p2 else 0

      self.ptr += adv

    self.halted = True

  def __repr__(self):
    return '%s|%r' % (self.phase, self.inputs)


init_codes = [int(c) for c in fileinput.input()[0].strip().split(',')]
guesses = (5, 6, 7, 8, 9)

max_ = -1
for guess in permutations(guesses):
  amplifiers = []
  for i in range(5):
    amplifiers.append(IntCodeComputer(init_codes[:], guess[i]))

  next_value = 0
  idx = 0
  while True:
    prev_value = next_value
    next_value = amplifiers[idx].get_output(next_value)
    if next_value is None:
      break
    idx += 1
    if idx == len(amplifiers):
      idx = 0

  if prev_value > max_:
    max_ = prev_value

print(max_)
