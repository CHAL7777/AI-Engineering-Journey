
def averagec(num):
    if num==0:
        return False
    return sum(num)/len(num)

def calci(num):
    aver=averagec(num)
    if aver>=50:
        return "C"
    elif aver>=70:
        return "B"
    elif aver>=80:
        return "A"
    else:
        return "F"

def create_student(name,num):
    grade=calci(num)
    ave =averagec(num)
    stud={
        "name":name,
        "score":num,
        "average":ave,
        "status":grade
    }
    return stud

student = create_student("Chala", [80, 90, 100])
student2=create_student("Aanaa",[33,46,43])
print(student)
print(student2)