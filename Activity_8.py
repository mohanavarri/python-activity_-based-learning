#Smart Parking Fee Management:

Problem statement:
Calculate parking fees according to the number of hours a vehicle is parked.
1.Algorithm:
Start.
Input parking hours.
Charge ₹20 per hour for the first two hours.
Charge ₹10 for each additional hour.
Display the total fee.
Stop.
2.Flowchart:

                               Start
                                ↓
                        Input parking hours
                                ↓
                     Parking hours ≤ 2?
                                ↓
                      Yes → Fee = Hours × ₹20
                       No → Fee = ₹40 + (Hours - 2) × ₹10
                                ↓
                            Display fee
                                ↓
                               Stop
3.Python code:
parking_hours = int(input("Enter parking hours: "))
if parking_hours <= 2:
    fee = parking_hours * 20
else:
    fee = 40 + (parking_hours - 2) * 10
print("Total parking fee =", fee)

4.Sample output:
Enter parking hours: 5
Total parking fee = 70
5.Conclusion:
The program calculates parking fees based on the number of hours a vehicle is parked, applying different rates for the first two hours and subsequent hours.
