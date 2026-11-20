# Kapak D2: antrasit premium

Onay tarihi 20 Kasım 2026. Tüm Reels kapakları ve videoların kapak karesi bu şablonla yapılır. Eski D1 (renge eriyen) ve lacivert bantlı kapakların yerini aldı.

Profil fotoğrafı, X banner'ı ve Facebook kapağıyla aynı dili konuşur: koyu antrasit stüdyo fonu, sağdan koyu kırmızı kenar ışığı. Amaç, profil ızgarasının tek bir yayın gibi premium ve kurumsal görünmesi.

## Ne sabit, ne değişir
- **Sabit:** zemin (antrasit, bulutlu doku, gren, vinyet), kırmızı kenar ışığı, tipografi, yerleşim.
- **Habere göre değişen:** fotoğraf, etiket, iki satır başlık, vurgu rengi (2. satır ve çizgi).

## Ölçüler
- 1080×1920 PNG.
- Fotoğraf üstte 1080 px yükseklikte durur ve zemine yumuşakça erir.
- Yazılar 3:4 ızgara kırpımının içinde kalır (y 240-1680). Başlık bloğu alttan 300 px yukarıda biter.
- Başlık 215 px'tir. Satır 908 px'i geçerse iki satır birlikte küçülür.

## Vurgu renkleri
| Renk | Kod | Kullanım |
|---|---|---|
| sarı | #f2c418 | ekonomi, cebimize dokunan |
| kırmızı | #ff5a5f | acil, maç, anma |
| camgöbeği | #4fc8e0 | |
| yeşil | #5fd38f | |
| turkuaz | #4fd6b4 | |
| limon | #b8e34a | |
| pembe | #f064b4 | |
| mavi | #5aaef5 | |
| açık mavi | #86ccf5 | |
| gül | #e07a86 | |

## Kullanım
1. Fotoğrafı `foto/` klasörüne koy. Telifsiz olmalı, Unsplash'tan alınabilir. Dosya adı kapak numarası olur (ör. `foto/26.jpg`).
2. `uret.py` içindeki `C` listesine bir satır ekle: numara, etiket, 1. satır, 2. satır, vurgu rengi, fotoğraf konumu, rozet. Rozet yalnız özel haberde kullanılır, ör. `'ÖZEL HABER|TEKSTİL'`; değilse `''` bırakılır.
3. `python3 uret.py 26` komutunu çalıştır. Çıktı `cikti/kapak_26.png` olarak gelir. Numara vermezsen listedeki tüm kapaklar üretilir.

Gerekenler: Python Playwright ve Chromium. Fontlar `assets/` içinde, Barlow Condensed 600 ve 800 (latin + latin-ext, ₺ dahil).

Kapak, Instagram mobil uygulamada Reels → Düzenle → Kapağı düzenle yolundan değiştirilir.
