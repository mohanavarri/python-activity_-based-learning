#ATM Transaction Simulation

Problem statement:
Simulate deposits and withdrawals while maintaining a bank balance.
1.Algorithm:
Start.
Set the initial balance to ₹5,000.
Choose deposit or withdrawal.
Update the balance if the transaction is valid.
Display the final balance.
Stop.
2.Flowchart:
                           Start
                             ↓
                  Set initial balance = ₹5,000
                             ↓
                 Choose deposit or withdrawal
                             ↓
                Is the transaction valid?
                             ↓
          Yes → Update balance and display final balance
          No → Display error message
                             ↓
                            Stop
3.Python code:
initial_balance = 5000
transaction_type = input("Enter transaction type (deposit/withdrawal): ").lower()
if transaction_type == "deposit":
    amount = float(input("Enter deposit amount: "))
    initial_balance += amount
    print("Final balance =", initial_balance)
elif transaction_type == "withdrawal":
    amount = float(input("Enter withdrawal amount: "))
    if amount <= initial_balance:
        initial_balance -= amount
        print("Final balance =", initial_balance)
    else:
        print("Error: Insufficient funds.")
else:
    print("Error: Invalid transaction type.")
4.Sample output:
Enter transaction type (deposit/withdrawal): deposit
Enter deposit amount: 2000
Final balance = 7000.0
5.Conclusion:
The program simulates ATM transactions by allowing users to deposit or withdraw money while ensuring that the balance remains valid.
