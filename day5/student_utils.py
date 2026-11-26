# task6
class Student:
    """represent a student and manage their marks"""

    def __init__(self, name: str, roll: int) -> None:
        """initialize a student.
        args:
            name: student's name
            roll: student's roll"""
        self.name = name
        self.roll = roll
        self.marks: list[float] = []

    def add_marks(self, score: float) -> None:
        """add a mark to the student's record
        args:
            score: marks to add"""
        self.marks.append(score)

    def averege(self) -> float:
        """calculate the average of the student's marks
        returns:
            average mark, or 0.0 if no marks exist"""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def higest(self) -> float:
        """return the highest mark
        returns:
            highhest mark, or 0.0 if no mark exist"""
        if not self.marks:
            return 0.0
        return max(self.marks)

    def lowest(self) -> float:
        """return the lowest mark
        returns:
            lowest mark, or 0.0 if no mark exist"""
        if not self.marks:
            return 0.0
        return min(self.marks)
