#HW 7, Section 007
#Namita Nair, nair0025

#Problem A
#==========================================
# Name: StudentGrades
# Purpose: A class that contains student information
# Precondition: contains studentID, first and last name, and list of grades
# Input Parameter(s): 
#   -studentID: integer value
#   -lastName: string of student's last name
#   -firstName: string of student's first name
#   -grades: list of lists representing quiz, homework and lab scores
# Return Value(s): 
#   -getStudentID returns studentID
#   -getLastName returns last name
#   -getFirstName returns first name
#   -getGrades returns list of grades
#   -averageGrades returns a list of the average scores for quizzes, hw, and labs
#   -__str__ overloads the string operater and returns the formatted StudentGrades object
#============================================
class StudentGrades:
    
    def __init__(self, studentID = 0, lastName = '', firstName = '', grades = [[],[],[]]):
        self.studentID = studentID
        self.lastName = lastName
        self.firstName = firstName
        self.grades = grades
        
    def setLastName(self, string):
        self.lastname = string
        
    def setfirstName(self, string):
        self.firstName = string
        
    def getStudentID(self):
        return self.studentID
    
    def getLastName(self):
        return self.lastname
    
    def getFirstName(self):
        return self.firstName
    
    def getGrades(self):
        return self.grades
    
    def addGrade(self, num, string):
        if string == 'Q':
            self.grades[0].append(num)
        elif string == 'H':
            self.grades[1].append(num)
        else:
            self.grades[2].append(num)
    
    def averageGrades(self):
        newlist = []
        for i in self.grades:
            sum1 = 0
            ave = 0
            for j in i:
                sum1 += j
            if i == []:
                ave = 0
            else:
                ave = round(sum1 / len(i))
            newlist.append(ave)
        return newlist
    
    def __str__(self):
        return ('ID: '+ str(self.studentID) + '\n'+ 'Grades: ' + str(self.grades)+ '\n' + 'Averages: ' + str(StudentGrades.averageGrades(self)))

#Problem B
#==========================================
# Name: CourseGrades
# Purpose: A class containing course information
# Precondition: The class inherits the StudentGrades class information
# Input Parameter(s): 
#   -course: string of the course name
#   -section: string of the section number
#   -semester: string of the semester
#   -year: int value of the year
#   -grades: list of StudentGrades objects
# Return Value(s):
#   -getGrades returns the grades list
#   -averages returns a list of averages of quiz, hw and lab scores for
#       all students in the course
#   -__str__ overloads the string operator and returns the formatted CourseGrades object
#============================================
class CourseGrades(StudentGrades):
    
    def __init__(self, course = '', section = '', semester = '', year = 0, grades = []):
        self.course = course
        self.section = section
        self.semester = semester
        self.year = year
        self.grades = grades
        
    def getGrades(self):
        return self.grades
    
    def printStudents(self):
        for i in self.grades:
            print(StudentGrades.i)
        
    def averages(self):
        quizave = []
        hwave = []
        labave = []
        avelist = []
        sum1 = 0
        for student in self.grades:
            ave = StudentGrades.averageGrades(student)
            quizave.append(ave[0])
            hwave.append(ave[1])
            labave.append(ave[2])
        for i in quizave:
            sum1 += i
        avelist.append(round(sum1/len(quizave)))
        for i in hwave:
            sum1 += i
        avelist.append(round(sum1/len(hwave)))
        for i in labave:
            sum1 += i
        avelist.append(round(sum1/len(labave)))
        return avelist

    def addStudent(self, student):
        self.grades.append(student)
        
    def __str__(self):
        return(str(self.course)+', '+str(self.section)+', '+str(self.semester)+', '+str(self.year)+', '+str(CourseGrades.averages(self)))

if __name__ == '__main__':
    
    #A
    a_list = []
    Student1 = StudentGrades(123456, 'Smith', 'John', [[80, 70, 80], [75, 90, 90, 80], [100, 95, 80, 90]])
    Student2 = StudentGrades(179876, 'Johnson', 'Anna', [[90, 85, 70], [100, 90, 80, 70], [100, 95, 85, 90]])
    Student3 = StudentGrades(197625, 'Lee', 'Sarah', [[80, 95, 100], [75, 90, 80, 65], [100, 100, 90, 85]])
    a_list.append(Student1)
    a_list.append(Student2)
    a_list.append(Student3)
    for i in a_list:
        print(i)
            
    #B
    Course1 = CourseGrades('CSCI 1133', '007', 'SPRING', 2020, a_list)
    print(Course1)



















