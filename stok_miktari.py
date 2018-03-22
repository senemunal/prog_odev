stok_miktari=10000
i=0
alinan_urun=100
satilan_urun=500
fark=alinan_urun-satilan_urun
while(stok_miktari>0):  # tam tersi işaret çünkü 0 dan büyük olduğu sürece döngü çalışacak 0 olduğunda çalışmayacak.
    stok_miktari=stok_miktari+fark #fark - çıktığı için + yaptık.
    i=i+1
print(i,". ayda stok sıfırlanmıştır.")