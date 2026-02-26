
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



