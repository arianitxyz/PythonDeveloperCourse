# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'  # looks like a string -> it really is an array of bytes
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=', ')
print()

print(equation.decode('utf-8'))
