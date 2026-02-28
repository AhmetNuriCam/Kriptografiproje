import os


TURKISH_ALPHABET = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
ALPHABET_LEN = len(TURKISH_ALPHABET)

def _clean_key_tr(key: str) -> str:
    key = key.upper()
    cleaned = "".join(ch for ch in key if ch in TURKISH_ALPHABET)
    if not cleaned:
        raise ValueError("Anahtar Türk alfabesinden en az bir harf içermeli.")
    return cleaned

def vigenere_encrypt_tr(text: str, key: str) -> str:
    key = _clean_key_tr(key)
    result = []
    key_index = 0

    for ch in text:
        upper_ch = ch.upper()
        if upper_ch in TURKISH_ALPHABET:
            p = TURKISH_ALPHABET.index(upper_ch)
            k = TURKISH_ALPHABET.index(key[key_index % len(key)])
            c = (p + k) % ALPHABET_LEN

            enc = TURKISH_ALPHABET[c]
            if ch.islower():
                enc = enc.lower()

            result.append(enc)
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)

def vigenere_decrypt_tr(text: str, key: str) -> str:
    key = _clean_key_tr(key)
    result = []
    key_index = 0

    for ch in text:
        upper_ch = ch.upper()
        if upper_ch in TURKISH_ALPHABET:
            c = TURKISH_ALPHABET.index(upper_ch)
            k = TURKISH_ALPHABET.index(key[key_index % len(key)])
            p = (c - k) % ALPHABET_LEN

            dec = TURKISH_ALPHABET[p]
            if ch.islower():
                dec = dec.lower()

            result.append(dec)
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)



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
    

def sezar_sifre(metin: str, kaydirma: int) -> str:
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
    return sezar_sifre(sifreli, -kaydirma)



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

def atbash_sifrele(metin: str) -> str:
    """Her harfi alfabenin ayna karakteriyle değiştirir (A↔Z, B↔Y …).
    Atbash kendi tersidir; şifreleme = deşifreleme."""
    sonuc = []
    for karakter in metin:
        if karakter.isalpha():
            if karakter.isupper():
                yeni_harf = chr(ord('Z') - (ord(karakter) - ord('A')))
            else:
                yeni_harf = chr(ord('z') - (ord(karakter) - ord('a')))
            sonuc.append(yeni_harf)
        else:
            sonuc.append(karakter)
    return "".join(sonuc)


def atbash_desifrele(sifreli: str) -> str:
    """Atbash simetriktir; aynı fonksiyon deşifre için de kullanılır."""
    return atbash_sifrele(sifreli)




title()
secim = algoritma_sec()

if secim == "2":   
    mesaj = input("Lütfen metni girin: ")
    anahtar = input("Anahtar kelimeyi girin: ")
    islem = islem_sec()

    if islem == "1":
        print("Şifreli metin:", vigenere_encrypt_tr(mesaj, anahtar))
    else:
        print("Çözülmüş metin:", vigenere_decrypt_tr(mesaj, anahtar))

elif secim == "3":  # Senin mevcut XOR akışın
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

