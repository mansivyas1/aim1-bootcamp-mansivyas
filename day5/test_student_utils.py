from day5.student_utils import Student


def test_add_marks():
    """checks that marks are added correctly"""
    student = Student("mansi", 101)

    student.add_marks(90)
    student.add_marks(80)

    assert student.marks == [90, 80]


def test_averege():
    """check the average calculation"""
    student = Student("mansi", 101)

    student.add_marks(90)
    student.add_marks(80)
    student.add_marks(70)

    assert student.averege() == 80.0


def test_average_without_marks():
    """check average when no marks are available"""
    student = Student("mansi", 101)

    assert student.averege() == 0.0


def test_higest():
    """check the highest mark"""
    student = Student("mansi", 101)

    student.add_marks(90)
    student.add_marks(80)
    student.add_marks(70)

    assert student.higest() == 90


def test_lowest():
    """check the lowest mark"""
    student = Student("mansi", 101)

    student.add_marks(90)
    student.add_marks(80)
    student.add_marks(70)

    assert student.lowest() == 70


def test_higest_without_marks():
    """check highest mark when no marks are available"""
    student = Student("mansi", 101)

    assert student.higest() == 0.0


def test_lowest_without_marks():
    """checks lowest mark when no marks are available"""
    student = Student("mansi", 101)

    assert student.lowest() == 0.0
