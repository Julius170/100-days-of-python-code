# THE BASIC FORMAT OF LIST COMPREHENSION

# name_of_variable = [new_item for item in list if test]


# EXERCISE 1 Day 26.1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 41, 55]

# squared_numbers = [n*n for n in numbers]

# print(squared_numbers)

# EXERCISE 2 Day 26.2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# result = [nums for nums in numbers if nums % 2 == 0]

# print(result)


# import pandas

# with open ("file1.txt") as file1:
#     file_1_data = file1.readlines()

# with open ("file2.txt") as file2:
#     file_2_data = file2.readlines()

# result = [int(nums) for nums in file_1_data if nums in file_2_data]

# print(result)

# MODIFYING THE GAME 50 U.S. GAME IN DAY 25


# DICTIONARY COMPREHENSIONS

# BASIC FORMAT OF DICTIONARRY COMPREHENSION 

# new_dict = {new_key: new_value for item in list} ...or... 
# new_dict = {new_key: new_value for (key,value) in dic.item} ...for reading data from another dictionary...



