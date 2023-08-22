# uključiti OpenCV modul
import cv2

# Učitati ćemo prethodno trenirani model!

# NAPOMENA: Za posebne slučajeve ovo je potrebno odraditi "ručno" za što je
# potrebno jako puno podataka. 
# Dakle, trebali bismo jako puno fotografija na kojima je objekt koji želimo
# prepoznati.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Učitajmo fotgorafiju:
fotografija = cv2.imread('Algebra_greyp.jpg')

# Prepoznavanje objekta radi se na crno bijeloj fotografiji
# pa prije nego "propustimo" fotografiju kroz model, moramo je pretvoriti u crno bijelu
cb_fotografija = cv2.cvtColor(fotografija, cv2.COLOR_BGR2GRAY)

# Pokrenimo prepoznavanje željenih objekata. 
# Output će nam biti lista koordinata pravokutnih područja gdje su prepoznata lica!

prepoznata_lica = face_cascade.detectMultiScale(
    cb_fotografija,
    # Hiperparametri
    scaleFactor=1.1,
    minNeighbors = 5,
    minSize = (30, 30)
)

# Broj prepoznatih lica
print(f"Pronašao sam {len(prepoznata_lica)} lica!")

# Iscrtajmo pravokutnike iz liste koju smo dobili propuštanjem slike kroz model
for (x, y, w, h) in prepoznata_lica:
    cv2.rectangle(fotografija, (x,y), (x+w, y+h), (0, 255, 0), 2)

# Prikazi fotografiju s ucrtanim pravokutnicima na mjestima gdje je model "pronašao"
# ljude

cv2.imshow('Pronađena lica', fotografija)

# Zaustavi izvršavanje programa da bismo mogli vidjeti fotografiju
cv2.waitKey()