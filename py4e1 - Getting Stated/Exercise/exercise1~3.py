# Exercise1
print("hello world")

# Exercise2.3
hrs = input("Enter Hours:")
rate = input("Enter rate:")
pay = float(hrs) * float(rate)
print(pay)

# Exercise3.1
hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
if h > 40:
  pay = 40 * r + (h-40) * 1.5 * r
    
else:
  pay = h * r

print(pay)

# Exercise3.3
score = input("Enter Score: ")
grade = ""
try:
    fs = float(score)
except:
    print("wrong input")
    quit()

if fs >= 0.9:
    grade = "A"
elif fs >= 0.8:
    grade = "B"
elif fs >= 0.7:
    grade = "C"
elif fs >= 0.6:
    grade = "D"
elif fs < 0.5:
    grade = "F"
print(grade)