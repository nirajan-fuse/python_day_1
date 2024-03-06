# [dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values, 
# create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.

std_name = ['Ram', 'Shyam', 'Hari', 'Gita', 'sita']

std_mark = [76, 81, 69, 90, 56]

student_dict = {k:v for k, v in zip(std_name, std_mark) if v>80}

print(student_dict)