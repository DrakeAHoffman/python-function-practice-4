#Question 1

def max_num(num1, num2, num3):
    return max(num1, num2, num3)

# Example usage:
result = max_num(5, 12, 8)
print("The maximum number is:", result)

#Question 2

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers_list = [2, 3, 4, 5]
result = mult_list(numbers_list)
print("The product of the numbers in the list is:", result)


#Question 3

def rev_string(input_string):
    return input_string[::-1]

# Example usage:
original_string = "Hello, World!"
reversed_string = rev_string(original_string)
print("Original String:", original_string)
print("Reversed String:", reversed_string)

#Question 4

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

# Examples:
result1 = num_within(3, 2, 4)
result2 = num_within(3, 1, 3)
result3 = num_within(10, 2, 5)

print(result1)  # Output: True
print(result2)  # Output: True
print(result3)  # Output: False

#Question 5

def pascal(n):
    for i in range(n):
        # Use a list to store the values in the current row
        row_values = []
        # Calculate the values in the current row
        for j in range(i + 1):
            if j == 0 or j == i:
                value = 1
            else:
                value = row_values[j - 1] * (i - j + 1) // j
            row_values.append(value)
        # Print the values in the current row
        print(" ".join(map(str, row_values)).center(n * 3))

# Example usage:
num_rows = 5
pascal(num_rows)

