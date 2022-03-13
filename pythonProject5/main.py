"""
Kaveh Masoudinia
section 1 exercise 5
"""
good_perf=(10*3)/100
bad_perf=-(10*3)/100
performance=input("Enter your employee's performance (good/bad):")
num_years=int(input("Enter number of years:"))
if performance == 'good':
    new_pay = 10 * (1 + good_perf) ** num_years
elif performance == 'bad':
    new_pay = 10 * (1 + bad_perf) ** num_years
print(int(new_pay))