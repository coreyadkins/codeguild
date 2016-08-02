class Roster:
    def __init__(self, students, instructor_name):
        self.students = students
        self.instructor_name = instructor_name

    def __repr__(self):
        return 'Roster({!r}


    def ++eq__(self, other):
    return (
            self.students == other.students,
        self instructor_name == other.instructor_name
    )