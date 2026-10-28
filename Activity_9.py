#Examination Result and Grace-Mark Validation

from tracemalloc import start


Problem statement:
Calculate a student's total marks and determine whether the student passes or fails in three subjects.
1.Algorithm:
Start.
Input marks in three subjects.
Check that each subject has at least 35 marks.
Calculate total and average.
Display the result.
Stop.
2.Flowchart:
                  start
                    ↓
            Input marks in three subjects
                    ↓
          Check if each subject ≥ 35?
                    ↓
          Yes → Calculate total and average
            No → Display fail message
                        ↓
                     Display result
                        ↓
                     Stop
3.Python code:
subject1 = int(input("Enter marks in subject 1: "))
subject2 = int(input("Enter marks in subject 2: "))
subject3 = int(input("Enter marks in subject 3: "))

if subject1 >= 35 and subject2 >= 35 and subject3 >= 35:
    total = subject1 + subject2 + subject3
    average = total / 3
    print("Total marks:", total)
    print("Average marks:", average)
else:
    print("Student has failed in one or more subjects.")

4.Sample output:
Enter marks in subject 1: 40
Enter marks in subject 2: 50
Enter marks in subject 3: 30
Student has failed in one or more subjects.
5.Conclusion:
The program calculates a student's total marks and average, and checks if the student passes or fails based on the minimum passing marks for each subject.