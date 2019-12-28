import fileinput

codes = [int(c) for c in fileinput.input()[0].split(',')]

ptr = 0
while codes[ptr] != 99:
  code_str = str(codes[ptr])[::-1]

  opcode = int(code_str[0])
  modes = [-1]
  for m in code_str[2:]:
    modes.append(m)

  if opcode == 1 or opcode == 2:
    if len(modes) < 2 or modes[1] == '0':
      p1 = codes[codes[ptr+1]]
    else:
      p1 = codes[ptr+1]

    if len(modes) < 3 or modes[2] == '0':
      p2 = codes[codes[ptr+2]]
    else:
      p2 = codes[ptr+2]

    out_pos = codes[ptr + 3]
    adv = 4
  elif opcode == 3 or opcode == 4:
    if len(modes) < 2 or modes[1] == '0':
      out_pos = codes[ptr+1]
    else:
      out_pos = ptr+1
    adv = 2

  if opcode == 1:
    codes[out_pos] =  p1 + p2
  elif opcode == 2:
    codes[out_pos] = p1 * p2
  elif opcode == 3:
    in_value = input('Input for opcode 3 at position %s: ' % ptr)
    codes[out_pos] = int(in_value.strip())
  elif opcode == 4:
    out_value = codes[out_pos]
    print('Output for opcode 4 at position %s: %s' % (ptr, out_value))

  ptr += adv
