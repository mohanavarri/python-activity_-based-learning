#progressive slabs for electricity billing:

Problem statement:
  Calculate an electricity bill according to the number of units consumed.
1.Algorithm:
Start.
Input electricity units.
Calculate charges using consumption slabs.
Add a fixed charge of ₹50.
Display the total bill.
Stop.
2.Flowchart:
                             Start
                               ↓
                        Input units
                               ↓
                     Calculate slab charges
                               ↓
                     Add ₹50 fixed charge
                               ↓
                     Display total bill
                               ↓
                             Stop
3.Python code:
units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 2
    bill += 50
    print("Total bill =", bill)
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3 + 50
    print("Total bill =", bill)
else:
    bill = 200 + 300 + (units - 200) * 5 + 50
    print("Total bill =", bill)
4.Sample output
Enter units consumed: 150
Total bill = 450
5.Conclusion:
The program calculates electricity charges using conditional statements and progressive slabs.

