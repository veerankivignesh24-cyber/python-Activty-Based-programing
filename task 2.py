# Progressive Electricity Billing System

months = []
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nEnter details for Month", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    # Calculate slab charges
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charges
    fixed_charge = 50

    # Surcharge
    surcharge = energy_charge * 0.05

    # Rebate for low consumption
    if units <= 100:
        rebate = 20
    else:
        rebate = 0

    # Total bill
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    months.append(month)
    bills.append(total_bill)

    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total_bill, 2))


# Monthly bill comparison
print("\n------ MONTHLY BILL COMPARISON ------")

for i in range(n):
    print(months[i], ": Rs.", round(bills[i], 2))

# Identify unusual increases
print("\n------ UNUSUAL BILL INCREASES ------")

found = False

for i in range(1, n):
    increase = bills[i] - bills[i - 1]

    if increase > 0:
        percentage = (increase / bills[i - 1]) * 100

        if percentage > 30:
            print(months[i], "has an unusual increase of",
                  round(percentage, 2), "%")
            found = True

if not found:
    print("No unusual bill increases found.")

print("\nAverage Monthly Bill: Rs.",
      round(sum(bills) / n, 2))
