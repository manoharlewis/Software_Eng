import math


#Fermat's Last Theorem Near Miss Finder
#File Name : Assignment-2
#Course and Section Number : FA24-CPSC-60500-2
#COMPLETION DATE : 09/08/2024
"""This program searches for "near misses" to Fermat's Last Theorem by checking 
if x^n + y^n comes close to any z^n values for given integers x, y, z, and n. 
The user provides the power n and the upper limit k for x and y. 
The program calculates the relative miss between x^n + y^n and the closest z^n or (z+1)^n. 
It tracks and prints the smallest miss found, along with the corresponding values of x, y, and z. 
The goal is to identify cases where x^n + y^n almost equals z^n for powers greater than 2.
"""


def find_near_misses(n, k):
    """This function searches for near misses of Fermat's Last Theorem."""
    # Variables to store the smallest miss found
    smallest_miss = float('inf')
    best_x, best_y, best_z = None, None, None
    best_miss_value, best_relative_miss = None, None

    # Iterate over all combinations of x and y
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Calculate x^n + y^n
            lhs = x ** n + y ** n

            # Find the closest z such that z^n is close to x^n + y^n
            z = int(lhs ** (1 / n))  # Closest integer z where z^n <= lhs

            # Calculate z^n and (z+1)^n
            z_n = z ** n
            z_plus_1_n = (z + 1) ** n

            # Determine which of z^n or (z+1)^n is closer to x^n + y^n
            miss1 = abs(lhs - z_n)
            miss2 = abs(z_plus_1_n - lhs)

            # Find the smaller miss
            actual_miss = min(miss1, miss2)
            relative_miss = actual_miss / lhs  # Relative size of the miss

            # If this is the smallest miss so far, store the values
            if relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_x, best_y, best_z = x, y, z
                best_miss_value = actual_miss
                best_relative_miss = relative_miss

                # Print out the current smallest miss
                print(f"New smallest miss found:")
                print(f"x = {x}, y = {y}, z = {z}")
                print(f"Actual miss: {actual_miss}")
                print(f"Relative miss: {relative_miss:.10f}")
                print("-" * 50)

    # After the loop ends, print out the best miss found
    print(f"Smallest near miss:")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}")
    print(f"Actual miss: {best_miss_value}")
    print(f"Relative miss: {best_relative_miss:.10f}")


# Main part of the program
if __name__ == "__main__":
    print("Welcome to Fermat's Last Theorem Near Miss Finder!")

    # Get user inputs for n and k
    n = int(input("Enter the power n (3 <= n < 12): "))
    k = int(input("Enter the upper limit k (k > 10): "))

    # Ensure the inputs are valid
    if n < 3 or n >= 12:
        print("n must be between 3 and 11.")
    elif k <= 10:
        print("k must be greater than 10.")
    else:
        # Call the function to find near misses
        find_near_misses(n, k)

    # Pause the program to let the user review the results
    input("Press Enter to exit...")
