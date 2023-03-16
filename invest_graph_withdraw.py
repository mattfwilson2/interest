##### TO-DOS #####
# Add in birthdate to calculate time to required retirement withdrawal
# Add function that calculates interest only
# Create stacked bar graphs showing individual principal vs interest growth

import matplotlib
matplotlib.use('TkAgg', force=True)
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import datetime

principal = 675000
int_rate = .075
num_comp = 12
comp_years = 13
counter = 0
contribution = 30000
withdrawal = 70000
age = 36
x_labels = []
y_labels = []
year_totals = []
year_labels = []

# compounding func appending each year to total list
def calc_investing(principal, rate, num_comp, time, contribution, counter):
    for year in range(time):
        principal += contribution
        amount = principal * (pow((1 + rate / num_comp), num_comp * (year + 1)))
        year_totals.append(amount)
        print(f'Year {year + 1} - ${round(amount, 2)}')
        counter += 1
    return amount, counter

def calc_retirement(principal, rate, num_comp, withdraw, counter):
    while principal > 0:
        if principal > withdraw:
            principal -= withdraw
            year_totals.append(principal)
            print(f'Year {counter + 1} - ${round(principal, 2)}')
            counter += 1
        else:
            principal -= principal
    return principal, counter

# count increment for graph tick labels
principal, counter = calc_investing(principal, int_rate, num_comp, comp_years, contribution, counter)
retire_years, counter = calc_retirement(principal, int_rate, num_comp, withdrawal, counter)

print(f'Investment years: {principal}')
print(f'Retirement years: {retire_years}')
print(len(f'X labels: {x_labels}'))
print(len(f'Y labels: {y_labels}'))
print(f'Total Accrued: {year_totals}')

percentage = '{:.2%}'.format(int_rate)
round_dollars = round(principal, 2)
comma_dollars = '{:,}'.format(round_dollars)

today = datetime.date.today()  
current_year = today.year
for i in year_totals:
    year_labels.append(current_year)
    current_year += 1  
print(year_labels)
print(len(year_labels))
print(len(year_totals))

# graph data with matplot
fig, ax = plt.subplots(figsize=(14, 9))
fig.suptitle(f'Compound principal + accrued interest over {comp_years} years', fontsize='20', fontweight='bold')
plt.title(f'Interest: {percentage} -- Retire year peak: ${comma_dollars} -- {age + len(year_totals)} years old when savings runs out', fontsize='12', fontweight='regular')

colors = ['yellowgreen' if i < max(year_totals) else 'olivedrab' for i in year_totals]
plt.bar(range(counter), year_totals, tick_label=year_labels, width=.5, color=colors)
plt.xticks(rotation=90)
plt.ylabel('Total value (millions)', fontweight='bold')
ax.xaxis.set_label_coords(.5, -.1)
plt.xlabel('Years of compounding/withdrawing', fontweight='bold')
ax.yaxis.set_label_coords(-.05, .5)

plt.show()