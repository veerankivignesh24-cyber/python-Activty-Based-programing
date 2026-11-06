# Railway Fare and Reservation Calculator

print("===== RAILWAY RESERVATION SYSTEM =====")

# Distance and Passenger Details
distance = float(input("Enter Travel Distance (KM): "))
n = int(input("Enter Number of Passengers: "))

# Validate Details
if distance <= 0 or n <= 0:
    print("Invalid distance or passenger count!")

else:
    total_fare = 0

    # Distance Slab Charges
    if distance <= 100:
        base_rate = 1.00
    elif distance <= 500:
        base_rate = 1.50
    elif distance <= 1000:
        base_rate = 2.00
    else:
        base_rate = 2.50

    print("\nSelect Travel Class:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    travel_class = int(input("Enter Class (1-4): "))

    # Class Multipliers
    if travel_class == 1:
        class_name = "Sleeper"
        multiplier = 1.0
        reservation_fee = 20
    elif travel_class == 2:
        class_name = "AC 3 Tier"
        multiplier = 1.5
        reservation_fee = 40
    elif travel_class == 3:
        class_name = "AC 2 Tier"
        multiplier = 2.0
        reservation_fee = 50
    elif travel_class == 4:
        class_name = "AC First Class"
        multiplier = 3.0
        reservation_fee = 60
    else:
        print("Invalid Travel Class!")
        exit()

    # Cancellation Option
    print("\nCancellation Option:")
    print("1. No Cancellation")
    print("2. Cancel Ticket")

    cancellation = int(input("Enter Option (1-2): "))

    # Passenger Fare Calculation
    for i in range(1, n + 1):

        print("\nPassenger", i)

        name = input("Enter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))

        if age <= 0:
            print("Invalid age!")
            exit()

        # Calculate Base Fare
        fare = distance * base_rate * multiplier

        # Age-Based Concession
        concession = 0

        if age >= 60:
            concession = fare * 0.40
        elif age < 12:
            concession = fare * 0.50

        # Final Passenger Fare
        final_fare = fare - concession + reservation_fee

        # Cancellation Penalty
        penalty = 0

        if cancellation == 2:
            penalty = final_fare * 0.25
            final_fare = penalty

        total_fare += final_fare

        # Passenger Bill
        print("\n----- Passenger Fare -----")
        print("Passenger Name:", name)
        print("Age:", age)
        print("Travel Class:", class_name)
        print("Base Fare: Rs.", round(fare, 2))
        print("Concession: Rs.", round(concession, 2))
        print("Reservation Fee: Rs.", reservation_fee)
        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Final Fare: Rs.", round(final_fare, 2))

    # Final Summary
    print("\n===== RAILWAY BILL SUMMARY =====")
    print("Travel Distance:", distance, "KM")
    print("Travel Class:", class_name)
    print("Number of Passengers:", n)
    print("Total Amount: Rs.", round(total_fare, 2))
    print("================================")
