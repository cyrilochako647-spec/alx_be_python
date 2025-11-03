

try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values for income and expenses.")
    
    monthly_income = 0
    monthly_expenses = 0


monthly_savings = monthly_income - monthly_expenses


ANNUAL_INTEREST_RATE = 0.05 


annual_base_savings = monthly_savings * 12


interest_earned = annual_base_savings * ANNUAL_INTEREST_RATE


projected_annual_savings = annual_base_savings + interest_earned


print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
