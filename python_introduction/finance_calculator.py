monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int (input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are: $",monthly_savings)
print ("Projected savings after one year, with interest: $", projected_annual_savings)