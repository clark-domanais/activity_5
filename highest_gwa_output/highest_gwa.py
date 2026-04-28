class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)

class GWAFinder:
    def __init__(self, filename):
        self.filename = filename
        self.students = []



if __name__ == "__main__":
    finder = GWAFinder('students.txt')
    finder.read_students()
    highest_student = finder.find_highest()
