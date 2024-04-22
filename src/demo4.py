# Poorly written Python code

import random

def generate_random_numbers(n):
    """
    Generate a list of n random numbers.
    """
    numbers = []
    for i in range(n):
        numbers.append(random.random())
    return numbers

def compute_average(numbers):
    """
    Compute the average of a list of numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    """
    Main function to demonstrate the functionality.
    """
    num_count = input("Enter the number of random numbers to generate: ")
    try:
        num_count = int(num_count)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if num_count <= 0:
        print("Number of numbers to generate must be greater than zero.")
        return

    random_numbers = generate_random_numbers(num_count)
    print("Generated random numbers:", random_numbers)

    avg = compute_average(random_numbers)
    print("Average of the generated numbers:", avg)

if __name__ == "__main__":
    main()
