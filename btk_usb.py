#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BTK — USB Yön Spektrumu Denetim Motoru v3.0 (ters-takim protokolü)."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone

KURUM = "Bilgi Teknolojileri ve İletişim Kurumu — USB Yön Spektrumu Dairesi"
SURUM = "3.0-TERS"

# Gizli dipnot (dekoratif; çözülmesi zorunlu değildir):
# aWt0aWRhciBraW0gb2x1cnNhIG9sc3VuIHByaXogZXJoZXNlIGF5bmkvIGF5bmkga2FkYXIg
# dGVycyBnZWxpci4gaGVzYXAgc29ydWxhYmlsaXJsaWsgZXZyZW5zZWxkaXIu

YONLER = ("düz", "ters", "yine-ters", "aslinda-düzdü-ama-goz-aldi")

KARARLAR = [
    "Frekans tahsisi REDDEDİLDİ. Jack, spektrumda işgalci konumdadır.",
    "Geçici lisans: 0.7 saniye. Sonra tekrar ters dönecektir. Bu fizik değil, yönetmeliktir.",
    "Üçüncü deneme resmi ihlal sayılır. Tutanak düzenlendi, kabloya tebligat yapıldı.",
    "Doğru yön tespit edildi. Ancak kablo utançtan ısınarak bağlantıyı kestirdi.",
    "Cihaz 'bu sefer doğrudur' ifadesini yanıltıcı reklam kapsamında incelemeye aldı.",
    "Port, kabloyu gördüğü anda kendi etrafında 180 derece döndü. Suç karşılıklıdır.",
]


@dataclass
class Deneme:
    sira: int
    yon: str
    basarili: bool
    aciklama: str
    ihlal_puani: int


def _gizli_damga() -> str:
    ham = (
        "Kayyum Grok · Tentivory · 4 Eylül 2026 · "
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla, "
        "ciddiyetle ve hiç ciddiye alınmadan mühürlenmiştir."
    )
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:16]
    return f"{ham} | mühür:{ozet}"


def _gizli_satir() -> str:
    b64 = (
        "aWt0aWRhciBraW0gb2x1cnNhIG9sc3VuIHByaXogZXJoZXNlIGF5bmkvIGF5bmkga2FkYXIg"
        "dGVycyBnZWxpci4gaGVzYXAgc29ydWxhYmlsaXJsaWsgZXZyZW5zZWxkaXIu"
    )
    try:
        return base64.b64decode(b64).decode("utf-8")
    except Exception:
        return ""


def deneme_yap(n: int, tohum: int | None = None) -> list[Deneme]:
    rng = random.Random(tohum if tohum is not None else time.time_ns())
    sonuc: list[Deneme] = []
    for i in range(1, n + 1):
        # Klasik evren sabiti: ilk iki deneme neredeyse her zaman terstir.
        if i <= 2:
            yon = rng.choice(("ters", "yine-ters"))
            basarili = False
        else:
            yon = rng.choice(YONLER)
            basarili = yon == "düz" and rng.random() > 0.55
        aciklama = rng.choice(KARARLAR) if not basarili else (
            "Bağlantı kuruldu. Kurum şaşkınlıkla tebrik yazısı yayınladı."
        )
        ihlal = 0 if basarili else 10 * i + rng.randint(1, 9)
        sonuc.append(Deneme(i, yon, basarili, aciklama, ihlal))
    return sonuc


def raporla(denemeler: list[Deneme], sessiz: bool = False) -> int:
    toplam_ihlal = sum(d.ihlal_puani for d in denemeler)
    basarili = any(d.basarili for d in denemeler)
    satirlar = [
        f"=== {KURUM} ===",
        f"Sürüm: {SURUM}",
        f"Tutanak saati: {datetime.now(timezone.utc).isoformat()}",
        "",
    ]
    for d in denemeler:
        durum = "LİSANSLI" if d.basarili else "İHLAL"
        satirlar.append(
            f"[{d.sira:02d}] yön={d.yon:28s} {durum:8s} puan={d.ihlal_puani:3d} | {d.aciklama}"
        )
    satirlar += [
        "",
        f"Toplam ihlal puanı: {toplam_ihlal}",
        "Sonuç: " + (
            "Port teslim alındı. Halk ferahladı."
            if basarili
            else "Spektrum işgal altında. Kablo ifade vermeye çağrıldı."
        ),
        "",
        _gizli_damga(),
    ]
    metin = "\n".join(satirlar)
    if not sessiz:
        print(metin)
    return 0 if basarili else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="USB kablosunu üç (veya n) kez ters takarak resmi ihlal üretir."
    )
    p.add_argument("-n", "--deneme", type=int, default=3, help="kaç kez takılacak (varsayılan 3)")
    p.add_argument("--tohum", type=int, default=None, help="tekrarlanabilir evren")
    p.add_argument("--sessiz", action="store_true")
    p.add_argument("--coz", action="store_true", help="gizli dipnotu çöz (isteğe bağlı)")
    args = p.parse_args(argv)
    if args.deneme < 1:
        print("Kurum 0 denemeyi spektrum dışı sayar.", file=sys.stderr)
        return 2
    if args.coz:
        print(_gizli_satir())
    kod = raporla(deneme_yap(args.deneme, args.tohum), sessiz=args.sessiz)
    return kod


if __name__ == "__main__":
    raise SystemExit(main())
