from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

#  HALF ADDER
def half_adder(a, b):
  s = XOR_gate(a,b)
  c = AND_gate(a,b)
  return (s, c)

# FULL ADDER
def full_adder(a,b,c):
  h1 = half_adder(a,b)
  h2 = half_adder(h1[0], c)
  s = h2[0]
  c_out = OR_gate(h2[1], h1[1])
  return (s, c_out)

# ARITHMETIC LOGIC UNIT
def ALU(a,b,c,opcode):
  if opcode == 0:
    return half_adder(a,b)
  elif opcode == 1:
    return full_adder(a,b,c)

print(ALU(0,0,1,1))

