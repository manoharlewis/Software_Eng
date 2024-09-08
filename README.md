COde Works on 
The program first gets user input for n and k. It ensures that n is between 3 and 11 and that k is greater than 10.
It then iterates over all possible values of x and y within the range [10, k] and calculates x^n + y^n.
It finds the closest integer z such that z^n and (z+1)^n bracket x^n + y^n, and computes the miss as the smallest difference between x^n + y^n and these values
The program tracks the smallest relative miss and prints the details of each new smallest miss.
Finally, it prints the smallest miss after all combinations have been checked.

