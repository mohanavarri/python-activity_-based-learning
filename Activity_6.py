#Travel expense calculator:

Problem statement:
 Calculate total travel expenses and check whether the expenses are within the planned budget.
1.Algorithm:
Start.
Input food, transport, and hotel expenses.
Calculate total expenses.
Input the travel budget.
Compare expenses with the budget.
Display the result.
Stop.
2.Flowchart:
                               Start
                                ↓
                   Input travel expenses and budget
                                ↓
                        Calculate total expenses
                                ↓
                     Expenses ≤ Budget?
                                ↓
                      Yes → Within budget
                       No → Over budget
                                ↓
                               Stop
3.Python code:
food_expense = float(input("Enter food expenses: "))
transport_expense = float(input("Enter transport expenses: "))
hotel_expense = float(input("Enter hotel expenses: "))
total_expenses = food_expense + transport_expense + hotel_expense
budget = float(input("Enter travel budget: "))
if total_expenses <= budget:
    print("Expenses are within the planned budget.")
else:
    print("Expenses exceed the planned budget.")

4.Sample output:
Enter food expenses: 2000
Enter transport expenses: 1500
Enter hotel expenses: 3000
Enter travel budget: 7000
Expenses are within the planned budget.
5.Conclusion:
The program calculates total travel expenses and checks whether they are within the planned budget using basic arithmetic operations
