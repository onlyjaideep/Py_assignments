# Demonstrate List Slicing
#Creates a list of numbers from 1 to 10.
original_list = list(range(1, 11))

extracted_list = original_list[:5] 

reversed_list = extracted_list[::-1]

# 4. Prints both the extracted list and the reversed list.
print(f"Original List (1-10): {original_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")