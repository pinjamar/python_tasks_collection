import cv2
import numpy

# Definirajmo foto datoteku s kojom ćemo raditi !
fotografija = 'Algebra_greyp.jpg'

# Uvezimo predefinirane modele iz OpenCV repozitorija
model = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'weights.caffemodel')

# Učitajmo fotografiju pomoću imread
fotografija_cv2 = cv2.imread(fotografija)

print(fotografija_cv2.shape)

(height, width) = fotografija_cv2.shape[:2]

# Nakon obrade dohvatimo "blob" (Binary large object)

blob_image = cv2.dnn.blobFromImage(fotografija_cv2)

# Propustimo našu sliku kroz model
model.setInput(blob_image)

detektirana_lica = model.forward()

print(detektirana_lica.shape)
print(detektirana_lica)
# # Sada kada imamo prepoznavanje, prodimo kroz listu i oznacimo ih na fotografiji
broj_lica = 0
for i in range(0, detektirana_lica.shape[2]):
    okvir = detektirana_lica[0, 0, i, 3:7] * numpy.array([width, height, width, height])
    (startX, startY, endX, endY) = okvir.astype('int')

    # Broj prepoznatih lica ja jako velik. Pomocu postotka kolika je vjerojatnost da je sekcija slike
    # u stvari prepoznato lice, mozemo se "igrati" s prikazom pravokutnika.
    # Iz ovog primjer: ako je vjerojatnost veca od 14%, onda iscrtaj okvir na slici
    vjerojatnost = detektirana_lica[0, 0, i, 2]
    if (vjerojatnost > 0.140):
        cv2.rectangle(fotografija_cv2, (startX, startY), (endX, endY), (0, 255, 0), 2)
        broj_lica += 1

cv2.imshow('Pronađena lica', fotografija_cv2)
cv2.waitKey()
