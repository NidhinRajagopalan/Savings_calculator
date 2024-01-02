def calculate_monthly_savings(target_savings, num_months):
    if num_months <= 0:
        print("Number of months should be greater than zero.")
        return
    
    monthly_savings = target_savings / num_months
    return monthly_savings

def generate_savings_plan(target_savings, max_months):
    savings_plan = []

    for num_months in range(1, max_months + 1):
        monthly_savings = calculate_monthly_savings(target_savings, num_months)
        savings_plan.append((num_months, monthly_savings))

    return savings_plan

def display_savings_plan(savings_plan):
    print("Savings Plan:")
    print("Months \t Monthly Savings")
    for entry in savings_plan:
        print(f"{entry[0]} \t Rs.{entry[1]:.2f}")

target_savings = float(input("Enter your target savings: "))
max_months = int(input("Enter the max number of months to consider: "))

plan = generate_savings_plan(target_savings, max_months)
display_savings_plan(plan)
