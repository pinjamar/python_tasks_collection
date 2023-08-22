# Kao i uvijek potrebno je importati željeni modul
from PIL import Image

# help(Image)

fotografija_putanja = './Algebra_campus.jpg'

# Pomoću Image.open() možemo fotografija učitati u varijablu
fotografija_varijabla = Image.open(fotografija_putanja)

print(fotografija_varijabla)

print()
print(f"Format slike:\t{fotografija_varijabla.format}.")
print(f"Mod slike:\t{fotografija_varijabla.mode}.")
print(f"Dimenzija slike:\t{fotografija_varijabla.size}.")
print()

# fotografija_varijabla.show()

# help(fotografija_varijabla.crop)

print(fotografija_varijabla.size)

lijevo = 0 + 500
gore = 0 + 500
desno = fotografija_varijabla.size[0] - 500
dolje = fotografija_varijabla.size[1] - 500

fotografija_varijabla_crop = fotografija_varijabla.crop((lijevo, gore, desno, dolje))

# fotografija_varijabla.show()
# fotografija_varijabla_crop.show()

# Želimo pohraniti izmijenjenu foto datoteku
# fotografija_varijabla_crop.save('Algebra_campus_crop.jpg', 'JPEG')
# fotografija_varijabla_crop.save('Algebra_campus_crop.png', 'PNG')

# help(fotografija_varijabla.convert)

fotografija_varijabla_convert = fotografija_varijabla.convert(mode = 'L')

# fotografija_varijabla_convert.show()

# fotografija_varijabla_convert.save('Algebra_campus_convert.jpg', 'JPEG')

# Sad želimo dobiti sliku u slici pomoću .paste() naredbe
# Učitat ćemo python logo u varijablu

fotografija_python_logo = Image.open('./Python_logo_and_wordmark.png')

# help(fotografija_varijabla.paste)

print(fotografija_python_logo.size)
print(fotografija_varijabla.size)

# fotografija_varijabla.paste(fotografija_python_logo, (500, 300))
# fotografija_varijabla.show()

# help(fotografija_varijabla.transpose)

# fotografija_trans_TB = fotografija_varijabla.transpose(Image.FLIP_TOP_BOTTOM).show()
# fotografija_trans_LR = fotografija_varijabla.transpose(Image.FLIP_LEFT_RIGHT).show()
# fotografija_trans_TS = fotografija_varijabla.transpose(Image.TRANSPOSE).show()
# fotografija_trans_TV = fotografija_varijabla.transpose(Image.TRANSVERSE).show()

help(fotografija_varijabla.close)