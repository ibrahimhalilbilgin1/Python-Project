def toplama(x, y):  
    return x + y  

def cikarma(x, y):  
    return x - y  

def carpma(x, y):  
    return x * y  

def bolme(x, y):  
    if y != 0:  
        return x / y  
    else:  
        return "Bir sayıyı sıfıra bölemezsiniz!"  

print("Hesap Makinesi")  
print("1. Toplama")  
print("2. Çıkarma")  
print("3. Çarpma")  
print("4. Bölme")  

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")  

sayi1 = float(input("Birinci sayıyı girin: "))  
sayi2 = float(input("İkinci sayıyı girin: "))  

if secim == '1':  
    print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")  
elif secim == '2':  
    print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")  
elif secim == '3':  
    print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")  
elif secim == '4':  
    print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")  
else:  
    print("Geçersiz seçim!")
