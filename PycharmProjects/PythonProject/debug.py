students = [
    {"name": "Chala", "scores": [80, 90, 100]},
    {"name": "Aanaa", "scores": [33, 46, 43]},
    {"name": "Mimi", "scores": [75, 85, 95]},
    {"name":"Jerry","scores":[99,90,100]}
]

def get_av(student):
    scores = student["scores"]
    average = sum(scores) / len(scores)
    return average

def get_top_student(students):
    best_student = students[0]

    for student in students:
        current_average = get_av(student)
        best_average = get_av(best_student)


        if current_average > best_average:
            best_student = student

    return best_student

top = get_top_student(students)

print("Top student:", top["name"])
print("Average:", get_av(top))