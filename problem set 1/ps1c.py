

steps = 0
annual_salary = float(input("Enter your starting salary?"))


# low and high will help in finding the best saving percentage between 0% and 100%
low = 0
# placed at 10000 to avoid infinite possibilities between 0 and 1, will be neutralized by dividing midpoint by 10000
high = 10000


def Binary_Search_Recursive(annual_salary, low, high, steps):
    # Total cost of the house
    total_cost = 1000000
    # Downpayment amount which is 25% of the total_cost
    portion_down_payment = 0.25 * total_cost
    # semi anual raise which is 7% of the annual salary
    semi_annual_raise = 0.07
    # Initialize current saving amount
    current_savings = 0.0
    return_rate = 0.04/12
    monthly_salary = annual_salary/12
    mid = (low + (high - low)//2)
    portion_saved = mid / 10000
    steps += 1

    for i in range(1, 37):
        # add monthly_savings from salary plus bank monthly return to current savings

        monthly_savings = portion_saved * monthly_salary
        monthly_return = current_savings * return_rate
        addition = (monthly_return + (monthly_savings))
        current_savings += addition
        if (i % 6) == 0 and i != 0:
            # monthly salary increases by semi_annual_raise amount/percentage
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
            # monthly savings changes as a result of increase in salary
            monthly_saving = portion_saved * monthly_salary
        if abs(portion_down_payment - current_savings) < 100:
            # portion_saved = mid
            # print('Congrats, you can save the amount in {} months, {}th step, you will have saved {}'.format(
            #     i, steps, current_savings))
            print('Best saving rate:{}'.format(portion_saved))
            return ('Steps in bisection search: {}'.format(steps))
        elif low == high:
            return ("Sorry your salary is not sufficient to save for the Downpayment in 36 months, {}, {}".format(low, high))
        if (i == 36):
            if abs(portion_down_payment - current_savings) < 100:
                print('Steps in bisection search: {} \n portion saved is {}'.format(
                    steps, portion_saved))
            elif portion_saved > 0.99:
                return "It is not possible to pay the down payment in three years."
            elif abs(portion_down_payment - current_savings) > 100:
                if portion_down_payment > current_savings:
                    return Binary_Search_Recursive(annual_salary, mid, high, steps)
                elif current_savings > portion_down_payment:
                    return Binary_Search_Recursive(annual_salary, low, mid, steps)
                return Binary_Search_Recursive(annual_salary, mid, high, steps)

    return True


print(Binary_Search_Recursive(annual_salary, low, high, steps))
