'''
    This program Calculate Simple Rate of intrest Earn Intrest and Per month EMI
'''

# Finding Simple Intrest Function
def SI(p,r,t):
    K = (p*r*t)/100
    return K

# Takin User Input 
P = float(input("Enter Principal : "))
R = float(input("Enter Rat Of Intrest : "))
T = float(input("Enter Time in Year : "))

# Fatchin Value Frome SI Function and stor in si Variable
si = SI(P,R,T)

# Calculating Permonth EMI Pyable of Customer
prM = (si+P)/(T*12)

#Finasl Output of Resul
print(f"Principal Amount is = {P} \n Earn Intrest = {si} \n Total Amount is = {si + P}")
print(f"\n Per Month Amount is {prM}")

print("Follow : https://github.com/javid14395")