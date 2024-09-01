#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        print([])  # No numbers to display
        return
    elif length == 1:
        print([0])  # Only the first Fibonacci number
        return

    # Initialize the list with the first two Fibonacci numbers
    fibonacci_list = [0, 1]

    # Generate the Fibonacci sequence until the list reaches the desired length
    for i in range(2, length):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    # Print the resulting Fibonacci sequence
    print(fibonacci_list)

# Example usage
print_fibonacci(9)  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
