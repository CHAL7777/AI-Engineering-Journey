students = [
    {'name': 'Chala', 'scores': [80, 90, 100]},
    {'name': 'Aanaa', 'scores': [33, 46, 43]},
    {'name': 'Mimi', 'scores': [75, 85, 95]}
]
def num(numr):
    aver=sum(numr)/len(numr)
    return aver

def count_passing(students):
    lis=[]
    for i in range(len(students)):
        lis.append(num(students[i]["scores"]))
    nums=0
    for j in lis:
        if j>=50:
            nums=nums+1
    return nums

    # Your code here
    # pass

print(count_passing(students))  # 2