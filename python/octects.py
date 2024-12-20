a = ['zero', 'one', 'two', 'three', 'four', 'five']
for i in range(len(a)):
    print(i, a[i])

octets = [128, 64, 32, 16, 8, 4, 2, 1]
# Convert the first four octets to a single hexadecimal string
hex_string = '{:02X}{:02X}{:02X}{:02X}'.format(*octets[:4])
print(f"Hexadecimal string: {hex_string}")

# Create a centered string with fill characters
centered_string = '{:*^30}'.format('KYLE')
print(f"Centered string with *: '{centered_string}'")

# Alignment examples
for align, text in zip('<^>', ['left', 'center', 'right']):
    aligned_string = '{0:{fill}{align}16}'.format(text, fill=align, align=align)
    print(f"Aligned ({align}): '{aligned_string}'")

