# 1. CONTOUR
# 2. EDGE_ENHANCE
# 3. EDGE_ENHANCE_MORE
# 4. EMBOSS
# 5. FIND_EDGES
# 6. SHARPEN
# 7. SMOOTH
# 8. SMOOTH_MORE
# 9. BoxBlur
# 10. GaussianBlur
# 11. UnsharpMask
# 12. MaxFilter
# 13. MedianFilter
# 14. MinFilter

# 1. Importamo potrebni modul
from PIL import Image, ImageFilter, ImageDraw

# 2. Učitamo fotografiju u varijablu
img = Image.open('./Algebra_campus.jpg')

# 3. Primjena filtera
# img1 = img.filter(ImageFilter.CONTOUR).show()
# img2 = img.filter(ImageFilter.EDGE_ENHANCE).show()
# img3 = img.filter(ImageFilter.SMOOTH).show()
# img4 = img.filter(ImageFilter.EMBOSS).show()

# help(ImageFilter.MedianFilter)

# img5 = img.filter(ImageFilter.MaxFilter(size=7)).show()

img_draw = ImageDraw.Draw(img)
img_draw.rectangle((800, 500, 3400, 2200), fill = None, outline = 'red', width = 5)

img.show()

img_draw.ellipse((800, 500, 3400, 2200), fill=None, outline='red', width=5)
img.show()