class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

class GWAFinder:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def read_students(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(':')
                    if len(parts) == 2:
                        name, gwa = parts
                        self.students.append(Student(name, gwa))
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except ValueError:
            print("Error parsing GWA values.")

    def find_highest(self):
        if not self.students:
            return None
        highest = min(self.students, key=lambda s: s.gwa)
        return highest

if __name__ == "__main__":
    finder = GWAFinder('students.txt')
    finder.read_students()
    highest_student = finder.find_highest()
    if highest_student:
        print(f"The student with the highest GWA is {highest_student.name} with a GWA of {highest_student.gwa}")
    else:
        print("No students found.")