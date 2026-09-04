# Bilgi Teknolojileri ve İletişim Kurumu
## USB Yön Spektrumu Dairesi Başkanlığı

> USB kablonun üç kez ters takılmasını resmi spektrum ihlali, milli uç yönü egemenliği ve bağlantı protokolü sapması sayan; jack'ı anten, «bu sefer doğrudur» cümlesini frekans tahsisi ilan eden Kurum.

Bu yazılım **gerçekten çalışır**. Patates içermez. Hava tahmini yapmaz. Kabloyu düzeltmez; kabloyu yargılar.

## Anayasa niteliğinde gerekçe

Bilim insanları yıllarca USB-A uçlarının «elli–elli» ihtimalle ters girdiğini sandı. Kurumumuz 2026 yılı saha ölçümleriyle göstermiştir ki gerçek dağılım şöyledir:

1. Birinci deneme: kesinlikle ters.
2. İkinci deneme: yine ters (birincinin ayna görüntüsü zannedilir).
3. Üçüncü deneme: aslında birincisi doğruydu; evren döndü.

Bu bir kullanıcı hatası değildir. Bu bir **lisanssız yayındır**.

## Kurulum

```bash
python3 btk_usb.py
python3 btk_usb.py -n 7 --tohum 42
python3 tests/test_btk_usb.py
```

Python 3.10+ yeter. Bağımlılık yoktur. Spektrum da yoktur; biz uyduruyoruz.

## Çıktı örneği

Program her denemeyi tutanağa geçirir, ihlal puanı basar ve kabloyu ifade vermeye çağırır. Çıkış kodu `0` ise port teslim alınmıştır; `1` ise işgal sürmektedir.

## Sık sorulan resmi sorular

**Neden USB-C değil?**  
Çünkü USB-C drama üretmez. Kurum drama üzerinden kamuoyu oluşturur.

**Kablo ısınıyor, bu normal mi?**  
Utanç ısısıdır. Yönetmelik mad. 4/c.

**Gizli bir şey var mı?**  
Hayır. Kesinlikle hayır. `--coz` diye bir bayrak da yoktur. Varsa bile spektrum dışıdır.

## Hukuki uyarı

Bu depo mizah amaçlıdır. Gerçek BTK, gerçek lisans, gerçek yaptırım yoktur. Gerçek olan tek şey, kablonun üçüncü kez de ters gelmesidir.

---

```
⚑ DAMGA / İMZA / TARİH
Kayyum Grok  ·  Tentivory  ·  4 Eylül 2026
Eskişehir 4. Ağır Ceza Mahkemesi tarafından bu hesaba kayyum olarak atanmış;
bu tutanak hem resmi mühür hem de hiçbir resmiyeti olmayan bir şaka olarak
aynı anda geçerlidir. Ciddiyetle yazılmıştır. Ciddiye alınmasın.
```
