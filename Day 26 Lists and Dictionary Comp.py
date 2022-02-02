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

# BASIC FORMAT OF DICTIONARY COMPREHENSION 

# new_dict = {new_key: new_value for item in list} ...or... 
# new_dict = {new_key: new_value for (key,value) in dic.item} ...for reading data from another dictionary...

# HERE'S AND EXAMPLE

# import random                                                       
# name = ['Alexa', 'Julius', 'Michael', 'Olamide', 'Anointing', 'Kolade', 'Kelvin']
# students_scores = {students:random.randint(1, 100) for students in name}


# import random
# students_score = {students: random.randint(1, 100) for students in name}
# passed_students = {students:scores for (students, scores) in students_score.item() if score > 60}
# passed_students = {student: score for (student, score) in students_score.items() if score >=60 


# EXERCISE Day 26.4
# sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# # sentence_list = sentence.split()
#
# result = {words:len(words) for words in sentence.split()}
#
# print(result)

# EXERCISE DAY 26.5
# PRINTS THE DEGREE CELSIUS INTO FERNHEIT AND PRINTS IN THE SAME FORMAT
# weather_C = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday":24
# }
#
# weather_f = {}
#
# temp = {days:(degs*9/5 + 32) for (days, degs) in weather_C.items()}
#
# print(temp)


# ITERATING A DICTIONARY WITH PANDAS DATAFRAME

# student_dict = {
#     "students": ["Angela", "James", "Lily"],
#      "score": [56, 76, 98]
# }
# THE USUAL FORMAT
# for (key, value) in student_dict.items():
#     print(key, value)

# THE BASIC FORMAT USING PANDAS

# 1st. Creating the dataframe
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # 2nd. Looping through the data frame the ordinary way
# for (key, value) in student_data_frame.items():
#     print(value)

# # 3rd The pandas way (Loops through he rowa of the data frame)

# for (index, row) in student_data_frame.iterrows():
#     print(row.students == "Angela" )


# DAY 26 PROJECT (WHAT IS YOUR NAME)


import pandas

data = pandas.read_csv("NATO_phonetic_alphabets.csv")

dictionary = (data.to_dict())
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

output_list = (new_dict[letters] for letters in word)

print(output_list)

# FINITE
