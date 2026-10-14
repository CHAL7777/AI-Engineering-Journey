students = [
    {"name": "Chala", "scores": [80, 90, 100]},
    {"name": "Aanaa", "scores": [33, 46, 43]},
    {"name": "Mimi", "scores": [75, 85, 95]}
]

def get_av(student):
    scores=student["scores"]

    average=sum(scores)/len(scores)

    return average

print(get_av(students[1]))



