# class Student():
#     pass
#
# student1=Student()
# student2=Student()
#
# student1.name="Chala Gobena"
#
# print(student1.name)

# class Car:
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#
#
# car1=Car("Toyota","Red",1993)
# car2=Car("BMW","Black",2000)
#
# print(car1.brand)
# print(car2.brand)

# class Student:
#     def greet(self):
#         print("hello ,OOP")
#
#
# stud=Student()
#
# stud.greet()

class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores

    def calculateA(self):
        return sum(self.scores)/len(self.scores)

    def displayinformation(self):
        print("Name",self.name)
        print("Scores",self.scores)
        print("Average",self.calculateA())

stud=Student("Chala Gobena",[88,91,90])
stud2=Student("Dibora Ayele",[85,91,80])

stud.displayinformation()
stud2.displayinformation()