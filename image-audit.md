# Image audit vs reference (01M65CN90DC9EQVR32ZTB5A0SX.png) — 2026-10-29
Criteria: ≥2 light sources visibly ON, warm golden light, light palette (≤1 dark-wood accent, no dark doors), fully styled (plants, wall art, pillows, throw, books, rug, decor), small room, Alabaster walls/trim/doors (no marble).

| # | Image | Result | Issues |
|---|---|---|---|
| 0 | p1-hemat-cm-kamar-tidur-v2 | FAIL | lamp off, no ceiling light, dark teak dresser+headboard |
| 1 | p1-hemat-cm-ruang-makan-v3 | FAIL | pendant not glowing, sparse, no art layering |
| 2 | p1-hemat-cm-ruang-tamu-v2 | FAIL | lamps off, dark walnut credenza+table, sparse |
| 3 | p1-hemat-ct-kamar-tidur-v3 | PASS | ceiling+sconce on, light palette, styled |
| 4 | p1-hemat-ct-ruang-makan-v3 | PASS (borderline) | ceiling on + candles, plants, art; plain jute |
| 5 | p1-menengah-cm-kamar-tidur-v2 | FAIL | lamp off, dark wood, flat light |
| 6 | p1-menengah-cm-ruang-makan-v3 | FAIL | pendant dim, sparse |
| 7 | p1-menengah-cm-ruang-tamu-v2 | FAIL | lamps off, dark wood x2 |
| 8 | p1-menengah-ct-kamar-tidur-v3 | PASS | ceiling+2 sconces on, Persian rug, styled (dark nightstand = 1 accent) |
| 9 | p1-premium-cm-kamar-tidur-v2 | FAIL | lamp off, dark wood, flat |
| 10 | p1-premium-cm-ruang-makan-v3 | FAIL (borderline) | pendant/lamp weak glow, sparse styling |
| 11 | p1-premium-cm-ruang-tamu-v2 | FAIL | lamps off, dark walnut credenza+tables |
| 12 | p1-premium-ct-kamar-tidur-v3 | PASS (borderline) | ceiling+2 lamps on; bed mid-tone wood |
| 13 | v4/b-cm | FAIL | dark wood stool/trim band, sparse |
| 14 | v4/b-ct | FAIL | lights off, bare, cool light |
| 15 | v4/d-ct | FAIL | pendant off, bare walls, no plants/art |
| 16 | v4/e-cm | FAIL | MARBLE walls, bare, no light on |
| 17 | v4/e-ct | FAIL | bare, no lamps on |
| 18 | v4/k-cm | FAIL | pendant dim, sparse |
| 19 | v4/k-ct | FAIL | lights off, sparse |
| 20 | v4/l-ct-hemat | FAIL | MARBLE walls, dark door, open plan too big, bare |
| 21 | v4/l-ct-men | FAIL | dark door, lamp off, bare, oversized |
| 22 | v4/l-ct-prem | FAIL | lamps off, bare, cold |
| 23 | v4/o-cm | FAIL | marble-ish wall, lamp off, bare |

Totals: 4 PASS (3 borderline), 20 FAIL.

## Regenerated 2026-10-29 (12 GenerateImage calls, ref image + item photos) → img/combos/v5/
| New image | Combos | Result |
|---|---|---|
| v5-l-ct-hemat | hemat-ct-ruang-tamu | PASS lighting/palette/styling; still open-plan kitchen visible (scale) |
| v5-l-ct-men | menengah-ct-ruang-tamu | PASS |
| v5-l-ct-prem | premium-ct-ruang-tamu | PASS |
| v5-e-cm | menengah-cm-entry | PASS (ice bucket not rendered; hotspot on basket/planter) |
| v5-e-ct | menengah-ct-entry | PASS (coat stand mid-tone beech) |
| v5-d-ct | menengah+premium-ct-ruang-makan | PASS |
| v5-o-cm | all 3 cm-ruang-kerja | PASS (desk = wood accent) |
| v5-l-cm-prem | premium-cm-ruang-tamu | PARTIAL: open plan + 3 dark pieces (Eames, credenza, coffee table) |
| v5-l-cm-men | menengah-cm-ruang-tamu | PASS (coffee table mid-tone) |
| v5-l-cm-hemat | hemat-cm-ruang-tamu | FAIL: dark front door + dark credenza & coffee table |
| v5-bd-cm-prem | premium-cm-kamar-tidur | PASS borderline (mid-tone walnut headboard+chest) |
| v5-k-ct | hemat+menengah-ct-dapur | PASS |

Still failing (not regenerated): p1-hemat-cm-kamar-tidur-v2, p1-menengah-cm-kamar-tidur-v2, 3 cm ruang-makan v3 (weak pendant glow), v4/b-ct, v4/b-cm (bath), v4/k-cm (premium-cm-dapur), plus v5-l-cm-hemat and v5-l-cm-prem.

## Audit 2026-11-01 — tumpukan lantai / tech / kabel (35 gambar kombo)
Tumpukan bingkai/seni di lantai: **0 gambar gagal** (tidak ditemukan di 35 kombo, termasuk 3 HR v2).
Catatan minor (tidak sampai gagal, regenerasi tidak diprioritaskan):
- p1-menengah-ct-ruang-tamu: stereo + 2 speaker terbuka di konsol (idealnya speaker kecil di antara buku).
- p1-hemat-ct-ruang-tamu: TV biasa di dinding, bukan Frame TV dalam gallery wall.
- p1-premium-ct-ruang-tamu: TV di atas perapian, bukan Art Mode di gallery wall.
- p1-premium-cm-kamar-mandi: lampu meja di bangku dekat wastafel, kabel kemungkinan ada (tidak terlihat jelas).
- p1-*-ruang-kerja (3): kabel iMac tidak terlihat; OK.
Kabel terlihat jelas: tidak ada.
