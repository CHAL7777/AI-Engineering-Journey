
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def create_student(name, scores):
    aver = calculate_average(scores)
    grade = get_grade(aver)

    dic = {
        "name": name,
        "scores": scores,
        "average": aver,
        "grade": grade
    }

    return dic


student = create_student("Chala", [80, 90, 100])
print(student)
