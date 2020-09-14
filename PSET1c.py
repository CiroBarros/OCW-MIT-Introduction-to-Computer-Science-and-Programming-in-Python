# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:18:02 2020

@author: Ciro Barros
"""

total_cost = 1000000
down_payment = total_cost/4
semi_annual_raise = .07
annual_return = 0.04
r_per_month = 1.04**(1/12)-1
possible_to_pay = True
annual_salary = float(input("Enter the starting salary: "))
# Bisection search
begin = 0
end = 10000
guess = end
steps = 0
while True:
    steps += 1
    month_salary = annual_salary/12
    current_savings = 0
    rend_month = current_savings*r_per_month
    best_saving_rate = guess/10000
    month_save = month_salary*best_saving_rate
    months = 0  
    while months <= 36:
        current_savings += month_save + rend_month
        rend_month = current_savings*r_per_month
        months += 1
        if months % 6 == 0:
            month_salary += month_salary*semi_annual_raise
            month_save = month_salary*best_saving_rate
    if abs(current_savings - down_payment) <= 100:
        break
    if current_savings > down_payment:
        end = guess
    elif current_savings < down_payment:
        begin = guess
    if begin == end:
        possible_to_pay = False
        break
    guess = (end+begin)/2
if possible_to_pay:
    print("Best savings rate:", best_saving_rate)
    print("Steps in bisection search:", steps)
else:
    print("It's not possible to pay the down payment in three years")
        
    
    


