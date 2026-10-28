#Campus Event Financial Planning:

Problem statement:
Calculate the total cost of a campus event and determine the registration fee required per participant.
1.Algorithm:
Start.
Input venue, equipment, catering, and certificate costs.
Calculate the total event cost.
Input the number of participants.
Calculate the cost per participant.
Display the result.
Stop.
2.Flowchart:
                               Start
                                ↓
                   Input all event expenses
                                ↓
                        Calculate total event cost
                                ↓
                     Input participant count
                     Participants above zero?
                                ↓
Yes → Fee = Total Cost ÷ Participants
No → Display invalid count
                                ↓
                            Display fee
                                ↓
                               Stop
Python code:
venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))
catering_cost = float(input("Enter catering cost: "))
certificate_cost = float(input("Enter certificate cost: "))
total_cost = venue_cost + equipment_cost + catering_cost + certificate_cost
participants = int(input("Enter number of participants: "))
if participants > 0:
    fee_per_participant = total_cost / participants
    print("Registration fee per participant =", fee_per_participant)
else:
    print("Invalid number of participants")

4.Sample output:
Enter venue cost: 5000
Enter equipment cost: 2000
Enter catering cost: 3000
Enter certificate cost: 1000
Enter number of participants: 100
Registration fee per participant = 110.0
5.Conclusion:
The program calculates the total cost of a campus event and determines the registration fee required per participant using
