### DATETIME MODUL ###

import datetime as dt
import locale # modul za uključivanje lokalizacije - nacin prikazivanja datuma, valuta, vremena itd.

### DANASNJI DATUM

# datetime modul ima dvije klase, date i datetime
# date je zadužen samo za datume (godina, mjesec, dan)

danasnji_dan = dt.date.today()
print(f'\nDanasnji dan je {danasnji_dan}.')

# Dobiveni datum je u tzv ISO formatu ispisa datuma YYYY-MM-DD

# datetime je zaduzen za detalje o datumu i VREMENU
sadasnji_trenutak = dt.datetime.now()
print(f'\nSadasnji trenutak je {sadasnji_trenutak}.')

# format ispisa je u obliku YYYY-MM-DD HH:MM:SS.MS

### ISPIS DATUMA I VREMENA ###

### DAN U TJEDNU ###
dan_u_tjednu = dt.date.weekday(danasnji_dan)
print(f'Danas je {dan_u_tjednu}. dan u tjednu')

if dan_u_tjednu == 0:
    print(f'Danas je PONEDJELJAK, {dan_u_tjednu + 1}. dan u tjednu\n')
elif dan_u_tjednu == 1:
    print(f'Danas je UTORAK, {dan_u_tjednu + 1}. dan u tjednu\n')
elif dan_u_tjednu == 2:
    print(f'Danas je SRIJEDA, {dan_u_tjednu + 1}. dan u tjednu\n')
elif dan_u_tjednu == 3:
    print(f'Danas je ČETVRTAK, {dan_u_tjednu + 1}. dan u tjednu\n')
elif dan_u_tjednu == 4:
    print(f'Danas je PETAK, {dan_u_tjednu + 1}. dan u tjednu\n')
elif dan_u_tjednu == 5:
    print(f'Danas je SUBOTA, {dan_u_tjednu + 1}. dan u tjednu\n')
else:
    print(f'Danas je NEDJELJA, {dan_u_tjednu + 1}. dan u tjednu\n')

# Kada želimo dobiti podatak o danu u tjednu, a da ne pišemo ogromnu IF petlju,
# koristimo metodu za pretvaranje datetime varijable u string - .strftime(nacin_formatiranja)

print('DAN U TJEDNU "%A - puni naziv i "%a" - skraceni naziv')
print(f'Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime("%A")}.')
print(f'Skraceni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime("%a")}.')
print()
print()

# Gornji prikaz ispisuje nazive dana na jeziku na kojem je vaše računalo
# pomoću modula locale podesimo jezik i pozovemo iste naredbe

# 1. KORAK - podesimo jezik samo za vrijeme 
locale.setlocale(locale.LC_TIME, 'hr_HR')

# 2. KORAK pozovimo iste naredbe
print('DAN U TJEDNU "%A - puni naziv i "%a" - skraceni naziv')
print(f'Puni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime("%A")}.')
print(f'Skraceni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime("%a")}.')

print(f'Skraceni naziv danasnjeg dana u tjednu je {danasnji_dan.strftime("%A")[:3]}.')

# 3. KORAK vratimo postavke jezika na sistemske postavke
locale.setlocale(locale.LC_ALL, '')

### ISPIS GODINE ###
# Pomoću strftime() mozemo ispisati samo dio koji prikazuje koji je mjesec u godini
print(f'Puni naziv mjeseca je: {danasnji_dan.strftime("%B")}')
print(f'Skraćeni naziv mjeseca je: {danasnji_dan.strftime("%b")}')
print(f'Današnji mjesec je: {danasnji_dan.strftime("%m")}')

### Dan u mjesecu ###
print(f'Danas je {danasnji_dan.strftime("%d")}. dan u mjesecu')

# DRUGACIJI PRIKAZ
print(f'Sadasnji trenutak: {sadasnji_trenutak.strftime("%A")}, {sadasnji_trenutak.strftime("%d.%m.%Y %H:%M:%S")}')