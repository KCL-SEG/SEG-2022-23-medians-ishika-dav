"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def order_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    return numbers

def find_median(numbers):
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length//2] + numbers[(length//2) - 1]) / 2
    else:
        median = numbers[length//2]
    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = order_numbers(numbers)
        median = find_median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
