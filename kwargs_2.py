# [**kwargs] Create a function create_student_report that takes the student's name as the first argument, the student's age 
# as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. 
# The function should return a dictionary with the student's information and a list of subjects along with their scores.

def create_student_report(std_name, std_age, **kwargs):
    report_card = {'Name': std_name,
                    'Age': std_age}
    
    result = []
    
    for subject, mark in kwargs.items():
        result.append((subject, mark))

    report_card['Result'] = result

    return report_card



print(create_student_report('Nirajan', 24, Math=80, Computer=90, Science=70))