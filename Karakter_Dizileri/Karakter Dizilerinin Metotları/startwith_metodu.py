veri = "batuhan"

print(veri.startswith("b"))

#True

print(veri.startswith("n"))

#False

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"

for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.startswith("p"):
        print(i)