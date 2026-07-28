# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(num):
    """Generates a multiplication table for a single number from 1 to 12."""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        # Using f-strings to match the expected spacing format
        print(f"  {num}  x  {i:<2} =  {num * i}")

def print_multiple_tables(n):
    """Generates multiplication tables for every number from 1 to N."""
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        
        if current_num < n:
            print("  ---------------------------")

def main():
    print("--- PART A: Single Table ---")
    try:
        user_num = int(input("Enter a number for the multiplication table: "))
        if user_num <= 0:
            print("Error: Please enter a positive integer.")
            return
        print_single_table(user_num)
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
        return

    print("\n--- PART B: Tables from 1 to N ---")
    try:
        n_val = int(input("Enter a number N for tables 1 through N: "))
        if n_val <= 0:
            print("Error: Please enter a positive integer.")
            return
        print_multiple_tables(n_val)
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()