# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:17:15 2020

@author: Ciro Barros
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
month_salary = annual_salary/12
month_save = month_salary*portion_saved
downpay = total_cost/4
current_savings = 0
r = 0.04
rate_month = 1+r
r_month = rate_month**(1/12)-1
rend_month = current_savings*r_month
months = 0
while downpay > 0:
    current_savings += month_save + rend_month
    rend_month = current_savings*r_month
    downpay -= month_save + rend_month
    months += 1
print()
print("Number of months:", months)
    
    