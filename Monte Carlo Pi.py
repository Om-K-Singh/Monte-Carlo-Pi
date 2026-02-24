import numpy as np
from math import pi

within_quadrant = 0
batch_size = 100_000_000                                        # Adjust based on system RAM for performance. 100,000,000 used approx. 4.5 GB
iterations = int(input("Enter number of iterations to run: "))  # Number of random points to calculate pi with
remaining = iterations

while remaining > 0:

    current_batch = min(batch_size, remaining)                          # Batching to manage RAM usage. Using 2D array has better performance at the cost of higher RAM consumption
    points = np.random.uniform(0, 1, (current_batch, 2))                # Generate 2 random floats between 0 and 1, giving us X and Y coords for points in the space
    within_quadrant += np.sum(points[:,0] ** 2 + points[:,1]**2 <= 1)   # If X and Y squared is less than or equal to 1, it is within the quadrant. Using a unit circle simplifies logic
    remaining -= current_batch                                          # Remaining number of points to be used is reduced by the number of points in the current batch
    
#   print(remaining)                                                      Used as progress indicator with very large iteration numbers (>1,000,000,000)

MC_pi_approximate = 4 * (within_quadrant / iterations)                  # Value of pi is approximated by how many points would have fallen into the full circle compared to the total number of points used.

print(f"\nMonte Carlo Method calculation of pi = {MC_pi_approximate}")
print(f"Accuracy: {((MC_pi_approximate / pi) * 100):.2f}% over {iterations} iterations.")
# print(f"Verbose accuracy = {(MC_pi_approximate/pi)*100}%)")