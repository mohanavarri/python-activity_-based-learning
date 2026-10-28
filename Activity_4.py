#Employee Payroll and Deduction Analysis:

Problem statement:
Calculate an employee's gross salary, deductions, and net salary.
1.Algorithm:
Start.
Input basic salary, allowances, and deductions.
Calculate gross salary as the sum of basic salary and allowances.
Calculate net salary as the difference between gross salary and deductions.
Display gross salary, deductions, and net salary.
Stop.
2.Flowchart:
                         Start
                           ↓
                Input basic salary, allowances, and deductions
                            ↓
                  Calculate gross salary
                            ↓
                   Calculate net salary
                            ↓
                   Display results
                            ↓
                           Stop
3.Python code:
basic_salary = float(input("Basic salary: "))
allowances = float(input("Allowances: "))
deductions = float(input("Deductions: "))

gross_salary = basic_salary + allowances
net_salary = gross_salary - deductions

print("Gross salary =", gross_salary)
print("Deductions =", deductions)
print("Net salary =", net_salary)
4.Sample output:
Basic salary: 50000
Allowances: 10000
Deductions: 5000
Gross salary = 60000.0
Deductions = 5000.0
Net salary = 55000.0
5.Conclusion:
The program calculates an employee's gross salary, deductions, and net salary using basic arithmetic operations.




