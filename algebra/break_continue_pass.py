# Ponekad želimo izvršavanje petlje završiti prije kraja - 'nasilno izaći' 
# Za to imamo BREAK

for slovo in 'Python Programer':
    print(slovo, end=' ')
print()

# PITANJE: Što ako želimo da se petlja prestane izvršavati kad dođe do slova 'g'
# ODGOVOR: Dodat ćemo IF uvjer ako je slovo jednako 'g' napravi BREAK

for slovo in 'Python Programer':
    if slovo == 'g':
        break
    print(slovo, end = ' ')
print()

# Ovakva konstrukcija znači beskonačnu petlja:
while True:
    print('Pozdrav iz potencijalno beskonačne WHILE petlje s True uvjetom!')

    # Korisnik mora unijeti 1 ili 0
    odgovor = int(input('Želite li prekinuti ovu petlju? (Da=1/Ne=0)'))
    if odgovor == 1:
        print('\nViše NIJE potencijalno beskonačna WHILE petlja s True uvjetom. Upravo je završila')
        break
    else:
        pass

# Nekada imamo situaciju da NE želimo izaći iz petlje, ali želimo da se jedan ili više ciklusa
# ne izvrši do kraja, nego da se preostali dio PRESKOČI i ako su ispunjeni uvjeti započne novi ciklus
# Za to koristimo naredbu CONTINUE!

for slovo in 'Python Programer':
    if slovo == 'g':
        continue    
    print(slovo, end = ' ')
print()