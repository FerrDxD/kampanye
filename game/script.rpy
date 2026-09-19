# Characters defined in characters.rpy

# Global Variables
default current_day = 1
default prolog_complete = False
default player_path = None
default day_action_taken = False
default game_ended = False
default ending_id = None
default total_votes = 0
default passive_votes = 0
default threshold_fanya = 25
default threshold_flourine = 32
default robotika_daily_bonus_active = False
default robotika_unique_quest_status = "locked"

default npc_state = {name: {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None} for name in ["adam", "adi", "anggun", "lulu", "inez", "angga", "ferdi", "juan", "faizal", "nayra", "aulia", "ellisa", "desti", "lukman", "bagus", "yura", "ayya", "ami", "cecillia"]}

default fanya_stage = 0
default flourine_stage = 0

init python:
    def get_votes_from_relationship(rel_quality):
        if rel_quality >= 8:
            return 3
        elif rel_quality >= 3:
            return 2
        elif rel_quality > 0:
            return 1
        else:
            return 0
            
    def calc_total_votes():
        return sum(npc["votes_banked"] for npc in npc_state.values()) + passive_votes

    def complete_quest(npc, meter):
        npc_state[npc]["relationship_quality"] += meter
        npc_state[npc]["quest_status"] = "completed"
        npc_state[npc]["votes_banked"] = get_votes_from_relationship(npc_state[npc]["relationship_quality"])
        store.total_votes = calc_total_votes()

label start:
    jump prolog

label prolog:
    scene expression Transform("images/bg_aula.jpg", size=(1920, 1080))
    "Aula utama itu berbau seperti furnitur tua dan ambisi yang terlalu lama dipendam."
    "Di atas panggung kayu yang berderit, tiga kursi kosong telah disiapkan."
    "Satu untuk sang petahana yang dingin dan tak tersentuh. Satu untuk sang primadona yang dipuja massa."
    "Dan satu lagi..."
    "Untukmu."
    
    "Pemilihan Ketua OSIS tahun ini bukanlah sekadar ajang popularitas khas anak SMA biasa."
    "Ini adalah medan perang berdarah dingin. Permainan catur empat dimensi di mana setiap senyum menyembunyikan belati politik."
    
    ar "15 hari..."
    "Kamu menatap pantulan dirimu di kaca jendela koridor yang basah oleh sisa hujan sore itu."
    "Aruna Wirasena Wisnu. Kelas 11 MIPA 2."
    "Kamu hanya punya 15 hari sebelum debat akbar dan pemungutan suara dimulai."
    
    "Pilihannya hanya dua."
    "Bermain bersih dengan merangkul simpati mereka, menggalang dukungan secara jujur..."
    "Atau bermain kotor, merangsek masuk ke ruang ganti lawan, dan mematahkan mental mereka dari dalam."
    
    "Jam pasir telah dibalik. Dan sejarah sekolah ini hanya akan mengingat nama sang pemenang."
    
    $ prolog_complete = True
    jump main_loop

label main_loop:
    if current_day > 15:
        jump evaluate_ending

    "Hari ke-[current_day] kampanye dimulai."
    "Total Dukungan (Votes): [total_votes]"

    if robotika_daily_bonus_active:
        $ passive_votes += 3
        $ total_votes = calc_total_votes()
        "Dukungan ekskul Robotika memberikan +3 vote pasif! (Total: [total_votes])"

    label map_navigation:
        scene expression Transform("images/bg_school_map.jpg", size=(1920, 1080))
        "Aruna memikirkan langkah selanjutnya. Ke mana ia harus pergi mencari dukungan?"
        
        call screen school_map
        $ current_location = _return
        
        if current_location == "heist":
            jump robotika_heist
        elif current_location == "pulang":
            "Aruna memutuskan untuk mengakhiri harinya dan pulang ke rumah."
            jump end_day_routine
        elif current_location != "mundur":
            $ renpy.jump(current_location)
            
        if current_location == "mundur":
            "Aruna memandangi formulir pencalonannya. Apakah ini saatnya untuk berhenti?"
            menu:
                "Ya, aku mengundurkan diri.":
                    if player_path == "rival" and fanya_resolved in ["withdrew_relieved", "withdrew_used"] and flourine_resolved == "withdrew":
                        $ ending_id = "siapa_dalangnya"
                    else:
                        $ ending_id = "mungkin_lain_kali"
                    jump show_ending
                "Tidak, aku harus terus berjuang!":
                    jump map_navigation

label quest_adam:
    $ npc_state["adam"]["quest_status"] = "in_progress"
    $ npc_state["adam"]["approached_day"] = current_day
    $ adam_meter = 0
    
    scene expression Transform("images/bg_ekskul_jurnalistik.jpg", size=(1920, 1080))
    "Kamu menemui Adam di ruang jurnalistik. Ia sedang sibuk mengetik sesuatu di laptopnya. Ruangan ini pengap, penuh dengan tumpukan kertas koran sekolah bulan lalu."
    "Mendengar langkahmu, ia berhenti mengetik, lalu memutar kursinya."
    
    ad "Aruna. Gue baru aja mikir kapan lo bakal mampir ke sini."
    ad "Duduk. Gue lagi nyusun liputan profil kandidat. Tapi jujur aja, profil lo sejauh ini membosankan."
    ar "Membosankan gimana maksud lo, Dam?"
    ad "Semua tentang lo... terlalu rapi. Visi misi lo terbaca kayak proposal anggaran ke kepsek. Nggak ada jiwanya."
    ad "Gue butuh angle. Sesuatu yang bikin orang mikir, 'Oh, ternyata Aruna tuh orangnya begini.'."
    ad "Jadi, jawab pertanyaan gue baik-baik. Kenapa lo ngerasa lo lebih pantas duduk di kursi ketua dibanding Flourine yang udah punya pengalaman, atau Fanya yang populer?"

    menu:
        "Gue punya visi yang jelas dan rencana kerja yang terukur.":
            $ adam_meter -= 2
            ad "Visi dan rencana kerja. Klise."
            jump adam_path_klise

        "Karena gue sadar gue banyak kurangnya, jadi gue mau dengar aspirasi siswa.":
            $ adam_meter += 2
            ad "Merendah untuk meroket? Menarik. Tapi apa lo beneran siap dengerin 'semua' orang?"
            jump adam_path_populis

        "Karena Flourine cuma cari aman, dan Fanya cuma cari tenar.":
            $ adam_meter += 4
            ad "Wow. Langsung nyerang leher. Gue suka gaya lo."
            jump adam_path_agresif

label adam_path_klise:
    ad "Oke, 'rencana kerja terukur'. Mari kita bedah."
    ad "Di poin ketiga visi lo, lo bilang mau meningkatkan transparansi kas OSIS."
    ad "Tahun lalu, kas OSIS minus. Flourine menutupinya dengan dana dari kantong panitia. Kalau lo jadi ketua, apa lo bakal bongkar bobrok pengurus lama ke publik?"
    
    menu:
        "Tentu saja. Siswa berhak tahu ke mana uang mereka pergi.":
            $ adam_meter += 3
            ar "Transparansi itu mutlak."
            ad "Bagus. Tapi kalau lo ngelakuin itu, lo bakal dimusuhi sama seluruh jajaran elit kelas 12 yang tahun lalu jadi panitia. Termasuk pembina OSIS."
            jump adam_path_klise_2

        "Kita harus lihat konteksnya dulu. Nggak semua hal bisa dibuka begitu saja.":
            $ adam_meter -= 3
            ar "Kalau membongkarnya malah bikin gaduh, kita harus cari cara yang lebih halus."
            ad "Jadi intinya lo bakal ngelindungin kesalahan mereka juga? Lo gak beda jauh sama Flourine."
            jump adam_path_klise_2_fail

label adam_path_klise_2:
    ad "Gimana lo mau mimpin kalau sejak awal lo udah bikin musuh sama orang-orang yang pegang kekuasaan di sekolah ini?"
    menu:
        "Gue bakal cari celah buat negosiasi sama mereka.":
            $ adam_meter -= 2
            ad "Negosiasi dengan koruptor? Cerdas, tapi licik."
            jump adam_ending

        "Gue nggak peduli. Kalau salah ya salah. Gue butuh dukungan siswa, bukan elit.":
            $ adam_meter += 4
            ad "Idealis radikal. Ini bakal jadi headline yang gila."
            jump adam_ending

label adam_path_klise_2_fail:
    ad "Gue kira lo beda, Aruna. Ternyata lo cuma politisi abu-abu yang cari aman."
    ad "Saran gue, mending lo revisi lagi visi lo sebelum debat minggu depan. Gue nggak dapet materi apa-apa dari lo."
    jump quest_adam_ending_fail

label adam_path_populis:
    ad "Kalau lo beneran mau dengerin semua orang, gimana kalau aspirasi mereka saling bertentangan?"
    ad "Ekskul Rohis minta jam istirahat Jumat diperpanjang, tapi ekskul Olahraga minta lapangan nggak dipakai buat kajian sore karena bentrok sama jadwal latihan basket. Lo mau dengerin siapa?"
    
    menu:
        "Gue akan ambil jalan tengah, misal bagi jadwal pemakaian lapangan.":
            $ adam_meter -= 2
            ad "Jalan tengah itu cuma ilusi. Di dunia nyata, kompromi berarti kedua belah pihak sama-sama kecewa."
            jump adam_path_populis_2

        "Gue bakal dengerin mayoritas. Siapa yang paling banyak butuh, itu yang didahulukan.":
            $ adam_meter += 3
            ad "Tirani mayoritas. Keputusan yang logis, tapi lo siap dibenci sama kaum minoritas di sekolah ini?"
            jump adam_path_populis_2

        "Gue akan panggil ketua dari kedua ekskul dan paksa mereka debat sampai ketemu solusi.":
            $ adam_meter += 5
            ad "Lempar tanggung jawab ke mereka? Manipulatif. Lo cuci tangan dan biarin mereka yang berantem. Gue makin tertarik."
            jump adam_path_populis_2

label adam_path_populis_2:
    ad "Satu pertanyaan terakhir. Kalau di tengah jalan lo sadar kalau janji populis lo ini gak mungkin terwujud, lo bakal lakuin apa?"
    menu:
        "Gue akan minta maaf secara terbuka ke seluruh siswa.":
            $ adam_meter += 2
            ad "Keberanian buat ngaku salah. Langkah PR yang bagus."
            jump adam_ending

        "Gue bakal diam-diam cari kambing hitam buat disalahin.":
            $ adam_meter += 4
            ad "Jawaban yang sangat gelap, tapi sangat jujur. Ini profil yang gue cari."
            jump adam_ending

label adam_path_agresif:
    ad "Flourine cari aman, Fanya cari tenar. Oke, pernyataan yang berani."
    ad "Tapi kalau gue kutip kata-kata lo ini di buletin besok, lo sadar kan Flourine bakal langsung pakai koneksi OSIS-nya buat nge-blacklist kampanye lo?"
    
    menu:
        "Tulis aja. Gue nggak takut sama Flourine.":
            $ adam_meter += 5
            ar "Biar satu sekolah tau kalau petahana anti-kritik."
            ad "Lo bener-bener mau bakar jembatan ya? Keren."
            jump adam_path_agresif_2
            
        "Tunggu dulu, jangan ditulis nama mereka secara langsung. Pakai inisial aja.":
            $ adam_meter -= 4
            ar "Kita main cantik aja, Dam. Biar orang mikir sendiri."
            ad "Tadi lo garang banget nyebut nama, giliran mau dipublish lo ciut. Pengecut."
            jump adam_path_agresif_2_fail

label adam_path_agresif_2:
    ad "Karena lo berani nantang Flourine, gue mau tanya. Lo tau kan kelemahan terbesar Flourine itu apa?"
    menu:
        "Dia suka bikin keputusan sepihak tanpa musyawarah.":
            $ adam_meter += 4
            ad "Bingo. Dan gue punya buktinya di sini. Pertanyaannya, kalau gue serahin bukti ini ke lo... lo mau pake buat apa?"
            menu:
                "Buat senjata rahasia saat debat terbuka.":
                    $ adam_meter += 3
                    ad "Brilian. Lo bakal permalukan dia di depan umum."
                    jump adam_ending
                "Gue bakal kasih ke panitia biar dia didiskualifikasi.":
                    $ adam_meter -= 2
                    ad "Bermain lewat jalur belakang? Kurang seru buat bahan berita, tapi efektif."
                    jump adam_ending

        "Gue nggak peduli kelemahan dia, gue menang pakai kekuatan gue sendiri.":
            $ adam_meter += 2
            ad "Klise lagi. Padahal gue tadinya mau kasih lo info berharga. Ya sudahlah."
            jump adam_ending

label adam_path_agresif_2_fail:
    ad "Kalau lo nggak berani pasang badan buat kata-kata lo sendiri, wawancara ini buang-buang waktu gue."
    ad "Keluar dari ruang jurnalistik sekarang."
    jump quest_adam_ending_fail

label adam_ending:
    ad "Oke, cukup. Gue udah dapet profil yang gue butuhin."
    ar "Gimana menurut lo? Apa artikelnya bakal menguntungkan buat gue?"
    if adam_meter >= 8:
        ad "Lo nggak usah khawatir. Besok pagi, nama Aruna bakal jadi perbincangan utama di kantin. Lo narasumber terbaik gue minggu ini."
        "Adam tersenyum puas. Wawancara ini berjalan sangat sukses."
    ar "Jadi, gimana? Lo dapet apa yang lo mau?"
    ad "Lebih dari cukup."
    
    if adam_meter >= 10:
        ad "Lo bahaya, Aruna. Dan orang-orang bakal suka baca soal seberapa bahayanya lo."
        ar "Gue anggap itu pujian."
        ad "Anggap aja gitu. Besok cek mading. Nama lo bakal ada di sana."
        "Wawancara ini terasa seperti adu tinju mental, dan kamu baru saja menang KO."
    elif adam_meter >= 5:
        ad "Profil lo... lumayan. Nggak sempurna, tapi jauh lebih baik dari Flourine yang kaku."
        ar "Thanks. Gue tunggu artikelnya."
        ad "Ya. Jangan berharap terlalu banyak, gue bakal tetap netral."
        "Kamu keluar dengan perasaan lega. Wawancara yang intens."
    else:
        ad "Jujur, artikelnya bakal biasa aja. Lo nggak se-edgy yang lo kira."
        ar "Gue cuma jadi diri sendiri."
        ad "Sayangnya 'diri sendiri' lo itu kurang ngejual."
        "Kamu meninggalkan ruangan dengan sedikit kecewa."
    
    jump quest_adam_wrap_up

label quest_adam_wrap_up:
    $ complete_quest("adam", adam_meter)
    
    "Quest Adam selesai! Akumulasi Support: [adam_meter]."
    "Kamu mendapatkan [npc_state['adam']['votes_banked']] vote dari ekskul Jurnalistik."
    jump end_day_routine


label robotika_heist:
    scene expression Transform("images/bg_school_night.jpg", size=(1920, 1080))
    "Jam dua belas malam. Sekolah yang biasanya riuh dengan suara bel dan tawa siswa kini terbaring dalam keheningan yang mencurigakan."
    "Bulan purnama menyoroti gapura sekolah yang tertutup, memberikan bayangan panjang yang terlihat seperti mencengkeram."
    "Aruna memegang peta sekolah yang dilukis tangan di kertas bekas. Ada tanda merah di lantai dua—ruangan kepala sekolah."
    "Piala Ekskul Robotika, yang tanpa alasan jelas disita kepala sekolah dua bulan lalu, harus kembali ke tempatnya."
    "Tapi ada sesuatu yang tidak beres malam ini. Aruna bisa merasakannya dalam tulang-tulangnya."

    "Terdengar suara langkah kaki di kejauhan. Berat. Teratur. Tidak seperti langkah biasa."

    menu:
        "Sembunyi di balik tembok depan dan tunggu langkah itu lewat.":
            "Aruna menekan punggung ke tembok dingin, napas tertahan."
            "Langkah itu mendekat. Berat sekali—seperti seseorang yang membawa beban."
            "Sebuah sosok tinggi melewati gapura. Satpam Pak Budi... tapi dia membawa sesuatu yang dibungkus kain putih."
            "Aruna menahan napas saat Pak Budi berhenti sejenak, menengok ke arah gelap di mana Aruna bersembunyi."
            "Tiga detik terasa seperti satu jam."
            "Pak Budi melanjutkan langkahnya menuju gedung utama. Aruna bisa melihat kain putih itu bergerak-gerak—seperti ada sesuatu yang hidup di dalamnya."
            jump heist_choice_1

        "Lari menuju sisi kanan tembok dan cari jalan alternatif.":
            "Aruna memilih bergerak cepat daripada menunggu."
            "Berlari menyusuri pagar samping sekolah, mencari tembok yang lebih rendah."
            "Suara langkah kaki itu tidak terdengar lagi, tapi ada suara lain."
            "Kicauan burung hantu yang terlalu dekat. Suara rantai bergerak."
            "Aruna menemukan tembok rendah di dekat area belakang lab, tapi ada penutup kawat berduri yang tampak baru dipasang."
            "Terdengar suara gemerisik dari semak-semak di sebelah kanan."
            jump heist_choice_1_alternative

        "Kembali dulu. Ini terlalu mencurigakan.":
            "Aruna memutuskan untuk mundur. Malam ini ada sesuatu yang salah."
            "Tapi saat membalikkan badan, sebuah tangan menepuk bahunya dari belakang."
            "Juan berdiri di sana dengan mata merah karena kurang tidur."
            juan "Lo beneran bakal ke lantai dua malam ini, Aruna?"
            juan "Gue udah nunggu dari jam sembilan. Gue bisa bantu lo, tapi ada kondisinya."
            jump heist_juan_encounter

        "Cari Ferdi di area belakang lab.":
            "Aruna ingat Ferdi sering berada di area belakang lab Robotika bahkan malam-malam."
            "Berjalan menuju area itu dengan hati-hati."
            "Di balik gudang Robotika, Aruna melihat siluet seseorang sedang duduk di bangku kayu tua."
            "Ferdi sedang memegang kepala dengan kedua tangannya."
            jump heist_ferdi_encounter

label heist_choice_1:
    "Aruna berdiri di tempat, jantung masih berdebar."
    "Pak Budi sudah masuk ke gedung utama. Sekarang ada dua pilihan jalan menuju lantai dua."

    menu:
        "Masuk lewat pintu utama yang mungkin tidak terkunci.":
            "Pintu utama sekolah biasanya tidak dikunci rapat, tapi malam ini..."
            "Aruna mendekati pintu kayu besar itu. Ada gembok baru—berwarna merah, bukan gembok biasa."
            "Tapi ada celah kecil di bawah pintu. Aruna bisa melihat ada sinar remang keluar dari dalam."
            "Ada seseorang di ruang depan."
            jump heist_main_door

        "Cari jalan menuju sisi belakang gedung, naik lewat tangga darurat.":
            "Aruna mengelilingi gedung ke arah belakang. Tangga darurat besi terlihat menggantung di lantai dua."
            "Tapi ada kamera CCTV baru yang dipasang tepat di bawah tangga itu."
            "Lampu merah kamera berkedip-kedip seperti mata makhluk buas."
            jump heist_staircase

        "Coba lewat jendela lab di lantai satu dulu.":
            "Jendela lab Kimia di lantai satu sering dibiarkan terbuka karena AC rusak."
            "Aruna mendekati jendela itu. Benar, ada celah kecil."
            "Tapi saat mencongkel, ada suara teriakan tertahan dari dalam lab."
            "Seseorang sedang menangis di dalam gelap."
            jump heist_lab_window

label heist_choice_1_alternative:
    "Aruna terdiam di hadapan kawat berduri baru itu."
    "Suara gemerisik dari semak-semak semakin jelas."

    menu:
        "Abaikan suara itu dan temukan cara lewat kawat berduri.":
            "Aruna mencari kayu atau tali untuk menutupi kawat itu."
            "Ada papan bekas di sebelahnya. Aruna meletakkannya di atas kawat."
            "Berhasil menyeberang, tapi saat turun ke sisi lain, kaki Aruna terkena rantai yang tergeletak di tanah."
            "PRING! Suara berdengung menghentak malam."
            "Suara langkah kaki dari dalam gedung berubah arah menuju ke sini."
            jump heist_pursuit_start

        "Selidiki dulu suara dari semak-semak.":
            "Aruna mendekati semak-semak dengan hati-hati."
            "Bayangan kecil melompat keluar—kucing hitam dengan kerah berwarna biru."
            "Kucing itu menatap Aruna, lalu berlari menuju pagar yang ada celah kecilnya."
            "Celah itu cukup besar untuk orang dewasa masuk, tapi terlihat seperti jalan ke gudang belakang."
            jump heist_cat_path

        "Balik dan cari cara lain lagi.":
            "Aruna memutuskan jalan ini terlalu berisiko."
            "Tapi saat berbalik, Pak Budi muncul dari balik pojok gedung."
            "Wajahnya pucat, ada luka gores di pipinya."
            "Pak Budi menatap Aruna dengan mata kosong, lalu berbalik dan berlari menuju gedung utama tanpa berkata apa-apa."
            jump heist_budi_encounter

label heist_ferdi_encounter:
    "Ferdi mengangkat kepalanya perlahan saat mendengar langkah kaki Aruna."
    "Matanya merah, wajahnya penuh kelelahan yang mendalam. Ada botol air kosong di sebelahnya."

    ferdi "Aruna? Lo lagi nyari gue malam-malam gini?"
    ferdi "Atau lo lagi nyari sesuatu yang lain di sekolah?"

    menu:
        "Tanya Ferdi apa yang sedang dia lakukan di area belakang lab.":
            ar "Ferdi, lo ngapain di sini? Keliatan lo lagi berat banget."
            ferdi "Gue... gue lagi mikirin nasib ekskul kita."
            ferdi "Dua bulan Pak Kepsek sita piala kita. Tapi itu baru permulaan."
            ferdi "Sekarang dia mau tutup ekskul Robotika dengan alasan 'efisiensi anggaran'."
            jump heist_ferdi_concern

        "Jujur mengakui ingin mengambil piala Robotika kembali.":
            ar "Gue dateng buat ambil piala kita kembali dari ruangan Pak Kepsek."
            ferdi "Lo nyuri? Serius?"
            ferdi "Gue appreciate niat lo, tapi itu terlalu berisiko."
            ferdi "Gue sudah pertimbangkan segala cara, tapi Pak Kepsek terlalu kuat."
            jump heist_ferdi_warning

        "Tanya Ferdi di mana Juan dan Faizal malam ini.":
            ar "Lo sendirian? Juan dan Faizal di mana?"
            ferdi "Juan sedang cari jalan lain buat urus dokumen kita."
            ferdi "Faizal... gue nggak tau. Dia udah nggak muncul di lab sejak dua hari lalu."
            ferdi "Gue khawatir sama dia. Pak Kepsek panggil dia ke ruangannya hari terakhir."
            jump heist_ferdi_worry

label heist_ferdi_concern:
    "Ferdi menghela napas panjang, tangannya gemetar sedikit."

    ferdi "Gue sebagai ketua ekskul merasa gagal total."
    ferdi "Gue nggak bisa lindungi anggota gue. Gue nggak bisa jaga piala kita."
    ferdi "Sekarang gue harus pikirin gimana caranya nggak bikin anak-anak kecewa kalau ekskul kita bubar."

    menu:
        "Tawarkan bantuan untuk mempertahankan ekskul Robotika.":
            ar "Jangan menyerah, Ferdi. Gue bakal bantu lo pertahain ekskul ini."
            ferdi "Bantu gimana? Lo calon ketua OSIS, bukan penyelamat."
            ferdi "Tapi... kalau lo beneran mau bantu, gue punya ide."
            jump heist_ferdi_proposal

        "Tanyakan apakah ada cara legal untuk melawan Pak Kepsek.":
            ar "Gak ada cara legal nggak? Lo mustahil coba semua jalur resmi?"
            ferdi "Gue udah lapor ke pembina, ke MPK, bahkan ke orang tua siswa."
            ferdi "Semua pada bilang 'ikuti aturan' atau 'sabar aja'."
            ferdi "Padahal aturan itu sendiri yang dipakai Pak Kepsek buat tekan kita."
            jump heist_ferdi_frustration

        "Fokus kembali ke misi mengambil piala.":
            ar "Intinya gue pengen ambil piala kita dulu. Itu simbol ekskul kita."
            ferdi "Piala cuma simbol, Aruna. Kalau ekskul bubar, piala nggak ada artinya."
            ferdi "Tapi kalau lo tetep mau ngambil, gue nggak bisa ngelarang lo."
            jump heist_ferdi_resignation

label heist_ferdi_warning:
    "Ferdi menatap Aruna dengan mata yang penuh kekhawatiran."

    ferdi "Pak Kepsek udah pasang kamera baru di semua sudut sekolah."
    ferdi "Dia udah ganti semua gembok dengan yang elektronik."
    ferdi "Bahkan dia punya tim keamanan khusus yang berjaga malam ini."
    ferdi "Lo pikir lo bisa masuk ke ruangannya cuma kayak gitu?"

    menu:
        "Tanyakan bagaimana Ferdi tahu semua detail keamanan itu.":
            ar "Lo tau banget soal keamanan sekolah. Dari mana lo dapat info?"
            ferdi "Gue... gue pernah dipanggil Pak Kepsek ke ruangannya."
            ferdi "Dia nunjukin ke gue semua sistem keamanan baru yang dia pasang."
            ferdi "Dia bilang ini buat 'keamanan', tapi gue rasa ini buat ngawasin kita."
            jump heist_ferdi_intel

        "Terima tantangan dan tetap melanjutkan misi.":
            ar "Makin berat makin seru. Gue tetep mau coba."
            ferdi "Lo nekat banget. Tapi gue hormati keberanian lo."
            ferdi "Kalau lo beneran mau, gue kasih info yang mungkin bisa bantu."
            jump heist_ferdi_assistance

        "Minta Ferdi untuk membantu secara langsung.":
            ar "Kalau lo tau semua itu, kenapa nggak lo yang ambil pialanya?"
            ferdi "Gue nggak bisa. Gue udah di-warning sama Pak Kepsek."
            ferdi "Kalau gue ketahuan macem-macem lagi, ekskul kita langsung bubar."
            jump heist_ferdi_constraints

label heist_ferdi_worry:
    "Ferdi menatap ke arah gedung utama dengan wajah gelisah."

    ferdi "Gue udah coba hubungi Faizal, tapi HP-nya mati."
    ferdi "Juan bilang Faizal dipanggil Pak Kepsek buat 'proyek khusus'."
    ferdi "Gue nggak enak banget ngerasa nggak bisa bantu temen gue sendiri."

    menu:
        "Tawarkan untuk mencari Faizal bersama-sama.":
            ar "Kita cari Faizal bareng. Mungkin dia ada di suatu tempat di sekolah."
            ferdi "Lo mau bantu gue cari Faizal? Padahal lo dateng buat piala?"
            ferdi "Gue... gue hargai banget kalau lo mau prioritaskan temen daripada piala."
            jump heist_ferdi_gratitude

        "Fokus ke piala dulu, baru cari Faizal nanti.":
            ar "Gue ambil piala dulu, abis itu gue bantu lo cari Faizal."
            ferdi "Prioritas lo tetep piala ya? Gue ngerti."
            ferdi "Tapi hati-hati, kalau Faizal dalam bahaya, piala jadi nomor sekian."
            jump heist_ferdi_disappointment

        "Tanyakan detail tentang 'proyek khusus' Pak Kepsek.":
            ar "Proyek khusus apa? Pak Kepsek mau Faizal ngapain?"
            ferdi "Juan nggak tau detailnya. Cuma bilang sesuatu soal IT dan pemrograman."
            ferdi "Faizal emang jago IT, tapi proyek Pak Kepsek pasti nggak bener."
            jump heist_ferdi_suspicion

label heist_ferdi_proposal:
    "Ferdi menatap Aruna dengan sedikit harapan di matanya."

    ferdi "Gue punya ide, tapi ini nggak legal sama sekali."
    ferdi "Kita nggak ambil piala doang. Kita ambil bukti-bukti juga."
    ferdi "Bukti bahwa Pak Kepsek salah pakai dana ekskul dan melanggar hak siswa."
    ferdi "Kalau kita punya bukti, kita bisa bikin dia mundur atau minimal lepas kendali."

    menu:
        "Setuju dengan rencana Ferdi dan kumpulkan bukti.":
            ar "Ini ide bagus! Bukti lebih kuat dari sekadar piala."
            ferdi "Bukan ide bagus, ini ide berbahaya. Tapi mungkin satu-satunya jalan."
            ferdi "Gue kasih lo petanya tempat dia simpan dokumen-dokumen rahasia."
            jump heist_ferdi_evidence_plan

        "Tanya risiko dari rencana ini.":
            ar "Risikonya apa? Kalau ketahuan bisa-bisa kita di-skors."
            ferdi "Bukan cuma skors. Bisa di-drop out, bahkan kriminal kalau Pak Kepsek mau main kotor."
            ferdi "Tapi gue udah terlalu capek nurutin aturan yang salah."
            jump heist_ferdi_risk_assessment

        "Tetap fokus ke piala saja, yang lain besok.":
            ar "Terlalu berat sekaligus. Gue ambil piala dulu aja."
            ferdi "Yaudah. Gue nggak maksa. Tapi ingat, piala tanpa perubahan cuma hiasan."
            jump heist_ferdi_trophy_focus

label heist_ferdi_frustration:
    "Ferdi memukul bangku kayu di sampingnya dengan frustasi."

    ferdi "Semua pada bilang 'prosedur', 'aturan', 'birokrasi'."
    ferdi "Sementara Pak Kepsek main kartu truf buat tekan kita."
    ferdi "Dia pegang semua kunci: dana, fasilitas, bahkan masa depan akademik kita."

    menu:
        "Tawarkan bantuan politik sebagai calon ketua OSIS.":
            ar "Kalau gue jadi ketua OSIS, gue bisa bantu lo dari dalam sistem."
            ferdi "Lo jadi ketua OSIS? Lo serius mau bantu kita?"
            ferdi "Kalau lo beneran komit, gue kasih lo dukungan penuh ekskul Robotika."
            jump heist_ferdi_political_support

        "Cari cara untuk mengungkap kecurangan Pak Kepsek.":
            ar "Gue bantu lo cari bukti kecurangan Pak Kepsek supaya bisa dilapor."
            ferdi "Gue udah coba cari bukti, tapi dokumen-dokumen penting dia simpan di ruang pribadi."
            ferdi "Ruangan yang keamanannya sangat ketat."
            jump heist_ferdi_evidence_challenge

        "Tanyakan apakah Ferdi pernah mempertimbangkan melawan secara terbuka.":
            ar "Lo pernah mikir buat demo atau protes terbuka nggak?"
            ferdi "Protes? Dengan siapa? Anak-anak pada takut sama Pak Kepsek."
            ferdi "Kalau ada yang protes, dia langsung kena sanksi sebelum kata kedua keluar."
            jump heist_ferdi_fear_factor

label heist_ferdi_resignation:
    "Ferdi mengangkat bahu dengan lelah."

    ferdi "Silakan. Gue nggak bisa ngelarang lo."
    ferdi "Tapi ingat, kalau lo ketahuan, jangan sebut nama gue atau ekskul kita."
    ferdi "Gue nggak mau ekskul Robotika ikut kena imbas kesalahan lo."

    menu:
        "Janji akan melindungi identitas Ferdi dan ekskul.":
            ar "Gue janji, lo dan ekskul Robotika nggak bakal kena imbas."
            ferdi "Gue percaya sama lo, Aruna. Lo beda dari yang lain."
            ferdi "Kalau lo gagal, jangan salahkan gue nggak kasih warning."
            jump heist_ferdi_trust

        "Tanyakan apakah Ferdi punya tips untuk menghindari keamanan.":
            ar "Sebelum gue pergi, ada tips nggak buat nghindarin keamanan?"
            ferdi "Tips? Jangan pergi lewat jalan yang obvious."
            ferdi "Pak Kepsek pintar, dia pasti prediksi jalan yang paling logis."
            jump heist_ferdi_tactical_advice

        "Pamit dan langsung melanjutkan misi.":
            ar "Oke, gue pergi sekarang. Makasih infonya."
            ferdi "Hati-hati, Aruna. Dan... makasih udah peduli."
            jump heist_choice_1

label heist_ferdi_intel:
    "Ferdi menunduk, suaranya rendah."

    ferdi "Gue nggak sengaja dapet info ini. Pak Kepsek yang nunjukin ke gue."
    ferdi "Dia kayak mau pamer kekuasaan sekaligus ngintimidasi."
    ferdi "Dia nunjukin monitor CCTV yang bisa pantau seluruh sekolah."
    ferdi "Dia nunjukin sistem gembok elektronik yang cuma dia yang punya kodenya."

    menu:
        "Gunakan intel Ferdi untuk merencanakan infiltrasi yang lebih baik.":
            ar "Dengan info ini, gue bisa rencanain infiltrasi yang lebih aman."
            ferdi "Gue kasih lo skema kasar sistem keamanan dari yang gue inget."
            ferdi "Tapi ingat, Pak Kepsek bisa ubah setting kapan aja."
            jump heist_ferdi_blueprint

        "Tanyakan apakah ada celah di sistem keamanan itu.":
            ar "Dari yang lo liat, ada celah nggak di sistemnya?"
            ferdi "Ada satu. Saat jam 2-3 pagi, sistem CCTV restart buat maintenance."
            ferdi "Tapi cuma 5 menit. Itu kesempatan lo satu-satunya."
            jump heist_ferdi_vulnerability

        "Skeptis terhadap intel yang diberikan Pak Kepsek.":
            ar "Lo yakin info yang diberi Pak Kepsek bener? Bisa jadi jebakan."
            ferdi "Gue juga mikirin itu. Tapi dari yang gue liat, sistemnya beneran ada."
            ferdi "Tapi bisa jadi dia sengaja kasih info buat uji siapa yang berani nyusup."
            jump heist_ferdi_trap_suspicion

label heist_ferdi_assistance:
    "Ferdi mengambil kertas dari sakunya."

    ferdi "Ini peta kasar jalur yang mungkin aman dari kamera."
    ferdi "Gue gambar dari ingetan waktu dia nunjukin ke gue."
    ferdi "Tapi gue nggak jamin 100% akurat. Pak Kepsek bisa ubah kapan aja."

    menu:
        "Gunakan peta Ferdi sebagai panduan utama.":
            ar "Makasih, Ferdi. Ini bakal sangat bantu."
            ferdi "Semoga bener. Kalau lo gagal, jangan salahkan gue ya."
            jump heist_ferdi_map_usage

        "Gunakan peta Ferdi sebagai referensi tambahan saja.":
            ar "Gue pakai ini referensi tambahan, tapi gue tetap pegang insting gue."
            ferdi "Pilihan bijak. Jangan 100% andalkan peta orang lain."
            jump heist_ferdi_caution

        "Tanyakan apakah Ferdi punya informasi lain yang berguna.":
            ar "Masih ada info lain nggak yang bisa bantu gue?"
            ferdi "Satu. Pak Kepsek punya kebiasaan."
            ferdi "Setiap jam 2 pagi dia minum kopi di ruang guru. Itu waktu dia paling lengah."
            jump heist_ferdi_habit_intel

label heist_ferdi_constraints:
    "Ferdi menatap tangan sendiri yang gemetar."

    ferdi "Gue udah di-warning. Kalau gue ketahuan macem-macem, bukan cuma gue."
    ferdi "Seluruh ekskul Robotika bakal kena sanksi. Gue nggak mau ngorbanin anak-anak."
    ferdi "Itu sebabnya gue di sini. Gue lagi mikirin cara buat selamatin mereka tanpa melanggar aturan."

    menu:
        "Hargai keputusan Ferdi dan tawarkan bantuan alternatif.":
            ar "Gue ngerti posisi lo, Ferdi. Gue bantu cari cara lain."
            ferdi "Cara lain? Gue udah mikirin semuanya."
            ferdi "Mungkin lo sebagai orang luar bisa lihat yang gue nggak lihat."
            jump heist_ferdi_alternative_perspective

        "Tekan Ferdi untuk berani melawan demi ekskulnya.":
            ar "Lo ketua, Ferdi! Lo harus berani lindungin anggota lo!"
            ferdi "Mudah bilang gitu kalau bukan posisi gue!"
            ferdi "Lo nggak tau gimana rasanya tanggung jawab 20 orang di pundak lo!"
            jump heist_ferdi_emotional_break

        "Terima penjelasan Ferdi dan fokus ke misi sendiri.":
            ar "Oke, gue ngerti. Gue nggak akan maksa lo."
            ferdi "Makasih ngerti. Gue cuma bisa doain lo berhasil."
            jump heist_choice_1

label heist_ferdi_gratitude:
    "Ferdi menatap Aruna dengan mata yang berkaca-kaca."

    ferdi "Gue... gue nggak nyangka lo bakal prioritasin temen daripada piala."
    ferdi "Banyak orang yang dateng ke ekskul kita cuma buat piala, buat prestasi."
    ferdi "Tapi lo... lo beda."

    menu:
        "Jelaskan bahwa teman lebih penting dari piala.":
            ar "Piala bisa dicari lagi. Tapi kalau ada temen yang bahaya, itu yang prioritas."
            ferdi "Makasih, Aruna. Lo bener-bener temen yang baik."
            ferdi "Kita cari Faizal bareng. Gue punya dugaan dia di mana."
            jump heist_ferdi_faizal_search

        "Tanyakan dugaan Ferdi tentang lokasi Faizal.":
            ar "Lo punya dugaan Faizal di mana?"
            ferdi "Juan bilang terakhir kali Faizal ada di lab Kimia."
            ferdi "Tapi itu sudah dua hari lalu. Gue takut dia udah dipindah."
            jump heist_ferdi_location_theory

        "Fokus ke pencarian Faizal dengan hati-hati.":
            ar "Oke, kita cari Faizal pelan-pelan. Hati-hati sama keamanan."
            ferdi "Gue ikut lo. Gue lebih tau area sekolah dari lo."
            jump heist_ferdi_team_search

label heist_ferdi_disappointment:
    "Ferdi mengangguk pelan, tapi ekspresinya menunjukkan kekecewaan."

    ferdi "Yaudah. Gue ngerti prioritas lo."
    ferdi "Tapi gue pengen kasih tau satu hal."
    ferdi "Piala itu pernah disimpan di lemari besi pribadi Pak Kepsek."
    ferdi "Tapi dua hari lalu dia pindahin ke lokasi yang gue nggak tau."

    menu:
        "Tanyakan kenapa Pak Kepsek memindahkan piala.":
            ar "Kenapa dia pindahin piala? Ada apa?"
            ferdi "Gue nggak tau pasti. Mungkin karena dia tau ada yang bakal nyuri."
            ferdi "Atau mungkin ada alasan lain yang lebih gelap."
            jump heist_ferdi_trophy_mystery

        "Terima informasi dan tetap melanjutkan misi.":
            ar "Oke, gue tetap coba cari piala di ruangannya."
            ferdi "Hati-hati. Kalau lokasinya udah berubah, lo bisa ketemu hal yang nggak diharapkan."
            jump heist_choice_1

        "Ubah rencana dan cari Faizal dulu.":
            ar "Gue ubah rencana. Cari Faizal dulu, baru piala."
            ferdi "Lo yakin? Faizal bisa jadi lebih susah dicari dari piala."
            ar "Teman lebih penting, Ferdi."
            ferdi "Baik. Kita cari Faizal bareng."
            jump heist_ferdi_faizal_search

label heist_ferdi_suspicion:
    "Ferdi menatap ke arah gedung utama dengan rasa curiga."

    ferdi "Juan cuma bilang 'proyek khusus' soal IT dan pemrograman."
    ferdi "Tapi Faizal itu jenius di bidang hacking dan security system."
    ferdi "Gue takut Pak Kepsek pakai kemampuan Faizal buat hal yang nggak bener."

    menu:
        "Tanyakan apakah Ferdi pernah mencoba menghubungi Faizal.":
            ar "Lo pernah coba hubungi Faizal lewat cara lain?"
            ferdi "Gue udah coba semua: WA, telepon, bahkan ke rumahnya."
            ferdi "Orang tuanya bilang Faizal 'pergi ke sekolah buat tugas tambahan'."
            ferdi "Tugas tambahan tengah malam? Ngaco."
            jump heist_ferdi_contact_attempts

        "Waspadai kemungkinan Faizal dipaksa melakukan sesuatu yang ilegal.":
            ar "Kalau Faizal dipaksa ngelakuin hal ilegal, kita harus bantu dia."
            ferdi "Tapi gimana caranya? Kita nggak tau dia di mana."
            ferdi "Dan kalau kita salah langkah, malah bisa bahayain dia."
            jump heist_ferdi_rescue_dilemma

        "Curigai Pak Kepsek sedang membangun sistem pengawasan.":
            ar "Proyek IT tengah malam? Mungkin dia lagi bangun sistem pengawasan."
            ferdi "Gue juga mikirin itu. Sistem yang bisa pantau semua aktivitas siswa."
            ferdi "Kalau itu bener, ini lebih berbahaya dari sekadar piala."
            jump heist_ferdi_surveillance_fear

label heist_ferdi_evidence_plan:
    "Ferdi menyerahkan kertas lipat kecil ke Aruna."

    ferdi "Ini petanya. Dokumen rahasia Pak Kepsek biasanya disimpan di laci kiri meja kerjanya."
    ferdi "Tapi dia juga punya lemari besi kecil di sudut ruangan."
    ferdi "Gue nggak tau isinya apa, tapi itu pasti penting."

    menu:
        "Ikuti rencana Ferdi dan kumpulkan bukti.":
            ar "Oke, gue ikuti rencana lo. Kita ambil bukti-bukti."
            ferdi "Hati-hati. Kunci lemari besi itu elektronik, cuma dia yang tau kodenya."
            ferdi "Tapi mungkin lo bisa nemu kodenya di sekitar meja kerjanya."
            jump heist_ferdi_evidence_execution

        "Tanyakan apakah ada cara untuk membuka lemari besi tanpa kode.":
            ar "Kalo nggak ada kodenya, gimana cara buka lemari besinya?"
            ferdi "Ada teknik lockpick buat lemari besi elektronik, tapi itu butuh skill khusus."
            ferdi "Atau... lo bisa coba tebak kodenya. Orang sering pake tanggal lahir atau angka gampang."
            jump heist_ferdi_safe_cracking

        "Fokus ke dokumen di laci dulu, abaikan lemari besi.":
            ar "Lemari besi terlalu berisiko. Gue fokus ke laci dulu aja."
            ferdi "Pilihan aman. Tapi barang-barang paling penting biasanya di lemari besi."
            jump heist_ferdi_safe_focus

label heist_ferdi_risk_assessment:
    "Ferdi menatap Aruna dengan serius."

    ferdi "Risikonya besar. Bukan cuma buat lo, tapi buat gue dan seluruh ekskul."
    ferdi "Kalau ketahuan, Pak Kepsek pasti bakal balas dendam ke kita."
    ferdi "Dia bisa tutup ekskul kita, skors anak-anak, bahkan blacklist nama kita."

    menu:
        "Terima risiko demi keadilan.":
            ar "Gue terima risikonya. Kalau nggak ada yang berani, nggak ada yang berubah."
            ferdi "Lo berani banget, Aruna. Gue respect itu."
            ferdi "Tapi ingat, keberanian tanpa strategi cuma bunuh diri."
            jump heist_ferdi_bravery_acknowledged

        "Pertimbangkan kembali dan cari cara yang lebih aman.":
            ar "Mungkin gue harus pikir ulang. Terlalu berisiko."
            ferdi "Gue nggak maksa. Kalau lo mau mundur, gue ngerti."
            ferdi "Tapi kalau semua orang pada mundur, siapa yang bakal berubah?"
            jump heist_ferdi_retreat_consideration

        "Tanyakan apakah ada cara untuk meminimalkan risiko.":
            ar "Gimana caranya biar risikonya lebih kecil?"
            ferdi "Plan semuanya harus matang. Exit strategy harus jelas."
            ferdi "Dan yang paling penting: jangan greedy. Ambil yang cukup, lalu kabur."
            jump heist_ferdi_risk_management

label heist_ferdi_trophy_focus:
    "Ferdi mengangguk, sedikit kecewa tapi mengerti."

    ferdi "Yaudah. Silakan ambil piala."
    ferdi "Tapi ingat satu hal: kalau Pak Kepsek tetap berkuasa, dia bisa sita piala lagi kapan aja."
    ferdi "Tanpa perubahan sistem, piala cuma sementara."

    menu:
        "Terima nasihat Ferdi dan tetap fokus ke piala.":
            ar "Gue ngerti. Untuk sekarang, piala dulu aja."
            ferdi "Baik. Hati-hati, dan semoga berhasil."
            jump heist_choice_1

        "Pikirkan kembali dan ubah prioritas.":
            ar "Lo bener. Mungkin gue harus pikir ulang prioritas gue."
            ferdi "Gue seneng lo mikirin begitu. Itu tandanya lo pemimpin yang baik."
            jump heist_ferdi_priority_change

        "Tanyakan apa yang seharusnya menjadi prioritas.":
            ar "Jadi menurut lo, apa yang harus jadi prioritas?"
            ferdi "Perubahan. Bukan simbol."
            ferdi "Kalau lo bisa bikin sistem yang lebih adil, piala bakal ikut sendiri."
            jump heist_ferdi_wisdom

label heist_ferdi_political_support:
    "Ferdi menatap Aruna dengan mata yang bersinar."

    ferdi "Lo serius mau bantu kita dari dalam sistem?"
    ferdi "Kalau lo beneran komit, seluruh ekskul Robotika bakal dukung lo 100%."
    ferdi "Bukan cuma suara doang, tapi dukungan penuh dalam segala hal."

    menu:
        "Buat komitmen resmi untuk membantu ekskul Robotika.":
            ar "Gue komit. Kalau gue jadi ketua OSIS, ekskul Robotika prioritas gue."
            ferdi "Gue percaya sama lo, Aruna. Ini serius."
            ferdi "Dukungan Robotika bakal jadi aset besar buat kampanye lo."
            jump heist_ferdi_alliance_formed

        "Berhati-hati dengan janji politik.":
            ar "Gue mau bantu, tapi gue nggak mau janji-janji kosong."
            ferdi "Gue ngerti. Tapi minimal lo harus beneran coba."
            ferdi "Gue dan anak-anak bakal evaluasi tindakan lo, bukan janji."
            jump heist_ferdi_cautionary_trust

        "Tanyakan apa yang ekskul Robotika butuhkan secara spesifik.":
            ar "Secara spesifik, kalian butuh apa dari gue?"
            ferdi "Dana yang adil, fasilitas yang layak, dan perlindungan dari intimidasi."
            ferdi "Tiga hal sederhana tapi mustahil dapat selama Pak Kepsek berkuasa."
            jump heist_ferdi_specific_needs

label heist_ferdi_evidence_challenge:
    "Ferdi menghela napas."

    ferdi "Gue udah coba. Ruang Pak Kepsek keamanannya sangat ketat."
    ferdi "CCTV di luar, sensor gerak di dalam, gembok elektronik di pintu."
    ferdi "Bahkan dia punya alarm yang langsung hubungin ke HP-nya."

    menu:
        "Tantang keamanan itu dengan strategi yang matang.":
            ar "Gue butuh strategi yang matang buat tembus semua itu."
            ferdi "Strategi bagus, tapi gue nggak punya skill buat ngelakuinnya."
            ferdi "Lo butuh ahli teknis atau minimal info detail soal sistemnya."
            jump heist_ferdi_technical_challenge

        "Cari celah di sistem keamanan Pak Kepsek.":
            ar "Pasti ada celah di sistemnya. Manusia nggak sempurna."
            ferdi "Mungkin ada. Tapi Pak Kepsek itu cerdik."
            ferdi "Dia mungkin sengaja tinggalin celah kecil buat 'perangkap'."
            jump heist_ferdi_trap_possibility

        "Ubah pendekatan dan cari cara lain.":
            ar "Kalau tembus keamanan mustahil, gue cari cara lain."
            ferdi "Cara lain apa? Semua jalur legal udah tertutup."
            ferdi "Mungkin lo harus kreatif nemu jalan yang nggak terpikir orang."
            jump heist_ferdi_creative_approach

label heist_ferdi_fear_factor:
    "Ferdi menunduk, suaranya gemetar."

    ferdi "Anak-anak pada takut. Gue juga takut."
    ferdi "Pak Kepsek bukan cuma bisa skors. Dia bisa hancurin masa depan akademik kita."
    ferdi "Dia bisa kasih nilai jelek, bikin rekomendasi buruk, bahkan blacklist ke universitas."

    menu:
        "Tawarkan perlindungan bagi ekskul Robotika.":
            ar "Kalau gue jadi ketua OSIS, gue bakal lindungin kalian dari dia."
            ferdi "Lo bisa lindungin kita dari kepala sekolah? Bagaimana caranya?"
            ferdi "Kepala sekolah punya kuasa lebih besar dari ketua OSIS."
            jump heist_ferdi_power_dynamics

        "Mendorong Ferdi untuk berani demi masa depan anak-anak.":
            ar "Lo harus berani, Ferdi! Demi masa depan anak-anak Robotika!"
            ferdi "Mudah bilang kalau bukan posisi gue!"
            ferdi "Lo nggak tau gimana rasanya tanggung jawab 20 orang di pundak lo!"
            jump heist_ferdi_emotional_pressure

        "Akui ketakutan dan cari cara bersama-sama.":
            ar "Gue ngerti lo takut. Gue juga takut. Tapi kita harus lawan bareng."
            ferdi "Bareng? Lo mau bantu gue?"
            ferdi "Kalau lo beneran mau bantu, gue mungkin bisa lebih berani."
            jump heist_ferdi_shared_courage

label heist_ferdi_blueprint:
    "Ferdi memberikan skema kasar yang digambar di kertas bekas."

    ferdi "Ini skema dari yang gue inget. Garis merah itu kamera."
    ferdi "Kotak hijau itu area blind spot. Lingkaran kuning itu sensor gerak."
    ferdi "Tapi ingat, ini bisa berubah kapan aja."

    menu:
        "Hafalkan skema dan gunakan sebagai panduan.":
            ar "Makasih, Ferdi. Gue hafal skemanya."
            ferdi "Hati-hati. Jangan 100% andalkan ini."
            ferdi "Gunakan insting lo juga. Kalau ada yang nggak bener, segera kabur."
            jump heist_ferdi_blueprint_usage

        "Tanyakan apakah ada rute yang paling aman.":
            ar "Dari skema ini, rute mana yang paling aman?"
            ferdi "Rute belakang lewat gudang. Tapi itu jauh dan makan waktu."
            ferdi "Rute cepat lewat tangga darurat, tapi kamera di sana aktif."
            jump heist_ferdi_route_analysis

        "Curigai skema ini bisa jadi jebakan.":
            ar "Lo yakin skema ini bener? Bisa jadi jebakan Pak Kepsek."
            ferdi "Gue juga mikirin itu. Tapi gue nggak punya pilihan lain."
            ferdi "Lo harus putuskan sendiri: percaya atau tidak."
            jump heist_ferdi_trust_dilemma

label heist_ferdi_vulnerability:
    "Ferdi menatap Aruna dengan serius."

    ferdi "Jam 2-3 pagi, CCTV restart buat maintenance. Cuma 5 menit."
    ferdi "Itu kesempatan lo satu-satunya masuk tanpa ketahuan."
    ferdi "Tapi ingat, setelah restart, sistem bisa lebih sensitif dari sebelumnya."

    menu:
        "Tunggu sampai jam 2 pagi untuk eksekusi.":
            ar "Oke, gue tunggu sampai jam 2 pagi."
            ferdi "Waktu sempit banget. Lo harus gerak cepat dan tepat."
            ferdi "Satu kesalahan kecil, dan lo ketahuan."
            jump heist_ferdi_timing_strategy

        "Coba masuk sebelum jam 2 pagi untuk mengurangi risiko.":
            ar "Gue coba masuk sebelum jam 2 pagi. Mungkin lebih aman."
            ferdi "Lebih aman? Jam sebelum 2 pagi itu jam paling ketat keamanan."
            ferdi "Pak Kepsek biasanya masih ada di sekolah jam segitu."
            jump heist_ferdi_early_risk

        "Tanyakan apakah ada celah lain selain restart CCTV.":
            ar "Cuma restart CCTV doang celahnya? Nggak ada yang lain?"
            ferdi "Menurut gue cuma itu. Tapi Pak Kepsek cerdik, mungkin ada celah lain."
            ferdi "Tapi gue nggak tau apa. Lo harus cari sendiri."
            jump heist_ferdi_unknown_variables

label heist_ferdi_trap_suspicion:
    "Ferdi mengangguk pelan."

    ferdi "Gue juga mikirin itu. Bisa jadi jebakan."
    ferdi "Pak Kepsek mungkin sengaja kasih info ke gue buat uji siapa yang berani nyusup."
    ferdi "Kalau lo ketahuan, dia bisa bilang gue yang nyuruh lo."

    menu:
        "Terima risiko dan tetap melanjutkan rencana.":
            ar "Gue terima risikonya. Kalau ini jebakan, gue hadapi."
            ferdi "Lo nekat banget. Tapi gue respect itu."
            ferdi "Kalau ketahuan, jangan sebut nama gue ya."
            jump heist_ferdi_trap_acceptance

        "Ubah rencana dan cari jalan yang lebih aman.":
            ar "Kalau ini jebakan, gue cari jalan lain."
            ferdi "Jalan lain apa? Semua jalur udah diketahui Pak Kepsek."
            ferdi "Mungkin lo harus kreatif cari jalan yang nggak terpikir."
            jump heist_ferdi_alternative_path

        "Tanyakan apakah Ferdi punya ide untuk menguji kebenaran info.":
            ar "Gimana caranya tau info ini bener atau jebakan?"
            ferdi "Coba dekati area kecil dulu. Lihat apakah ada yang mencurigakan."
            ferdi "Kalau terlalu tenang, mungkin jebakan. Kalau normal, mungkin bener."
            jump heist_ferdi_test_approach

label heist_ferdi_map_usage:
    "Aruna menghafalkan skema yang diberikan Ferdi."
    "Gar merah untuk kamera, kotak hijau untuk blind spot, lingkaran kuning untuk sensor."

    menu:
        "Ikuti rute blind spot sesuai skema.":
            "Aruna mengikuti rute yang ditunjukkan skema Ferdi."
            "Bergerak dari satu blind spot ke blind spot lain dengan hati-hati."
            jump heist_ferdi_blind_spot_route

        "Gunakan skema sebagai referensi tapi tetap waspada.":
            "Aruna menggunakan skema sebagai referensi, tapi tetap waspada."
            "Mengamati sekitar dengan hati-hati di setiap langkah."
            jump heist_ferdi_cautious_approach

        "Abaikan skema dan gunakan insting sendiri.":
            "Aruna memutuskan untuk mengabaikan skema dan mengandalkan insting."
            "Merasa skema mungkin tidak akurat atau sengaja misleading."
            jump heist_ferdi_instinct_override

label heist_ferdi_caution:
    "Ferdi mengangguk mengerti keputusan Aruna."

    ferdi "Pilihan bijak. Jangan 100% andalkan peta orang lain."
    ferdi "Gunakan insting lo juga. Kalau ada yang nggak bener, segera kabur."

    menu:
        "Gunakan skema sebagai panduan dasar saja.":
            ar "Gue pakai skema ini sebagai panduan dasar, tapi gue tetap waspada."
            ferdi "Baik. Hati-hati, dan semoga berhasil."
            jump heist_ferdi_basic_guidance

        "Fokus ke insting dan pengamatan langsung.":
            ar "Gue lebih andelin insting dan pengamatan langsung."
            ferdi "Baik juga. Tapi ingat, Pak Kepsek cerdik."
            ferdi "Jangan remehkan dia."
            jump heist_ferdi_instinct_focus

        "Tanya Ferdi apakah ada tanda bahaya yang harus diwaspadai.":
            ar "Ada tanda bahaya tertentu yang harus gue waspadai?"
            ferdi "Kalau ada yang terlalu sunyi atau terlalu ramai, itu bahaya."
            ferdi "Keamanan yang normal biasanya seimbang, nggak ekstrem."
            jump heist_ferdi_danger_signs

label heist_ferdi_habit_intel:
    "Ferdi menatap Aruna dengan tatapan serius."

    ferdi "Setiap jam 2 pagi Pak Kepsek minum kopi di ruang guru."
    ferdi "Itu waktu dia paling lengah dan paling mungkin tertidur."
    ferdi "Tapi jangan terlalu percaya diri. Dia orang yang sangat disiplin."

    menu:
        "Tunggu jam 2 pagi untuk eksekusi saat Pak Kepsek minum kopi.":
            ar "Oke, gue tunggu jam 2 pagi. Saat dia minum kopi."
            ferdi "Waktu sempit. Lo harus gerak cepat."
            ferdi "Dan jangan kaget kalau dia ternyata nggak tertidur."
            jump heist_ferdi_coffee_timing

        "Coba masuk sebelum jam 2 pagi saat dia masih terjaga.":
            ar "Gue coba masuk sebelum jam 2 pagi. Mungkin lebih aman."
            ferdi "Lebih aman? Saat dia masih terjaga dan waspada?"
            ferdi "Lo pikir logis kah jalan kayak gitu?"
            jump heist_ferdi_logic_question

        "Cari informasi lebih detail tentang kebiasaan Pak Kepsek.":
            ar "Lo tau lebih detail nggak soal kebiasaannya? Durasi, lokasi, dll?"
            ferdi "Biasanya 15-20 menit di ruang guru, kadang sampai 30 menit."
            ferdi "Dia duduk di meja kerja beliau depan jendela."
            jump heist_ferdi_detailed_habit

label heist_ferdi_blueprint_usage:
    "Aruna menghafalkan skema kasar yang diberikan Ferdi."
    "Gar merah untuk kamera, kotak hijau untuk blind spot, lingkaran kuning untuk sensor."

    menu:
        "Ikuti rute blind spot sesuai skema.":
            "Aruna mengikuti rute yang ditunjukkan skema Ferdi."
            "Bergerak dari satu blind spot ke blind spot lain dengan hati-hati."
            jump heist_ferdi_blind_spot_navigation

        "Gunakan skema sebagai referensi tapi tetap waspada.":
            "Aruna menggunakan skema sebagai referensi, tapi tetap waspada."
            "Mengamati sekitar dengan hati-hati di setiap langkah."
            jump heist_ferdi_cautious_navigation

        "Abaikan skema dan gunakan insting sendiri.":
            "Aruna memutuskan untuk mengabaikan skema dan mengandalkan insting."
            "Merasa skema mungkin tidak akurat atau sengaja misleading."
            jump heist_ferdi_instinct_navigation

label heist_ferdi_trust:
    "Ferdi menatap Aruna dengan mata yang menunjukkan kepercayaan."

    ferdi "Gue percaya sama lo, Aruna. Lo beda dari yang lain."
    ferdi "Kalau lo gagal, jangan salahkan gue nggak kasih warning."
    ferdi "Tapi kalau lo berhasil, gue bakal kasih dukungan penuh ekskul Robotika."

    menu:
        "Janji akan berhati-hati dan tidak membawa nama Ferdi.":
            ar "Gue janji bakal berhati-hati dan nggak bakal sebut nama lo."
            ferdi "Makasih, Aruna. Gue tunggu kabar baik dari lo."
            jump heist_choice_1

        "Tanyakan apakah Ferdi punya saran terakhir.":
            ar "Sebelum gue pergi, ada saran terakhir nggak?"
            ferdi "Satu: jangan greedy. Ambil yang cukup, lalu kabur."
            ferdi "Jangan coba-coba ambil lebih dari yang direncanakan."
            jump heist_ferdi_final_advice

        "Pamit dan langsung melanjutkan misi.":
            ar "Oke, gue pergi sekarang. Makasih sudah percaya."
            ferdi "Hati-hati, Aruna. Dan semoga berhasil."
            jump heist_choice_1

label heist_ferdi_tactical_advice:
    "Ferdi memberikan saran taktis yang berharga."

    ferdi "Jangan pergi lewat jalan yang obvious. Pak Kepsek pasti prediksi itu."
    ferdi "Coba jalan yang tidak logis, yang mungkin tidak terpikir olehnya."
    ferdi "Tapi ingat, jalan yang tidak logis juga bisa berbahaya."

    menu:
        "Cari jalan yang tidak logis tapi masih aman.":
            ar "Gue akan cari jalan yang tidak logis tapi masih aman."
            ferdi "Jalan seperti apa? Mungkin lewat ventilasi atau atap?"
            ferdi "Tapi ingat, jalan seperti itu butuh skill fisik yang bagus."
            jump heist_ferdi_unconventional_route

        "Gunakan jalan logis tapi dengan teknik stealth yang baik.":
            ar "Gue pakai jalan logis, tapi dengan teknik stealth yang maksimal."
            ferdi "Jalan logis berarti kemungkinan besar ada jebakan."
            ferdi "Tapi kalau stealth lo bagus, mungkin bisa tembus."
            jump heist_ferdi_stealth_approach

        "Kombinasikan jalan logis dan tidak logis.":
            ar "Gue kombinasikan keduanya. Logis di awal, tidak logis di akhir."
            ferdi "Ide menarik. Bisa membingungkan pihak lawan."
            ferdi "Tapi juga bisa bikin lo sendiri bingung kalau nggak hati-hati."
            jump heist_ferdi_hybrid_strategy

label heist_ferdi_map_usage:
    "Aruna menghafalkan skema yang diberikan Ferdi."
    "Memutuskan untuk menggunakannya sebagai panduan utama."

    menu:
        "Ikuti rute blind spot sesuai skema.":
            "Aruna mengikuti rute yang ditunjukkan skema Ferdi."
            "Bergerak dari satu blind spot ke blind spot lain dengan hati-hati."
            jump heist_ferdi_blind_spot_execution

        "Gunakan skema sebagai referensi tapi tetap waspada.":
            "Aruna menggunakan skema sebagai referensi, tapi tetap waspada."
            "Mengamati sekitar dengan hati-hati di setiap langkah."
            jump heist_ferdi_cautious_execution

        "Abaikan skema dan gunakan insting sendiri.":
            "Aruna memutuskan untuk mengabaikan skema dan mengandalkan insting."
            "Merasa skema mungkin tidak akurat atau sengaja misleading."
            jump heist_ferdi_instinct_override

label heist_ferdi_caution:
    "Ferdi mengangguk mengerti keputusan Aruna."

    ferdi "Pilihan bijak. Jangan 100% andalkan peta orang lain."
    ferdi "Gunakan insting lo juga. Kalau ada yang nggak bener, segera kabur."

    menu:
        "Gunakan skema sebagai panduan dasar saja.":
            ar "Gue pakai skema ini sebagai panduan dasar, tapi gue tetap waspada."
            ferdi "Baik. Hati-hati, dan semoga berhasil."
            jump heist_ferdi_basic_guidance

        "Fokus ke insting dan pengamatan langsung.":
            ar "Gue lebih andelin insting dan pengamatan langsung."
            ferdi "Baik juga. Tapi ingat, Pak Kepsek cerdik."
            ferdi "Jangan remehkan dia."
            jump heist_ferdi_instinct_focus

        "Tanya Ferdi apakah ada tanda bahaya yang harus diwaspadai.":
            ar "Ada tanda bahaya tertentu yang harus gue waspadai?"
            ferdi "Kalau ada yang terlalu sunyi atau terlalu ramai, itu bahaya."
            ferdi "Keamanan yang normal biasanya seimbang, nggak ekstrem."
            jump heist_ferdi_danger_signs

label heist_ferdi_habit_intel:
    "Ferdi menatap Aruna dengan tatapan serius."

    ferdi "Setiap jam 2 pagi Pak Kepsek minum kopi di ruang guru."
    ferdi "Itu waktu dia paling lengah dan paling mungkin tertidur."
    ferdi "Tapi jangan terlalu percaya diri. Dia orang yang sangat disiplin."

    menu:
        "Tunggu jam 2 pagi untuk eksekusi saat Pak Kepsek minum kopi.":
            ar "Oke, gue tunggu jam 2 pagi. Saat dia minum kopi."
            ferdi "Waktu sempit. Lo harus gerak cepat."
            ferdi "Dan jangan kaget kalau dia ternyata nggak tertidur."
            jump heist_ferdi_coffee_timing

        "Coba masuk sebelum jam 2 pagi saat dia masih terjaga.":
            ar "Gue coba masuk sebelum jam 2 pagi. Mungkin lebih aman."
            ferdi "Lebih aman? Saat dia masih terjaga dan waspada?"
            ferdi "Lo pikir logis kah jalan kayak gitu?"
            jump heist_ferdi_logic_question

        "Cari informasi lebih detail tentang kebiasaan Pak Kepsek.":
            ar "Lo tau lebih detail nggak soal kebiasaannya? Durasi, lokasi, dll?"
            ferdi "Biasanya 15-20 menit di ruang guru, dekat meja kerja beliau."
            ferdi "Kadang sampai 30 menit kalau dia lagi banyak pikiran."
            jump heist_ferdi_detailed_habit

label heist_ferdi_alternative_perspective:
    "Ferdi menatap Aruna dengan sedikit harapan."

    ferdi "Mungkin lo sebagai orang luar bisa lihat yang gue nggak lihat."
    ferdi "Gue terlalu dekat dengan masalah ini, mungkin gue jadi buta."
    ferdi "Lo punya pandangan yang lebih segar dan objektif."

    menu:
        "Analisis situasi dari perspektif pemimpin OSIS.":
            ar "Sebagai calon ketua OSIS, gue lihat ini masalah struktur kekuasaan."
            ferdi "Struktur kekuasaan? Jelaskan."
            ar "Pak Kepsek kekuasaan berlebih, OSIS lemah. Harus ada balance."
            ferdi "Menarik. Lo lihat ini dari sudut pandang politik."
            jump heist_ferdi_political_analysis

        "Analisis situasi dari perspektif siswa biasa.":
            ar "Sebagai siswa, gue lihat ini ketidakadilan yang harus dilawan."
            ferdi "Idealis. Tapi idealis butuh strategi, bukan semangat doang."
            ferdi "Kalau lo semangat doang tanpa strategi, lo bakal kalah."
            jump heist_ferdi_idealist_warning

        "Analisis situasi dari perspektif ketua ekskul.":
            ar "Sebagai calon pemimpin, gue ngerti beban lo sebagai ketua."
            ferdi "Lo ngerti beban gue? Bagus sekali."
            ferdi "Berarti lo nggak cuma cari suara, tapi beneran peduli."
            jump heist_ferdi_empathy_connection

label heist_ferdi_emotional_break:
    "Ferdi menatap Aruna dengan mata yang berkaca-kaca."

    ferdi "Mudah bilang gitu kalau bukan posisi gue!"
    ferdi "Lo nggak tau gimana rasanya tanggung jawab 20 orang di pundak lo!"
    ferdi "Setiap hari gue mikirin: gimana caranya lindungin mereka tanpa melanggar aturan?"

    menu:
        "Menenangkan Ferdi dan menawarkan dukungan.":
            ar "Tenang, Ferdi. Gue ngerti posisi lo. Gue bantu lo."
            ferdi "Lo ngerti? Lo baru beberapa minggu jadi calon, gue setahun jadi ketua."
            ferdi "Tapi... gue appreciate kalau lo mau bantu."
            jump heist_ferdi_emotional_support

        "Minta maaf karena terlalu menekan.":
            ar "Sori, gue terlalu menekan. Gue nggak ngerti situasi lo."
            ferdi "Gue nggak marah. Gue cuma capek dan frustasi."
            ferdi "Terkadang gue butuh vent ke orang yang ngerti."
            jump heist_ferdi_vent_session

        "Tetap mendorong Ferdi untuk berani, tapi dengan cara yang lebih lembut.":
            ar "Gue nggak maksud menekan. Tapi lo harus tetap berani, Ferdi."
            ferdi "Berani gimana? Gue udah berani sejauh yang gue bisa."
            ferdi "Lebih dari itu, gue takut bakal ngorbanin anak-anak."
            jump heist_ferdi_courage_boundary

label heist_ferdi_faizal_search:
    "Ferdi bangkit dari bangku dengan semangat baru."

    ferdi "Kita cari Faizal bareng. Gue punya dugaan dia di mana."
    ferdi "Juan bilang terakhir kali Faizal ada di lab Kimia."
    ferdi "Tapi itu sudah dua hari lalu. Kita harus hati-hati."

    menu:
        "Menuju lab Kimia bersama Ferdi.":
            ar "Oke, kita ke lab Kimia. Hati-hati ya."
            ferdi "Gue ikut lo. Gue lebih tau area sekolah dari lo."
            "Bersama-sama mereka menuju lab Kimia dengan hati-hati."
            jump heist_lab_destination

        "Tanyakan apakah ada lokasi lain yang mungkin.":
            ar "Selain lab Kimia, ada kemungkinan dia di tempat lain nggak?"
            ferdi "Mungkin di ruang komputer, atau di gudang belakang."
            ferdi "Atau... di ruangan Pak Kepsek sendiri."
            jump heist_location_theory

        "Bagi tugas pencarian untuk lebih efisien.":
            ar "Kita bagi tugas biar lebih efisien. Lo cek satu tempat, gue cek tempat lain."
            ferdi "Bagi tugas? Berbahaya kalau kita terpisah."
            ferdi "Tapi mungkin lebih efisien. Oke, coba aja."
            jump heist_divided_search

label heist_ferdi_location_theory:
    "Ferdi menatap ke arah gedung utama dengan wajah gelisah."

    ferdi "Juan bilang terakhir kali Faizal ada di lab Kimia."
    ferdi "Tapi itu sudah dua hari lalu. Gue takut dia udah dipindah."
    ferdi "Mungkin ke ruang Pak Kepsek, atau ke tempat yang lebih tersembunyi."

    menu:
        "Cek lab Kimia terlebih dahulu.":
            ar "Kita cek lab Kimia dulu. Itu lokasi terakhir yang diketahui."
            ferdi "Baik. Tapi hati-hati, bisa jadi itu jebakan."
            jump heist_lab_destination

        "Cek ruangan Pak Kepsek langsung.":
            ar "Kita cek langsung ruangan Pak Kepsek."
            ferdi "Terlalu berisiko! Keamanan di sana sangat ketat."
            ferdi "Tapi kalau Faizal memang di sana, kita nggak punya pilihan."
            jump heist_direct_principal_approach

        "Cari petunjuk atau jejak Faizal di sekitar sekolah.":
            ar "Kita cari petunjuk atau jejak Faizal dulu."
            ferdi "Jejak apa? Mungkin barang-barang pribadinya?"
            ferdi "Atau mungkin ada saksi yang melihat dia terakhir kali."
            jump heist_clue_search

label heist_ferdi_team_search:
    "Ferdi bangkit dan siap untuk mencari bersama."

    ferdi "Gue ikut lo. Gue lebih tau area sekolah dari lo."
    ferdi "Kita harus hati-hati. Pak Kepsek punya mata di mana-mana."

    menu:
        "Mulai pencarian dari area lab Kimia.":
            ar "Kita mulai dari lab Kimia. Itu lokasi terakhir yang diketahui."
            ferdi "Baik. Tapi ingat, Faizal bisa jadi bukan satu-satunya yang ada di sana."
            jump heist_lab_team_search

        "Mulai pencarian dari area gudang belakang.":
            ar "Kita mulai dari gudang belakang. Kadang Faizal suka ke sana."
            ferdi "Gudang? Mungkin. Tapi itu area gelap dan berbahaya."
            jump heist_warehouse_team_search

        "Mulai pencarian dengan bertanya ke satpam yang mungkin melihat.":
            ar "Kita tanya satpam dulu. Mungkin ada yang melihat Faizal."
            ferdi "Tanya satpam? Mereka pasti bilang nggak tau atau pura-pura nggak tau."
            ferdi "Tapi boleh juga dicoba. Siapa tahu ada yang bersedia bantu."
            jump heist_guard_inquiry

label heist_ferdi_contact_attempts:
    "Ferdi menatap Aruna dengan rasa putus asa."

    ferdi "Gue udah coba semua: WA, telepon, bahkan ke rumahnya."
    ferdi "Orang tuanya bilang Faizal 'pergi ke sekolah buat tugas tambahan'."
    ferdi "Tugas tambahan tengah malam? Ngaco."

    menu:
        "Mencoba menghubungi Faizal dengan cara lain.":
            ar "Gue coba hubungi Faizal lewat cara lain."
            ferdi "Cara lain apa? Semua cara udah gue coba."
            ferdi "Mungkin lo punya ide yang gue nggak pikirin."
            jump heist_alternative_contact

        "Menyimpulkan bahwa Faizal sengaja diisolasi.":
            ar "Sepertinya Faizal sengaja diisolasi sama Pak Kepsek."
            ferdi "Isolasi? Kenapa? Apa yang dia lakuin sampai harus diisolasi?"
            ferdi "Ini makin mencurigakan. Kita harus segera cari dia."
            jump heist_isolation_conclusion

        "Fokus ke pencarian fisik Faizal di sekolah.":
            ar "Kita fokus cari Faizal fisik di sekolah. Komunikasi nggak efektif."
            ferdi "Baik. Kita cari fisik. Tapi di mana kita mulai?"
            ferdi "Sekolah ini besar, dan malam gelap."
            jump heist_physical_search_start

label heist_ferdi_rescue_dilemma:
    "Ferdi menatap Aruna dengan wajah penuh kekhawatiran."

    ferdi "Kalau Faizal dipaksa ngelakuin hal ilegal, kita harus bantu dia."
    ferdi "Tapi gimana caranya? Kita nggak tau dia di mana."
    ferdi "Dan kalau kita salah langkah, malah bisa bahayain dia."

    menu:
        "Rencanakan penyelamatan yang hati-hati dan terukur.":
            ar "Kita rencanain penyelamatan yang hati-hati dan terukur."
            ferdi "Rencana seperti apa? Kita nggak punya informasi apapun."
            ferdi "Tanpa informasi, rencana apa pun terlalu berisiko."
            jump heist_planned_rescue

        "Cari informasi dulu sebelum bertindak.":
            ar "Kita cari informasi dulu sebelum ngapain."
            ferdi "Informasi dari mana? Semua orang pada takut ngomong."
            ferdi "Mungkin kita harus cari sendiri, walau berisiko."
            jump heist_information_first

        "Ambil risiko dan langsung mencari Faizal.":
            ar "Gue ambil risiko. Kita langsung cari Faizal."
            ferdi "Langsung cari? Di mana? Sekolah ini besar!"
            ferdi "Tapi gue setuju. Faizal butuh bantuan segera."
            jump heist_immediate_search

label heist_ferdi_surveillance_fear:
    "Ferdi menatap Aruna dengan rasa takut yang mendalam."

    ferdi "Proyek IT tengah malam? Mungkin dia lagi bangun sistem pengawasan."
    ferdi "Sistem yang bisa pantau semua aktivitas siswa."
    ferdi "Kalau itu bener, ini lebih berbahaya dari sekadar piala."

    menu:
        "Mengutamakan pencegahan sistem pengawasan daripada piala.":
            ar "Kalau itu bener, kita harus prioritasin cegah sistem pengawasan."
            ferdi "Cegah gimana? Kita nggak punya akses ke sistemnya."
            ferdi "Mungkin lewat Faizal. Kalau dia yang bikin, dia mungkin bisa disable."
            jump heist_surveillance_prevention

        "Mencari tahu lebih lanjut tentang proyek ini.":
            ar "Kita harus cari tau lebih lanjut soal proyek ini."
            ferdi "Caranya gimana? Pak Kepsek pasti merahasiain ini."
            ferdi "Mungkin ada dokumen atau bukti di ruangannya."
            jump heist_project_investigation

        "Tetap fokus ke piala tapi waspada terhadap sistem pengawasan.":
            ar "Gue tetap fokus ke piala, tapi gue waspada sistem pengawasan."
            ferdi "Piala masih prioritas? Padahal sistem pengawasan lebih bahaya?"
            ferdi "Gue nggak mengerti prioritas lo, Aruna."
            jump heist_priority_conflict

label heist_juan_encounter:
    "Juan menggigit bibir, tangan gemetar memegang kartu ID siswa."

    juan "Lo harus tahu. Piala itu bukan satu-satunya yang disita."
    juan "Pak Kepsek juga menyita dokumen penting tim Robotika. Data desain robot kita tahun ini."
    juan "Kalau gue butuh piala doang, gue bisa minta bantu orang lain. Tapi data itu... itu nyawa tim gue."

    menu:
        "Tanya Juan kenapa dia tidak melaporkan ini secara resmi.":
            "Aruna menatap Juan dengan curiga."
            ar "Kenapa nggak lapor ke panitia atau orang tua? Ini jelas melanggar aturan."
            juan "Lo pikir gue nggak coba? Pak Kepsek punya dokumen lain juga."
            juan "Dokumen yang bisa menghancurkan karier Pak Kepsek kalau bocor. Dia pakai itu buat tekan anak-anak Robotika diam."
            juan "Sekarang gue kasih pilihan: lo tolong gue ambil dua-duanya, atau lo pulang dan pura-pura nggak pernah ketemu gue malam ini."
            jump heist_juan_ultimatum

        "Terima tawaran Juan, tapi minta detail rencananya.":
            ar "Oke, lo bantu gue dan gue bantu lo. Tapi gue butuh detail."
            juan "Gue udah pelajari jadwal patroli Pak Budi selama seminggu."
            juan "Setengah jam lagi dia bakal ke area belakang buat merokok. Itu kesempatan kita."
            juan "Lo naik lewat tangga belakang, gue jaga di bawah buat ngalihin perhatian kalau ada yang datang."
            jump heist_juan_plan

        "Tolak bantuan Juan dan lanjut sendiri.":
            ar "Ini terlalu berisiko kalau berdua. Gue bakal sendirian."
            juan "Gila. Lo mau mati sendirian ya? Oke, silakan."
            "Juan pergi dengan tatapan kecewa. Aruna melanjutkan sendirian."
            jump heist_choice_1

label heist_main_door:
    "Aruna menempelkan telinga ke pintu. Ada suara bisikan dari dalam."
    "Suara perempuan menangis... tapi bukan menangis biasa. Ada sesuatu yang berat dalam isak tangis itu."

    menu:
        "Tendang pintu dengan keras dan masuk paksa!":
            "Aruna mengumpulkan keberanian, menendang pintu kayu tua itu dengan sekuat tenaga."
            "BLAM! Pintu terbuka, tapi tidak kosong."
            "Di tengah ruang depan, Flourine—petahana ketua OSIS—berdiri dengan piala Robotika di tangannya."
            flourine "Lo pikir lo satu-satunya yang 'berani' nyuri malam-malam, Aruna?"
            "Flourine tersenyum dingin. Piala itu berkilau di tangannya seperti senjata."
            jump heist_flourine_confrontation

        "Coba congkel gembok dengan kertas klip yang ada di saku.":
            "Aruna mencari kertas klip di saku. Ada satu bekas dari proyek kelas."
            "Congkelan gembok biasanya mudah, tapi ini gembok baru dengan mekanisme berbeda."
            "Terdengar klik kecil saat salah satu kawat masuk ke tempatnya."
            "Tapi bukan gembok yang terbuka—itu trigger alarm."
            "WEEW-WEEW-WEEW! Alarm sekolah berbunyi di seluruh gedung."
            jump heist_alarm_triggered

        "Tinggalkan pintu utama dan cari jalan lain.":
            "Aruna menyadari risikonya terlalu besar. Ada orang di dalam, pintu terkunci baru."
            "Memutuskan mundur dan mencari jalan lain menuju lantai dua."
            jump heist_choice_1

label heist_staircase:
    "Aruna menatap tangga darurat besi yang menggantung di atas."
    "Kamera CCTV itu terus mengawasi dengan mata merahnya."

    menu:
        "Matikan kamera dengan lemparan batu dari kejauhan.":
            "Aruna mencari batu di sekitar. Ada beberapa ukuran kecil."
            "Mengukur jarak. Sekitar lima meter. Tingkat keberhasilan rendah."
            "Melempar batu pertama—MELESET! Kamera masih menyala."
            "Batu kedua—KENA! Kamera berayang, tapi tidak mati. Sebaliknya, lampu merah berubah menjadi biru."
            "Seseorang di ruang monitoring pasti melihat ini!"
            jump heist_monitoring_room_alert

        "Cari cara naik tanpa terlihat kamera.":
            "Aruna mengamati pola rotasi kamera. Setiap 15 detik berputar 90 derajat."
            "Ada celah 3 detik saat kamera menghadap ke arah lain."
            "Tapi tangga itu berkarat dan berbunyi kalau dinaiki."
            "Aruna harus bergerak sangat pelan... dan tepat saat kamera berputar."
            jump heist_staircase_stealth

        "Tanya diri sendiri: apakah ini benar-benar cara terbaik?":
            "Aruna menghentikan langkah. Ada sesuatu yang tidak masuk akal."
            "Kenapa kamera baru dipasang malam ini? Kenapa gembok baru di pintu utama?"
            "Seperti seseorang sudah tahu ada yang akan mencoba menyusup malam ini."
            "Arthurs membalikkan badan, merasa ini jebakan."
            jump heist_trap_realization

label heist_lab_window:
    "Aruna mencongkel jendela lab Kimia pelan-pelan."
    "Isak tangis dari dalam lab berhenti seketika saat ada suara gesekan."

    menu:
        "Masuk dan tanya siapa yang ada di dalam.":
            "Aruna melompat masuk ke dalam lab yang gelap gulita."
            "Di sudut ruangan, ada siluet terguguk di lantai."
            "Faizal—anggota Robotika lainnya—sedang menggigil sambil memeluk laptop."
            faizal "Lo... lo datang buat nolong gue kan?"
            faizal "Gue udah terkunci di sini dari jam enam sore. Pak Kepsek benci gue karena gue nolak jadi mata-mata dia."
            jump heist_faizal_rescue

        "Tinggalkan jendela dan cari jalan lain.":
            "Aruna menyadari ini terlalu berisiko. Ada orang lain di dalam."
            "Mundur pelan-pelan, tapi saat berbalik, ada tangan yang mencengkeram bahunya."
            "Pak Budi berdiri di sana dengan wajah dingin."
            pak_budi "Anak-anak manis malam-malam begini. Pasti cuma mau belajar ya?"
            jump heist_caught_by_budi

        "Tanya dari luar siapa yang ada di dalam.":
            ar "Siapa yang ada di dalam? Gue bisa bantu."
            "Tidak ada jawaban. Hanya suara ketikan laptop yang semakin cepat."
            "Aruna melihat ke dalam—Faizal sedang mengetik sesuatu dengan wajah tegang."
            faizal "Jangan masuk! Ini... ini bukan urusan lo!"
            "Faizal menutup laptop dengan keras saat Aruna melihat ke dalam."
            jump heist_faizal_secret

label heist_pursuit_start:
    "Langkah kaki semakin dekat. Aruna harus bertindak cepat."

    menu:
        "Sembunyi di balik pohon besar di taman.":
            "Aruna melompat ke balik pohon beringin tua di tengah taman."
            "Langkah kaki berhenti tepat di sisi lain pohon."
            "Suara napas berat. Tiga orang—dua laki-laki dan satu perempuan."
            suara_tak_dikenal "Lapor ke atasan. Ada intruder. Area belakang tidak aman."
            "Salah satu dari mereka membawa alat komunikasi."
            jump heist_security_team

        "Lari menuju tangga belakang gedung dan naik secepat mungkin.":
            "Aruna memilih lari daripada bersembunyi."
            "Berlari mengejar waktu menuju tangga belakang yang tidak terkunci."
            "Berhasil sampai di lantai dua, tapi pintu ke koridor utama terkunci rapat."
            "Langkah kaki pengejar mulai terdengar dari bawah tangga."
            jump heist_rooftop_trap

        "Keliru dan pura-pura jadi siswa yang baru pulang dari perpustakaan.":
            "Aruna mengambil buku dari tanah—buku bekas yang tergeletak di semak-semak."
            "Berjalan santai ke arah gerbang seolah-olah baru selesai belajar."
            "Saat bertemu tiga orang petugas keamanan itu, mereka menatap dengan curiga."
            "Tapi salah satunya melihat buku di tangan Aruna dan mengangguk."
            petugas "Oke, pulang. Sekolah mau tutup."
            "Aruna berhasil lolos... tapi tidak sampai ke ruangan kepala sekolah."
            jump heist_failed_escape

label heist_cat_path:
    "Aruna mengikuti kucing hitam itu menuju celah pagar."
    "Celah itu memang mengarah ke area gudang belakang, tapi ada sesuatu yang aneh."

    menu:
        "Ikuti kucing itu masuk ke gudang.":
            "Aruna menyusup lewat celah itu. Kucing hitam menunggu di sisi lain."
            "Gudang itu penuh dengan kotak-kotak tua dan alat-alat lab yang tidak terpakai."
            "Tapi di sudut terdalam, ada kotak baru dengan stiker 'CONFIDENTIAL'—Rahasia."
            "Kucing itu duduk di depan kotak itu, menatap Aruna seolah meminta untuk dibuka."
            jump heist_secret_box

        "Lewati gudang dan lanjut ke gedung utama.":
            "Aruna memilih fokus ke tujuan utama—ruangan kepala sekolah."
            "Melanjutkan perjalanan melewati gudang yang sunyi itu."
            "Tapi terdengar suara radio dari dalam gudang."
            suara_radio "Target dalam jangkauan. Siap untuk eksekusi rencana B."
            "Aruna membeku. Ada rencana apa ini?"
            jump heist_radio_discovery

        "Ambil kucing itu dan bawa pulang. Ini terlalu berbahaya.":
            "Aruna mengangkat kucing hitam itu. Binatang itu tidak melawan."
            "Membawa kucing itu pulang, merasa malam ini terlalu berisiko untuk dilanjutkan."
            "Esok hari, Aruna menemukan kerah kucing itu ada tulisan kecil: 'Bantu Robotika'."
            "Kucing itu hilang dari rumah Aruna keesokan harinya."
            jump heist_cat_mystery

label heist_budi_encounter:
    "Pak Budi yang biasanya ramah dan humoris kini terlihat seperti orang yang kehilangan akal."
    "Luka gores di pipinya masih berdarah sedikit."

    menu:
        "Tanya Pak Budi apa yang terjadi padanya.":
            ar "Pak, lo kenapa? Ada yang sakiti lo?"
            pak_budi "Jangan tanya! Jangan tanya apa-apa!"
            "Pak Budi berlari masuk ke gedung utama, meninggalkan Aruna bingung."
            "Tapi saat dia berlari, sesuatu jatuh dari sakunya—kunci dengan logo kepala sekolah."
            jump heist_budi_key_drop

        "Ikuti Pak Budi diam-diam ke dalam gedung.":
            "Aruna memutuskan mengikuti Pak Budi dari jarak aman."
            "Pak Budi naik ke lantai dua, berhenti di depan ruangan kepala sekolah."
            "Dia tidak masuk, hanya berdiri di depan pintu sambil menggigil."
            "Lalu dia berbisik sesuatu ke pintu itu seperti sedang berdoa."
            jump heist_budi_prayer

        "Biarkan Pak Budi pergi dan fokus ke misi utama.":
            "Aruna menyadari Pak Budi sedang dalam kondisi tidak stabil."
            "Memutuskan untuk tidak memperburuk keadaan dan melanjutkan misi sendiri."
            "Tapi ada perasaan tidak enak meninggalkan seseorang yang jelas-jelah dalam masalah."
            jump heist_choice_1

label heist_juan_ultimatum:
    "Aruna menatap Juan dengan serius. Ini bukan lagi sekadar mencuri piala."

    menu:
        "Terima ultimatum Juan. Ambil dua-duanya.":
            ar "Oke. Lo bantu gue, gue bantu lo. Kita selesaikan ini berdua."
            juan "Serius? Lo berani ambil risiko segede itu?"
            ar "Piala itu buat ekskul lo. Data itu buat masa depan lo. Gue ngerti."
            juan "Baik. Gue kasih lo peta lengkap dan kunci cadangan yang gue punya."
            "Juan menyerahkan kertas lipat dan kunci kecil berwarna emas."
            jump heist_juan_partnership

        "Tolak ultimatum. Ambil piala saja.":
            ar "Gue cuma mau ambil piala. Data-data itu urusan kalian sendiri."
            juan "Jadi lo kayak mereka juga cuma peduli piala dan suara doang?"
            "Juan pergi dengan tatapan sangat kecewa."
            "Aruna melanjutkan sendirian, tapi perasaan bersalah mulai menggerogoti."
            jump heist_solo_mission_guilt

        "Tawarkan kompromi: ambil piala dulu, data nanti.":
            ar "Gue nggak bisa ngambil dua-duanya sekaligus. Terlalu berisiko."
            ar "Ambil piala dulu, nanti gue bantu lo urus datanya lewat cara legal."
            juan "Cara legal? Lo naif banget Aruna. Pak Kepsek bakal bakar data itu sebelum lo bisa ngapain."
            jump heist_juan_refusal

label heist_juan_plan:
    "Juan menunjuk ke tangga belakang gedung yang tidak terlihat dari jalan utama."

    juan "Tangga itu jarang dipakai, biasanya buat eskalasi kebakaran aja."
    juan "Gue udah cek seminggu ini, gak pernah ada satpam yang patroli ke sana."
    juan "Lo naik ke lantai dua, cari ruangan di ujung koridor sebelah kanan."
    juan "Sementara gue jaga di bawah. Kalau ada yang datang, gue bakal kirim sinyal lewat HP."

    menu:
        "Ikuti rencana Juan sepenuhnya.":
            ar "Oke, kepercayaan penuh. Lo jaga di bawah, gue naik ke atas."
            juan "Siap. Gue bakal kabarin kalau ada bahaya."
            "Aruna mulai naik tangga belakang yang berkarat itu."
            jump heist_juan_execution

        "Modifikasi rencana: gue naik duluan, lo ikut belakangan.":
            ar "Gue naik duluan buat cek situasi. Lo ikut belakangan kalau aman."
            juan "Kenapa? Lo nggak percaya sama gue?"
            ar "Bukan nggak percaya, cuma safety first."
            "Juan mengangguk pelan, tapi Aruna bisa melihat kekecewaan di matanya."
            jump heist_modified_plan

        "Tanya apakah Juan punya cadangan kalau rencana gagal.":
            ar "Kalau rencana ini gagal, lo punya plan B nggak?"
            juan "Plan B? Gue nggak mikirin plan B. Plan A harus berhasil."
            ar "Itu bahaya, Juan. Selalu harus ada opsi lain."
            juan "Gue nggak punya opsi lain, Aruna. Ini satu-satunya kesempatan gue."
            jump heist_desperate_plan

label heist_flourine_confrontation:
    "Flourine mengangkat piala itu tinggi-tinggi, senyumnya penuh kemenangan."

    flourine "Lo pikir lo pahlawan penyelamat ekskul Robotika?"
    flourine "Gue yang udah deal dengan Pak Kepsek buat piala ini. Gue yang bakal balikin ke mereka dengan syarat."
    flourine "Syaratnya: seluruh suara Robotika ke gue di hari pemilihan."

    menu:
        "Tantang Flourine berduel fisik untuk piala itu!":
            ar "Lo nggak punya hak atas piala itu! Ini milik Robotika!"
            "Aruna melangkah maju siap bertarung, tapi Flourine tertawa."
            flourine "Duel fisik? Lo mau jadi preman sekolah?"
            "Flourine melempar piala itu ke lantai. Piala itu pecah menjadi dua."
            flourine "Lihat? Sekarang nggak ada yang bisa dapat."
            jump heist_broken_trophy

        "Coba negosiasi dengan Flourine secara diplomatis.":
            ar "Lo cuma mau suara doang? Jujur aja Flourine."
            flourine "Politik itu semua tentang kepentingan, Aruna. Lo bakal ngerti nanti."
            flourine "Tapi fine, kita bisa negosiasi. Lo bantu gue ngalahin Fanya, gue bagi-bagi suara Robotika."
            jump heist_flourine_deal

        "Tanya Flourine kenapa dia ada di sini malam-malam.":
            ar "Kenapa lo ada di sini malam-malam? Lo juga curi?"
            flourine "Curik? Gue ketua OSIS, gue punya kunci ruangan ini legal."
            flourine "Gue dateng buat ngambil piala sebelum ada 'tikus-tikus' yang nyuri duluan."
            "Flourine mengibaskan kunci di tangan kanannya."
            jump heist_flourine_keys

label heist_alarm_triggered:
    "Alarm sekolah berbunyi keras di seluruh gedung. Lampu-lampu mulai menyala satu per satu."

    menu:
        "Lari secepat mungkin keluar dari sekolah!":
            "Aruna berlari menuju gerbang terdekat, tapi semua pintu otomatis terkunci saat alarm aktif."
            "Suara langkah kaki banyak orang mulai terdengar dari segala arah."
            "Aruna terjebak di tengah taman sekolah yang mulai diterangi lampu sorot."
            jump heist_caught_in_spotlight

        "Sembunyi di gedung dan tunggu alarm mati.":
            "Aruna berlari ke dalam gedung, mencari ruangan gelap untuk bersembunyi."
    "Bersembunyi di ruang gudang lantai satu, di antara tumpukan meja kayu tua."
            "Alarm mati setelah dua menit, tapi sekarang ada patroli ekstra ketat."
            jump heist_hiding_during_alarm

        "Cari cara mematikan alarm secara manual.":
            "Aruna mengingat ada panel kontrol alarm di ruang maintenance dekat lab fisika."
            "Berlari menuju sana saat alarm masih berbunyi, melewati koridor yang mulai terang."
            "Panel kontrol itu terbuka, tapi butuh kode untuk mematikannya."
            jump heist_alarm_panel_code

label heist_staircase_stealth:
    "Aruna menunggu kamera berputar ke kiri, lalu melompat ke anak tangga pertama."
    "Besi karat itu berbunyi KRIK saat dinaiki. Kamera mulai berputar kembali."

    menu:
        "Berhenti sejenak sampai kamera berputar lagi.":
            "Aruna membeku di posisi anak tangga ketiga."
            "Kamera berputar perlahan, mata merahnya menyapu area tangga."
            "Lewat tepat di atas kepala Aruna. Berhasil terhindar."
            "Lanjut naik pelan-pelan, menghitung detik setiap gerakan."
            jump heist_staircase_success

        "Lari cepat saat kamera menghadap ke arah lain.":
            "Aruna memilih mengambil risiko. Lari secepat mungkin ke atas."
            "Setengah jalan, kamera berputar lebih cepat dari perkiraan."
            "Lampu biru kamera mulai berkedip-kedip—sedang merekam."
            jump heist_camera_caught

        "Tutupi kamera dengan kain atau kertas.":
            "Aruna mencari sesuatu di sekitar. Ada banner bekas acara sekolah tergeletak di bawah."
            "Melempar banner itu ke arah kamera saat berputar."
            "Berhasil menutupi lensa kamera! Tapi banner itu jatuh dan membuat suara keras."
            "Suara itu menarik perhatian seseorang dari dalam gedung."
            jump heist_banner_noise

label heist_trap_realization:
    "Aruna mundur pelan-pelan, semakin yakin ini adalah jebakan."

    menu:
        "Investigasi lebih lanjut sebelum pulang.":
            "Aruna memutuskan untuk tidak langsung pulang, tapi mengamati dari kejauhan."
            "Dari balik tembok, Aruna melihat dua orang dalam seragam satpam keluar dari gedung utama."
            "Mereka membawa kotak besar dengan stiker yang sama seperti yang dilihat sebelumnya."
            "Mereka memasukkan kotak itu ke mobil van gelap yang parkir di luar gerbang."
            jump heist_van_observation

        "Pulang dan kembali besok dengan persiapan lebih baik.":
            "Aruna menyadari butuh informasi lebih sebelum melanjutkan misi ini."
            "Pulang dengan hati-hati, merencanakan strategi baru untuk besok."
            jump heist_retreat_plan

        "Cari tahu siapa yang memasang kamera dan gembok baru.":
            "Aruna mendekati area kantin, ada beberapa satpam sedang ngopi dan ngobrol."
            "Bersembunyi di balik tembok kantin untuk menguping pembicaraan mereka."
            satpam1 "Kenapa ekstra tight malam ini? Biasanya nggak segini."
            satpam2 "Perintah langsung dari Pak Kepsek. Ada yang mau nyuri malam ini katanya."
            jump heist_guard_conversation

label heist_faizal_rescue:
    "Faizal menggigil di sudut lab Kimia yang gelap."

    faizal "Gue... gue udah terkunci di sini dari jam enam sore."
    faizal "Pak Kepsek bilang gue curang di kompetisi, padahal gue nggak! Dia mau hancurin karier gue!"

    menu:
        "Tanya Faizal apa yang sebenarnya terjadi.":
            ar "Tenang, ceritain pelan-pelan. Apa yang sebenarnya terjadi?"
            faizal "Gue nemu celah di sistem scoring kompetisi. Gue mau lapor, tapi Pak Kepsek malah tuduh gue curang."
            faizal "Dia konfiskasi laptop gue dan ngunci gue di sini supaya gak ngomong ke siapa-siapa."
            jump heist_faizal_truth

        "Bantu Faizal keluar dari lab sekarang juga.":
            ar "Gue bantu lo keluar dari sini dulu. Cerita di jalan."
            "Aruna mencari cara membuka pintu lab yang terkunci dari luar."
            "Tapi tidak ada cara pintu itu bisa dibuka dari luar tanpa kunci."
            jump heist_locked_lab_dilemma

        "Tanya Faizal tentang piala Robotika.":
            ar "Lo tau nggak di mana piala Robotika sekarang?"
            faizal "Piala? Itu juga disita Pak Kepsek. Dia taruh di ruangannya sendiri."
            faizal "Tapi Aruna, lo harus tau: piala itu cuma permukaan. Ada yang lebih penting disita."
            jump heist_faizal_priority

label heist_caught_by_budi:
    "Pak Budi menatap Aruna dengan tatapan yang tidak bisa dibaca."

    pak_budi "Aruna... putra dari Pak Wirasena kan?"
    pak_budi "Lo sini malam-malam buat apa? Pasti bukan buat belajar."

    menu:
        "Jujur mengakui niat mengambil piala Robotika.":
            ar "Gue dateng buat ambil piala Robotika yang disita Pak Kepsek tanpa alasan."
            pak_budi "Piala... iya, piala itu."
            "Pak Budi tertawa kecil, tertawa yang penuh kesedihan."
            pak_budi "Lo nggak ngerti apa yang lagi terjadi di sekolah ini, Nak."
            jump heist_budi_revelation

        "Beralasan baru pulang dari perpustakaan belajar.":
            ar "Gue baru selesai belajar di perpus, Pak. Cuma mau pulang."
            pak_budi "Perpus tutup jam delapan. Sekarang jam dua belas."
            "Pak Budi menggelengkan kepala."
            pak_budi "Jangan bohong sama orang yang sudah ngelihat semua kebohongan di dunia ini."
            jump heist_budi_confrontation

        "Tanya Pak Budi kenapa dia ada di sini.":
            ar "Pak sendiri malam-malam ada di sini buat apa, Pak?"
            pak_budi "Gue? Gue penjaga, Nak. Gue selalu di sini."
            "Tapi matanya mengatakan hal lain. Ada rasa takut yang mendalam di sana."
            jump heist_budi_fear

label heist_faizal_secret:
    "Faizal menutup laptop dengan keras, menutup sesuatu yang jelas-jelah sedang dikerjakannya."

    faizal "Jangan masuk! Jangan lihat apa yang ada di laptop gue!"
    faizal "Ini... ini bukan urusan lo. Ini urusan hidup mati gue!"

    menu:
        "Dorong Faizal untuk menjelaskan apa yang sedang dia kerjakan.":
            ar "Lo ketakutan banget Faizal. Ada apa sebenarnya?"
            faizal "Gue... gue lagi bikin backup data tim Robotika sebelum dihapus sama Pak Kepsek."
            faizal "Tapi gue juga lagi ngerjain sesuatu yang lain... sesuatu yang bisa membahayakan."
            jump heist_faizal_confession

        "Hormati privasi Faizal dan tawarkan bantuan lain.":
            ar "Oke, gue nggak akan paksa lo cerita. Tapi lo butuh bantuan nggak?"
            faizal "Lo cuma peduli piala doang kan? Piala itu di ruang Pak Kepsek."
            faizal "Ambil piala lo, dan lupakan gue."
            jump heist_faizal_rejection

        "Coba melihat isi laptop Faizal saat lengah.":
            "Aruna melihat kesempatan saat Faizal lengah untuk sekilas melihat layar laptop."
            "Ada kode-kode rumit dan diagram yang terlihat seperti rencana jaringan sekolah."
            "Ada tulisan besar di pojok: 'PROYEK PENGAWASAN TOTAL'."
            jump heist_surveillance_project

label heist_security_team:
    "Aruna menahan napas di balik pohon beringin tua."
    "Tiga orang petugas keamanan berdiri tidak jauh dari tempat persembunyian."

    suara_tak_dikenal "Area belakang secure. Lanjutkan pencarian ke area depan."
    petugas2 "Copy. Kami akan cek area lab dan perpus."
    petugas3 "Bagus. Ingat, target bukan intruder biasa. Target yang diincar punya keterkaitan dengan kasus Robotika."

    menu:
        "Tunggu sampai mereka pergi, lalu lanjutkan misi.":
            "Aruna menunggu sepuluh menit sampai area benar-benar sepi."
            "Petugas keamanan pergi ke arah lain, menyisakan kesempatan."
            "Tapi perasaan tidak aman semakin menguat. Mereka menyebut 'kasus Robotika'."
            jump heist_after_security_clears

        "Ikuti petugas keamanan untuk mencari tahu lebih banyak.":
            "Aruna memutuskan mengikuti mereka dari jarak aman."
            "Mereka menuju ruang guru, di mana ada cahaya yang masih menyala."
            "Dari kejauhan, Aruna melihat mereka sedang berdiskusi dengan seseorang yang dikenal."
            "Flourine—ketua OSIS petahana—sedang berbicara dengan mereka."
            jump heist_flourine_with_security

        "Kembali ke gerbang dan pulang. Ini terlalu berbahaya.":
            "Aruna menyadari ini sudah melampaui misi sederhana mengambil piala."
            "Ada konspirasi yang lebih besar yang sedang berlangsung."
            "Memutuskan untuk mundur dan mengumpulkan informasi lebih dulu."
            jump heist_strategic_retreat

label heist_rooftop_trap:
    "Aruna terjebak di atap gedung utama. Pintu ke koridor terkunci, pengejar mulai naik tangga."

    menu:
        "Cari jalan ke atap gedung lain lewat talang air.":
            "Aruna melihat talang air yang menghubungkan gedung utama dengan gedung lab."
            "Berisiko tinggi, tapi mungkin satu-satunya jalan keluar."
            "Berjalan pelan-pelan di atap yang licin karena embun malam."
            jump heist_rooftop_crossing

        "Hadapi pengejar saat mereka sampai di atap.":
            "Aruna memutuskan untuk tidak lari lagi. Waktunya menghadapi konsekuensi."
            "Menyiapkan diri untuk penjelasan yang masuk akal."
            "Tapi saat mereka sampai, Aruna menyadari mereka bukan satpam biasa."
            "Mereka berpakaian hitam-hitam dan membawa alat-alat yang tidak biasa."
            jump heist_mysterious_team

        "Cari tempat bersembunyi di atap sampai mereka pergi.":
            "Aruna mencari tempat bersembunyi di atap—ada AC unit besar di pojok."
            "Bersembunyi di belakang unit itu, menunggu mereka pergi."
            "Tapi mereka tidak pergi. Mereka mulai mencari secara sistematis."
            jump heist_rooftop_hide_seek

label heist_failed_escape:
    "Aruna berhasil keluar dari sekolah tanpa tertangkap, tapi misi gagal total."

    menu:
        "Kembali besok malam dengan persiapan lebih baik.":
            "Aruna menyadari butuh rencana yang lebih matang."
            "Malam ini terlalu banyak kejadian yang tidak terduga."
            jump heist_failed_retry

        "Cari cara lain untuk mendapatkan piala selain mencuri.":
            "Mungkin ada cara legal untuk mendapatkan piala kembali."
            "Lobi secara resmi, minta bantuan guru, atau cari bukti bahwa penyitaan tidak sah."
            jump heist_legal_approach

        "Terima bahwa piala mungkin tidak sepadan dengan risikonya.":
            "Aruna mulai mempertanyakan apakah piala ini benar-benar sepadan dengan semua bahaya ini."
            "Mungkin ada cara lain untuk membantu ekskul Robotika tanpa harus mencuri."
            jump heist_moral_questioning

label heist_secret_box:
    "Kotak berstiker 'CONFIDENTIAL' itu terletak di sudut gudang yang paling gelap."
    "Kucing hitam masih duduk di depannya, menatap Aruna dengan mata kuningnya."

    menu:
        "Buka kotak itu untuk melihat isinya.":
            "Aruna membuka kotak itu dengan hati-hati."
            "Di dalamnya ada dokumen-dokumen dengan kop resmi sekolah, dan sebuah USB drive."
            "Dokumen itu berisi daftar nama siswa yang pernah 'dipantau' oleh pihak sekolah."
            "Termasuk nama Aruna sendiri, dengan catatan: 'Potensi bahaya - Monitor ketat'."
            jump heist_surveillance_files

        "Ambil USB drive saja dan tutup kembali kotaknya.":
            "Aruna memutuskan untuk tidak membaca dokumen-dokumen itu."
            "Hanya mengambil USB drive yang mungkin berisi informasi penting."
            "Menutup kembali kotaknya seolah-olah tidak pernah dibuka."
            jump heist_usb_only

        "Tinggalkan kotak itu dan lanjut ke misi utama.":
            "Aruna menyadari kotak ini terlalu berbahaya untuk disentuh."
            "Memutuskan untuk fokus ke tujuan utama—mengambil piala Robotika."
            "Kucing itu mengeong pelan seolah kecewa."
            jump heist_abandon_secret

label heist_radio_discovery:
    "Suara dari radio di dalam gudang jelas terdengar."

    suara_radio "Target dalam jangkauan. Siap untuk eksekusi rencana B."
    suara_radio "Over. Tim A, siap di posisi masing-masing."

    menu:
        "Masuk ke gudang untuk mencari sumber radio.":
            "Aruna menyelinap masuk ke gudang dengan sangat hati-hati."
            "Di sudut gudang, ada radio komunikasi yang ditinggalkan menyala."
            "Tidak ada orang di dalam gudang, tapi ada peta dengan tanda-tanda merah di seluruh sekolah."
            jump heist_radio_map

        "Catat frekuensi radio dan bawa informasi ini keluar.":
            "Aruna mencatat frekuensi radio dan beberapa kata kunci yang terdengar."
            "Ini bisa berguna untuk memahami apa yang sebenarnya terjadi."
            "Lalu melanjutkan perjalanan ke gedung utama."
            jump heist_intelligence_gathering

        "Lari menjauh dari gudang secepat mungkin.":
            "Aruna menyadari ini terlalu berbahaya. Langsung pergi dari area gudang."
            "Menuju gerbang sekolah, berharap bisa keluar tanpa ketahuan."
            jump heist_escape_from_gudang

label heist_cat_mystery:
    "Keesokan harinya, Aruna mencari kucing hitam itu di sekitar rumah."
    "Tapi kucing itu sudah tidak ada lagi. Hanya kerah dengan tulisan 'Bantu Robotika' yang tertinggal."

    menu:
        "Investigasi tentang kucing itu di sekolah keesokan harinya.":
            "Aruna bertanya-tanya ke siswa lain tentang kucing hitam dengan kerah biru."
            "Beberapa siswa mengaku pernah melihat kucing itu sering berada di area ekskul Robotika."
            "Katanya kucing itu sering membawa 'pesan-pesan' aneh."
            jump heist_cat_investigation

        "Anggap ini kebetulan dan fokus ke misi lain.":
            "Aruna memutuskan untuk tidak memusingkan kucing aneh itu."
            "Fokus kembali ke kampanye dan misi-misi lain."
            jump heist_ignore_cat

        "Cari hubungan antara kucing itu dengan ekskul Robotika.":
            "Aruna langsung mendatangi ekskul Robotika keesokan harinya."
            "Menanyakan tentang kucing itu kepada Juan dan Faizal."
            "Reaksi mereka mengejutkan—mereka saling berpandangan dengan ketakutan."
            jump heist_cat_connection

label heist_budi_key_drop:
    "Kunci dengan logo kepala sekolah itu tergeletak di tanah, berkilau di bawah sinar bulan."

    menu:
        "Ambil kunci itu dan gunakan untuk masuk ke ruangan kepala sekolah.":
            "Aruna mengambil kunci itu dengan tangan gemetar."
            "Ini kunci master yang bisa membuka semua ruangan di lantai dua."
            "Sekarang Aruna punya akses langsung ke ruangan kepala sekolah."
            jump heist_master_key_access

        "Kembalikan kunci itu ke Pak Budi atau ke kantor satpam.":
            "Aruna menyadari mengambil kunci ini adalah tindakan kriminal serius."
            "Memutuskan untuk mengembalikannya ke tempat yang semestinya."
            jump heist_honest_choice

        "Simpan kunci itu untuk penggunaan masa depan.":
            "Aruna menyimpan kunci itu di saku, merasa ini bisa berguna nanti."
            "Tapi perasaan bersalah mulai menggerogoti."
            "Malam ini bukan waktu yang tepat untuk menggunakannya."
            jump heist_key_hoarding

label heist_budi_prayer:
    "Pak Budi berbisik ke pintu ruangan kepala sekolah seperti sedang berdoa."

    pak_budi "Ampunilah... ampunilah dosa-dosa yang terpaksa gue lakukan."
    pak_budi "Untuk anak-anak... untuk masa depan mereka..."

    menu:
        "Dekati Pak Budi dan tanya apa yang sedang dia lakukan.":
            "Aruna mendekati Pak Budi pelan-pelan."
            ar "Pak, lo lagi ngapain? Ada apa?"
            "Pak Budi terkejut, hampir jatuh saat melihat Aruna."
            pak_budi "Aruna? Lo... lo tidak boleh di sini!"
            jump heist_budi_alarmed

        "Tunggu sampai Pak Budi selesai, lalu tanyakan tentang kunci.":
            "Aruna menunggu di kejauhan sampai Pak Budi selesai 'berdoa'."
            "Setelah Pak Budi pergi, Aruna mendekati pintu dan mencoba kunci yang jatuh tadi."
            "Kunci itu cocok! Pintu ruangan kepala sekolah terbuka."
            jump heist_door_opens

        "Rekam doa Pak Budi sebagai bukti.":
            "Aruna mengambil HP dan merekam bisikan Pak Budi."
            "Ini bisa menjadi bukti penting jika ada sesuatu yang salah di sekolah ini."
            "Tapi merasa bersalah merekam seseorang dalam momen pribadi."
            jump heist_moral_dilemma_recording

label heist_juan_partnership:
    "Juan tersenyum tipis saat Aruna menerima ultimatumnya."

    juan "Gue seneng lo beda dari yang lain, Aruna."
    juan "Ini peta ruangan lantai dua, dan ini kunci cadangan yang gue curi dari ruang satpam."
    juan "Lo naik lewat tangga belakang, gue jaga di bawah buat ngalihin perhatian."

    menu:
        "Ikuti rencana Juan sepenuhnya.":
            ar "Siap. Lo jaga di bawah, gue naik ke atas."
            "Aruna mulai naik tangga belakang dengan peta Juan di tangan."
            jump heist_juan_execution

        "Tanyakan apakah Juan pernah melakukan ini sebelumnya.":
            ar "Lo pernah nyuri kunci satpam sebelumnya ini?"
            juan "Ini pertama kalinya. Gue biasanya orang yang nurutin aturan."
            juan "Tapi kalau aturan udah nggak adil, gue nggak bisa nurut terus."
            jump heist_juan_moral_justification

        "Bagi strategi: gue masuk lewat jalan lain, lo tetap jaga di bawah.":
            ar "Gue punya ide lain buat masuk. Lo tetap jaga di bawah."
            juan "Ide lain? Apa? Kita nggak punya banyak waktu!"
            ar "Gue bakal kasih tau kalau berhasil. Siapin jalan keluar kalau-kalau ada yang datang."
            jump heist_alternate_strategy

label heist_solo_mission_guilt:
    "Aruna melanjutkan perjalanan sendirian, tapi perasaan bersalah terus mengganggu."

    menu:
        "Tetap fokus ke misi utama—mengambil piala.":
            "Aruna mencoba mengabaikan perasaan bersalah dan fokus ke tujuan."
            "Naik ke lantai dua lewat tangga belakang yang gelap."
            jump heist_solo_ascent

        "Kembali mencari Juan dan tawarkan bantuan yang lebih realistis.":
            "Aruna menyadari mungkin ada cara lain untuk membantu Juan."
            "Berbalik untuk mencari Juan, tapi dia sudah tidak ada di tempat semula."
            jump heist_juan_disappeared

        "Fokus ke data Faizal yang mungkin lebih penting dari piala.":
            "Aruna mulai berpikir bahwa data Robotika mungkin lebih penting dari sekadar piala."
            "Mengubah arah misi menuju lab Kimia tempat Faizal mungkin berada."
            jump heist_priority_shift

label heist_juan_refusal:
    "Juan menatap Aruna dengan tatapan kecewa yang dalam."

    juan "Lo sama aja kayak yang lain, Aruna. Cuma peduli piala dan suara doang."
    juan "Gue nggak butuh bantu lo. Gue bakal cari cara sendiri."
    "Juan pergi tanpa menoleh lagi. Aruna melanjutkan sendirian."

    menu:
        "Lanjutkan misi sendirian meskipun merasa bersalah.":
            "Aruna menekan perasaan bersalah dan melanjutkan misi."
            "Tapi setiap langkah terasa lebih berat dari sebelumnya."
            jump heist_guilty_ascent

        "Ubah pikiran dan kejar Juan untuk menawarkan bantuan penuh.":
            "Aruna menyadari keputusannya salah. Berlari mengejar Juan."
            "Tapi Juan sudah hilang dalam kegelapan malam."
            jump heist_too_late_to_help

        "Fokus ke misi lain dan kembali membantu Juan besok.":
            "Aruna memutuskan untuk kembali besok dengan penawaran yang lebih baik."
            "Malam ini terlalu emosional untuk mengambil keputusan yang tepat."
            jump heist_deferred_help

label heist_juan_execution:
    "Aruna naik tangga belakang yang berkarat dan gelap."
    "Peta Juan menunjukkan jalur yang aman menghindari area dengan kamera."

    menu:
        "Ikuti peta Juan secara ketat.":
            "Aruna mengikuti setiap instruksi di peta Juan."
            "Berhasil menghindari kamera dan area patroli satpam."
            "Sampai di depan ruangan kepala sekolah tanpa insiden."
            jump heist_arrival_principal_office

        "Ambil jalan pintas meskipun berisiko.":
            "Aruna melihat jalan pintas yang lebih cepat, tapi melewati area dengan kamera."
            "Memutuskan mengambil risiko untuk menghemat waktu."
            jump heist_shortcut_risk

        "Modifikasi rute berdasarkan insting sendiri.":
            "Aruna merasa ada beberapa bagian peta yang tidak efisien."
            "Memutuskan untuk memodifikasi rute berdasarkan pengetahuan sendiri tentang sekolah."
            jump heist_modified_route

label heist_modified_plan:
    "Aruna naik duluan, Juan mengikuti dari belakang dengan jarak aman."

    menu:
        "Cek setiap sudut sebelum memberi sinyal ke Juan.":
            "Aruna sangat berhati-hati, mengecek setiap sudut sebelum memberi isyarat."
            "Prosesnya lambat, tapi lebih aman."
            "Juan mulai tampak tidak sabar di bawah."
            jump heist_slow_progress

        "Bergerak cepat dan percaya Juan bisa mengikuti.":
            "Aruna bergerak dengan cepat, mengasumsikan Juan bisa mengikuti."
            "Tapi Juan tersandung di tangga yang berkarat, membuat suara keras."
            jump heist_juan_stumble

        "Komunikasi lewat HP untuk koordinasi yang lebih baik.":
            "Aruna menghubungi Juan lewat HP untuk koordinasi yang lebih baik."
            "Tapi sinyal di dalam gedung sangat lemah."
            jump heist_poor_signal

label heist_desperate_plan:
    "Juan menatap Aruna dengan mata yang menunjukkan ketidakputusasaan."

    juan "Gue nggak punya plan B, Aruna. Ini satu-satunya kesempatan gue."
    juan "Kalau gagal, tim Robotika bubar. Pak Kepsek bakal pastiin gue di-skors."

    menu:
        "Terima ketidakputusasaan Juan dan bantu semaksimal mungkin.":
            ar "Oke, gue ngerti. Kita buat plan A ini berhasil seberapapun mustahilnya."
            juan "Makasih, Aruna. Lo bener-bener beda."
            jump heist_commitment_to_success

        "Tawarkan untuk membuat plan B bersama-sama.":
            ar "Kita masih punya waktu buat mikirin plan B. Jangan menyerah sebelum mulai."
            juan "Waktu? Gue nggak punya waktu! Deadline besok pagi!"
            jump heist_time_pressure

        "Tanyakan apakah ada orang lain yang bisa membantu.":
            ar "Selain gue, masih ada orang lain yang bisa bantu nggak?"
            juan "Gue udah tanya semua orang. Semua pada takut sama Pak Kepsek."
            juan "Lo orang terakhir yang gue harapkan."
            jump heist_last_resort

label heist_broken_trophy:
    "Piala Robotika pecah menjadi dua di lantai ruang depan."
    "Flourine tersenyum dingin melihat pecahan itu."

    flourine "Sekarang nggak ada yang bisa dapat. Semua rugi."
    flourine "Kecuali gue. Gue masih punya dokumen-dokumen penting Robotika."

    menu:
        "Tantang Flourine untuk menyerahkan dokumen itu.":
            ar "Serahkan dokumen-dokumen itu sekarang juga!"
            flourine "Atau lo apa? Lapor ke guru? Siapa yang bakal percaya lo?"
            jump heist_flourine_power

        "Ambil pecahan piala dan bawa sebagai bukti.":
            "Aruna mengambil pecahan piala itu. Setidaknya ada bukti."
            "Flourine tertawa melihat Aruna mengambil sampah."
            jump heist_trophy_evidence

        "Tanya Flourine apa motivasinya melakukan semua ini.":
            ar "Kenapa lo harus sampai segini? Demu ketua OSIS?"
            flourine "Lo nggak ngerti, Aruna. Ini bukan cuma soal jabatan."
            flourine "Ini soal kekuasaan. Dan lo baru belajar pelajaran pertamanya."
            jump heist_flourine_lesson

label heist_flourine_deal:
    "Flourine memegang piala itu dengan santai, seolah itu miliknya."

    flourine "Deal? Lo bantu gue ngalahin Fanya, gue bagi-bagi suara Robotika."
    flourine "Atau lo pulang dengan tangan kosong. Pilihan lo."

    menu:
        "Terima deal Flourine demi ekskul Robotika.":
            ar "Oke, gue terima. Tapi gue butuh jaminan."
            flourine "Jaminan? Kata gue saja cukup."
            jump heist_moral_compromise

        "Tolak deal dan cari cara lain untuk membantu Robotika.":
            ar "Gue nggak akan jadi alat politik lo, Flourine."
            flourine "Maka lo kehilangan satu-satunya kesempatan bantu Robotika."
            jump heist_moral_stand

        "Tawarkan counter-deal yang lebih menguntungkan.":
            ar "Gue bantu lo ngalahin Fanya, tapi gue mau lebih dari sekadar bagi-bagi suara."
            ar "Gue mau lo serahkan semua dokumen Robotika yang lo punya."
            jump heist_negotiation

label heist_flourine_keys:
    "Flourine mengibaskan kunci di tangan kanannya, senyum penuh kemenangan."

    flourine "Gue punya kunci legal ke semua ruangan di sekolah ini."
    flourine "Termasuk ruangan kepala sekolah. Termasuk ruang arsip."
    flourine "Lo apa cuma bisa nyusup malam-malam kayak tikus?"

    menu:
        "Tanya bagaimana Flourine mendapatkan kunci-kunci itu.":
            ar "Dari mana lo dapat kunci-kunci itu? Itu bukan wewenang ketua OSIS."
            flourine "Koneksi, Aruna. Koneksi lebih penting dari aturan."
            jump heist_flourine_connections

        "Coba merebut kunci dari Flourine.":
            "Aruna melompat maju mencoba merebut kunci dari tangan Flourine."
            "Tapi Flourine terlalu siap. Dia menendang Aruna dan kunci jatuh ke lantai."
            jump heist_struggle_for_keys

        "Pura-pura setuju dengan Flourine untuk mendekat.":
            ar "Iya, lo hebat Flourine. Lo punya segalanya."
            "Aruna mendekat pelan-pelan, mencari kesempatan untuk merebut kunci."
            jump heist_deceptive_approach

label heist_caught_in_spotlight:
    "Lampu sorot mulai menyinari taman sekolah dari segala arah."
    "Aruna terjebak di tengah area terbuka tanpa tempat bersembunyi."

    menu:
        "Lari menuju area gelap di sebelah kanan taman.":
            "Aruna berlari ke arah area yang masih gelap."
            "Berhasil menyelinap ke balik semak-semak tepat saat lampu sorot menyapu area itu."
            jump heist_bush_escape

        "Tenggelamkan diri di kolam ikan di tengah taman.":
            "Aruna melihat kolam ikan di tengah taman. Berisiko, tapi mungkin berhasil."
            "Melompat ke dalam kolam, berendam di dalam air yang dingin."
            jump heist_pond_hiding

        "Berhenti bergerak dan berharap tidak terlihat.":
            "Aruna membeku di tempat, berharap menjadi tidak terlihat dalam kegelapan."
            "Tapi lampu sorot terus mencari secara sistematis."
            jump heist_frozen_failure

label heist_hiding_during_alarm:
    "Aruna bersembunyi di ruang gudang lantai satu di antara tumpukan meja kayu tua."
    "Alarm mati setelah dua menit, tapi sekarang ada patroli ekstra ketat."

    menu:
        "Tunggu sampai patroli berkurang sebelum keluar.":
            "Aruna menunggu di dalam gudang selama satu jam."
            "Patroli mulai berkurang, memberikan kesempatan untuk keluar."
            jump heist_post_alarm_escape

        "Cari jalan lain keluar dari gudang tanpa ketahuan.":
            "Aruna mencari ventilasi atau jalan lain untuk keluar dari gudang."
            "Ada ventilasi kecil di bagian atas dinding."
            jump heist_ventilation_escape

        "Keluar saat aman dan lanjutkan misi ke ruangan kepala sekolah.":
            "Aruna memutuskan untuk tidak menyerah meskipun alarm sudah berbunyi."
            "Menganggap ini kesempatan untuk melanjutkan misi saat orang-orang sibuk dengan alarm."
            jump heist_bluff_continuation

label heist_alarm_panel_code:
    "Panel kontrol alarm terbuka, tapi butuh kode untuk mematikannya."
    "Ada tulisan kecil di panel: 'KODE DIUBAH HARI INI - LIHAT DI LOG HARIAN'."

    menu:
        "Cari log harian di sekitar area maintenance.":
            "Aruna mencari buku log harian petugas maintenance."
            "Menemukannya di laci meja kerja di sudut ruangan."
            "Membuka halaman hari ini, mencari kode alarm baru."
            jump heist_code_search

        "Coba menebak kode berdasarkan pola yang biasa dipakai.":
            "Aruna mencoba beberapa kombinasi yang biasa dipakai sekolah."
            "1234, 0000, tanggal hari ini, tapi semuanya salah."
            jump heist_code_guessing

        "Biarkan alarm tetap menyala dan cari jalan lain.":
            "Aruna menyadari menebak kode hanya membuang waktu."
            "Membiarkan alarm tetap menyala dan mencari jalan lain."
            jump heist_abandon_alarm

label heist_staircase_success:
    "Aruna berhasil sampai di lantai dua tanpa terlihat kamera."
    "Tangga karat itu tidak runtuh meskipun berbunyi KRIK-KRIK."

    menu:
        "Lanjut ke koridor utama menuju ruangan kepala sekolah.":
            "Aruna melangkah masuk ke koridor lantai dua yang gelap."
            "Ruangan kepala sekolah ada di ujung koridor sebelah kanan."
            jump heist_corridor_navigation

        "Cek apakah ada bahaya lain di area tangga.":
            "Aruna memutuskan untuk berhati-hati dan mengecek area sekitar tangga."
            "Menemukan bahwa ada sensor gerak baru di dekat pintu keluar tangga."
            jump heist_motion_sensor_discovery

        "Istirahat sejenak untuk menenangkan diri.":
            "Jantung Aruna masih berdebar kencang dari naik tangga berkarat itu."
            "Memutuskan untuk istirahat sejenak di area tangga."
            jump heist_staircase_rest

label heist_camera_caught:
    "Lampu biru kamera berkedip-kedip—sedang merekam gerakan Aruna."
    "Segera akan ada orang yang datang ke area ini."

    menu:
        "Lari secepat mungkin ke lantai dua sebelum mereka tiba.":
            "Aruna berlari naik tangga secepat mungkin."
            "Berhasil sampai di lantai dua, tapi suara langkah kaki sudah terdengar dari bawah."
            jump heist_desperate_ascent

        "Sembunyi di balik tembok dekat tangga dan berharap tidak dilihat.":
            "Aruna bersembunyi di balik tembok dekat tangga."
            "Suara langkah kaki mendekat, melewati tempat persembunyian tanpa berhenti."
            jump heist_close_call

        "Hancurkan kamera dengan lemparan batu sebelum kabur.":
            "Aruna melempar batu ke arah kamera dengan keras."
            "KAMERA HANCUR! Tapi suara hancurnya kamera menarik perhatian."
            jump heist_camera_destruction

label heist_banner_noise:
    "Banner bekas acara sekolah jatuh dan membuat suara keras yang menggelegar."
    "Suara itu menarik perhatian seseorang dari dalam gedung."

    menu:
        "Sembunyi segera sebelum orang itu sampai.":
            "Aruna bersembunyi di balik tembok dekat tangga."
            "Seorang satpam keluar dan melihat banner yang jatuh."
            "Dia mengambil banner dan kembali ke dalam tanpa curiga ada orang lain."
            jump heist_banner_close_call

        "Lari ke lantai dua sebelum orang itu sampai.":
            "Aruna berlari naik tangga secepat mungkin."
            "Berhasil sampai di lantai dua tanpa ketahuan."
            jump heist_staircase_success

        "Pura-pura jadi siswa yang baru pulang dari acara sekolah.":
            "Aruna berdiri di tempat dengan tenang seolah-olah baru selesai acara."
            "Saat satpam sampai, Aruna menjelaskan dengan santai."
            ar "Eh Pak, gue baru selesai bantu rapat OSIS. Banner tadi kegencet angin."
            jump heist_bluff_guard

label heist_van_observation:
    "Dari balik tembok, Aruna melihat dua orang satpam memasukkan kotak berstiker 'CONFIDENTIAL' ke mobil van gelap."
    "Mobil van itu segera pergi meninggalkan area sekolah."

    menu:
        "Catat plat nomor van itu untuk investigasi masa depan.":
            "Aruna mencatat plat nomor van gelap itu: B 4567 XYZ."
            "Bisa berguna untuk mencari tahu siapa yang sebenarnya mengambil kotak-kotak itu."
            jump heist_plate_number_recorded

        "Ikuti van itu untuk melihat ke mana mereka pergi.":
            "Aruna mempertimbangkan untuk mengikuti van itu, tapi menyadari terlalu berisiko."
            "Van itu sudah jauh, dan Aruna tidak punya kendaraan."
            jump heist_van_lost

        "Pulang dan melaporkan kejadian ini ke pihak berwenang.":
            "Aruna menyadari ini sudah melampaui misi sederhana."
    "Memutuskan untuk melaporkan kejadian mencurigakan ini ke pihak berwenang."
            jump heist_report_authorities

label heist_guard_conversation:
    "Dari balik tembok kantin, Aruna menguping pembicaraan dua satpam."

    satpam1 "Kenapa ekstra tight malam ini? Biasanya nggak segini."
    satpam2 "Perintah langsung dari Pak Kepsek. Ada yang mau nyuri malam ini katanya."
    satpam1 "Nyuri apa? Piala? Dana?"
    satpam2 "Bukan. Katanya ada dokumen penting yang bocor. Pak Kepsek parno banget."

    menu:
        "Gunakan informasi ini untuk merencanakan strategi baru.":
            "Aruna menyadari Pak Kepsek mencari dokumen, bukan piala."
            "Mungkin mengambil piala lebih aman dari yang dipikirkan."
            jump heist_strategic_insight

        "Cari tahu dokumen apa yang dimaksud Pak Kepsek.":
            "Aruna semakin penasaran dengan dokumen yang dimaksud Pak Kepsek."
            "Mungkin dokumen itu lebih penting dari piala Robotika."
            jump heist_document_priority

        "Abaikan informasi ini dan fokus ke misi utama.":
            "Aruna memutuskan untuk tidak terlalu memusingkan informasi satpam."
            "Fokus kembali ke tujuan utama—mengambil piala Robotika."
            jump heist_focus_on_trophy

label heist_faizal_truth:
    "Faizal menggigil saat menceritakan apa yang terjadi."

    faizal "Gue nemu celah di sistem scoring kompetisi. Bukan buat nyontek, tapi buat bantu tim gue menang fair."
    faizal "Tapi Pak Kepsek nyalahin gue. Dia bilang gue curang dan mau hancurin reputasi sekolah."
    faizal "Dia ambil semua data tim gue dan ngunci gue di sini supaya gak ngomong ke siapa-siapa."

    menu:
        "Janji akan membantu Faizal membersihkan namanya.":
            ar "Gue janji bakal bantu lo bersihin nama lo, Faizal."
            faizal "Lo bisa bantu? Tapi Pak Kepsek pegang semua bukti yang salah!"
            jump heist_faizal_promise

        "Tanyakan apa yang ada di laptop Faizal sekarang.":
            ar "Sekarang di laptop lo ada apa? Data tim?"
            faizal "Iya, backup terakhir sebelum diambil. Kalau ini ilang, tim Robotika bubar."
            jump heist_laptop_priority

        "Cari cara membuka pintu lab dari luar.":
            "Aruna mencari cara untuk membuka pintu lab yang terkunci dari luar."
            "Tapi tidak ada cara pintu itu bisa dibuka tanpa kunci."
            jump heist_locked_lab_solution

label heist_locked_lab_dilemma:
    "Pintu lab Kimia terkunci dari luar. Aruna tidak bisa membantunya keluar."

    menu:
        "Cari kunci cadangan di area sekitar lab.":
            "Aruna mencari di bawah karpet depan pintu, di atas pintu, di tempat-tempat umum."
            "Tidak ada kunci cadangan di mana pun."
            jump heist_no_spare_key

        "Coba membuka kunci dengan kertas klip.":
            "Aruna mengambil kertas klip dari saku dan mencoba membuka kunci pintu."
            "Tapi kunci pintu lab lebih kompleks dari biasanya."
            jump heist_lockpick_failure

        "Tanyakan Faizal apakah dia punya ide untuk keluar.":
            ar "Lo punya ide nggak buat keluar dari sini?"
            faizal "Ada ventilasi kecil di dinding belakang, tapi gue gak muat."
            faizal "Tapi lo bisa masuk lewat sana buat bantu gue."
            jump heist_ventilation_idea

label heist_faizal_priority:
    "Faizal menatap Aruna dengan serius."

    faizal "Piala itu cuma simbol, Aruna. Data tim gue... itu nyawa."
    faizal "Kalau piala ilang, Robotika masih bisa lanjut. Tapi kalau data ilang, tiga tahun kerja keras gue hilang."

    menu:
        "Ubah prioritas misi menjadi membantu Faizal dulu.":
            ar "Oke, gue ubah rencana. Gue bantu lo dulu, baru piala."
            faizal "Lo bener-bener beda, Aruna. Gue nggak nyangka."
            jump heist_priority_faizal

        "Tawarkan untuk melakukan dua misi sekaligus.":
            ar "Gue bisa coba lakukan dua-duanya. Bantu lo dan ambil piala."
            faizal "Nggak mungkin! Terlalu berisiko. Lo harus pilih."
            jump heist_impossible_dual

        "Tetap fokus ke piala, tapi janji akan membantu Faizal besok.":
            ar "Gue harus ambil piala dulu buat ekskul lo. Besok gue bantu lo urus datanya."
            faizal "Besok? Pak Kepsek bakal bakar data itu sebelum besok!"
            jump heist_faizal_urgency

label heist_budi_revelation:
    "Pak Budi tertawa kecil, tertawa yang penuh kesedihan."

    pak_budi "Lo nggak ngerti apa yang lagi terjadi di sekolah ini, Nak."
    pak_budi "Piala itu cuma permukaan. Ada yang jauh lebih besar lagi di balik semua ini."
    pak_budi "Dan gue... gue terjebak di tengahnya."

    menu:
        "Tanya Pak Budi apa yang sebenarnya terjadi di sekolah ini.":
            ar "Pak, ada apa sebenarnya? Lo bisa cerita sama gue."
            pak_budi "Gue nggak bisa. Gue nggak berani."
            "Pak Budi menatap Aruna dengan mata yang penuh rasa takut."
            jump heist_budi_fear_confirmed

        "Tawarkan bantuan untuk membantu Pak Budi keluar dari masalah.":
            ar "Kalau lo ada masalah, gue bisa bantu. Lo percaya sama gue?"
            pak_budi "Bantu? Lo masih anak sekolah. Lo nggak ngerti seberapa besar masalah ini."
            jump heist_budi_dismissal

        "Tanyakan tentang kunci yang jatuh dari saku Pak Budi.":
            ar "Kunci yang jatuh dari saku lo tadi itu kunci apa, Pak?"
            pak_budi "Kunci itu... kunci ke pintu gerbang."
            "Pak Budi mengambil kunci itu dan menyembunyikannya kembali."
            jump heist_gate_key_mystery

label heist_budi_confrontation:
    "Pak Budi menggelengkan kepala, menatap Aruna dengan tatapan kecewa."

    pak_budi "Jangan bohong sama orang yang sudah ngelihat semua kebohongan di dunia ini."
    pak_budi "Tapi gue nggak akan melaporkan lo. Kalau gue lapor, lo bakal celaka."

    menu:
        "Tanya kenapa Pak Budi tidak melaporkan Aruna.":
            ar "Kenapa lo nggak lapor gue, Pak?"
            pak_budi "Karena gue tahu lo punya niat baik. Lo cuma mau bantu ekskul Robotika."
            jump heist_budi_understanding

        "Minta Pak Budi untuk tidak memberitahu siapa pun tentang kejadian ini.":
            ar "Pak, tolong jangan kasih tau siapa-siapa soal gue malam ini."
            pak_budi "Gue sudah bilang gue nggak akan lapor. Tapi lo harus janji satu hal."
            jump heist_budi_condition

        "Tawarkan bantuan kepada Pak Budi yang jelas-jelah dalam masalah.":
            ar "Pak, lo jelas-jelah ada masalah. Biar gue bantu."
            pak_budi "Lo nggak bisa bantu gue, Nak. Masalah gue terlalu besar."
            jump heist_budi_refusal

label heist_budi_fear:
    "Mata Pak Budi menunjukkan rasa takut yang mendalam."

    menu:
        "Tanyakan apa yang membuat Pak Budi takut.":
            ar "Pak, lo takut sama apa? Ada yang mengancam lo?"
            pak_budi "Gue nggak bisa ngomong. Gue nggak berani."
            "Pak Budi mundur pelan-pelan, seolah ingin menjauh dari Aruna."
            jump heist_budi_secret

        "Katakan pada Pak Budi bahwa dia tidak sendirian.":
            ar "Pak, lo nggak sendirian. Kalau lo ada masalah, kita bisa cari solusi bareng."
            pak_budi "Bareng? Lo nggak ngerti. Ini bukan masalah yang bisa diselesaikan berdua."
            jump heist_budi_isolation

        "Biarkan Pak Budi pergi dan fokus ke misi utama.":
            "Aruna menyadari Pak Budi tidak akan membuka diri sekarang."
            "Membiarkannya pergi dan melanjutkan misi."
            jump heist_budi_departure

label heist_faizal_confession:
    "Faizal menggigit bibir, tampak sangat tertekan."

    faizal "Gue lagi bikin backup data tim Robotika... tapi gue juga lagi ngerjain sesuatu yang lain."
    faizal "Pak Kepsek paksa gue bikin program pengawasan buat sekolah."
    faizal "Program yang bisa pantau semua aktivitas siswa, chat, bahkan lokasi mereka."
    faizal "Gue nggak mau ngerjainnya, tapi dia ancam bakal hancurin tim Robotika."

    menu:
        "Janji akan membantu Faizal keluar dari situasi ini.":
            ar "Gue bakal bantu lo, Faizal. Lo nggak harus kerjain hal itu."
            faizal "Tapi dia pegang semua kartu! Data tim, karier gue, semuanya!"
            jump heist_faizal_desperation

        "Tanyakan apakah program itu sudah selesai.":
            ar "Program itu udah selesai belum?"
            faizal "Belum. Masih 60%. Kalau selesai, sekolah ini bakal jadi penjara digital."
            jump heist_program_status

        "Minta Faizal menghancurkan program itu sekarang juga.":
            ar "Hancurin program itu sekarang juga sebelum terlambat!"
            faizal "Gue nggak bisa! Laptop gue ada tracking dia. Kalau gue hapus, dia bakal tau!"
            jump heist_program_dilemma

label heist_faizal_rejection:
    "Faizal menutup laptopnya dan menolak bantuan Aruna."

    faizal "Ambil piala lo, dan lupakan gue."
    faizal "Gue nggak butuh belas kasihan orang yang cuma peduli piala doang."

    menu:
        "Tetap mencoba membantu Faizal meskipun ditolak.":
            ar "Gue nggak cuma peduli piala! Lo butuh bantuan!"
            faizal "Pergi saja! Lo nggak ngerti apa yang gue alami!"
            jump heist_faizal_pushed_away

        "Terima penolakan dan fokus ke piala.":
            "Aruna menyadari Faizal terlalu emosional untuk diajak bicara."
            "Memutuskan untuk fokus ke misi utama dulu."
            jump heist_focus_on_trophy

        "Biarkan Faizal sendiri dan janji akan kembali dengan bantuan.":
            ar "Oke, gue pergi dulu. Tapi gue janji bakal balik dengan bantuan."
            faizal "Jangan balik. Lo cuma bakal bahayain diri lo sendiri."
            jump heist_faizal_warning

label heist_surveillance_project:
    "Di layar laptop Faizal, Aruna melihat diagram rumit yang terlihat seperti rencana jaringan sekolah."
    "Ada tulisan besar di pojok: 'PROYEK PENGAWASAN TOTAL'."

    menu:
        "Ambil foto layar laptop sebagai bukti.":
            "Aruna mengambil HP dan memfoto layar laptop dengan cepat."
            "Faizal menyadari dan langsung menutup laptop dengan keras."
            faizal "Lo ngapain?! Jangan ambil foto itu!"
            jump heist_photo_evidence

        "Tanya Faizal detail tentang proyek pengawasan ini.":
            ar "Ini proyek apa, Faizal? Pengawasan total? Maksudnya apa?"
            faizal "Gue nggak bisa cerita! Gue nggak berani!"
            "Faizal menutup laptop dan menunduk, menolak melanjutkan percakapan."
            jump heist_faizal_sealed

        "Coba menghentikan Faizal dari proyek ini.":
            ar "Faizal, lo nggak boleh lanjutin proyek ini. Ini melanggar privasi!"
            faizal "Gue nggak punya pilihan! Dia ancam bakal hancurin semuanya!"
            jump heist_faizal_coercion

label heist_after_security_clears:
    "Area belakang sepi setelah petugas keamanan pergi."
    "Aruna keluar dari balik pohon beringin, tapi perasaan tidak aman tetap ada."

    menu:
        "Lanjutkan misi ke ruangan kepala sekolah.":
            "Aruna memutuskan untuk melanjutkan misi meskipun ada risiko."
            "Menuju tangga belakang untuk naik ke lantai dua."
            jump heist_staircase_approach

        "Investigasi area yang baru saja diperiksa petugas keamanan.":
            "Aruna penasaran dengan apa yang sedang dicari petugas keamanan."
            "Mendekati area yang baru saja mereka periksa."
            jump heist_area_investigation

        "Pulang dan kembali besok dengan informasi lebih.":
            "Aruna menyadari terlalu banyak yang tidak diketahui malam ini."
            "Memutuskan untuk kembali besok dengan persiapan lebih baik."
            jump heist_deferred_mission

label heist_flourine_with_security:
    "Dari kejauhan, Aruna melihat Flourine sedang berbicara dengan tiga orang petugas keamanan di ruang guru."
    "Flourine terlihat seperti memberikan instruksi, bukan diperiksa."

    menu:
        "Dekat lebih dekat untuk mendengar percakapan mereka.":
            "Aruna menyelinap lebih dekat ke ruang guru."
            "Bisa mendengar suara Flourine memberikan perintah."
            flourine "Pastikan area lantai dua aman. Target mungkin akan mencoba lewat tangga belakang."
            jump heist_flourine_commanding

        "Ambil foto Flourine dengan petugas keamanan sebagai bukti.":
            "Aruna mengambil HP dan memfoto Flourine bersama petugas keamanan."
            "Ini bukti bahwa Flourine terlibat dalam operasi keamanan malam ini."
            jump heist_flourine_evidence

        "Pulang dan merencanakan strategi baru menghadapi Flourine.":
            "Aruna menyadari Flourine adalah musuh yang jauh lebih berbahaya dari yang dikira."
            "Memutuskan untuk pulang dan merencanakan strategi baru."
            jump heist_strategic_withdrawal

label heist_strategic_retreat:
    "Aruna menyadari ini sudah melampaui misi sederhana mengambil piala."
    "Ada konspirasi yang lebih besar yang sedang berlangsung di sekolah ini."

    menu:
        "Kembali besok dengan persiapan dan informasi lebih.":
            "Aruna menyadari butuh informasi lebih sebelum kembali."
            "Malam ini terlalu banyak kejadian yang tidak terduga."
            jump heist_planned_return

        "Cari tahu lebih banyak tentang Flourine dan operasi malam ini.":
            "Aruna memutuskan untuk menginvestigasi Flourine dan apa yang sedang dia lakukan."
            "Mungkin ada cara untuk menghentikannya."
            jump heist_flourine_investigation

        "Fokus ke kampanye dan abaikan misteri ini.":
            "Aruna menyadari ini terlalu berbahaya untuk terlibat lebih jauh."
            "Memutuskan untuk fokus ke kampanye dan mengabaikan misteri ini."
            jump heist_campaign_focus

label heist_rooftop_crossing:
    "Aruna berjalan pelan-pelan di atap yang licin karena embun malam."
    "Talang air yang menghubungkan dua gedung terlihat rapuh."

    menu:
        "Berhati-hati menyeberang talang air.":
            "Aruna melangkah dengan sangat hati-hati di talang air yang licin."
            "Berhasil menyeberang ke atap gedung lab tanpa insiden."
            jump heist_lab_rooftop

        "Cari jalan lain yang lebih aman.":
            "Aruna melihat ada jalan lain yang mungkin lebih aman."
            "Melewati sisi atap yang lebih stabil, tapi lebih panjang."
            jump heist_alternative_roof_path

        "Lompat langsung ke atap gedung lab.":
            "Aruna mempertimbangkan untuk melompat langsung ke atap gedung lab."
            "Jaraknya sekitar dua meter, cukup untuk lompatan yang berani."
            jump heist_rooftop_jump

label heist_mysterious_team:
    "Tiga orang berpakaian hitam-hitam muncul di atap."
    "Mereka bukan satpam biasa—membawa alat-alat yang tidak biasa untuk satpam sekolah."

    menu:
        "Beri diri up dan menyerah kepada mereka.":
            "Aruna menyadari ini sudah melampaui kemampuan."
            "Mengangkat tangan dan menyerah kepada tim misterius itu."
            jump heist_surrender

        "Coba berunding dengan mereka.":
            ar "Siapa lo? Kenapa lo ada di sini?"
            "Salah satu dari mereka menatap Aruna dengan dingin."
            unknown "Anda tidak seharusnya ada di sini."
            jump heist_negotiation_attempt

        "Cari cara melarikan diri dari atap.":
            "Aruna melihat ada talang air yang bisa digunakan untuk turun."
            "Memutuskan untuk mencoba melarikan diri."
            jump heist_rooftop_escape

label heist_rooftop_hide_seek:
    "Aruna bersembunyi di balik AC unit besar di atap gedung."
    "Tim misterius mulai mencari secara sistematis di sekitar atap."

    menu:
        "Tunggu sampai mereka lelah mencari dan pergi.":
            "Aruna menunggu di balik AC unit selama dua puluh menit."
            "Tim misterius mulai kelelahan mencari dan memutuskan untuk turun."
            jump heist_hide_success

        "Cari kesempatan untuk melarikan diri saat lengah.":
            "Aruna melihat kesempatan saat salah satu dari mereka berbalik."
            "Berlari menuju talang air untuk turun."
            jump heist_escape_opportunity

        "Sengaja membuat suara untuk mengalihkan perhatian mereka.":
            "Aruna melempar batu ke sisi lain atap untuk mengalihkan perhatian."
            "Tim misterius bergerak ke arah suara itu."
            jump heist_diversion_success

label heist_failed_retry:
    "Malam ini terlalu banyak kejadian yang tidak terduga."
    "Aruna menyadari butuh rencana yang lebih matang."

    menu:
        "Kembali besok malam dengan peta dan persiapan lebih baik.":
            "Aruna menyusun rencana untuk besok malam."
            "Akan membawa peta sekolah yang lebih detail dan peralatan yang mungkin dibutuhkan."
            jump heist_tomorrow_plan

        "Cari informasi tentang situasi sekolah dari siswa lain.":
            "Aruna memutuskan untuk mencari tahu lebih banyak tentang apa yang terjadi di sekolah."
            "Mungkin ada siswa lain yang tahu sesuatu."
            jump heist_information_gathering

        "Ubah strategi menjadi pendekatan legal.":
            "Aruna mulai mempertimbangkan pendekatan legal untuk mendapatkan piala."
            "Mungkin lobi secara resmi atau mencari bukti bahwa penyitaan tidak sah."
            jump heist_legal_strategy

label heist_legal_approach:
    "Aruna mulai mempertimbangkan cara legal untuk mendapatkan piala kembali."

    menu:
        "Lobi kepala sekolah secara resmi besok pagi.":
            "Aruna akan meminta pertemuan dengan kepala sekolah besok pagi."
            "Meminta penjelasan tentang penyitaan piala Robotika."
            jump heist_official_lobby

        "Cari bukti bahwa penyitaan piala tidak sah.":
            "Aruna akan mencari dokumen atau aturan yang melarang penyitaan seperti ini."
            "Mungkin ada preseden kasus serupa di masa lalu."
            jump heist_evidence_search

        "Minta bantuan guru pembina Robotika.":
            "Aruna akan mendekati guru pembina Robotika untuk bantuan."
            "Guru pembina mungkin punya wewenang untuk meminta piala kembali."
            jump heist_teacher_support

label heist_moral_questioning:
    "Aruna mulai mempertanyakan apakah piala ini benar-benar sepadan dengan semua bahaya ini."

    menu:
        "Tetap percaya bahwa membantu Robotika adalah hal yang benar.":
            "Aruna menyadari mengambil piala kembali adalah hal yang benar."
            "Ekskul Robotika berhak atas pencapaian mereka."
            jump heist_moral_conviction

        "Cari cara lain untuk membantu Robotika tanpa mencuri.":
            "Aruna menyadari ada cara lain untuk membantu Robotika."
            "Mungkin membantu mereka mendapatkan piala baru atau penghargaan lain."
            jump heist_alternative_help

        "Fokus ke kampanye dan misi lain yang lebih penting.":
            "Aruna menyadari kampanye dan misi lain lebih penting."
            "Mengabaikan piala Robotika untuk sementara waktu."
            jump heist_campaign_priority

label heist_surveillance_files:
    "Dokumen-dokumen itu berisi daftar nama siswa yang pernah 'dipantau' oleh pihak sekolah."
    "Termasuk nama Aruna sendiri, dengan catatan: 'Potensi bahaya - Monitor ketat'."

    menu:
        "Ambil semua dokumen sebagai bukti.":
            "Aruna mengambil semua dokumen dari kotak itu."
            "Ini bukti yang sangat kuat tentang aktivitas pengawasan ilegal sekolah."
            jump heist_document_collection

        "Ambil foto dokumen dan kembalikan ke tempatnya.":
            "Aruna memfoto setiap halaman dokumen dengan HP."
            "Mengembalikan dokumen ke tempatnya agar tidak ketahuan."
            jump heist_document_photos

        "Biarkan dokumen itu dan fokus ke misi utama.":
            "Aruna menyadari dokumen ini terlalu berbahaya untuk disentuh."
            "Membiarkannya dan fokus ke misi utama."
            jump heist_ignore_documents

label heist_usb_only:
    "Aruna hanya mengambil USB drive dari kotak 'CONFIDENTIAL'."
    "Menutup kembali kotaknya seolah-olah tidak pernah dibuka."

    menu:
        "Periksa isi USB drive saat aman di rumah.":
            "Aruna menyimpan USB drive di saku untuk diperiksa nanti."
            "Mungkin berisi informasi penting tentang apa yang terjadi di sekolah."
            jump heist_usb_examination

        "Bawa USB drive ke Juan atau Faizal untuk diperiksa.":
            "Aruna mempertimbangkan untuk memberikan USB drive ke Juan atau Faizal."
            "Mereka mungkin bisa mengerti isinya lebih baik."
            jump heist_usb_to_robotika

        "Buang USB drive karena terlalu berisiko.":
            "Aruna menyadari USB drive ini terlalu berbahaya."
            "Memutuskan untuk membuangnya di tempat aman."
            jump heist_usb_disposal

label heist_abandon_secret:
    "Aruna memutuskan untuk tidak menyentuh kotak 'CONFIDENTIAL' itu."
    "Kucing hitam mengeong pelan seolah kecewa."

    menu:
        "Lanjutkan misi ke ruangan kepala sekolah.":
            "Aruna fokus kembali ke tujuan utama—mengambil piala Robotika."
            "Menuju tangga belakang untuk naik ke lantai dua."
            jump heist_staircase_approach

        "Investigasi gudang lebih lanjut sebelum pergi.":
            "Aruna penasaran dengan apa lagi yang ada di gudang ini."
            "Mencari kotak-kotak lain yang mungkin berisi informasi."
            jump heist_warehouse_search

        "Pulang dan ceritakan tentang kotak misterius ini ke orang lain.":
            "Aruna menyadari kotak ini terlalu mencurigakan untuk diabaikan."
            "Memutuskan untuk pulang dan berdiskusi dengan orang lain."
            jump heist_mystery_report

label heist_radio_map:
    "Di dalam gudang, ada peta dengan tanda-tanda merah di seluruh sekolah."
    "Tanda-tanda itu menunjukkan posisi kamera, sensor, dan area patroli."

    menu:
        "Ambil foto peta untuk navigasi yang lebih baik.":
            "Aruna mengambil foto peta dengan HP."
            "Sekarang Aruna punya peta sistem keamanan sekolah yang lengkap."
            jump heist_security_map_acquired

        "Hancurkan peta agar tidak digunakan pihak lain.":
            "Aruna merobek peta itu dan membuangnya."
            "Setidaknya pihak lain tidak bisa menggunakan peta ini."
            jump heist_map_destroyed

        "Biarkan peta dan lanjutkan misi.":
            "Aruna membiarkan peta itu dan melanjutkan misi."
            "Mengingat posisi-posisi penting dari peta itu."
            jump heist_map_memory

label heist_intelligence_gathering:
    "Aruna mencatat frekuensi radio dan beberapa kata kunci yang terdengar."
    "Target dalam jangkauan. Eksekusi rencana B. Tim A posisi masing-masing."

    menu:
        "Gunakan informasi ini untuk menghindari area berbahaya.":
            "Aruna menggunakan informasi radio untuk menghindari area yang mungkin berbahaya."
            "Memilih rute yang lebih aman berdasarkan intel yang didapat."
            jump heist_safe_route

        "Cari tahu lebih banyak tentang 'rencana B' yang disebutkan.":
            "Aruna penasaran dengan apa yang dimaksud dengan 'rencana B'."
            "Mungkin ada cara untuk mencegah eksekusi rencana itu."
            jump heist_plan_b_investigation

        "Fokus ke misi utama dan abaikan intel radio.":
            "Aruna menyadari intel ini terlalu rumit untuk diikuti."
            "Fokus kembali ke misi utama—mengambil piala Robotika."
            jump heist_focus_on_mission

label heist_escape_from_gudang:
    "Aruna berlari menjauh dari gudang secepat mungkin."
    "Tapi terdengar suara langkah kaki mendekat dari arah berlawanan."

    menu:
        "Sembunyi di balik tembok dekat gudang.":
            "Aruna bersembunyi di balik tembok dekat gudang."
            "Langkah kaki itu lewat tanpa menyadari keberadaan Aruna."
            jump heist_gudang_hide_success

        "Lari menuju gerbang sekolah dan keluar.":
            "Aruna berlari menuju gerbang sekolah yang masih terbuka."
            "Berhasil keluar tanpa ketahuan, tapi misi gagal."
            jump heist_escape_success

        "Pura-pura jadi siswa yang baru pulang dari gudang.":
            "Aruna berjalan santai menuju gerbang seolah-olah baru selesai kerja di gudang."
            "Saat bertemu satpam di gerbang, Aruna menjelaskan dengan tenang."
            jump heist_gudang_bluff

label heist_cat_investigation:
    "Beberapa siswa mengaku pernah melihat kucing hitam dengan kerah biru sering berada di area ekskul Robotika."
    "Katanya kucing itu sering membawa 'pesan-pesan' aneh."

    menu:
        "Cari tahu lebih banyak tentang pesan-pesan yang dibawa kucing itu.":
            "Aruna bertanya tentang pesan-pesan yang dibawa kucing itu."
            "Siswa-siswa itu mengaku kadang melihat kucing itu membawa kertas kecil."
            jump heist_cat_messages

        "Cari kucing itu lagi di area ekskul Robotika.":
            "Aruna pergi ke area ekskul Robotika mencari kucing itu."
            "Mungkin kucing itu masih ada di sekitar area itu."
            jump heist_cat_search

        "Anggap ini kebetulan dan fokus ke kampanye.":
            "Aruna menyadari ini mungkin hanya kebetulan."
            "Fokus kembali ke kampanye dan misi-misi lain."
            jump heist_cat_coincidence

label heist_ignore_cat:
    "Aruna memutuskan untuk tidak memusingkan kucing aneh itu."
    "Fokus kembali ke kampanye dan misi-misi lain."

    menu:
        "Lanjutkan ke misi lain yang lebih penting.":
            "Aruna kembali ke peta dan memilih misi lain."
            "Mengabaikan misteri kucing itu sepenuhnya."
            jump end_day_routine

        "Cari NPC lain untuk diapproach hari ini.":
            "Aruna memutuskan untuk mencari NPC lain untuk diajak bicara."
            "Mungkin ada yang bisa memberikan dukungan penting."
            jump map_navigation

        "Pulang dan istirahat untuk hari ini.":
            "Aruna merasa lelah setelah malam yang mencurigakan."
            "Memutuskan untuk pulang dan istirahat."
            jump end_day_routine

label heist_cat_connection:
    "Reaksi Juan dan Faizal mengejutkan—mereka saling berpandangan dengan ketakutan."
    "Mereka jelas-jelah menyembunyikan sesuatu tentang kucing itu."

    menu:
        "Tekan Juan dan Faizal untuk menjelaskan tentang kucing itu.":
            ar "Lo kenapa takut? Ada apa dengan kucing itu?"
            juan "Kucing itu... kucing itu pembawa pesan dari Pak Kepsek."
            faizal "Dia paksa kami buat kerjain hal-hal yang nggak bener lewat kucing itu."
            jump heist_cat_messenger_revelation

        "Biarkan mereka menyembunyikan rahasia mereka.":
            "Aruna menyadari Juan dan Faizal tidak siap untuk membuka diri."
            "Membiarkan mereka menyembunyikan rahasia mereka untuk sekarang."
            jump heist_cat_secret_kept

        "Tawarkan bantuan untuk mengatasi masalah dengan kucing itu.":
            ar "Kalau kucing itu jadi masalah, gue bisa bantu."
            juan "Lo nggak bisa bantu. Ini udah terlalu jauh."
            faizal "Terima kasih, tapi ini urusan internal Robotika."
            jump heist_cat_help_refused

label heist_master_key_access:
    "Kunci master itu cocok dengan semua pintu di lantai dua."
    "Aruna sekarang punya akses langsung ke ruangan kepala sekolah."

    menu:
        "Langsung menuju ruangan kepala sekolah.":
            "Aruna menggunakan kunci master untuk membuka ruangan kepala sekolah."
            "Berhasil masuk tanpa insiden."
            jump heist_principal_office_entry

        "Cek ruangan lain dulu untuk melihat apa yang ada di dalamnya.":
            "Aruna penasaran dengan apa yang ada di ruangan lain di lantai dua."
            "Membuka beberapa ruangan lain dengan kunci master."
            jump heist_other_rooms_exploration

        "Simpan kunci master untuk penggunaan masa depan.":
            "Aruna menyimpan kunci master di saku untuk penggunaan masa depan."
            "Memutuskan untuk tidak menggunakannya malam ini."
            jump heist_key_hoarding

label heist_honest_choice:
    "Aruna menyadari mengambil kunci ini adalah tindakan kriminal serius."
    "Memutuskan untuk mengembalikannya ke tempat yang semestinya."

    menu:
        "Kembalikan kunci ke kantor satpam.":
            "Aruna pergi ke kantor satpam dan mengembalikan kunci itu."
            "Berharap Pak Budi tidak menyadari kuncinya pernah hilang."
            jump heist_key_returned

        "Cari Pak Budi dan mengembalikan kunci langsung kepadanya.":
            "Aruna mencari Pak Budi untuk mengembalikan kunci langsung."
            "Menemukan Pak Budi sedang duduk di taman dengan wajah sedih."
            jump heist_budi_key_return

        "Tinggalkan kunci di tempat yang aman dan beri tahu Pak Budi.":
            "Aruna meninggalkan kunci di tempat yang aman dan akan memberi tahu Pak Budi besok."
            "Merasa ini cara terbaik untuk mengembalikan kunci tanpa ketahuan."
            jump heist_key_safe_return

label heist_key_hoarding:
    "Aruna menyimpan kunci master di saku, merasa ini bisa berguna nanti."
    "Tapi perasaan bersalah mulai menggerogoti."

    menu:
        "Gunakan kunci master untuk misi malam ini.":
            "Aruna memutuskan untuk menggunakan kunci master malam ini."
            "Menuju ruangan kepala sekolah dengan kunci itu."
            jump heist_master_key_usage

        "Simpan kunci master untuk penggunaan masa depan.":
            "Aruna menyimpan kunci master untuk masa depan."
            "Malam ini bukan waktu yang tepat untuk menggunakannya."
            jump heist_key_future_use

        "Kembalikan kunci master besok pagi.":
            "Aruna menyadari tidak etis menyimpan kunci ini."
            "Memutuskan untuk mengembalikannya besok pagi."
            jump heist_key_tomorrow_return

label heist_budi_alarmed:
    "Pak Budi terkejut, hampir jatuh saat melihat Aruna."

    pak_budi "Aruna? Lo... lo tidak boleh di sini!"
    pak_budi "Ini... ini bukan tempat untuk anak seusia lo!"

    menu:
        "Tanyakan Pak Budi apa yang sedang dia lakukan di sana.":
            ar "Pak, lo lagi ngapain? Kenapa berdoa di depan pintu ruang kepala sekolah?"
            pak_budi "Gue... gue cuma minta maaf. Untuk semua yang terpaksa gue lakukan."
            jump heist_budi_confession

        "Tawarkan bantuan kepada Pak Budi yang jelas-jelah dalam masalah.":
            ar "Pak, lo jelas ada masalah. Biar gue bantu."
            pak_budi "Gue nggak bisa dibantu! Masalah gue terlalu besar!"
            jump heist_budi_despair

        "Minta Pak Budi untuk tidak memberitahu siapa pun tentang kejadian ini.":
            ar "Pak, tolong jangan kasih tau siapa-siapa soal gue malam ini."
            pak_budi "Gue nggak akan lapor. Tapi lo harus janji satu hal."
            jump heist_budi_promise

label heist_door_opens:
    "Pintu ruangan kepala sekolah terbuka dengan kunci yang jatuh dari saku Pak Budi."
    "Aruna berdiri di ambang pintu, siap memasuki ruangan kepala sekolah."

    menu:
        "Masuk dan cari piala Robotika.":
            "Aruna masuk ke ruangan kepala sekolah."
            "Mencari piala Robotika di antara perabotan kantor."
            jump heist_office_search

        "Cek apakah ada bahaya lain di dalam ruangan.":
            "Aruna berhati-hati mengecek sekeliling ruangan sebelum masuk."
            "Memastikan tidak ada jebakan atau orang lain di dalam."
            jump heist_room_safety_check

        "Tunggu sampai yakin aman sebelum masuk.":
            "Aruna menunggu di luar pintu selama beberapa menit."
            "Memastikan tidak ada yang akan datang."
            jump heist cautious_entry

label heist_moral_dilemma_recording:
    "Aruna mengambil HP dan merekam bisikan Pak Budi."
    "'Ampunilah... ampunilah dosa-dosa yang terpaksa gue lakukan...'"

    menu:
        "Simpan rekaman sebagai bukti untuk masa depan.":
            "Aruna menyimpan rekaman itu di HP."
            "Ini bisa menjadi bukti penting jika ada sesuatu yang salah di sekolah ini."
            jump heist_recording_saved

        "Hapus rekaman karena merasa bersalah.":
            "Aruna menyadari merekam seseorang dalam momen pribadi adalah salah."
            "Menghapus rekaman itu segera."
            jump heist_recording_deleted

        "Tunjukkan rekaman kepada Pak Budi dan minta penjelasan.":
            "Aruna memutuskan untuk menunjukkan rekaman kepada Pak Budi."
            "Meminta penjelasan tentang apa yang sedang dia lakukan."
            jump heist_recording_confrontation

label heist_juan_moral_justification:
    "Juan menjelaskan alasannya mencuri kunci satpam."

    juan "Gue biasanya orang yang nurutin aturan. Tapi kalau aturan udah nggak adil, gue nggak bisa nurut terus."
    juan "Tim Robotika butuh piala itu. Dan butuh data yang disita Pak Kepsek."

    menu:
        "Setuju dengan justifikasi moral Juan.":
            ar "Lo bener, Juan. Kalau aturan nggak adil, kita wajib ngelawan."
            juan "Makasih, Aruna. Gue seneng lo ngerti."
            jump heist_moral_agreement

        "Tanyakan apakah ada cara legal untuk mengatasi masalah ini.":
            ar "Tapi nggak ada cara legal nggak? Lo mustahil coba semua cara legal dulu?"
            juan "Gue udah coba! Satu bulan gue udah coba cara legal!"
            jump heist_legal_exhausted

        "Waspadai bahwa Juan mungkin terlalu impulsif.":
            "Aruna mulai merasa Juan mungkin terlalu impulsif dalam keputusannya."
            "Perlu berhati-hati dalam bekerja sama dengannya."
            jump heist_juan_caution

label heist_alternate_strategy:
    "Aruna memutuskan untuk menggunakan jalan lain selain tangga belakang."

    menu:
        "Coba masuk lewat jendela lab di lantai satu.":
            "Aruna mempertimbangkan untuk masuk lewat jendela lab Kimia."
            "Mungkin bisa naik ke lantai dua lewat tangga dalam lab."
            jump heist_lab_window_entry

        "Cari jalan masuk lewat area perpustakaan.":
            "Aruna mempertimbangkan untuk masuk lewat perpustakaan."
            "Perpustakaan punya tangga yang menghubungkan ke lantai dua."
            jump heist_library_entry

        "Gunakan ventilasi untuk masuk ke gedung.":
            "Aruna melihat ada ventilasi besar di dinding samping gedung."
            "Mungkin bisa masuk lewat sana."
            jump heist_ventilation_entry

label heist_solo_ascent:
    "Aruna naik tangga belakang yang gelap dan berkarat sendirian."
    "Setiap langkah terasa lebih berat tanpa bantuan Juan."

    menu:
        "Fokus sepenuhnya ke misi mengambil piala.":
            "Aruna menekan perasaan bersalah dan fokus ke tujuan."
            "Naik ke lantai dua dengan hati-hati."
            jump heist_solo_climb

        "Sesekali berhenti untuk memastikan tidak ada bahaya.":
            "Aruna berhenti beberapa kali untuk mengecek keamanan."
            "Lebih lambat, tapi lebih aman."
            jump heist_cautious_solo_climb

        "Bergerak cepat untuk menyelesaikan misi secepat mungkin.":
            "Aruna bergerak cepat ingin menyelesaikan misi secepat mungkin."
            "Mengambil risiko dengan kecepatan."
            jump heist_risky_solo_climb

label heist_juan_disappeared:
    "Aruna berbalik untuk mencari Juan, tapi dia sudah tidak ada di tempat semula."
    "Hanya kegelapan malam yang menyambut."

    menu:
        "Cari Juan di area sekitar sekolah.":
            "Aruna mencari Juan di area sekitar sekolah."
            "Berteriak memanggil namanya dengan pelan."
            jump heist_juan_search

        "Lanjutkan misi sendirian dan berharap Juan baik-baik saja.":
            "Aruna menyadari Juan mungkin sudah pulang atau bersembunyi."
            "Melanjutkan misi sendirian."
            jump heist_solo_continuation

        "Pulang dan cari Juan besok pagi.":
            "Aruna menyadari terlalu berbahaya mencari Juan di kegelapan."
            "Memutuskan untuk pulang dan mencari Juan besok pagi."
            jump heist_juan_tomorrow

label heist_priority_shift:
    "Aruna mulai berpikir bahwa data Robotika mungkin lebih penting dari sekadar piala."
    "Mengubah arah misi menuju lab Kimia tempat Faizal mungkin berada."

    menu:
        "Menuju lab Kimia untuk mencari Faizal.":
            "Aruna berjalan menuju lab Kimia di lantai satu."
            "Berharap Faizal masih ada di sana."
            jump heist_lab_destination

        "Cari informasi tentang lokasi Faizal dari Juan.":
            "Aruna mempertimbangkan untuk kembali mencari Juan."
            "Mungkin Juan tahu di mana Faizal berada."
            jump heist_juan_information

        "Fokus ke piala dulu, baru data Faizal nanti.":
            "Aruna menyadari sulit menemukan Faizal tanpa informasi."
            "Memutuskan untuk fokus ke piala dulu."
            jump heist_focus_return

label heist_guilty_ascent:
    "Aruna menekan perasaan bersalah dan melanjutkan misi."
    "Tapi setiap langkah terasa lebih berat dari sebelumnya."

    menu:
        "Tetap fokus ke misi meskipun merasa bersalah.":
            "Aruna memaksa diri untuk fokus ke misi."
            "Naik ke lantai dua dengan penuh tekad."
            jump heist_guilty_climb

        "Ambil waktu untuk merenung sebelum melanjutkan.":
            "Aruna berhenti sejenak untuk merenung keputusannya."
            "Mempertimbangkan apakah ini benar-benar jalan yang benar."
            jump heist_moral_reflection

        "Berbalik dan mencari Juan untuk memperbaiki kesalahan.":
            "Aruna tidak tahan dengan perasaan bersalah."
            "Berbalik untuk mencari Juan."
            jump heist_guilty_return

label heist_too_late_to_help:
    "Aruna berlari mengejar Juan, tapi dia sudah hilang dalam kegelapan malam."
    "Hanya suara angin malam yang menyambut."

    menu:
        "Terima bahwa terlambat untuk membantu Juan malam ini.":
            "Aruna menyadari terlambat untuk mengejar Juan malam ini."
            "Memutuskan untuk kembali besok dengan penawaran yang lebih baik."
            jump heist_too_late_acceptance

        "Cari Juan di rumahnya besok pagi.":
            "Aruna mempertimbangkan untuk mencari Juan di rumahnya besok pagi."
            "Mungkin Juan mau berbicara saat tidak berada di sekolah."
            jump heist_juan_home_visit

        "Fokus ke misi lain dan kembali membantu Juan besok.":
            "Aruna menyadari malam ini sudah terlalu emosional."
            "Memutuskan untuk fokus ke misi lain dan kembali besok."
            jump heist_deferred_juan_help

label heist_deferred_help:
    "Aruna memutuskan untuk kembali besok dengan penawaran yang lebih baik."
    "Malam ini terlalu emosional untuk mengambil keputusan yang tepat."

    menu:
        "Pulang dan susun rencana untuk membantu Juan besok.":
            "Aruna menyusun rencana untuk membantu Juan besok."
            "Akan mencari cara yang lebih baik untuk menolong."
            jump heist_tomorrow_juan_plan

        "Fokus ke kampanye dan misi lain untuk hari ini.":
            "Aruna menyadari masih ada misi lain yang penting."
            "Memutuskan untuk fokus ke kampanye dan misi lain."
            jump end_day_routine

        "Istirahat dan kembali besok dengan pikiran yang lebih jernih.":
            "Aruna merasa lelah secara emosional.
            "Memutuskan untuk istirahat dan kembali besok."
            jump end_day_routine

label heist_arrival_principal_office:
    "Aruna sampai di depan ruangan kepala sekolah tanpa insiden."
    "Pintu itu terlihat kokoh, dengan kunci elektronik baru."

    menu:
        "Coba membuka pintu dengan kunci cadangan dari Juan.":
            "Aruna menggunakan kunci cadangan yang diberikan Juan."
            "Kunci itu cocok! Pintu terbuka pelan-pelan."
            jump heist_principal_office_entry

        "Cek apakah ada alarm atau sensor di pintu.":
            "Aruna berhati-hati mengecek sekeliling pintu."
            "Ada sensor kecil di atas pintu yang mungkin terhubung dengan alarm."
            jump heist_sensor_check

        "Cari cara lain untuk masuk ke ruangan.":
            "Aruna melihat ada ventilasi kecil di dinding samping ruangan."
            "Mungkin bisa masuk lewat sana."
            jump heist_ventilation_attempt

label heist_shortcut_risk:
    "Aruna mengambil jalan pintas yang melewati area dengan kamera."
    "Berisiko tinggi, tapi menghemat waktu."

    menu:
        "Bergerak sangat cepat saat kamera berputar ke arah lain.":
            "Aruna bergerak sangat cepat melewati area kamera."
            "Berhasil! Tapi hampir ketahuan saat kamera berputar kembali."
            jump heist_shortcut_success

        "Gunakan peta untuk menemukan celah di coverage kamera.":
            "Aruna menggunakan peta Juan untuk menemukan celah di coverage kamera."
            "Ada area kecil yang tidak tercover kamera."
            jump heist_camera_blind_spot

        "Gunakan kain untuk menutupi kamera sebentar.":
            "Aruna menggunakan kain dari saku untuk menutupi kamera sebentar."
            "Berhasil melewati area tanpa terlihat."
            jump heist_camera_covered

label heist_modified_route:
    "Aruna memodifikasi rute berdasarkan pengetahuan sendiri tentang sekolah."
    "Mengambil jalan yang menurutnya lebih efisien."

    menu:
        "Ikuti rute yang dimodifikasi dengan hati-hati.":
            "Aruna mengikuti rute yang dimodifikasi."
            "Berhasil menghindari beberapa bahaya, tapi menemukan bahaya baru."
            jump heist_modified_route_results

        "Kembali ke rute Juan saat menemukan kesulitan.":
            "Aruna menemukan kesulitan di rute yang dimodifikasi."
            "Memutuskan untuk kembali ke rute Juan."
            jump heist_return_to_juan_route

        "Cari rute alternatif lain yang lebih baik.":
            "Aruna mencari rute alternatif lain yang mungkin lebih baik."
            "Menggabungkan pengetahuan sendiri dengan peta Juan."
            jump heist_hybrid_route

label heist_slow_progress:
    "Aruna bergerak sangat lambat, mengecek setiap sudut sebelum memberi isyarat ke Juan."
    "Prosesnya lambat, tapi lebih aman."

    menu:
        "Lanjutkan dengan kecepatan lambat demi keamanan.":
            "Aruna memutuskan untuk melanjutkan dengan kecepatan lambat."
            "Lebih aman, tapi memakan waktu lebih lama."
            jump heist_slow_progress_continued

        "Percepat sedikit karena Juan mulai tidak sabar.":
            "Aruna mempercepat sedikit untuk mengakomodasi Juan."
            "Berada di tengah antara keamanan dan kecepatan."
            jump heist_medium_pace

        "Berhenti sejenak untuk diskusi ulang strategi.":
            "Aruna berhenti untuk mendiskusikan ulang strategi dengan Juan."
            "Mungkin ada cara yang lebih baik."
            jump heist_strategy_discussion

label heist_juan_stumble:
    "Juan tersandung di tangga yang berkarat, membuat suara keras."
    "Suara itu menggema di dalam gedung yang sunyi."

    menu:
        "Beku di tempat dan berharap tidak ada yang mendengar.":
            "Aruna dan Juan membeku di tempat."
            "Menunggu dengan napas tertahan."
            jump heist_freeze_response

        "Sembunyi segera sebelum orang datang.":
            "Aruna menarik Juan untuk bersembunyi di balik tembok."
            "Menunggu langkah kaki mendekat."
            jump heist_hide_response

        "Berbalik dan turun kembali sebelum ketahuan.":
            "Aruna menyadari terlalu berisiko untuk melanjutkan."
            "Menarik Juan untuk turun kembali."
            jump heist_retreat_from_stumble

label heist_poor_signal:
    "Sinyal HP di dalam gedung sangat lemah."
    "Koneksi Aruna dengan Juan terputus-putus."

    menu:
        "Gunakan kode isyarat manual untuk komunikasi.":
            "Aruna dan Juan setuju untuk menggunakan kode isyarat manual."
            "Cubitan bahu, ketukan kaki, dan gerakan tangan."
            jump heist_manual_signals

        "Pindah ke area dengan sinyal lebih baik.":
            "Aruna mencari area dengan sinyal lebih baik."
            "Menemukan area dekat jendela dengan sinyal yang lebih kuat."
            jump heist_better_signal_area

        "Lanjutkan tanpa komunikasi dan berharap yang terbaik.":
            "Aruna menyadari komunikasi tidak mungkin dilakukan."
            "Melanjutkan tanpa koordinasi dengan Juan."
            jump heist_no_communication

label heist_commitment_to_success:
    "Aruna sepenuhnya berkomitmen untuk membantu Juan."
    "Keduanya bertekad untuk membuat rencana ini berhasil."

    menu:
        "Mulai eksekusi rencana dengan semangat tinggi.":
            "Aruna dan Juan mulai eksekusi rencana dengan semangat tinggi."
            "Bergerak dengan koordinasi yang baik."
            jump heist_execution_start

        "Buat rencana cadangan bersama-sama.":
            "Aruna meyakinkan Juan untuk membuat rencana cadangan."
            "Meskipun Juan ragu, mereka setuju untuk membuat plan B."
            jump heist_plan_b_creation

        "Fokus ke setiap langkah dengan sangat hati-hati.":
            "Aruna dan Juan berfokus ke setiap langkah dengan sangat hati-hati."
            "Meminimalkan risiko kesalahan."
            jump heist_careful_execution

label heist_time_pressure:
    "Juan menatap Aruna dengan putus asa."

    juan "Waktu? Gue nggak punya waktu! Deadline besok pagi!"
    juan "Kalau besok pagi data belum aman, semuanya selesai!"

    menu:
        "Janji akan membantu Juan bekerja semalam ini.":
            ar "Oke, gue bakal bantu lo bekerja semalam ini. Kita selesaikan."
            juan "Lo rela? Ini bakal sangat melelahkan."
            jump heist_all_night_work

        "Cari cara untuk memperpanjang deadline.":
            ar "Gue bakal cari cara buat perpanjang deadline."
            juan "Gimana caranya? Pak Kepsek nggak bisa dinegosiasi!"
            jump heist_deadline_extension

        "Tawarkan solusi alternatif yang lebih cepat.":
            ar "Gue punya ide lain yang lebih cepat. Lo mau denger?"
            juan "Apa ide lo? Cepat cerita!"
            jump heist_alternative_solution

label heist_last_resort:
    "Juan menatap Aruna dengan mata yang menunjukkan keputusasaan total."

    juan "Lo orang terakhir yang gue harapkan, Aruna."
    juan "Kalau lo juga menolak, gue nggak punya harapan lagi."

    menu:
        "Terima tawaran Juan tanpa ragu.":
            ar "Gue bakal bantu lo, Juan. Sampai kapanpun."
            juan "Makasih, Aruna. Lo benar-benar penyelamat."
            jump heist_final_acceptance

        "Tanyakan apakah ada opsi lain yang belum dipertimbangkan.":
            ar "Yakin nggak ada opsi lain yang belum lo pikirin?"
            juan "Gue udah pikirin semuanya selama sebulan! Ini jalan satu-satunya!"
            jump heist_exhausted_options

        "Berikan semangat dan keyakinan kepada Juan.":
            ar "Juan, jangan menyerah. Kita pasti bisa nemu jalan keluar."
            juan "Keyakinan saja nggak cukup, Aruna. Kita butuh aksi nyata."
            jump heist_motivational_speech

label heist_principal_office_entry:
    "Aruna masuk ke ruangan kepala sekolah yang gelap dan sepi."
    "Ruang itu luas, dengan meja kerja besar di tengah dan rak-rak arsip di dinding."

    menu:
        "Cari piala Robotika di rak-rak arsip.":
            "Aruna mulai mencari di rak-rak arsip di dinding."
            "Mungkin piala itu disimpan di sana."
            jump heist_archive_search

        "Cari piala Robotika di laci meja kerja.":
            "Aruna mencari di laci-laci meja kerja kepala sekolah."
            "Meja itu terkunci, tapi Aruna punya kunci."
            jump heist_desk_search

        "Cari piala Robotika di lemari besi di sudut ruangan.":
            "Aruna melihat ada lemari besi kecil di sudut ruangan."
            "Mungkin piala itu disimpan di sana."
            jump heist_safe_search

label heist_principal_office_success:
    "Aruna menemukan piala Robotika di laci meja kerja kepala sekolah!"
    "Piala itu berkilau dalam kegelapan, simbol kebanggaan ekskul Robotika."

    menu:
        "Ambil piala dan segera keluar dari ruangan.":
            "Aruna mengambil piala dengan hati-hati."
            "Segera keluar dari ruangan sebelum ketahuan."
            jump heist_trophy_acquired

        "Cek apakah ada dokumen penting lain di sekitar piala.":
            "Aruna melihat ada beberapa dokumen di sekitar piala."
            "Mungkin ada informasi penting lain."
            jump heist_document_check

        "Ambil foto piala sebagai bukti sebelum mengambilnya.":
            "Aruna mengambil foto piala sebagai bukti."
            "Lalu mengambil piala itu sendiri."
            jump heist_trophy_evidence_taken

label heist_principal_office_failure:
    "Aruna tidak menemukan piala Robotika di mana pun."
    "Ruang itu kosong dari barang-barang berharga yang dicari."

    menu:
        "Cari di ruangan lain di lantai dua.":
            "Aruna menyadari piala mungkin dipindahkan ke ruangan lain."
            "Mencari di ruangan lain di lantai dua."
            jump heist_other_rooms_search

        "Coba mencari petunjuk tentang keberadaan piala.":
            "Aruna mencari catatan atau dokumen yang bisa memberi petunjuk."
            "Mungkin ada informasi tentang di mana piala disimpan."
            jump heist_clue_search

        "Kembali ke Juan untuk meminta informasi lebih.":
            "Aruna menyadari perlu informasi lebih dari Juan."
            "Turun kembali untuk bertanya Juan."
            jump heist_juan_information_request

label heist_trophy_acquired:
    "Aruna berhasil mengambil piala Robotika!"
    "Sekarang saatnya keluar dari sekolah dengan selamat."

    menu:
        "Gunakan rute yang sama untuk keluar.":
            "Aruna menggunakan rute yang sama untuk keluar."
            "Berhati-hati menuruni tangga belakang."
            jump heist_same_route_exit

        "Cari rute alternatif untuk keluar.":
            "Aruna mencari rute alternatif untuk keluar."
            "Menghindari rute yang sama untuk mengurangi risiko."
            jump heist_alternative_exit

        "Kembali ke Juan dan beri tahu keberhasilan.":
            "Aruna kembali ke Juan untuk memberi tahu keberhasilan."
            "Juan pasti akan senang mendengarnya."
            jump heist_juan_success_report

label heist_success_ending:
    "Aruna berhasil keluar dari sekolah dengan piala Robotika!"
    "Dalam perjalanan pulang, Aruna merasa campuran antara lega dan kebanggaan."

    $ robotika_unique_quest_status = "completed"
    $ robotika_daily_bonus_active = True
    "Misi berhasil! Mulai besok, ekskul Robotika akan memberikan +3 Support pasif setiap hari."
    "Tapi Aruna juga menyadari malam ini mengungkapkan banyak misteri di sekolah."
    "Ada konspirasi yang lebih besar yang sedang berlangsung."
    "Untuk sekarang, fokus ke kemenangan kecil ini."

    menu:
        "Kembalikan piala ke ekskul Robotika besok pagi.":
            "Aruna merencanakan untuk mengembalikan piala besok pagi."
            "Ekskul Robotika pasti akan senang."
            jump end_day_routine

        "Simpan piala dulu dan kembalikan nanti.":
            "Aruna menyimpan piala di rumah untuk sementara."
            "Akan mengembalikannya saat waktu yang tepat."
            jump end_day_routine

        "Ceritakan ke Juan tentang apa yang dialami malam ini.":
            "Aruna merencanakan untuk menceritakan semua ke Juan."
            "Juan mungkin tahu lebih banyak tentang misteri ini."
            jump end_day_routine

label heist_failure_ending:
    "Aruna gagal mengambil piala Robotika malam ini."
    "Terlalu banyak rintangan dan bahaya yang tidak terduga."

    $ robotika_unique_quest_status = "pending"
    "Misi gagal hari ini. Kamu bisa mencobanya lagi besok tanpa kehilangan kesempatan."
    "Tapi Aruna menyadari malam ini mengungkapkan banyak hal mencurigakan."
    "Ada sesuatu yang tidak beres di sekolah ini."

    menu:
        "Kembali besok dengan persiapan lebih baik.":
            "Aruna menyusun rencana untuk besok malam."
            "Akan membawa persiapan yang lebih baik."
            jump end_day_routine

        "Cari cara lain untuk membantu Robotika.":
            "Aruna mempertimbangkan cara lain untuk membantu Robotika."
            "Mungkin ada pendekatan yang lebih aman."
            jump end_day_routine

        "Fokus ke kampanye dan misi lain untuk sementara.":
            "Aruna menyadari perlu fokus ke kampanye untuk sementara."
            "Misi Robotika bisa ditunda dulu."
            jump end_day_routine

label end_day_routine:
    "Hari pun berganti malam. Aruna pulang untuk beristirahat."
    $ current_day += 1
    jump main_loop

label evaluate_ending:
    if player_path == "support":
        if total_votes > threshold_flourine and total_votes > threshold_fanya:
            $ ending_id = "terima_kasih_dukungannya"
        elif (threshold_flourine - total_votes) < 5 or (threshold_fanya - total_votes) < 5:
            $ ending_id = "the_winner_takes_it_all"
        elif total_votes > 0:
            $ ending_id = "nice_try_aruna"
        else:
            $ ending_id = "kalah_sebelum_mulai"
    elif player_path == "rival":
        if flourine_resolved == "reported_to_panitia":
            $ ending_id = "kelicikanmu_berakhir"
        elif fanya_resolved == "withdrew_relieved" and flourine_resolved == "flipped_support":
            $ ending_id = "dominasi_mutlak"
        elif fanya_resolved in ["withdrew_relieved", "withdrew_used"] and flourine_resolved == "withdrew":
            $ ending_id = "easy_game"
        elif (fanya_resolved in ["withdrew_relieved", "withdrew_used"] and flourine_resolved == "flipped_support") or (fanya_resolved == "stayed_defiant" and flourine_resolved == "withdrew"):
            $ ending_id = "manipulator_ulung"
        else:
            $ ending_id = "kelicikanmu_berakhir" # Default bad ending if not resolved properly
    else:
        $ ending_id = "kalah_sebelum_mulai"

    jump show_ending

label show_ending:
    scene expression Transform("images/bg_aula.jpg", size=(1920, 1080))
    
    if ending_id == "terima_kasih_dukungannya":
        "Papan tulis di aula utama dipenuhi oleh garis kapur yang menyilang namamu."
        "Satu demi satu, perwakilan kelas membacakan suara mereka."
        "Sorak-sorai meledak. Kamu tidak hanya menang, kamu mendominasi."
        "Segala peluh, janji, dan kompromi yang kamu buat selama 15 hari ini terbayar lunas."
        ar "Kita berhasil."
        "ENDING 1/10: Terima Kasih Atas Dukungannya!"
        "Aruna meraih kemenangan mutlak di jalur Support."

    elif ending_id == "the_winner_takes_it_all":
        "Aula mendadak hening ketika perhitungan suara terakhir dibacakan."
        "Angka di bawah namamu hanya terpaut satu atau dua digit dari sang pemenang."
        "Beberapa pendukungmu menangis, yang lain menepuk pundakmu dengan bangga."
        ar "Hanya kurang sedikit lagi..."
        "Kekalahan yang terhormat, namun tetap saja sebuah kekalahan. Dalam politik, tidak ada medali perak."
        "ENDING 2/10: The Winner Takes it All"
        "Aruna kalah tipis setelah perjuangan keras di jalur Support."

    elif ending_id == "nice_try_aruna":
        "Perhitungan suara berjalan cepat, dan namamu tertinggal jauh di belakang."
        "Kamu tersenyum kecut melihat tumpukan kertas suara. Kamu sudah mencoba, tapi pesan kampanyemu gagal menggerakkan hati mayoritas siswa."
        ar "Yah, setidaknya gue udah nyoba."
        "Setidaknya kamu pulang dengan integritas yang masih utuh."
        "ENDING 3/10: Nice Try, Aruna!"
        "Aruna kalah telak, namun mendapatkan pengalaman berharga."

    elif ending_id == "kalah_sebelum_mulai":
        "Saat namamu dipanggil, tidak ada satu pun tepuk tangan yang terdengar."
        "Bahkan kertas suaramu sendiri terasa seperti beban. Kampanyemu layu sebelum berkembang."
        "Sejarah sekolah ini mungkin akan melupakan bahwa kamu pernah mencalonkan diri."
        "ENDING 4/10: Kalah Sebelum Mulai"
        "Aruna tidak mendapatkan dukungan sama sekali."

    elif ending_id == "mungkin_lain_kali":
        "Surat pengunduran dirimu tergeletak di atas meja panitia OSIS."
        "Beberapa orang berbisik, menyayangkan keputusanmu. Yang lain merasa lega."
        ar "Ini bukan pertarungan gue. Belum saatnya."
        "Terkadang, langkah paling berani dalam politik adalah mengetahui kapan harus mundur."
        "ENDING 5/10: Mungkin Lain Kali"
        "Aruna mundur dari pencalonan secara damai di jalur Support."

    elif ending_id == "easy_game":
        "Berita pengunduran diri Fanya dan Flourine menyebar seperti api liar di grup obrolan sekolah."
        "Tidak ada debat, tidak ada pemungutan suara yang menegangkan. Kamu berjalan menuju panggung sendirian."
        "Semua orang menatapmu—sebagian dengan kagum, sebagian dengan ketakutan."
        ar "Mudah sekali."
        "Manipulasimu bekerja dengan sempurna. Tak ada yang berani menghalangi jalanmu."
        "ENDING 6/10: Easy Game"
        "Kemenangan mutlak berkat kelicikan psikologis di jalur Rival."

    elif ending_id == "manipulator_ulung":
        "Satu lawan hancur, satu lawan lagi terpaksa berlutut."
        "Kamu mengatur bidak-bidak di papan catur ini dengan begitu rapi, membiarkan mereka saling serang sementara kamu menikmati hasilnya."
        "Kursi ketua OSIS kini milikmu, dan tidak ada yang tahu seberapa kotor tanganmu."
        "ENDING 7/10: Manipulator Ulung"
        "Menang dengan menyingkirkan satu kandidat dan memanfaatkan yang lain."

    elif ending_id == "kelicikanmu_berakhir":
        "Surat panggilan dari ruang Bimbingan Konseling menghancurkan segalanya."
        "Bukti-bukti manipulasimu, intrikmu, dan rumor yang kamu sebar telah sampai ke tangan panitia OSIS."
        "Bukan hanya pencalonanmu dibatalkan, reputasimu hancur berkeping-keping."
        ar "Sial... gue terlalu gegabah."
        "Dalam permainan kotor ini, yang kalah adalah mereka yang ketahuan."
        "ENDING 8/10: Kelicikanmu Berakhir"
        "Diskualifikasi akibat manuver licik yang terbongkar."

    elif ending_id == "dominasi_mutlak":
        "Ini bukan lagi soal menang atau kalah. Ini soal kekuasaan absolut."
        "Fanya telah mundur, dan Flourine, sang petahana yang angkuh, kini justru berdiri di belakangmu sebagai pendukung."
        "Kamu tidak hanya mengalahkan lawan-lawanmu. kamu menaklukkan mereka."
        ar "Sekolah ini sekarang milikku."
        "ENDING 9/10: Dominasi Mutlak"
        "Kemenangan politis paling menakutkan dan tak terbantahkan."

    elif ending_id == "siapa_dalangnya":
        "Fanya mundur. Flourine mundur. Dan keesokan harinya... kamu ikut menyebarkan surat pengunduran dirimu."
        "Sekolah dilanda kekacauan. Panitia OSIS kebingungan mencari kandidat baru di menit-menit terakhir."
        "Kamu berdiri di sudut koridor, mengamati kepanikan mereka dengan senyum tipis di bibirmu."
        ar "Kadang, melihat semuanya terbakar itu lebih menyenangkan daripada berkuasa."
        "ENDING 10/10: Siapa Dalangnya?!!"
        "Meninggalkan kekacauan epik setelah menghancurkan semua kandidat."

    else:
        "Waktu terus berjalan, dan lembaran sejarah sekolah ini ditutup dengan namamu."
        "ENDING: [ending_id]"
    
    "Terima kasih sudah bermain!"
    return
