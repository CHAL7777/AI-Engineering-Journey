# def numbers(num):
#     return num**2

# square=lambda num:num**2
#
# print(square(4))

students=[{
    "name":"Chala Gobena",
    "Department":"Software Engineering",
    "score":65},{
     "name":"Aanaa Andela",
    "Department":"Software Engineering",
    "score":76
}]

students.sort(key=lambda student:student["score"] )

print(students)