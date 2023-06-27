import time
import os

import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz
import locale
import dateutil


sadasnji_trenutak = dt.datetime.now()

# datum_korisnik = input('Upišite proizvoljan datum i vrijeme u formatu: "dan. naziv_mjeseca godina. sati:minuta:sekunda" ')

# datum_objekt = dt.datetime.strptime(datum_korisnik, '%d. %B %Y. %H:%M:%S')

# print(datum_korisnik)

# print(datum_objekt)

# razlika = datum_objekt - sadasnji_trenutak

# print(razlika)

# zbroj = datum_objekt + sadasnji_trenutak

# print(zbroj)

# Koji datum će biti za 14 dana od danasnjeg datuma
za_14_dana = sadasnji_trenutak + dt.timedelta(days=14)
# print(za_14_dana)

# parametri za timedelta su: days, seconds, microseconds, miliseconds, minutes, hours, weeks
danas = dt.date.today()
jucer = danas - dt.timedelta(days = 1)
sutra = danas + dt.timedelta(days = 1)

print(f'Jučerašnji datum je: {jucer}')
print(f'Današnji datum je: {danas}')
print(f'Sutrašnji datum je: {sutra}')

### DATEUTIL MODUL ###
# dateutil.relativedelta - više mogućnosti u odnosu na datetime.timedelta()
# '''
#     Definition:   relativedelta.relativedelta(self, dt1=None, dt2=None,
#     years=0, months=0, days=0, leapdays=0, weeks=0, hours=0, minutes=0,
#     seconds=0, microseconds=0, year=None, month=None, day=None,
#     weekday=None, yearday=None, nlyearday=None, hour=None, minute=None,
#     second=None, microsecond=None)
# '''

# Koji datum je zadnji petak (FRiday) u ovom mjesecu

rd = relativedelta(day=31, weekday=FR(-1))
print(rd)

print(sadasnji_trenutak + relativedelta(day=31, weekday=FR(-1)))

### VREMENSKA ZONE ###
# print(tz.tzlocal)

tz_zg = tz.gettz('Europe/Zagreb')
termin_zg = dt.datetime(2021, 3, 29, tzinfo = tz_zg)

print(termin_zg)

tz_ny = tz.gettz('America/New_York')
termin_ny = termin_zg.astimezone(tz_ny)

termin_utc_ny = dt.datetime(2021, 3, 29, tzinfo = tz_ny)
print(termin_ny)
print(termin_utc_ny)