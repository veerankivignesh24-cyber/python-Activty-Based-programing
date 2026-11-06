# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")

# Get User Requirements
data_usage = float(input("Enter Required Data Usage (GB): "))
required_validity = int(input("Enter Required Validity (Days): "))
budget = float(input("Enter Your Budget (Rs): "))

# Mobile Plans
plans = [
    {"name": "Basic Plan", "data": 2, "validity": 28,
     "price": 199, "extra": 50},

    {"name": "Standard Plan", "data": 3, "validity": 56,
     "price": 399, "extra": 40},

    {"name": "Premium Plan", "data": 5, "validity": 84,
     "price": 599, "extra": 30},

    {"name": "Unlimited Plan", "data": 10, "validity": 90,
     "price": 799, "extra": 20}
]

# Validate Input
if data_usage < 0 or required_validity <= 0 or budget < 0:
    print("Invalid Input! Please enter valid values.")

else:
    eligible_plans = []

    print("\n========== AVAILABLE PLANS ==========")

    # Compare All Plans
    for plan in plans:

        excess_data = max(0, data_usage - plan["data"])

        excess_charge = excess_data * plan["extra"]

        total_cost = plan["price"] + excess_charge

        print("\nPlan Name:", plan["name"])
        print("Data Limit:", plan["data"], "GB")
        print("Validity:", plan["validity"], "Days")
        print("Plan Price: Rs.", plan["price"])
        print("Excess Charge: Rs.", excess_charge)
        print("Total Cost: Rs.", total_cost)

        # Check Eligibility
        if (plan["data"] >= data_usage and
            plan["validity"] >= required_validity and
            total_cost <= budget):

            eligible_plans.append((plan, total_cost))

    # Find Most Economical Plan
    print("\n========== BEST PLAN ==========")

    if eligible_plans:
        best_plan, best_cost = min(
            eligible_plans, key=lambda x: x[1]
        )

        print("Recommended Plan:", best_plan["name"])
        print("Data Available:", best_plan["data"], "GB")
        print("Validity:", best_plan["validity"], "Days")
        print("Total Cost: Rs.", best_cost)
        print("Remaining Budget: Rs.", budget - best_cost)

    else:
        print("No eligible plan found!")
        print("Please increase your budget or reduce usage.")

    print("====================================")
