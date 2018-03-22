toplam=0
while True:
    print('Bir sayı giriniz, Çıkış için 0(sıfır)ı tuşlayınız.')
    girilen=int(input('Sayi: ')) #şart olduğu için True kullandık.
    if (girilen!=0):
        y=girilen%3
        toplam=toplam+y
        print('Toplam=',toplam)
    else:
        print('Çıkış yapıldı.')
        break #kodu durduruyor.