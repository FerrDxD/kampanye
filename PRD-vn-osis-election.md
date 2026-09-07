# PRD — "Kampanye"
### Visual Novel: Pemilihan Ketua OSIS

**Versi:** 0.1 (Draft)
**Engine:** Ren'Py (target build: Windows/Mac/Linux + Web via WebAssembly/Emscripten)
**Referensi format:** *How to Date an Entity (and Stay Alive)* — scope jam-style, ~15-20 menit per ending, playable di web dan native

---

## 1. Ringkasan (Overview)

Sebuah sekolah di Jawa Barat, Indonesia, sedang mengadakan pemilihan Ketua OSIS. Aruna Wirasena Wisnu, siswa kelas 11 MIPA 2, adalah salah satu kandidat. Untuk menang, Aruna harus mempersuasi teman-teman sekolahnya agar mendukung pencalonannya — tapi setiap orang yang diminta dukungannya punya syarat/permintaan sendiri sebelum mau memberikan suara.

**Genre:** Slice-of-life / Political Drama / Visual Novel dengan sistem persuasi & favor quest
**Platform:** Desktop (Win/Mac/Linux) + Web (Ren'Py Web Export)
**Estimasi durasi main:** ~1 jam 45 menit (bisa lebih tergantung kedalaman quest yang diambil pemain) — jauh lebih panjang dari target awal 15-20 menit karena scope sudah berkembang (19 NPC, Rival Path 15 hari penuh, Unique Quest heist). Estimasi ini masih indikatif, bisa berubah setelah balancing lebih lanjut.

---

## 2. Tujuan Produk

- Membuat VN singkat namun replayable, dengan gameplay loop yang jelas dan padat.
- Mengeksplorasi tema kampanye/politik sekolah dengan nuansa jujur, dramatis, dan relatable buat siswa Indonesia.
- Menyamai *How to Date an Entity* dari sisi: scope kecil tapi terasa "hidup", banyak ending, dan replay value tinggi meski durasi pendek.

---

## 3. Karakter Utama

| Karakter | Peran |
|---|---|
| **Aruna Wirasena Wisnu** | MC — siswa kelas 11 MIPA 2, kandidat Ketua OSIS |

### Kandidat Lawan (Rival Path target)

| Nama | Panggilan | Kelas |
|---|---|---|
| Flourine Azelya Bilqis | Flourine | 11 IPS 3 *(karakter fiktif)* |
| Fanya Fidelya | Fanya | 11 MIPA 1 |

> **Catatan penting:** Karakter yang tadinya bernama "Cecillia Natasya Sonthani" di slot Rival Path (target manipulasi tersulit) **diganti dengan karakter fiktif Flourine Azelya Bilqis** — mekanik dan tingkat kesulitan super sulit tetap sama persis seperti yang sudah didesain, cuma identitasnya diganti. Ini dilakukan karena Cecillia adalah representasi orang nyata (Ketua OSIS asli developer), dan developer tidak ingin nama aslinya dipakai dalam storyline manipulasi/licik. Cecillia (nama asli) sekarang muncul sebagai NPC di Support Path — lihat tabel di bawah.

### NPC yang Bisa Dipersuasi (Support Path)

| Nama | Panggilan | Peran/Organisasi |
|---|---|---|
| Adam Abdulloh Mu'arif | Adam | Ketua Ekskul Jurnalistik |
| Muhammad Fadhli Hidayatulloh | Adi | Anggota Ekskul Jurnalistik |
| Anggun Permata Jalasena Putri | Anggun | Anggota Ekskul Karate |
| Lulu Karpika | Lulu | Ketua Ekskul Karate |
| Inez Mikha Rahayu | Inez | Anggota Ekskul Seni |
| Erlangga Nuriansyah | Angga | Dewan Ambalan Pramuka |
| Maulana Ferdi Irawan | Ferdi | Ketua Ekskul Robotika |
| Juansyah Akbar | Juan | Anggota Ekskul Robotika |
| Faizal Arfa Mubaroq | Faizal | Anggota Ekskul Robotika |
| Nayra Septri Ramadhiani | Nayra | Ketua Ekskul Akustik |
| Aulia Febriani Tanjung | Aulia | Ketua Paskibra |
| Ellisa Abigail Gloria Palit | Ellisa | Anggota Ekskul Math Club |
| Desti Nur'ani | Desti | Ketua PMR |
| Luqman Permana Mahardika | Lukman | Ketua Ekskul Zoologi |
| Bagus Valent Nugroho | Bagus | Pustakawan (siswa) |
| Gadis Yura Safa Rasikah | Yura | Anggota Ekskul Jurnalistik |
| Kania Anada Pratiwi | Ayya | Ketua Ekskul FPSH (Forum Pemuda Sadar Hukum) |
| Amirah Hadjriah Haris | Ami | Anggota Ekskul Jurnalistik |
| Cecillia Natasya Sonthani | Cecillia | Ketua Ekskul Badminton |

**Total: 19 NPC.** Dengan 15 hari dan 1 interaksi signifikan/hari, pemain **tidak bisa mendekati semua NPC dalam satu playthrough** — ini otomatis jadi mekanik prioritas/pilihan strategis (NPC mana yang didekati duluan/dilewati), sekaligus jadi sumber replayability.

> Catatan: Nama diambil dari pengurus OSIS & MPK asli SMAN 2 Jonggol (kecuali Flourine, yang fiktif). Detail favor quest untuk Cecillia (ekskul Badminton) belum dibuat — lihat Open Items.

---

## 4. Core Gameplay Loop

Loop utama berputar di sekitar **satu quest utama** dengan banyak **side quest** sebagai jalannya:

1. **Quest Utama:** Aruna harus mengumpulkan dukungan (votes/support) dari siswa-siswi lain sampai mencapai ambang kemenangan.
2. **Approach seorang NPC** → tawarkan diri sebagai kandidat, minta dukungan.
3. NPC tidak langsung setuju — dia mengajukan **permintaan/tolong** (side quest) sebagai syarat dukungannya.
4. Pemain memilih cara menyelesaikan/menanggapi permintaan itu (bisa dikerjakan, dinegosiasikan, ditolak, atau dicurangi).
5. Hasil keputusan memengaruhi **Support Meter** dari NPC tersebut dan/atau reputasi umum Aruna.
6. Ulangi untuk NPC lain — total dukungan terkumpul menentukan ending.

### Diagram alur singkat
```
[Mulai] → [Pilih NPC utk didekati] → [Dialog persuasi]
   → [NPC ajukan permintaan] → [Pemain pilih respons]
   → [Update Support Meter] → [Kembali ke peta/menu pilih NPC]
   → (ulang sampai waktu/kesempatan habis) → [Hasil Pemilihan / Ending]
```

---

## 4.5 Fitur: Rival Manipulation Path

Selain jalur "kumpulkan dukungan" (Support Path), Aruna punya opsi kedua: **mempersuasi/memanipulasi kandidat lawan agar mengundurkan diri** (Flourine dan/atau Fanya).

### Karakteristik jalur ini:
- **Bukan side quest** — ini adalah **pergeseran Main Quest**. Begitu pemain mengambil langkah ke arah ini secara serius, fokus permainan berpindah dari "kumpulkan Support Meter dari NPC" ke "runtuhkan posisi kandidat lawan".
- **Tingkat kesulitan berbeda** dari Support Path — kemungkinan lebih berisiko (butuh leverage/informasi/momentum) tapi berpotensi lebih cepat mencapai goal akhir (menang pemilihan) karena mengurangi kompetisi langsung, bukan menambah dukungan.
- **Setiap rival (Flourine, Fanya) kemungkinan punya "kelemahan"/isu personal berbeda** yang bisa dieksploitasi Aruna — detail pendekatan per rival menyusul.
- **Konsekuensi moral/reputasi**: karena ini manipulasi terhadap orang, kemungkinan besar memengaruhi ending path (misal: "menang licik" vs "menang bersih" dari section Ending).
- **Eksklusif dengan Support Path**: begitu pemain memilih Rival Path secara penuh, jalur Support Path tertutup — **tidak bisa pindah jalur di tengah permainan**.
- **Trigger point commit — implisit, bukan menu pilihan**: Tidak ada layar "pilih jalurmu" eksplisit. Setelah prolog selesai, sistem melacak **tindakan pertama pemain**:
  - Kalau pemain langsung berinteraksi dengan salah satu **NPC (Support Path target)** → sesi game dikunci ke **Support Path**.
  - Kalau pemain langsung berinteraksi dengan salah satu **rival (Flourine/Fanya)** → sesi game dikunci ke **Rival Path**.
  - Interaksi di sini berarti percakapan/aksi bermakna dengan karakter tersebut (bukan sekadar melihat/lewat).

### Implikasi ke struktur Main Quest
Main Quest jadi punya **dua cabang besar** yang ditentukan dari tindakan pemain pasca-prolog, bukan pilihan eksplisit:
```
[Start] → [Prolog] → Aruna berinteraksi dengan siapa duluan?
   ├─ Interaksi pertama = NPC → Kunci ke Jalur A: Support Path
   └─ Interaksi pertama = Rival (Flourine/Fanya) → Kunci ke Jalur B: Rival Path
        → Main Quest bergeser fokus ke jalur ini
→ [Ending ditentukan oleh jalur yang diambil + cara menempuhnya]
```

---

## 5. Sistem Inti

### 5.1 Support Meter → Vote Conversion
- Setiap NPC punya nilai dukungan personal (Support Meter) yang naik/turun berdasarkan cara pemain merespons permintaan NPC dan pilihan dialog sepanjang quest.
- **Konversi ke vote TIDAK 1:1 per NPC** — di akhir interaksi dengan tiap NPC, kualitas hubungan yang terbangun (dari awal quest sampai akhir) menentukan berapa vote yang disumbangkan:
  - Hubungan sangat baik sepanjang quest → **+3 vote**
  - Hubungan cukup baik → **+2 vote**
  - Hubungan minim/seadanya → **+1 vote**
  - (Hubungan buruk/gagal total → kemungkinan 0 vote, meski NPC-nya "didekati")
- **Ambang menang (win threshold):** Aruna harus mengumpulkan vote **di atas 20** secara umum, tapi threshold sebenarnya ditentukan oleh kekuatan masing-masing rival:
  - Vote Fanya: **25**
  - Vote Flourine: **32**
  - Untuk mencapai ending kemenangan mutlak ("Terima Kasih atas dukungannya!"), total vote Aruna harus melampaui **kedua** angka ini — jadi ambang efektifnya adalah **di atas 32** (angka rival tertinggi).
  - Selisih vote Aruna vs total tertinggi rival menentukan ending lain (misal *The Winner Takes it All* untuk selisih kalah <5).

> Catatan: Dengan 19 NPC di Support Path dan skema +1/+2/+3 per NPC, jumlah vote maksimum teoritis (kalau semua NPC didekati dengan hubungan sempurna) jauh melebihi 32 — tapi karena hanya 1 interaksi/hari dan periode 15 hari, pemain realistanya cuma bisa mendekati maksimal 15 dari 19 NPC dalam satu playthrough (belum termasuk skip day), jadi threshold 32 tetap menantang untuk dicapai dengan kualitas hubungan tinggi secara konsisten.

### 5.2 Favor / Side Quest System
- Setiap NPC = 1 mini side-quest unik (permintaan tolong).
- Jenis permintaan bisa variatif: tugas sekolah, masalah pribadi, konflik sosial, dsb — detail menyusul per karakter.
- Cara pemain menangani permintaan (jujur/licik/menolak) memengaruhi bukan cuma Support Meter NPC itu, tapi berpotensi trigger konsekuensi ke NPC lain (reputasi berantai).

### 5.3 Sistem Ending

Karena kedua path bersifat **eksklusif**, ending dikelompokkan berdasarkan path yang diambil pemain.

#### Ending — Support Path

| Ending | Kondisi |
|---|---|
| **Terima Kasih atas dukungannya!** | Mendapat semua dukungan dalam periode waktu yang ditentukan |
| **The Winner Takes it All** | Kalah dengan selisih jumlah pendukung kurang dari 5 |
| **Nice Try, Aruna!** | Tidak berhasil mengumpulkan dukungan (gagal) selama periode waktu berjalan |
| **Kalah Sebelum Mulai** | Tidak mengumpulkan pendukung sama sekali dari awal sampai akhir |
| **Mungkin Lain Kali** | Aruna mundur dari pencalonan |

#### Ending — Rival Path

| Ending | Kondisi |
|---|---|
| **Easy Game** | Membuat Cecillia dan Fanya mundur dari kursi kandidat |
| **Manipulator Ulung** | Membantu salah satu kandidat sambil menjatuhkan kandidat yang lain |
| **Siapa dalangnya?!!** | Mengundurkan diri setelah menjatuhkan kedua kandidat — panitia OSIS kewalahan mencari dalangnya |
| **Kelicikanmu berakhir** | Tertangkap panitia OSIS saat mencoba memanipulasi salah satu kandidat |
| **Dominasi mutlak** | Membuat Cecillia dan Fanya berbalik mendukung Aruna |

> Total: **10 ending** (5 per path) — sejalan dengan referensi (game acuan punya ~10 ending juga).

### 5.4 Mekanik Waktu (Time Management)
- **Periode kampanye: 15 hari** (in-game). Ini adalah batas waktu keras untuk kedua jalur (Support Path & Rival Path).
- **Satu side quest/interaksi signifikan per hari** — setelah itu, hari otomatis berakhir ("pulang sekolah, Aruna istirahat") dan lanjut ke hari berikutnya.
- **Support Path (18 NPC, 15 hari):** slack waktu diisi dengan menambah jumlah NPC, bukan event filler — pemain otomatis harus memilih prioritas karena tidak semua NPC bisa didekati dalam satu playthrough. Ini jadi mekanik pilihan strategis sekaligus sumber replayability.
- **Rival Path (2 rival, 15 hari):** dirancang **makan durasi 15 hari penuh** — karena jalur ini dianggap main quest itu sendiri (bukan side content), setiap hari diisi dengan langkah-langkah manipulasi/persuasi yang panjang dan bertahap terhadap Cecillia dan/atau Fanya, bukan diselesaikan cepat lalu sisa waktu kosong.

### 5.5 Catatan Khusus: Tingkat Kesulitan Flourine vs Fanya
- **Flourine harus didesain sebagai target manipulasi paling sulit** di Rival Path — bukan cuma dari sisi stat/angka, tapi dari sisi desain (butuh lebih banyak langkah, leverage lebih spesifik, atau reaksi balik yang lebih kuat kalau pemain gagal).
- **Latar belakang keputusan desain ini:** Slot "target tersulit" ini awalnya dirancang berdasarkan karakter Cecillia (Ketua OSIS asli developer di kehidupan nyata). Karena developer tidak ingin nama & identitas asli dipakai dalam storyline manipulasi/licik, **identitas di slot ini diganti menjadi karakter fiktif Flourine Azelya Bilqis** — mekanik dan tingkat kesulitan super sulit yang sudah didesain **tetap dipertahankan sepenuhnya**, cuma nama & identitasnya yang berubah. Cecillia (nama asli) kini muncul sebagai NPC di Support Path (Ketua Ekskul Badminton) dengan konten yang terpisah sama sekali dari tema manipulasi.
- **Fanya didesain dengan tingkat kesulitan standar** (tidak dibuat sesulit Flourine) — karena Fanya adalah karakter fiktif sejak awal, tidak ada batasan serupa dari sisi developer.

### 5.6 Skip Day (Fitur Baru)
- Setiap pagi setelah Aruna tiba di sekolah, pemain punya opsi **"Jalani hari dengan tenang"** — melewati hari itu tanpa melakukan interaksi/quest, langsung lanjut ke hari berikutnya.
- Konsisten dengan pembatasan waktu: begitu sore tiba, Aruna otomatis harus pulang (baik karena sudah menyelesaikan 1 interaksi signifikan, memilih skip, atau — khusus Unique Quest Robotika — tertangkap satpam, lihat 5.7).

### 5.7 Unique Quest: Ekskul Robotika (Trigger dari Favor Quest #7)

Setelah pemain menyelesaikan favor quest ekskul Robotika (Ferdi/Juan/Faizal — paket 1 quest untuk 3 Support Meter) dan lanjut ke hari berikutnya, sebuah **Unique Quest** ter-trigger otomatis:

- **Syarat dari ekskul Robotika:** mereka mau bantu kampanye Aruna pakai robot mereka, tapi dengan syarat Aruna harus **merebut kembali piala dari rak pajangan piala di ruang kepala sekolah**.
- **Jenis gameplay: Heist/Stealth** — berbeda dari quest dialog-based lainnya.
  - Dilakukan **malam hari** (bukan siang seperti quest normal).
  - Aruna harus **menghindari satpam yang sedang patroli**.
  - **Kalau tertangkap:** Aruna disuruh pulang, hari langsung bergeser ke hari berikutnya — **tapi quest TIDAK gagal**, hanya **ditangguhkan** dan tetap bisa dicoba lagi **kapan saja tanpa batas percobaan (no-limit)**, selama periode 15 hari belum berakhir.
- **Reward kalau berhasil:** Ekskul Robotika resmi membantu kampanye Aruna dengan robot mereka. Sejak hari itu, Aruna mendapat **+3 Support secara pasif di awal setiap hari**, berlaku hingga hari ke-15.

**Tingkat kesulitan aktual vs yang dirasakan pemain (Fake Difficulty by Design):**
- Secara mekanik, kesulitan stealth-nya **dibuat standar/moderat** — bukan benar-benar sulit dari sisi sistem (pattern patroli satpam gak perlu terlalu rumit, hitbox/timing gak perlu presisi tinggi).
- Tapi secara **presentasi** (framing narasi, musik tegang, dialog batin Aruna yang cemas, sound design satpam mendekat, dsb.), quest ini harus **terasa jauh lebih berisiko dan mendebarkan** dari yang sebenarnya — bikin pemain merasa ini "misi berbahaya", padahal sistem di baliknya cukup forgiving.
- Kombinasi **no-limit retry + kesulitan aktual yang moderat** menjadikan Unique Quest ini sebagai **"game changer" yang secara desain memang bisa diselesaikan siapa saja** asal mau coba berkali-kali — bukan gatekeeping fitur +3 Support pasif di balik skill check yang sungguhan sulit.

**Implikasi desain:**
- Unique Quest ini jadi satu-satunya segmen gameplay non-dialog (stealth/heist) di Support Path — kontras yang bagus dari ritme dialog-choice yang dominan di quest lain.
- Karena reward-nya passive income Support Meter harian, ada insentif kuat buat pemain menyelesaikannya **secepat mungkin** (semakin awal berhasil, semakin banyak total +3/hari yang terkumpul sampai hari ke-15) — cocok jadi salah satu keputusan strategis besar di playthrough Support Path.

### 5.8 Tone
- **Drama**, tanpa elemen komedi. Nuansa politik-sekolah yang serius/tegang, terutama di Rival Path yang melibatkan manipulasi.

---

## 6. Scope & Batasan (Jam-style Constraint)

Karena target durasi ~15-20 menit per playthrough, scope dijaga ketat:

- **Jumlah NPC/target:** 18 NPC di Support Path (pemain pilih prioritas, tak semua bisa didekati dalam 15 hari), 2 rival di Rival Path (mengisi penuh 15 hari) — sudah final.
- **Time-box ketat:** 15 hari in-game, 1 side quest/interaksi signifikan per hari — otomatis membatasi total konten per playthrough tunggal, meski total konten keseluruhan (semua NPC + rival) lebih besar dari estimasi awal.
- **Percabangan dialog:** dalam, tapi tidak melebar — fokus ke kualitas pilihan, bukan kuantitas.
- **Art asset:** gaya **anime** dengan kualitas art tinggi — referensi visual: *Nekopara*, *Nukitashi* (mengacu ke kualitas & gaya art-nya saja, bukan konten dewasanya). Sprite karakter dengan beberapa ekspresi per karakter, background sekolah reused.
- **Replayability** datang dari kombinasi keputusan, bukan dari panjangnya durasi single playthrough.

---

## 7. Tech Stack

| Komponen | Tools |
|---|---|
| Engine | Ren'Py (Python + Ren'Py Script Language `.rpy`) |
| Rendering/Input | Pygame / SDL2 (built-in Ren'Py) |
| Web Export | Emscripten → WebAssembly + JS glue, dibungkus HTML5 |
| Art | *(menyusul — tools gambar yang biasa dipakai)* |
| BGM/SFX | *(menyusul — bisa reuse workflow Suno AI seperti di Teman Kos)* |
| Coding assist | Bisa manfaatkan AI (ChatGPT/Gemini) untuk logic Ren'Py, seperti pendekatan dev referensi |

---

## 8. Yang Masih Perlu Diputuskan (Open Items)

- [x] Detail favor quest per NPC (18 NPC awal) — selesai, lihat dokumen terpisah *Favor-Quest-Detail-Kampanye.md*
- [x] Struktur 15-hari Rival Path — selesai, lihat dokumen terpisah *Rival-Path-Detail-Kampanye.md* (perlu diupdate: ganti nama Cecillia → Flourine)
- [x] Balancing Unique Quest Robotika — diputuskan: kesulitan aktual standar, tapi presentasi dibuat terasa sulit; no-limit retry
- [x] Favor quest untuk Cecillia (NPC baru, Ketua Ekskul Badminton) — selesai, lihat *Favor-Quest-Detail-Kampanye.md* #19
- [x] Kelas/detail tambahan untuk Flourine Azelya Bilqis — 11 IPS 3
- [x] Estimasi durasi main yang baru — ~1 jam 45 menit (bisa lebih)

---

## 9. Referensi Pembanding

*How to Date an Entity (and Stay Alive)* — SFour, Ren'Py, ~15-20 menit/ending, 10 ending berdasarkan Interest Meter, web export via Emscripten/WebAssembly. Disamai dari sisi scope & teknis, bukan tema.
