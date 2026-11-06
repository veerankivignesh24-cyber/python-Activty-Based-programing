# Campus Event Financial Planning

print("======= CAMPUS EVENT FINANCIAL PLANNING =======")

# Input event expenses
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

# Input participant and sponsorship details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))

# Calculate fixed and variable costs
fixed_cost = venue + equipment + transport

variable_cost = (catering + certificate) * participants

total_cost = fixed_cost + variable_cost

# Calculate participant contributions
participant_contribution = participants * registration_fee

# Calculate total available funds
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate break-even registration count
available_funds = sponsorship
cost_per_participant = catering + certificate

if registration_fee > cost_per_participant:
    break_even = (fixed_cost - sponsorship) / (
        registration_fee - cost_per_participant
    )
    minimum_registrations = max(0, int(break_even) if break_even == int(break_even)
                                else int(break_even) + 1)
else:
    minimum_registrations = None

# Display financial report
print("\n======= EVENT FINANCIAL REPORT =======")

print("Venue Cost              : Rs.", venue)
print("Equipment Cost          : Rs.", equipment)
print("Catering Cost           : Rs.", round(catering * participants, 2))
print("Transport Cost          : Rs.", transport)
print("Certificate Cost        : Rs.", round(certificate * participants, 2))

print("--------------------------------------")
print("Total Event Cost        : Rs.", round(total_cost, 2))
print("Participant Contribution: Rs.", round(participant_contribution, 2))
print("Sponsorship Amount      : Rs.", round(sponsorship, 2))
print("Total Available Funds   : Rs.", round(total_funds, 2))
print("Sponsorship Shortfall   : Rs.", round(shortfall, 2))

print("--------------------------------------")

if minimum_registrations is not None:
    print("Minimum Registrations Needed:", minimum_registrations)
else:
    print("Break-even is not possible with the current registration fee.")

if total_funds >= total_cost:
    print("Status: Event is financially successful.")
else:
    print("Status: Additional funds are required.")

print("======================================")

