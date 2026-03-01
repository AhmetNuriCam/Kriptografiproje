
import os


def caesar_sifrele(metin: str, kaydirma: int) -> str:
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
    return caesar_sifrele(sifreli, -kaydirma)




TURKCE_ALFABE = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
ALFABE_UZUNLUGU = len(TURKCE_ALFABE)  

def anahtar_temizle(anahtar: str) -> str:
    anahtar = anahtar.upper()
    temiz = "".join(harf for harf in anahtar if harf in TURKCE_ALFABE)
    if not temiz:
        raise ValueError("Anahtar Türkçe alfabesinden en az bir harf içermeli.")
    return temiz


def vigenere_sifrele(metin: str, anahtar: str) -> str:
    anahtar = anahtar_temizle(anahtar)
    sonuc = []
    anahtar_indeks = 0

    for karakter in metin:
        buyuk_karakter = karakter.upper()
        if buyuk_karakter in TURKCE_ALFABE:
            p = TURKCE_ALFABE.index(buyuk_karakter)
            k = TURKCE_ALFABE.index(anahtar[anahtar_indeks % len(anahtar)])
            sifrelenmis_harf = TURKCE_ALFABE[(p + k) % ALFABE_UZUNLUGU]
            if karakter.islower():
                sifrelenmis_harf = sifrelenmis_harf.lower()
            sonuc.append(sifrelenmis_harf)
            anahtar_indeks += 1
        else:
            sonuc.append(karakter)   

    return "".join(sonuc)


def vigenere_desifrele(sifreli: str, anahtar: str) -> str:
    anahtar = anahtar_temizle(anahtar)
    sonuc = []
    anahtar_indeks = 0

    for karakter in sifreli:
        buyuk_karakter = karakter.upper()
        if buyuk_karakter in TURKCE_ALFABE:
            c = TURKCE_ALFABE.index(buyuk_karakter)
            k = TURKCE_ALFABE.index(anahtar[anahtar_indeks % len(anahtar)])
            orijinal_harf = TURKCE_ALFABE[(c - k) % ALFABE_UZUNLUGU]
            if karakter.islower():
                orijinal_harf = orijinal_harf.lower()
            sonuc.append(orijinal_harf)
            anahtar_indeks += 1
        else:
            sonuc.append(karakter)

    return "".join(sonuc)


def xor_sifrele(metin, anahtar):
    sonuc = []
    for i in range(len(metin)):
        xor_degeri = ord(metin[i]) ^ ord(anahtar[i % len(anahtar)])
        sonuc.append(str(xor_degeri))
    return ",".join(sonuc)


def xor_desifrele(sifreli, anahtar):
    sonuc = ""
    sayilar = sifreli.split(",")
    for i in range(len(sayilar)):
        orijinal = int(sayilar[i]) ^ ord(anahtar[i % len(anahtar)])
        sonuc += chr(orijinal)
    return sonuc


def atbash_sifrele(metin: str) -> str:
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
    return atbash_sifrele(sifreli)



def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')


def baslik_yazdir():
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


def ana_menu():
    while True:
        ekran_temizle()
        baslik_yazdir()

        print("\n  [1] Şifreleme / Deşifreleme Yap")
        print("  [0] Çıkış")
        secim = input("\nSeçiminiz: ").strip()

        if secim == "0":
            print("\nUygulama kapatıldı.")
            break

        elif secim == "1":
            ekran_temizle()
            baslik_yazdir()
            dosya_yolu = input("\nDosya yolunu girin (.txt): ").strip()
            if not os.path.isfile(dosya_yolu):
                input("Dosya bulunamadı. Entera basın.")
                continue
            metin = None
            for enc in ["utf-8", "utf-8-sig", "utf-16", "cp1254", "latin-1"]:
                try:
                    with open(dosya_yolu, "r", encoding=enc) as f:
                        metin = f.read()
                    if metin:
                        break
                except Exception:
                    continue
            if not metin:
                input("Dosya boş veya okunamadı. Entera basın.")
                continue
            print(f"Dosya okundu: {dosya_yolu} ({len(metin)} karakter)")

            algoritma = algoritma_sec()
            islem    = islem_sec()

            sonuc = None

            if algoritma == "1":
                try:
                    kaydirma = int(input("Kaydırma değeri (tam sayı): "))
                except ValueError:
                    input("Tam sayı giriniz. Devam için Entera basın.")
                    continue

                if islem == "1":
                    sonuc = caesar_sifrele(metin, kaydirma)
                elif islem == "2":
                    sonuc = caesar_desifrele(metin, kaydirma)

            elif algoritma == "2":
                anahtar = input("Anahtar kelime (Türkçe harf): ").strip()
                try:
                    if islem == "1":
                        sonuc = vigenere_sifrele(metin, anahtar)
                    elif islem == "2":
                        sonuc = vigenere_desifrele(metin, anahtar)
                except ValueError as hata:
                    input(f"{hata} Enter'a basın.")
                    continue

            elif algoritma == "3":
                anahtar = input("Anahtar kelime: ").strip()
                if not anahtar:
                    input("Anahtar boş olamaz. Enter'a basın.")
                    continue

                if islem == "1":
                    sonuc = xor_sifrele(metin, anahtar)
                elif islem == "2":
                    sonuc = xor_desifrele(metin, anahtar)

            elif algoritma == "4":
                if islem == "1":
                    sonuc = atbash_sifrele(metin)
                elif islem == "2":
                    sonuc = atbash_desifrele(metin)

            else:
                input("Geçersiz algoritma seçimi. Enter'a basın.")
                continue

            if sonuc is not None:
                islem_adi = "sifreli" if islem == "1" else "desifreli"
                dosya_adi = os.path.splitext(dosya_yolu)[0]
                cikti_yolu = f"{dosya_adi}_{islem_adi}.txt"
                with open(cikti_yolu, "w", encoding="utf-8") as f:
                    f.write(sonuc)
                print("\n" + "─" * 55)
                print(f"  İşlem tamamlandı!")
                print(f"  Çıktı dosyası: {cikti_yolu}")
                print("─" * 55)
            else:
                print("Geçersiz işlem seçimi.")

            input("\nAna menüye dönmek için Entera basın.")

        else:
            input("Geçersiz seçim. Devam için Enter'a basın.")



if __name__ == "__main__":
    ana_menu()
