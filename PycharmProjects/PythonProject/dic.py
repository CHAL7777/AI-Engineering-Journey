# student = {"name": "Chala"}
#
# print(student["name"])       # Chala
# print(student.get("age"))    # None
# print(student.get("age", 0)) # 0

# student={
#     "name":"Chala Gobena",
#     "age":23,
#     "Grade":"A"
# }
#
# for x in student.values():
#     print(x)

# words = ["python", "java", "python", "php", "java", "python"]
# neword={}
# for word in words:
#     if word in neword:
#         neword[word]+=1
#     else:
#         neword[word]=1
# print(neword)
#
# numbers = [12, 5, 20, 7, 30, 15, 8]
#
# num=[num for num in numbers if num>10]
# num.reverse()
#
# print(num)
#
# num2=[3, 5, 3, 7, 5, 9, 7, 10]
# nu=[]
# for i in num2:
#     if i not in nu:
#         nu.append(i)
#
# print(nu)


# profile={
#     "name":"Chala Gobena",
#     "age":23,
#     "Skills":["js","ts","java"]
# }
#
# profile["Skills"].append("Python")
# profile["City"]="Addis Abeba"
#
# print(profile)

# counts=['a', 'b', 'a', 'c', 'b', 'a', 'd']
#
# dic={}
# for i in counts:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)

students_list = [
    {
        "name": "Chala Gobena",
        "age": 23,
        "scores": [85, 92, 90]
    },
    {
        "name": "Aster Bekele",
        "age": 21,
        "scores": [48, 33, 44]
    },
    {
        "name": "Tolosa Lemma",
        "age": 24,
        "scores": [95, 100, 90]
    },
{
        "name": "Abebe Bikila",
        "age": 24,
        "scores": [40, 50, 30]
    }
]
def calca(av):
    return sum(av)/len(av)

for i in range(len(students_list)):
    students_list[i]["Average"]=calca(students_list[i]["scores"])

def passed(student):
    num = [i for i in student if i['Average'] >= 50]
    return num

def get_grade_counts(students):
    A=0
    B=0
    C=0
    F=0
    grade={}
    for i in students:
        if i["Average"]>=80:
            grade["A"]+=1
        elif i["Average"]>=70:
            grade["B"] += 1
        elif i["Average"]>=50:
            grade["C"]+=1
        else:
            grade["F"]+=1
    return grade

grade=get_grade_counts(students_list)
print(grade)
newdic=passed(students_list)
print(newdic)

# print(students_list)
