#Gross and Net salary of an Employee.
ecode=int(input("Employee Code:"))
ename=input("Employee Name:")
bsalary=int(input("Basic Salary:"))
hra=int(input("Housing Rent Allowance:"))
ta=int(input("Travelling Allowance:"))
da=int(input("Daily Allowance:"))
lic=int(input("Life Insurance Corporation:"))
it=int(input("income tax:"))
pf=int(input("Provident fund:"))
gsalary=bsalary+hra+ta+da
deduction=pf+lic+it
netsalary=gsalary-deduction
print("Gross Salary:",gsalary,"deduction Salary:",deduction,"netsalary:",netsalary)


