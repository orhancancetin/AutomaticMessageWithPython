import pyautogui as auto 
import time 

limit = input("Limiti giriniz: ")
message = input("Mesajı giriniz: ")

x = 0

time.sleep(5)

while x < int(limit):
    auto.typewrite(message)
    auto.press("Enter")
    x+=1 

# Öncelikle buradaki amacımız herhangi bir uygulama üzerinden defalarca aynı mesajı atmak olacak.
# Bunun için windows kullanıyorsanız powershell üzerinden pip install pyautogui yapmamız gerekiyor.
# Ardından bu dosyamızda import ettikten sonra istiyorsak bunu benim aldığım gibi auto veya başka isim ile de tanımlayabilirsiniz. (1.Satır)
# limit tanımlıyoruz yani aynı mesajtan kaç tane göndermek istiyoruz? (4.Satır)
# ardından mesajımızı girmesi için kullanıcıdan istediği yazıyı yazmasını söylüyoruz. (5.Satır)
# Bu projemizde while loopu kullanacağız bundan kaynaklı herhangi bir harf vererek 0 olarak tanımlıyorum. (7.Satır)
# import time yapmamızın bir sebebi vardı o da time.sleep kodunu kullanamak için,mesajımız kodu çalıştırdıktan 5 saniye sonra otomatik olarak gönderilecek.(9.Satır)
# Artık while döngüsü kullanma zamanı geldi sonsuz döngü yapmak için while x < int(limit) yaptık dikkat edelim integer kullanmalıyız! (11.Satır)
# Ardından pyautogui içerisinde kullandığımız typewrite'ın görevi message içerisindekilerin hepsini otomatik olarak yazmaktır.(12.Satır)
# press'in görevi ise otomatik olarak enter tuşuna basmasıdır.
# 14.Satırda kullandığımız x+=1 ise aslında x = x + 1 anlamına gelir.Bu da while döngüsünün verdiğimiz limite kadar döngüyü devam ettirmesi anlamına gelir.Bunu mutlaka
# kullanmamız gerekiyor yoksa program sonsuza kadar mesaj atmaya devam eder.
# Bu kodun çalışması için mesaj atmak istediğiniz uygulama örnek Instagram DM ,Whatsapp'taki bir kişiye veya gruba atmak istiyorsanız mesaj yazılan yere tıklayıp
# beklemeniz yeterli olacaktır eğer siz biraz daha zaman istiyorum diyorsanız time.sleep(10) veya daha uzun bir süre yapabilirsiniz.
# Gerekli açıklamaları da yaptıktan sonra artık istediğiniz sayıda mesaj göndermenin tadını yaşayabilirsiniz :)