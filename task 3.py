# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

# Get patient details
name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))

print("\nSelect Patient Type:")
print("1. General Patient")
print("2. Senior Citizen")
print("3. Emergency Patient")

patient_type = int(input("Enter Patient Type (1-3): "))

# Get hospital charges
consultation = float(input("Enter Consultation Charges: "))
diagnostic = float(input("Enter Diagnostic Charges: "))
treatment = float(input("Enter Treatment Charges: "))

# Validate billing constraints
if age <= 0 or min(consultation, diagnostic, treatment) < 0:
    print("Invalid patient details or billing charges!")

elif patient_type not in [1, 2, 3]:
    print("Invalid Patient Type!")

else:
    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply concessions
    concession = 0

    if patient_type == 2 or age >= 60:
        concession = total * 0.20
        category = "Senior Citizen"
    elif patient_type == 3:
        concession = total * 0.10
        category = "Emergency Patient"
    else:
        category = "General Patient"

    # Final bill
    final_bill = total - concession

    # Payment classification
    print("\nSelect Payment Status:")
    print("1. Paid")
    print("2. Partial Payment")
    print("3. Unpaid")

    payment = int(input("Enter Payment Status (1-3): "))

    if payment == 1:
        status = "Fully Paid"
        balance = 0
    elif payment == 2:
        amount_paid = float(input("Enter Amount Paid: "))
        if amount_paid <= 0 or amount_paid >= final_bill:
            print("Invalid partial payment!")
            exit()
        balance = final_bill - amount_paid
        status = "Partially Paid"
    elif payment == 3:
        status = "Unpaid"
        balance = final_bill
    else:
        print("Invalid Payment Status!")
        exit()

    # Display bill
    print("\n======= HOSPITAL BILL =======")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Category:", category)
    print("Consultation Charges:", consultation)
    print("Diagnostic Charges:", diagnostic)
    print("Treatment Charges:", treatment)
    print("Total Amount:", total)
    print("Concession:", concession)
    print("Final Bill:", final_bill)
    print("Payment Status:", status)
    print("Remaining Balance:", balance)
    print("=============================")
