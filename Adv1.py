#PWP/Dec 18, 2023/Advent of Code 1
import re

file_path = 'C:\\Users\\pwpat\\OneDrive\\Documents\\GitHub\\adventofcode23\\adv1_text.txt'
total_sum = 0

def extract_and_sum_calibration_values(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_count = 0
            for line in lines:
                line = line.strip()  # Remove leading/trailing whitespace
                first_digit = None
                last_digit = None

                for char in line:
                    if char.isdigit():
                        if first_digit is None:
                            first_digit = int(char)
                        last_digit = int(char)

                if first_digit is not None and last_digit is not None:
                    two_digit_number = first_digit * 10 + last_digit
                    total_count += two_digit_number

            return total_count
    except FileNotFoundError:
        return None

def calculate_calibration_value(file_path):
    total_sum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            # Initialize variables to store the first and last digits
            first_digit = None
            last_digit = None
            
            # Iterate through characters in the line
            for char in line:
                # Check if the character is a digit (0-9) or a spelled-out digit word
                if char.isdigit():
                    digit = int(char)
                    if first_digit is None:
                        first_digit = digit
                    last_digit = digit
                elif char.isalpha():
                    # Define a dictionary to map spelled-out digit words to their numerical values
                    word_to_digit = {
                        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
                    }
                    
                    # Check if the character is part of a spelled-out digit word
                    word_buffer = char
                    while word_buffer in word_to_digit:
                        digit = word_to_digit[word_buffer]
                        if first_digit is None:
                            first_digit = digit
                        last_digit = digit
                        # Continue reading characters to complete the word
                        word_buffer += line[len(word_buffer)]
            
            # If both first_digit and last_digit were found, calculate and add to the total_sum
            if first_digit is not None and last_digit is not None:
                combined_value = first_digit * 10 + last_digit
                total_sum += combined_value
    
    return total_sum

# Call the function to calculate the sum of all calibration values
#result = extract_and_sum_calibration_values(file_path)
total_count = calculate_calibration_value(file_path)
print( "the sum of the calibration value:  ", total_count)
