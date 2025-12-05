#crc.py
data = 0b1011001
poly = 0b1101       # generator
deg = poly.bit_length() - 1

# Append zeros
msg = data << deg

# Perform division
work = msg
for i in range((msg.bit_length() - deg), -1, -1):
    if (work >> (i + deg)) & 1:   # if current top bit is 1
        work ^= poly << i

remainder = work  # will be less than 2**deg
print(f"Remainder (binary): {remainder:0{deg}b}")