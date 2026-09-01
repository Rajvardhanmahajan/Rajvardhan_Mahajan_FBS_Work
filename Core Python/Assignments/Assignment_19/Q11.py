# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.


def memoize(func):
    cache = {}                 # Store already calculated results

    def wrapper(n):
        if n in cache:         # Check if result is already available
            return cache[n]    # Return cached result

        result = func(n)       # Call original function
        cache[n] = result      # Store result in cache
        return result          # Return result

    return wrapper             # Return wrapper function


@memoize                       # Apply memoize decorator to square()
def square(n):
    print("Calculating...")    # Executes only for new input
    return n * n               # Calculate square


print(square(5))               # First call → calculation
print(square(5))               # Second call → cached result