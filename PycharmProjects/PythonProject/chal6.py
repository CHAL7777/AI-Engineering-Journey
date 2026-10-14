
students = [
    {"name": "Chala", "scores": [80, 90, 100]},
    {"name": "Aanaa", "scores": [33, 46, 43]},
    {"name": "Mimi", "scores": [75, 85, 95]},
    {"name": "Jerry", "scores": [99, 90, 100]},
    {"name": "Sara", "scores": [50, 50, 50]}
]


def length(students):
    return len(students)


def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def get_student_average(student):
    return calculate_average(student["scores"])


def get_top_student(students):
    if not students:
        return None

    top_student = students[0]

    for student in students[1:]:
        if get_student_average(student) > get_student_average(top_student):
            top_student = student

    return top_student["name"]


def get_grade_counts(students):
    grade_counts = {
        "A": 0,
        "B": 0,
        "C": 0,
        "F": 0
    }

    for student in students:
        average = get_student_average(student)
        grade = get_grade(average)
        grade_counts[grade] += 1

    return grade_counts


def get_pass_fail_counts(students):
    passed = 0
    failed = 0

    for student in students:
        average = get_student_average(student)

        if average >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def get_class_average(students):
    if not students:
        return 0

    total = 0

    for student in students:
        total += get_student_average(student)

    return total / len(students)


def create_report(students):
    passed, failed = get_pass_fail_counts(students)

    report = {
        "total_students": length(students),
        "passed_count": passed,
        "failed_count": failed,
        "class_average": round(get_class_average(students), 2),
        "top_student": get_top_student(students),
        "grade_counts": get_grade_counts(students)
    }

    return report


def get_class_summary(students):
    return create_report(students)


print(get_class_summary(students))
