import requests
from bs4 import BeautifulSoup

url = 'https://www.udemy.com/course/complete-python-developer-zero-to-mastery/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1', {'data-purpose': 'lead-title'}).text
headline = soup.find('div', {'data-purpose': 'lead-headline'}).text
rating = soup.find('span', {'data-purpose': 'rating-number'}).text

course_objectives = soup.find('ul', {'class': "ud-unstyled-list ud-block-list what-you-will-learn--objectives-list--eiLce what-you-will-learn--objectives-list-two-column-layout--rZLJy"})
# print(title)
# print(headline)
# print(rating)

print(course_objectives)

object_items = course_objectives.find_all('li')

print(object_items)

summary_bullets = {}

for index, val in enumerate(object_items):
    summary_bullets[index] = val.text

print(summary_bullets)

# Probajte izvući još Description, Last updated date

# Probajte napraviti generalnije rješenje gdje korisnika pitate da unese url od coursea, a vi mu isprintate neke detalje o tom kursu.

# Sve podatke ispišite u nekom lijepom formatu.