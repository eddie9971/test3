placeholder = '[name]'

with open('../Files/names.txt') as names_file:
    names = names_file.readlines()

with open('../Files/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder, stripped_name)
        with open(f'../Output/letter_for_{stripped_name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)

