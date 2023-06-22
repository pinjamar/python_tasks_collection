# ZADATAK: Kreiraj funkciju koja pretvara udaljenost u km u milje. Funkcija treba primiti samo udaljenost u km,
# a vratiti udaljenost u miljama
# formula: miles = kilometers * 0.6214

# Neka naš program pita usera da unese udaljenost u km, a on mu vrati udaljenost u miljama
# Isprintajte formatiranu rečenicu oblika: Udaljenost xyz u km odgovara udaljenosti xyz u miljama

def kilometers_to_miles(distance_in_kilometers):
    return distance_in_kilometers * 0.6214

    # distance_in_miles = distance_in_kilometers * 0.6214
    # return distance_in_miles

kilometers = float(input('Unesite udaljenost u km:\t'))

print(f'Udaljenost {kilometers} km odgovara udaljenosti {kilometers_to_miles(kilometers)} u miljama')

# ZADATAK: Modificiraj gornju funkciju da osim što korisnik unosi udaljenost, unese i u kojoj je mjernoj
# jedinici ta udaljenost. Ako unese da je u km vrati mu milje, a ako unese da je u miljama vrati mu u km

