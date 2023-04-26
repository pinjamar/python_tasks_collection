#Docstring (dokumentacijski kod) pise se unutar trostrukih navodnika, na pocetku bilo da je rijec o funkciji, metodi, klasi ili modulu

# primjer docstring kod funkcije

def povrsinaPravokutnika(a,b):
    '''Funkcija povrsinaPravokutnika za pravokutnik s duljinama stranica a i b vraca njenu povrsinu'''
    povrsina = a * b
    return povrsina

x = 5
y = 7

print('pravokutnik sa stranicama a=', x, 'i b=', y, 'ima povrsinu', povrsinaPravokutnika(x,y), '\b. \n')

#ispis dokumentacijskog koda iz funkcije povrsinaPravokutnika

print(povrsinaPravokutnika.__doc__)