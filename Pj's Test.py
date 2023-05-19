def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1

    if count == 0:
        return 0

    average = total / count
    rounded_average = round(average, 2)
    
    return rounded_average


# Example usage
numbers_input = input("Enter a list of numbers separated by commas: ")
numbers_list = [float(num) for num in numbers_input.split(',')]

print(f"The average is: {calculate_average(numbers_list)}")
