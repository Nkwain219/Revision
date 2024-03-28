class Student:
    def __init__(self, name, matricule, birthdate):
        self.name = name
        self.matricule = matricule
        self.birthdate = birthdate

    def get_info(self):
        return f"Name: {self.name}\nMatricule: {self.matricule}\nBirthdate: {self.birthdate}"

students = {
    "2021001": Student("John Doe", "2021001", "2000-05-15"),
    "2021002": Student("Jane Smith", "2021002", "2001-02-28"),
    "2021003": Student("Alex Johnson", "2021003", "1999-11-10")
}

def query_student(matricule):
    student = students.get(matricule)
    if student:
        return student.get_info()
    return "No student found with the given matricule."
search_matricule = input("Enter the matricule of the student to search: ")
student_info = query_student(search_matricule)
print(student_info)
        