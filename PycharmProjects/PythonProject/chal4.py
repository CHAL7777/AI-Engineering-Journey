def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(scores):
    average = calculate_average(scores)

    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    elif  average >= 60:
        return "C"
    else:
        return "F"

def create_student(name, scores):
    grade = get_grade(scores)
    average = calculate_average(scores)

    return {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

student = create_student("Chala", [50, 90, 40])
print(student)