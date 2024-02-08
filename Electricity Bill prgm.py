Cr=input("Enter the value of the Current Reading: ")
Pr=input("Enter the value of the Previous Reading:")
T_r=(Cr - Pr)
if(T_r<=200):
    cpu=2
    amt=(T_r*cpu)
else:
    cpu=5
    amt=(T_r*cpu)
    print(T_r)
    print(cpu)
    print("cost of",T_r,"unit is",amt,"per unit",cpu) 