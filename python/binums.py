def list_binary_numbers():
    binary_list = []
    for i in range(256):
        binary_number = bin(i)[2:].zfill(8)
        binary_list.append(binary_number)
    return binary_list

def print_binary_numbers_in_columns(binary_list, columns=8):
    for i in range(0, len(binary_list), columns):
        row = binary_list[i:i+columns]
        print(" | ".join(row))

binary_numbers = list_binary_numbers()

print_binary_numbers_in_columns(binary_numbers, columns=8)
print(f"\nTotal count: {len(binary_numbers)}")

#def list_binary_numbers():
#    binary_list = []
#    for i in range(256):
#        binary_number = bin(i)[2:].zfill(8)
#        binary_list.append(binary_number)
#    return binary_list
#
#def print_binary_numbers_in_columns(binary_list, columns=8, file=None):
#    for i in range(0, len(binary_list), columns):
#        row = binary_list[i:i+columns]
#        line = "  ".join(row)
#        if file:
#            file.write(line + "\n")  # Write to file
#        else:
#            print(line)  # Print to console
#
# Generate the list of binary numbers
#binary_numbers = list_binary_numbers()
#
# Save to a file
#output_filename = "binary_numbers_output.txt"
#with open(output_filename, "w") as file:
#    print_binary_numbers_in_columns(binary_numbers, columns=8, file=file)
#    file.write(f"\nTotal count: {len(binary_numbers)}")  # Write total count to file
#
#print(f"Output saved to {output_filename}")
