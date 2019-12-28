# First attempt: reverse the program and find the combination of initial values
# that produce the output. Unfortunately, we of course end up with output like this:
# (+ (+ -2 (+ 4 (+ 2 (+ 1 (+ (+ 3 (* (+ 5 (+ (+ 2 (* (+ (+ 3 (* 5 (+ 2 (* (+ 2 
#   (+ (* 2 (* (* (+ (* (+ 1 (* 4 (+ (+ 1 (* (+ 2 (* 4 -1)) 2)) 3))) 4) 2) 2) 5
#     )) 1)) 3)))) 5) 4)) 5)) 4)) 4))))) 4)
#
# Which is a linear equation with two unknowns (-1 and -2 in this case) which
# of course can't be solved.
#
# import fileinput

# codes = [int(c) for c in fileinput.input()[0].split(',')]
# codes[1] = -1
# codes[2] = -2

# stop_pos = 0
# for pos in range(len(codes) - 1, 0, -1):
#   if codes[pos] == 99:
#     stop_pos = pos
#     break

# assert stop_pos, 'stop_pos not found'

# def value_of(idx, stop_pos):
#   for pos in range(stop_pos, 0, -4):
#     opcode, p1, p2, out = codes[pos-4:pos]
#     if out != idx:
#       continue

#     if opcode == 1:
#       return '(+ %s %s)' % (value_of(p1, pos-4), value_of(p2, pos-4))
#     elif opcode == 2:
#       return '(* %s %s)' % (value_of(p1, pos-4), value_of(p2, pos-4))
#   else:
#     return str(codes[idx])
  
# print(value_of(0, stop_pos))


# Second attempt, brute force guessing:
import fileinput

def process(codes):
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


codes = [int(c) for c in fileinput.input()[0].split(',')]
def attempt(tries):
  for noun in range(tries):
    for verb in range(tries):
      new_codes = codes[:]
      new_codes[1] = noun
      new_codes[2] = verb
      
      process(new_codes)
      if new_codes[0] == 19690720:
        return (noun, verb)
  else:
    assert False, 'Could not find answer'

noun, verb = attempt(100)
print(noun * 100 + verb)
