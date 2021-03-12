'''
ada seorang guru ingin membuat 5 soal penjumlahan angka 1 - 100 untuk muridnya.
guru tsb ingin membuat soal yang berbeda untuk setiap muridnya.
namun guru tersebut sangat malas untuk membuat soal, malas mengkoreksi, dan malas memberikan nilai.
jika nilai kurang dari 60 maka murid tidak lulus.
jikai nilai lebih dari sama dengan 60 maka murid lulus.
lalu guru membuat program menggunakan python.

'''

import random
benar = 0


a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
jawaban = int(input("{} + {} = ".format(a,b)))
if jawaban == c:
    benar+=1
else :
    benar+=0

a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
jawaban = int(input("{} + {} = ".format(a,b)))
if jawaban == c:
    benar+=1
else :
    benar+=0

a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
jawaban = int(input("{} + {} = ".format(a,b)))
if jawaban == c:
    benar+=1
else :
    benar+=0

a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
jawaban = int(input("{} + {} = ".format(a,b)))
if jawaban == c:
    benar= benar + 1
else :
    benar+=0

a = random.randint(0,100)
b = random.randint(0,100)
c = a+b
jawaban = int(input("{} + {} = ".format(a,b)))
if jawaban == c:
    benar+=1
else :
    benar+=0

nilai = benar*20
print("nilai murid : {}".format(nilai))

if nilai <60:
    print("tidak lulus")

elif nilai <= 100 and nilai>=60:
    print("lulus")
   