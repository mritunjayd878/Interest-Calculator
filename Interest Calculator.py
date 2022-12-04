p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time for interest in months: "))
I=p*r*t/1200
n=int(input("How the rate of interest has been implemented, for monthly enter 2,for quaterly enter 4, for half yearly enter 2, for yearly enter 1 : "))
t=t/n
CI=p*(1+r/(n*100))**(n*(t/12))-p
A1=p+I
A2=p+CI

print("Simple Interest is: ", I)
print("Amount with SI: ", A1)
print("Compound Interest is: ", CI)
print("Amount with CI: ", A2)


