 Hospital bill and patient classification:
 
Problem statement: 
Calculate a patient's hospital bill using consultation, diagnostic, and treatment charges.
1.Algorithm:
Start.
Input consultation, diagnostic, and treatment charges.
Calculate the total bill.
If the bill is above ₹5,000, give a 10% concession.
Display the final bill.
Stop.
2.Flowchart:
                         Start
                           ↓
                Input three charges
                            ↓
                  Calculate total bill
                            ↓
                   Bill above ₹5,000?
                            ↓
                Yes → Apply 10% discount
                   No → No discount
                            ↓
                   Display final bill
                            ↓
                           Stop
3.Python code:
consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

bill = consultation + diagnostic + treatment

if bill > 5000:
    bill = bill - bill * 0.10

print("Final hospital bill =", bill)
4.Sample output:
Consultation charge: 500
Diagnostic charge: 1500
Treatment charge: 4000
Final hospital bill = 5400.0
5.Conclusion:
The program calculates a patient's hospital bill and applies a discount if applicable.