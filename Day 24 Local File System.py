# FILES, DICTIONARIES AND PATH


#  HOW TO READ, WRITE, OPEN AND CLOSE FILES IN PYTHON

# READING THE FILE
# with open("HELLO.txt") as file:
#     content = file.read()
#     print(content)

# WRITING(mode = 'w')  AND APPENDING(mode = 'a') THE FILE
# with open("NewFiling.txt", mode='w') as file:
#     file.write("\nNew Text.")


# Paths
# ABSOLUTE FILE PATHS AND RELATIVE FILE PATHS
# with open("C:/Users/Phensic002/OneDrive/Desktop/25 websites/index.html") as file:
#     contents = file.read()
#     print(contents)


# MAIL MERGING

# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name
# Save the letters in the folder  "ReadyToSend"

PLACEHOLDER = "[name]"

with open("day 24 names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("day 24 letters.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"{stripped_name}.docx", mode ='w') as completed_letter:
            completed_letter.write(new_letter)



