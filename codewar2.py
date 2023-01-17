def is_isogram(string):
    # Convert the string to lowercase
    string = string.lower()
    # Check if the length of the string is equal to the length of its unique characters
    return len(string) == len(set(string))

def unique_in_order(iterable):
    # Initialize an empty list to store the result
    result = []
    # Check if iterable is not empty
    if iterable:
        # Initialize the first element as prev
        prev = iterable[0]
        # Append the first element to the result list
        result.append(prev)
        # Iterate over the rest of the elements
        for i in iterable[1:]:
            # Check if the current element is different than the previous one
            if i != prev:
                # Append the current element to the result list
                result.append(i)
                # Assign the current element as the previous one
                prev = i
    # Return the final result list
    return result

def xo(s):
    # Initialize the counts of 'x' and 'o'
    x = 0
    o = 0
    # Iterate over each char in the string and convert it to lowercase
    for i in s.lower():
        # Increment the count of 'x' if the char is 'x'
        if i == 'x':
            x += 1
        # Increment the count of 'o' if the char is 'o'
        elif i == 'o':
            o += 1
    # Check if the number of 'x's and 'o's are equal
    if x == o:
        return True
    else:
        return False

def get_middle(s):
    # Get the middle index of the string
    middle = len(s) // 2
    # Check if the string length is even or odd
    if len(s) % 2 == 0:
        # Return the two middle characters of an even-length string
        return s[middle - 1: middle + 1]
    else:
        # Return the middle character of an odd-length string
        return s[middle]

def find_short(s):
    # Split the string into a list of words
    words = s.split()
    # Initialize the minimum length to the length of the first word
    min_length = len(words[0])
    # Iterate through the list of words
    for word in words:
        # Check if the current word's length is less than the minimum length
        if len(word) < min_length:
            # Update the minimum length
            min_length = len(word)
    # Return the minimum length
    return min_length

