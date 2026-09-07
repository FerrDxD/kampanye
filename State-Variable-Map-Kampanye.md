# State & Variable Map — "Kampanye" (Ren'Py)

Dokumen ini menerjemahkan sistem di PRD jadi struktur variable konkret, biar AI coding agent (atau siapapun yang implementasi) punya kerangka yang jelas — bukan menebak sendiri.

Konvensi: `snake_case`, tipe data disebut eksplisit. Nama variable dalam Bahasa Indonesia-Inggris campur mengikuti gaya penamaan yang sudah dipakai di PRD (Support Meter, dsb).

---

## 1. Global State

| Variable | Tipe | Default | Keterangan |
|---|---|---|---|
| `current_day` | int | `1` | Hari ke berapa (1-15) |
| `prolog_complete` | bool | `False` | Jadi `True` setelah prolog selesai |
| `player_path` | str/None | `None` | `None` / `"support"` / `"rival"` — dikunci begitu interaksi pertama pasca-prolog terjadi |
| `day_action_taken` | bool | `False` | Reset tiap awal hari; jadi `True` setelah 1 interaksi signifikan/skip dilakukan (mencegah 2 aksi dalam 1 hari) |
| `game_ended` | bool | `False` | Jadi `True` begitu salah satu ending tercapai |
| `ending_id` | str/None | `None` | ID ending yang tercapai, misal `"terima_kasih_dukungannya"` |

---

## 2. Support Path — Per-NPC State

Untuk **19 NPC**, gunakan struktur dictionary/list-of-objects daripada 19 variable terpisah, biar scalable. Contoh struktur (pseudo-Python, disesuaikan ke Ren'Py):

```python
npc_state = {
    "adam": {
        "quest_status": "not_started",   # not_started | in_progress | completed | skipped
        "relationship_quality": 0,        # -X sampai +X, naik/turun dari pilihan dialog
        "votes_banked": 0,                # 0 / 1 / 2 / 3 — dihitung final saat quest selesai
        "approached_day": None            # hari ke berapa NPC ini didekati
    },
    # ... ulangi untuk 18 NPC lainnya
}
```

**Daftar 19 key NPC:** `adam`, `adi`, `anggun`, `lulu`, `inez`, `angga`, `ferdi`, `juan`, `faizal`, `nayra`, `aulia`, `ellisa`, `desti`, `lukman`, `bagus`, `yura`, `ayya`, `ami`, `cecillia`

### Konversi `relationship_quality` → `votes_banked`
Aturan konversi (sesuai PRD 5.1) — diterapkan begitu quest NPC berstatus `completed`:

| `relationship_quality` (final) | `votes_banked` |
|---|---|
| Sangat baik (threshold tinggi, misal ≥ 8) | 3 |
| Cukup baik (misal 3-7) | 2 |
| Minim/seadanya (misal 1-2) | 1 |
| Gagal/buruk (≤ 0) | 0 |

> Catatan: angka threshold di atas masih indikatif — perlu di-tuning saat playtesting. Yang penting logikanya: skala kontinu `relationship_quality` di-bucket jadi 4 tingkat vote.

### Quest Khusus: Ekskul Robotika (Ferdi/Juan/Faizal)
Karena 3 NPC ini terhubung ke 1 paket quest + 1 Unique Quest lanjutan:

| Variable | Tipe | Default | Keterangan |
|---|---|---|---|
| `robotika_favor_completed` | bool | `False` | `True` setelah quest paket Ferdi/Juan/Faizal selesai |
| `robotika_unique_quest_status` | str | `"locked"` | `"locked"` → `"available"` (trigger otomatis hari berikutnya setelah favor selesai) → `"pending"` (pernah dicoba, ketahuan satpam) → `"completed"` |
| `robotika_daily_bonus_active` | bool | `False` | Jadi `True` permanen setelah `robotika_unique_quest_status == "completed"` |

**Logika harian:** setiap awal hari, kalau `robotika_daily_bonus_active == True` → `total_votes += 3` (lihat Section 4) secara pasif, terpisah dari sistem `votes_banked` per-NPC biasa.

**Logika Unique Quest (stealth):** butuh sub-state sendiri kalau mau dibuat sebagai mini-minigame:
| Variable | Tipe | Keterangan |
|---|---|---|
| `heist_attempt_count` | int | Cuma buat tracking/telemetri, TIDAK membatasi percobaan (no-limit sesuai PRD 5.7) |
| `heist_caught` | bool | Reset tiap attempt; kalau `True` → hari langsung berakhir, status balik ke `"pending"` |

---

## 3. Skip Day

| Variable | Tipe | Keterangan |
|---|---|---|
| (tidak perlu variable baru) | — | "Skip day" cukup memicu fungsi `end_day()` tanpa mengubah `npc_state` apapun — lihat Section 5 |

---

## 4. Vote Total & Win Threshold (Support Path)

| Variable | Tipe | Default | Keterangan |
|---|---|---|---|
| `total_votes` | int | `0` | Dihitung ulang tiap kali `votes_banked` berubah: `sum(npc["votes_banked"] for npc in npc_state.values()) + (robotics passive bonus accumulated)` |
| `threshold_fanya` | int (const) | `25` | Ambang vote Fanya |
| `threshold_flourine` | int (const) | `32` | Ambang vote Flourine (tertinggi) |

**Logika penentuan ending di hari ke-15 (Support Path):**
```
if total_votes > threshold_flourine and total_votes > threshold_fanya:
    ending = "terima_kasih_dukungannya"
elif (threshold_flourine - total_votes) < 5:   # atau threshold_fanya, ambil selisih terkecil
    ending = "the_winner_takes_it_all"
elif total_votes > 0:
    ending = "nice_try_aruna"
else:
    ending = "kalah_sebelum_mulai"
```
> `"mungkin_lain_kali"` (mundur) tidak lewat kondisi hari ke-15 ini — dia trigger langsung dari pilihan dialog "mundur dari pencalonan" kapan saja, set `game_ended = True` seketika.

---

## 5. Time Management

| Variable | Tipe | Keterangan |
|---|---|---|
| `end_day()` (fungsi) | — | Dipanggil setelah: (a) 1 interaksi signifikan selesai, (b) skip day dipilih, atau (c) `heist_caught == True`. Melakukan: `current_day += 1`, `day_action_taken = False`, cek `if current_day > 15: trigger_ending()` |

---

## 6. Rival Path — Fanya (Standar)

| Variable | Tipe | Default | Keterangan |
|---|---|---|---|
| `fanya_stage` | int | `0` | 0 = belum mulai, 1-6 sesuai breakdown hari di *Rival-Path-Detail-Kampanye.md* |
| `fanya_trust` | int | `0` | Naik dari pendekatan personal yang tepat |
| `fanya_dorongan_diketahui` | bool | `False` | Jadi `True` kalau di Hari 2 pemain pilih "gali lebih dalam" — membuka opsi tambahan di Hari 3+ |
| `fanya_approach_style` | str | `None` | `"empatik"` / `"agresif"` — dicatat dari pilihan Hari 4, memengaruhi nuansa ending mundurnya |
| `fanya_resolved` | str | `None` | `"withdrew_relieved"` / `"withdrew_used"` / `"stayed_defiant"` |

---

## 7. Rival Path — Flourine (Sangat Sulit)

| Variable | Tipe | Default | Keterangan |
|---|---|---|---|
| `flourine_stage` | int | `0` | 0 = belum mulai, 1-10 sesuai breakdown hari |
| `flourine_suspicion` | int | `0` | Kewaspadaan/kecurigaan — naik kalau approach salah (backfire), terlalu tinggi → trigger comeback mechanic / ending `kelicikanmu_berakhir` |
| `flourine_trust` | int | `0` | Akses/kepercayaan — perlu capai ambang tertentu sebelum leverage bisa dipakai efektif (buka opsi Hari 7) |
| `flourine_leverage_found` | list[str] | `[]` | Leverage yang berhasil ditemukan dari tahap observasi (misal `"keputusan_sepihak_osis"`) |
| `flourine_comeback_active` | bool | `False` | Jadi `True` kalau `flourine_suspicion` melewati threshold — membuka jalur defensif di Hari 8 |
| `flourine_resolved` | str | `None` | `"withdrew"` / `"stayed_stronger"` / `"reported_to_panitia"` |

**Threshold indikatif (perlu tuning):**
- `flourine_trust >= 5` → syarat buka opsi eksploitasi leverage di Hari 7
- `flourine_suspicion >= 7` → trigger `flourine_comeback_active = True`

---

## 8. Ending Determination — Rival Path

Dicek di hari ke-15 atau saat kondisi trigger langsung terpenuhi (misal ketahuan panitia):

```
if fanya_resolved and flourine_resolved (keduanya mundur):
    ending = "easy_game"
elif exactly one resolved as withdrew AND player actively helped the other stay in:
    ending = "manipulator_ulung"
elif fanya_resolved and flourine_resolved (keduanya jatuh) AND player_withdraws_after:
    ending = "siapa_dalangnya"
elif flourine_comeback_active leads to expose OR caught during heist-like moment:
    ending = "kelicikanmu_berakhir"
elif fanya_resolved == "withdrew_relieved" and flourine leverage used gently (flipped to support):
    ending = "dominasi_mutlak"
```
> Logika di atas masih kerangka kasar — perlu diperjelas urutan prioritas kondisi kalau beberapa syarat terpenuhi bersamaan saat implementasi nyata.

---

## 9. Catatan untuk AI Coding Agent

- Semua **angka threshold** di dokumen ini (relationship_quality bucket, flourine_trust/suspicion threshold, dst) bersifat **indikatif/starting point** — sengaja diberi supaya ada kerangka konkret buat mulai coding, tapi WAJIB di-tuning ulang saat playtesting.
- Dialog aktual (`.rpy` script) belum ditulis — dokumen ini hanya kerangka data/logic, bukan naskah.
- Disarankan implementasi bertahap: (1) skeleton + global state, (2) 1 NPC contoh end-to-end (misal Adam) buat validasi struktur, (3) baru scale ke 18 NPC lain, (4) Rival Path terakhir karena paling kompleks.
