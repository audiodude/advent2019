import fileinput

codes = [int(c) for c in fileinput.input()[0].split(',')]
codes[1] = 12
codes[2] = 2

for pos in range(0, len(codes), 4):
  if codes[pos] == 99:
    break

  op1 = codes[codes[pos+1]]
  op2 = codes[codes[pos+2]]
  output_pos = codes[pos + 3]
  if codes[pos] == 1:
    codes[output_pos] =  op1 + op2
  elif codes[pos] == 2:
    codes[output_pos] = op1 * op2

print(codes[0])
