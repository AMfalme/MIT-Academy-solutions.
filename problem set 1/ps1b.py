'''
We calculate the number of months it will take to afford the downpayment of a house.
This takes into consideration a semi annual raise in the salary.
'''
annual_salary = float(input("Kindly input your annual salary?"))
portion_saved = float(input("Kindly input your desired savings as a decimal?"))
total_cost = float(input("Kindly input the total cost of the house?"))
semi_annual_raise = float(input("Kindly input the semi annual raise?"))
monthly_salary = annual_salary/12
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
number_of_months = 0
saved = portion_saved * monthly_salary
annual_return = 0.04
monthly_return = annual_return / 12
while current_savings < portion_down_payment:
    r = current_savings * monthly_return
    addition = (r + saved)
    current_savings += addition
    number_of_months += 1
    if (number_of_months % 6) == 0:
        monthly_salary = monthly_salary + (semi_annual_raise * monthly_salary)
        saved = portion_saved * monthly_salary
print("Number of months: ", number_of_months)
