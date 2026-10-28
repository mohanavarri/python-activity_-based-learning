#Attendance Recovery Computation:

Problem statement:
  Calculate attendance percentage and determine the minimum number of consecutive classes a student must attend to reach 75% attendance.
1.Algorithm:
Start.
Input classes attended and total classes.
Calculate attendance percentage.
If attendance is below 75%, repeatedly add one attended class until it reaches 75%.
Display the required classes.
Stop.
2.Flowchart:

                               Start
                                ↓
                   Input classes attended and total classes
                                ↓
                        Calculate attendance percentage
                                ↓
                     Attendance < 75%?
                                ↓
                      Yes → Add one attended class
                       No → Display required classes
                                ↓
                               Stop
3.Python code:
classes_attended = int(input("Enter number of classes attended: "))
total_classes = int(input("Enter total number of classes: "))
attendance_percentage = (classes_attended / total_classes) * 100
required_classes = 0
while attendance_percentage < 75:
    classes_attended += 1
    required_classes += 1
    attendance_percentage = (classes_attended / total_classes) * 100
print("Minimum consecutive classes to attend:", required_classes)

4.Sample output:
Enter number of classes attended: 30
Enter total number of classes: 40
Minimum consecutive classes to attend: 5
5.Conclusion:
The program calculates the attendance percentage and determines the minimum number of consecutive classes a student must attend to
