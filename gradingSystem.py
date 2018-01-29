#Grading System

#importing modules
import statistics as stat

#initial student list is empty
studentList = {}

#main function
def main():
    while True:#keeps running till someone enters 4 or exits
        print('Welcome to Grade Central\n')
        #tasks
        print('[1] - Enter Grades')
        print('[2] - Remove Student')
        print('[3] - Student Average Grades')
        print('[4] - Exit\n')
        
        #user assignes task
        userInput = input('What would you like to do today? (Enter a number): ')

        try:#if userinput is valid
            val = int(userInput)#task Number
            if val == 1:
                enterGrade()
            elif val == 2:
                removeStudent()
            elif val == 3:
                studentAvg()
            elif val == 4:
                quit()
            else:#if number is not between 1-4
                print('\nPlease choose between 1-4: ')
                continue
        except ValueError:#if input is not a number catch and loop
            print('\nThis is not a correct value, Please enter number between 1-4.')
            continue

#Function takes no parameter
#prints studentList with added grades for current students or new students
def enterGrade():
    while True:#keeps looping till user enters the grade correctly or adds a new student
        studentName = input('Student Name: ')
        grade = input('Grade: ')
        
        try:#checks if the grade is interger
            grade = int(grade)
            print('Adding Grade...')
            if studentName.lower() in studentList:
                #appends grade to the current student
                studentList[studentName.lower()].append(grade)
            else:
                #adds new student
                studentList[studentName.lower()] = [grade]
            print(studentList)
            break
        except ValueError:
            print('\nGrade must be numbers')
            continue

#Function to remove student takes no parameter
#prints studentList after removing the student
def removeStudent():
    while True:
        studentName = input('Which student would you like to remove?: ')
        try:
            del studentList[studentName.lower()]
            print('removing student...')
            print(studentList)
            break
        except Exception:
            print('\nStudent doesn\'t exists')
            continue

#Function that returns grade average of each students, takes no parameter
def studentAvg():
    if len(studentList) != 0:#if the studentList is not empty print each student avg
        for student in studentList:
            #using mean() function from statistics moudles to get the avg of each students grade
            average = stat.mean(studentList[student])
            print(student, 'has an avaerage of: ', average)
    else:
        print('Student List is empty')

#Executing the program
if __name__ == '__main__' :
    main()
