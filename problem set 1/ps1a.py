'''
We calculate the number of months it will take to afford the downpayment of a house.
'''
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
number_of_months = 0
portion_saved = portion_saved * annual_salary/12
annual_return = 0.04
monthly_return = annual_return / 12
while current_savings < portion_down_payment:
    r = current_savings * monthly_return
    addition = (r + portion_saved)
    current_savings = current_savings + addition
    number_of_months = number_of_months + 1

print("Number of months: ", number_of_months)
