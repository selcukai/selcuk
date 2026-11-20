import asyncio, json, sys, os
H=os.path.dirname(os.path.abspath(__file__))
from playwright.async_api import async_playwright
Y='#f2c418';R='#ff5a5f';ROSE='#e07a86';CY='#4fc8e0';G='#5fd38f';TL='#4fd6b4';LM='#b8e34a';PK='#f064b4';BL='#5aaef5';LB='#86ccf5'
C=[
(1,'TEKSTİL DOSYASI · KONYA','ESKİ KUMAŞLARA','ÖZLEM',ROSE,'50% 40%','ÖZEL HABER|TEKSTİL'),
(2,'KONYA · DOĞALGAZ DOSYASI','1 METREKÜP','4 BİN LİRA',Y,'50% 45%',''),
(3,'KONYA · ULAŞIM DOSYASI','METRO','NEREDE?',Y,'50% 30%',''),
(4,'KONYA · PANCAR DOSYASI','ŞEKER','KİM ÖDÜYOR?',Y,'50% 45%',''),
(5,'KONYA · SU DOSYASI','BARAJ DOLDU','PEKİ YA OVA?',CY,'50% 40%',''),
(6,'FRANSA 2-1 TÜRKİYE','KADER MAÇI','HÜSRAN',R,'50% 40%',''),
(7,'EKİM 2026 · ENFLASYON','ENFLASYON','HANGİSİ SENİN?',G,'50% 40%',''),
(8,'CUMHURİYET TARİHİNİN EN BÜYÜĞÜ','187 MİLYAR ₺','FON KRİZİ',Y,'50% 40%',''),
(9,'SON 24 YIL · TÜRKİYE','38.000 İŞÇİ','EVE DÖNMEDİ',Y,'50% 35%',''),
(10,'ARDA GÜLER · 20','TAM BİR','SERGEN GOLÜ',Y,'50% 60%',''),
(11,'6-12 KASIM 2026','KONYA','HAFTANIN ÖZETİ',TL,'50% 45%',''),
(12,'OYUN DÜNYASI','GTA VI','GERİ SAYIM',PK,'50% 40%',''),
(13,'10 KASIM · SAYGI VE ÖZLEMLE','ANLIYORUZ.','HİSSEDİYORUZ.',R,'50% 45%',''),
(14,'@SELCUKAI · REELS HİZMETİ','SİZİN İÇİN','REELS ÜRETEYİM',LM,'50% 40%',''),
(15,'APPLE · YAPAY ZEKÂ','SİRİ','TÜRKÇE ÖĞRENİYOR',BL,'50% 40%',''),
(16,'TÜRKİYE · MEDYA DOSYASI','GAZETECİLİK','BİTTİ.',BL,'50% 40%',''),
(17,'KONYA · BİSİKLET ŞEHRİ','BİSİKLETLE',"AVRUPA'DA",LM,'50% 50%',''),
(18,'AFYONKARAHİSAR · 5 KASIM',"İHSANİYE'DE",'SİLAHLI SALDIRI',R,'50% 40%',''),
(19,'KONYA · KELEBEK BAHÇESİ','KELEBEKLER',"COP31'DE",CY,'50% 40%',''),
(20,'KONYA · AİLE','ÇOCUK SPORDA',"AİLE NEFES'TE",Y,'50% 45%',''),
(21,'8 EYLÜL 1999 · KADEMELİ EMEKLİLİK','1 GÜN','= 20 YIL',Y,'50% 45%',''),
(22,'KONYA · RAYLI SİSTEM','TRAFİĞE GİRMEYEN','TREN GELİYOR',Y,'50% 50%',''),
(23,'KASIM 2026 · AYLIK ÖDEMELER','1,3 MİLYON KİŞİ','HESABA YATIYOR',CY,'50% 50%',''),
(24,'MERAM · SURİÇİ',"KONYA'NIN KALBİ",'YENİDEN DOĞUYOR',LM,'50% 40%',''),
(25,'TRAFİK · KIŞ DÖNEMİ','KIŞ LASTİĞİ','SON 11 GÜN',LB,'50% 40%',''),
]
T=open(os.path.join(H,'index.html')).read()
async def main():
  only=set(map(int,sys.argv[1:]))
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
    for n,lab,t1,t2,acc,pos,badge in C:
      if only and n not in only: continue
      h=T.replace('__DATA__',json.dumps(dict(n=n,lab=lab,t1=t1,t2=t2,acc=acc,pos=pos,badge=badge),ensure_ascii=False))
      open(os.path.join(H,'_cur.html'),'w').write(h)
      await pg.goto('file://'+os.path.join(H,'_cur.html')); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
      await pg.evaluate('fit()'); await pg.wait_for_timeout(100)
      await pg.screenshot(path=os.path.join(H,'cikti',f'kapak_{n:02d}.png'))
    await b.close()
asyncio.run(main())
