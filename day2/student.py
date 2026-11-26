# task1
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_marks(self, score: float):
        self.marks.append(score)

    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def highest(self) -> float:
        if not self.marks:
            return 0.0
        return max(self.marks)

    def lowlest(self) -> float:
        if not self.marks:
            return 0.0
        return min(self.marks)


if __name__ == "__main__":
    student1 = Student("amit", 101)
    student1.add_marks(90)
    student1.add_marks(80)
    print(f"{student1.name}'s, Average:{student1.average()}")

    student2 = Student("bob", 102)
    student2.add_marks(60)
    student2.add_marks(70)
    print(f"{student2.name}'s, Average:{student2.average()}")

    student3 = Student("charmi", 103)
    print(f"{student3.name}'s, Average:{student3.average()}")


# task2
class Stu:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student Name: {self.name}, roll: {self.roll}"

    def __repr__(self):
        return f"student('{self.name}', {self.roll})"


s1 = Stu("rohit", 1)
s2 = Stu("aarti", 2)

print(s1)
student = [s1, s2]
print(student)


# task3
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("name", self.name)


class Stud(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display_Stud(self):
        self.display_person()
        print("roll:", self.roll)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display_Teacher(self):
        self.display_person()
        print("subject:", self.subject)


su1 = Stud("mansi", 50)
te1 = Teacher("yash", "python")

print("student details")
su1.display_Stud()

print("techer details")
te1.display_Teacher()
