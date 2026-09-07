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

default npc_state = {
    "adam": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "adi": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "anggun": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "lulu": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "inez": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "angga": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ferdi": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "juan": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "faizal": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "nayra": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "aulia": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ellisa": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "desti": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "lukman": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "bagus": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "yura": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ayya": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ami": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "cecillia": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None}
}

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
        base = 0
        for key in npc_state:
            base += npc_state[key]["votes_banked"]
        return base + passive_votes

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
        
        if current_location == "gerbang":
            jump loc_gerbang
        elif current_location == "lapangan":
            jump loc_lapangan
        elif current_location == "ekskul":
            jump loc_ekskul
        elif current_location == "lab":
            jump loc_lab
        elif current_location == "perpus":
            jump loc_perpus
        elif current_location == "osis":
            jump loc_osis
        elif current_location == "uks":
            jump loc_uks
        elif current_location == "aula":
            jump loc_aula
        elif current_location == "pramuka":
            jump loc_pramuka
        elif current_location == "heist":
            jump robotika_heist
        elif current_location == "pulang":
            "Aruna memutuskan untuk mengakhiri harinya dan pulang ke rumah."
            jump end_day_routine
        elif current_location == "mundur":
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
    $ npc_state["adam"]["relationship_quality"] += adam_meter
    $ npc_state["adam"]["quest_status"] = "completed"
    $ npc_state["adam"]["votes_banked"] = get_votes_from_relationship(npc_state["adam"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    
    "Quest Adam selesai! Akumulasi Support: [adam_meter]."
    "Kamu mendapatkan [npc_state['adam']['votes_banked']] vote dari ekskul Jurnalistik."
    jump end_day_routine


label robotika_heist:
    scene expression Transform("images/bg_osis.jpg", size=(1920, 1080))
    "Malam harinya, Aruna menyelinap ke sekolah untuk merebut kembali piala ekskul Robotika dari ruang kepala sekolah."
    "Aruna harus berhati-hati menghindari satpam yang sedang patroli."

    menu:
        "Tunggu sampai satpam lewat, lalu menyusup ke ruangan.":
            "Aruna menunggu dengan sabar di balik tembok..."
            "Satpam lewat tanpa menyadari keberadaannya. Aruna berhasil masuk dan mengambil piala tersebut!"
            $ robotika_unique_quest_status = "completed"
            $ robotika_daily_bonus_active = True
            "Misi berhasil! Mulai besok, ekskul Robotika akan memberikan +3 Support pasif setiap hari."
            jump end_day_routine
            
        "Lari cepat mumpung satpam lengah!":
            "Aruna berlari secepat mungkin ke arah ruangan..."
            "PRUITTT!! Satpam menyadari bayangan Aruna."
            "Aruna terpaksa kabur dan pulang sebelum tertangkap."
            $ robotika_unique_quest_status = "pending"
            "Misi gagal hari ini. Kamu bisa mencobanya lagi besok tanpa kehilangan kesempatan."
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
