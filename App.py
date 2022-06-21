students = []


class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.average = 0
        self.lessons = {}
        self.grades = {}

    def register(self, n):
        for i in range(n):
            lesson_name = input('Enter lesson name: ')
            units = int(input('Enter units: '))
            self.lessons[lesson_name] = units

    def add_grade(self, lesson, grade):
        self.grades[lesson] = grade

    def calculate_average(self):
        total = 0
        for lesson, grade in self.grades.items():
            total += grade * self.lessons[lesson]
        self.average = round(total / sum(self.lessons.values()), 2)

    def __str__(self):
        return f'{self.name} has an average of {self.average}'


def unit_selection():
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    student = Student(name, major)
    student.register(int(input("Enter number of lessons: ")))
    students.append(student)


def grade_entry():
    student_name = input("Enter student name: ")
    for student in students:
        if student.name == student_name:
            print(f"\n{student.name} has '{student.major}' major:")
            for lesson, units in student.lessons.items():
                grade = int(input(f'   - Enter grade for {lesson}: '))
                student.add_grade(lesson, grade)
            student.calculate_average()
            print("Grades added.")


def show_averages():
    print()
    for student in students:
        print(f"- {student.name} has an average of {student.average}")


def top_students():
    for major in set([student.major for student in students]):
        print(f"\n{major} major:")
        for student in students:
            if student.major == major:
                if student.average == \
                        max(student.average for student in [student for student in students if student.major == major]):
                    print(
                        f"- {student.name} has the highest average of {student.average}")


def number_of_failed_students():
    count = 0
    for student in students:
        if student.average < 12:
            count += 1
    print(f"There are {count} failed students.")


def main():
    print("Welcome to the Student Registration System")

    COMMANDS = {
        1: unit_selection,
        2: grade_entry,
        3: show_averages,
        4: top_students,
        5: number_of_failed_students,
    }

    while (True):
        # clear the terminal
        print("\033c")

        # print menu
        print("Please select option:")
        print("1. Unit Selection")
        print("2. Grade Entry")
        print("3. Show Averages")
        print("4. Top Student")
        print("5. Failed Students")
        print("6. Exit")
        print()

        # get command
        selection = int(input("Please enter your selection: "))

        # check if selection is valid
        if selection not in range(1, 7):
            print("Invalid selection!")
            continue

        if selection == 6:
            print("Goodbye!")
            return

        # call the function associated with the command
        COMMANDS[selection]()

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
