rijec = "programiranje"

for slovo in rijec:
    print(slovo)
print("\n\n")

print(f"Broj slova u rijeci programiranje je {len(rijec)}")
print()
# print(f"Broj slova u rijeci {rijec} je {sum(rijec)}")
print()

rijec = "programiranje"
suma = 0

for slovo in rijec:
    ascii_kod = ord(slovo)
    suma += ascii_kod

print(f"Zbroj slova u rijeci {rijec} je {suma}")
