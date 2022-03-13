"""
Kaveh Masoudinia
section 1 exercise 4
"""
a=int(input("Enter your seconds to convert:"))
hour=a//3600
min=(a%3600)//60
sec=(a%3600)%60
print(hour,"_",min,"_",sec)