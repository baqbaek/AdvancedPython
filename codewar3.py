def solution(number):
    # Initialize a variable to store the sum
    sum = 0
    # Check if the number is negative
    if number <= 0:
        return 0
    # Iterate through the numbers below the input number
    for i in range(1, number):
        # Check if the current number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Add the current number to the sum
            sum += i
    # Return the sum
    return sum
