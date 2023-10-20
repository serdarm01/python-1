import json

def veritabaniyi_yukle():
    try:
        with open("veritabani.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {"sorular": [], "cevaplar": []}

def veritabanini_kaydet(veritabani):
    with open("veritabani.json", "w", encoding="utf-8") as dosya:
        json.dump(veritabani, dosya, ensure_ascii=False, indent=4)

def cevap_bul(soru, veritabani):
    sorular = veritabani["sorular"]
    cevaplar = veritabani["cevaplar"]
    for indeks, kayit in enumerate(sorular):
        yaklasik_eslesme = similar(soru, kayit)
        if yaklasik_eslesme >= 0.6:
            return cevaplar[indeks]
    return "Üzgünüm, bu soruya henüz bir cevabım yok."

def similar(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return 1.0
    elif a in b or b in a:
        return 0.8
    else:
        return 0.0

def chatbot():
    veritabani = veritabaniyi_yukle()

    while True:
        soru = input("Siz: ")

        if soru == 'çık':
            break

        cevap = cevap_bul(soru, veritabani)
        print("Bot:", cevap)

        if cevap == "Üzgünüm, bu soruya henüz bir cevabım yok.":
            yeni_cevap = input("Bot: Bu soruya bir cevap öğretebilir misiniz? (Evet/Hayır): ")
            if yeni_cevap.lower() == "evet":
                yeni_soru = soru
                yeni_cevap = input("Bot: Cevabınız nedir?: ")
                veritabani["sorular"].append(yeni_soru)
                veritabani["cevaplar"].append(yeni_cevap)
                veritabanini_kaydet(veritabani)
                print("Bot: Teşekkürler, yeni bir şey öğrendim.")

if __name__ == '__main__':
    chatbot()
