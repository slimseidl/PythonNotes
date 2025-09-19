# Inputs
# Gross Income
# # of dependents 
# 12,200 total deductions, 200 for each dependent

# Pseudocode

# User Input: gross income
# User Input: number of dependents
 
# taxable income = gross income - 12,200 - (2000 * number of dependents)
# tax due = amount calculated from tax table
 
# print tax due


gross = float(input("What is your gross income according to your W-2?\n"))
dependents = int(input("How many dependents are you claiming?\n"))

def tax_income(inc,deps):
    tax_inc = inc - 12200 - (2000*deps)
    tax_due = tax_inc * 0.1
    return tax_due

print(tax_income(gross,dependents))

tax_inc = gross - 12200 - (2000*dependents)
tax_due = tax_inc * 0.1

if tax_due <= 9875:
    tax_due = tax_inc *.1
tax_due = (9875 * .1) + ((tax_inc - 9875) * .12)




