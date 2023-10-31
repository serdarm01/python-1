import cv2
import time

kamera = cv2.VideoCapture(0)

mavi_aktif = False
mavi_cooldown = 0  # İlk başta cooldown süresi yok.

while True:
    ret, videoGoruntu = kamera.read()
    
    # Görüntüyü BGR renk uzayından HSV renk uzayına dönüştürün.
    hsv_goruntu = cv2.cvtColor(videoGoruntu, cv2.COLOR_BGR2HSV)
    
    # Mavi renk aralığını tanımlayın (örnek olarak, parlak mavi).
    alt_mavi = (90, 50, 50)  # Düşük mavi sınırı
    ust_mavi = (130, 255, 255)  # Yüksek mavi sınırı
    
    # Mavi renk aralığını maskeleyin.
    mavi_maske = cv2.inRange(hsv_goruntu, alt_mavi, ust_mavi)
    
    # Mavi maskeyi kullanarak mavi bölgeleri tespit edin.
    mavi_bolgeler = cv2.bitwise_and(videoGoruntu, videoGoruntu, mask=mavi_maske)
    
    # Mavi ışık algılandığında bir işlem yapabilirsiniz.
    if cv2.countNonZero(mavi_maske) > 100:
        if not mavi_aktif:
            print("Mavi ışık algılandı uygulamayı durdurmak için q'ye basın gösteriniz!")
            mavi_aktif = True
            mavi_cooldown = time.time() + 20  # 20 saniyelik cooldown süresi.
    elif mavi_aktif and time.time() > mavi_cooldown:
        mavi_aktif = False
    
    # Kırmızı ışık algılandığında dur.
    # (Kırmızı ışık algılama kodu buraya eklenebilir.)
    
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
