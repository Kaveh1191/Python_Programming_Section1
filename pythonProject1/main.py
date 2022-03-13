"""
Kaveh Masoudinia
section 1 exercise 1
"""
a=int(input("Enter number of eggs:"))
print("number of complete boxes of eggs:",a//6)
print("number of eggs left",a%6)
print("This amount of eggs is needed to complete the box",6-(a%6))