#University Scholarship Allocation

1.Algorrithm
Start.
Input student name, aggregate marks, subject-wise marks, attendance percentage, and family income.
Check whether the student satisfies all eligibility conditions.
If eligible, display “Eligible for Scholarship”; otherwise, display “Not Eligible for Scholarship.”
End.
Assumed eligibility conditions:
Aggregate marks must be at least 75%.
Each subject mark must be at least 40%.
Attendance must be at least 75%.
Family income must not exceed ₹2,00,000 per year.
2. Python program
# University Scholarship Allocation

name = input("Enter student name: ")
aggregate = float(input("Enter aggregate marks (%): "))

subject1 = float(input("Enter subject 1 marks (%): "))
subject2 = float(input("Enter subject 2 marks (%): "))
subject3 = float(input("Enter subject 3 marks (%): "))

attendance = float(input("Enter attendance (%): "))
income = float(input("Enter family annual income: Rs. "))

if (aggregate >= 75 and
    subject1 >= 40 and
    subject2 >= 40 and
    subject3 >= 40 and
    attendance >= 75 and
    income <= 200000):

    print("Student Name:", name)
    print("Eligible for Scholarship")
else:
    print("Student Name:", name)
  
    print("Not Eligible for Scholarship")
3.Flowchart
START
Input marks, subject scores, attendance and income
            ↓   
Are all eligibility conditions satisfied?
            ↓
YES
↓
Eligible for Scholarship
↓
END
4.Sample output
Enter student name: Ravi
Enter aggregate marks (%): 85
Enter subject 1 marks (%): 80
Enter subject 2 marks (%): 75
Enter subject 3 marks (%): 90
Enter attendance (%): 90
Enter family annual income: Rs. 150000

Student Name: Ravi
Eligible for Scholarship
Conclusion
The University Scholarship Allocation program determines scholarship eligibility using aggregate marks,
subject-wise minimum marks, attendance, and family income. It uses variables, input statements, comparison operators, and conditional statements to display the r
