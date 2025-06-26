def __init__(self, name):
        self.name = name
        self.grades= {}

def set_grade(self, course, grade):
    self.grades[course] = grade

def get_average(self):
    return sum(self.grades.values())/len(self.grades)