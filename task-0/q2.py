def process_list(numbers):
    # 1. Create a copy of the input list
    copied_list = numbers.copy()

    # 2. Remove all negative numbers
    copied_list = [x for x in copied_list if x >= 0]

    # 3. Append 0 to the list
    copied_list.append(0)

    # 4. Sort the list in ascending order
    copied_list.sort()

    # 5. Return the modified list
    return copied_list


# usage example
original = [5, -2, 8, -1, 3]
result = process_list(original)
print("Original:", original)
print("Result:", result)
