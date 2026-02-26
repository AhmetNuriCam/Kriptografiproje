
import os

def caesar_sifrele(metin: str, kaydirma: int) -> str:
    """Her harfi alfabe üzerinde <kaydirma> adım ilerletir."""
    sonuc = []
    for karakter in metin:
        if karakter.isalpha():
            baslangic = ord('A') if karakter.isupper() else ord('a')
            yeni_harf = chr((ord(karakter) - baslangic + kaydirma) % 26 + baslangic)
            sonuc.append(yeni_harf)
        else:
            sonuc.append(karakter)   
    return "".join(sonuc)


def caesar_desifrele(sifreli: str, kaydirma: int) -> str:
    """Caesar şifresini tersine çevirir."""
    return caesar_sifrele(sifreli, -kaydirma)


