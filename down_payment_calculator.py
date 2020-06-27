# -*- coding: utf-8 -*-
"""
Author: Jonathan Ashbeck

Name: Months to Save for Down Payment on Dream Home

Description: Calculates the number of months required to save in order to afford the down payment on user's dream home, given user's input on the home cost, down payment, interest rate, salary, and amount to save.
"""
print('Name: Months to Save for Down Payment on Dream Home.\n')

# Check whether the following user inputs are real number values.
try:
	# Take user inputs.
	home_cost = float(input('Enter cost of home: '))
	home_down_payment_percent = float(input('Enter down payment percentage (ie, 0.25 for 25%): '))
	annual_interest_rate = float(input('Enter interest rate (ie, 0.05 for 5%): '))
	annual_salary = float(input('Enter your salary: '))
	annual_salary_saved_percent = float(input('Enter percentage of salary saved (ie, 0.25 for 25%): '))
except ValueError:
	raise ValueError('Inputs must be real number values.')


# Check whether user inputs are impossible for calculation. Else, proceed normally.
assert home_cost >= 0, 'The cost of your home must have a non-negative value.'
assert 0 <= home_down_payment_percent <= 1, 'Home down payment percentage must range between 0 and 1.'
assert 0 <= annual_interest_rate <= 1, 'Annual interest rate must range between 0 and 1.'
assert annual_salary >= 0, 'Cannot have a negative salary.'
assert 0 <= annual_salary_saved_percent <= 1, 'Percentage salary saved must range between 0 and 1.'

if annual_salary == 0 or annual_salary_saved_percent == 0:
	print('\n\nResult:\n\tIt is not possible to save up for the down payment. Salary is $0, or no portion of salary is saved.')
else:
	current_savings = 0
	months = 0
	monthly_salary = annual_salary / 12
	monthly_interest_rate = annual_interest_rate / 12

	# Increment current savings according to interest rates and portion saved until savings meets or exceeds down payment on home.
	while current_savings < home_down_payment_percent * home_cost and months <= 1200:
		current_savings = current_savings * (1 + monthly_interest_rate) + annual_salary_saved_percent * monthly_salary
		months += 1

	if months > 1200:
		raise OverflowError('It will take in excess of 1200 months (100 years) to afford down payment.')
	else:
		print(f'\n\nResult:\n\tYou need to save for {months} months to afford down payment.')		