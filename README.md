# Selçuk — video motoru

Selçuk Özkan'ın (@selcukai) HyperFrames üzerine kurulu kişisel video motoru.
Amaç: her videonun ilk bakışta "bu Selçuk'un işi" dedirtmesi.

## Yapı
- `marka/` — fontlar, renkler, grid, künye, açılış/kapanış (imza katmanı)
- `kurallar/` — her videoda geçerli kurallar; motor bunlara uyar
- `sahneler/` — onaylanmış, tekrar kullanılabilir sahneler (manşet, rakam, maç…)
- `kontroller/` — render öncesi denetimler (takılma, telif, ses seviyesi)
- `dis-parcalar/` — diğer repolardan alınıp uyarlanan parçalar (kaynağıyla birlikte)
- `musteriler/` — ileride iş alınırsa müşteriye özel marka katmanları
- `projeler/` — tek tek video projeleri

## Çalışma şekli
Her yeni video motoru bir adım ileri taşır: beğenilen sahne kütüphaneye girer,
beğenilmeyen şey kurala dönüşür.

Altyapı: [HyperFrames](https://github.com/heygen-com/hyperframes) (Apache-2.0)
