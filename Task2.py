#Creates a list of numbers from 1 to 10.
#Extracts the first five elements from the list.
#Reverses these extracted elements.
#Prints both the extracted list and the reversed list
#Creates a list of numbers from 1 to 10
numbers = list(range(1, 11))
#Extracts the first five elements from the list
extracted_numbers = numbers[:5]
#Reverses these extracted elements
reversed_numbers = extracted_numbers[::-1]
#Prints both the extracted list and the reversed list
print("Original numbers:", numbers)
print("Extracted numbers:", extracted_numbers)
print("Reversed numbers:", reversed_numbers)
