from student import student
from roster import roster

def main():
    students = [
        Student('alice', 'alice@alice.com'),
        Student('Bob', 'bob@bob.com'),
        Student('Mel', 'mel@mel.com'),
    ]
    roster = Roster(students, 'David')

    intro_email = write_intro_email(roster)
    print(intro_email)

if __name__ == '__main__':
    main()

