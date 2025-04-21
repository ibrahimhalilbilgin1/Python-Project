import random
sayi=random.randint(1,20)
can=int(input('kaç hak kullanarak bilebilirsin?: '))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahminin: '))
    if sayi==tahmin:
        print(f'Sayıyı {sayac}. hakkınızda doğru tahmin ettiniz.Puanınız { 100-((100/can)*(sayac-1))} puandır')
        break
    elif sayi>tahmin:
        print('Sayı değeri daha yüksek bir değer')
    else:
        print('Sayı değeri daha düşük bir değer ')
    if hak==0:
        print(f'tahmin hakkınız bitmiştir.ÜZGÜNÜZ...Tahmin etmeye çalıştığın sayı {sayi} idi')