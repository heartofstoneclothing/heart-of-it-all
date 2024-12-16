def list_hexadecimal_numbers():
    hex_list = []
    for i in range(256):
        hex_number = hex(i)[2:].upper()
        hex_list.append(hex_number.zfill(2))
    return hex_list

def print_hexadecimal_numbers_in_columns(hex_list, columns=16):
    for i in range(0, len(hex_list), columns):
        row = hex_list[i:i+columns]
        print("  ".join(row))

hexadecimal_numbers = list_hexadecimal_numbers()

print("\nHexadecimal Numbers:")
print_hexadecimal_numbers_in_columns(hexadecimal_numbers, columns=15)
print(f"\nTotal count: {len(hexadecimal_numbers)}")
