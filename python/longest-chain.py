def collatz_sequence_length(n, memo):
    original_n = n
    length = 1  # Count the starting number
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n < original_n:
            length += memo[n]
            break
        length += 1
    memo[original_n] = length
    return length

def longest_collatz_chain(limit):
    max_length = 0
    starting_number = 0
    memo = {1: 1}  # Memoization to avoid recomputing sequences

    for i in range(2, limit):
        length = collatz_sequence_length(i, memo)
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number, max_length

# Run the function for numbers under 1 million
starting_number, max_length = longest_collatz_chain(1000000)

print(f"The starting number under 1 million that produces the longest chain is {starting_number}")
print(f"The length of the chain is {max_length}")
