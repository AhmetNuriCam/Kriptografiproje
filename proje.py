
import os

def title():
    print("=" * 55)
    print("   ŞİFRELEME / DEŞİFRELEME UYGULAMASI")
    print("=" * 55)
    print("  Algoritmalar:")
    print("    1) Caesar   — kaydırma değeri ile")
    print("    2) Vigenere — anahtar kelime ile")
    print("    3) XOR      — anahtar kelime ile")
    print("    4) Atbash   — anahtar gerekmez")
    print("=" * 55)


def algoritma_sec() -> str:
    print("\nHangi algoritmayı kullanmak istersiniz?")
    print("  [1] Caesar")
    print("  [2] Vigenere")
    print("  [3] XOR")
    print("  [4] Atbash")
    tercih = input("Seçiminiz (1-4): ").strip()
    return tercih


def islem_sec() -> str:
    print("\nİşlem seçin:")
    print("  [1] Şifrele")
    print("  [2] Deşifrele")
    tercih = input("Seçiminiz (1-2): ").strip()
    return tercih
    
def sezar_sifre(metin: str, kaydirma: int) -> str
    sonuc = []
    for karakter in metin:
        if karakter.isalpha():
            baslangic = ord('A') if karakter.isupper() else ord('a')
            yeni_harf = chr((ord(karakter) - baslangic + kaydirma) % 26 + baslangic)
            sonuc.append(yeni_harf)
        else:
            sonuc.append(karakter)   
    return "".join(sonuc)


def sezar_desifre(sifreli: str, kaydirma: int) -> str:
    return caesar_sifrele(sifreli, -kaydirma)



def xor_islemi(metin, anahtar):
    sonuc = ""
    anahtar_uzunluk = len(anahtar)
    
    if anahtar_uzunluk == 0:
        return metin
        
    for i in range(len(metin)):
        metin_karakteri = metin[i]
        anahtar_karakteri = anahtar[i % anahtar_uzunluk]
        
        xor_degeri = ord(metin_karakteri) ^ ord(anahtar_karakteri)
        sonuc += chr(xor_degeri)
        
    return sonuc

print("MESAJ SIFRELEYICIYE HOS GELDINIZ ")

girilen_metin = input("Lutfen sifrelemek istediginiz metni yazin: ")
anahtar = input("Gizli anahtar kelimenizi belirleyin: ")

sifreli_sonuc = xor_islemi(girilen_metin, anahtar)

print("Sifreli metin:", repr(sifreli_sonuc)) 

cozum_anahtari = input("Sİfreyi cozmek için anahtar kelimeyi girin: ")

if cozum_anahtari == anahtar:
    cozulmus_sonuc = xor_islemi(sifreli_sonuc, cozum_anahtari)
    print("Cozulmus Metin :", cozulmus_sonuc)
else:
    print("\nHATALI SIFRE! Erisim reddedildi.")
