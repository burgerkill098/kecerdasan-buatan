from ast import operator
from re import X


print("======================")
print("KALKULATOR SEDERHANA ")
print("======================")

operator = input("operator (+,-,*,/) :")
angka_1= float(input("masukan angka 1 ="))
angka_2= float(input("masukkan angka 2 ="))

if operator == "+":
    hasil =angka_1+angka_2
    print(f"hasilnya adalah {hasil}")
elif operator =="-":
    hasil= angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator =="*":
    hasil= angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator =="/":
    hasil= angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")