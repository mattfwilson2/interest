import matplotlib.pyplot as plt
import pyautogui

age = 37
principal = 750000
int_rate = .06
int_accrued = 0
withdraw_rate = 30000
inflation = .02
num_comp = 1
ss_contribution = 2000
years = []
net_worth = []

def full_screen():
    pyautogui.hotkey('alt', 'space')
    pyautogui.hotkey('x')

def calc_retire(principal, age, int_accrued):
    old_principal = principal
    new_principal = principal * (pow((1 + int_rate / 100), 52))
    int_accrued = new_principal - old_principal
    new_principal -= withdraw_rate
    age += 1
    years.append(age)
    net_worth.append(new_principal)
    return new_principal, age, int_accrued

def show_graph():
    colors = ['red' if value < 0 else 'green' for value in net_worth]
    plt.bar(years, net_worth, color=colors)
    plt.xlabel('Retirement Years', fontweight='bold', fontsize=16)
    plt.ylabel('Net Worth', fontweight='bold', fontsize=16)
    plt.title(f'Withdrawing ${withdraw_rate:,} annually, growing at {int_rate}% with {inflation}% inflation', fontsize=26, fontweight='bold', y=1.04)
    plt.legend()

    full_screen()
    plt.show()

while age < 100:
    if principal < 0:
        break
    elif principal > 5000000:
        break
    else:
        if age > 61:
            principal += ss_contribution
            principal, age, int_accrued = calc_retire(principal, age, int_accrued)
        else:
            principal, age, int_accrued = calc_retire(principal, age, int_accrued)
        print(f'Age: {age} - Principal: {principal}')

show_graph()