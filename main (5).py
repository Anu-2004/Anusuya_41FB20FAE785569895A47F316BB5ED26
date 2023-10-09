class student:
  definition(self,name,roll_number,cgpa):
  self.name = name
  self.roll_number = roll_number
  self.cgpa = cgpa

def sortStudent(studentList):
  sorted Student = sorted(studentList,key = lamba student:name,student:roll_number,student:cgpa,reverse = true)
  return sortedStudents


#Example usage:
student1 = Student("Alince","S123",3.7)
student2 = Student("Bob","S124",3.9)
student3 = Student("Charlie","S125",3.5)


students = [student1,student2,student3]

sortedStudents = sortStudends(students)

#print the sorted list of students by CGPA in descending order for student in sortedStudents:
   
  
  printf("Name:{student.name},Roll_Number:{student.roll_number},CGPA:{Student.cgpa}")
