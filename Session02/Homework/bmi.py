print("BMI Test")
h_cm = int(input("Nhap chieu cao cua ban (cm) "))
m_kg = int(input("Nhap can nang cua ban (kg)"))
h_m = h_cm / 100
b = m_kg / (h_m ** 2)
if b < 16 :
  print("Severely Underweight")
elif b < 18.5 :
  print("Underweight")
elif b < 25 :
  print("Normal")
elif b < 30 :
  print("Overweight")
else :
  print("Obese")
