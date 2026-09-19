define adi = Character('Adi', color="#1abc9c")
define ang = Character('Anggun', color="#e67e22")
define lul = Character('Lulu', color="#c0392b")
define inz = Character('Inez', color="#8e44ad")
define aga = Character('Angga', color="#d35400")
define fer = Character('Ferdi', color="#2980b9")

# ============================================================
# QUEST ADI
# ============================================================
label quest_adi:
    $ npc_state["adi"]["quest_status"] = "in_progress"
    $ npc_state["adi"]["approached_day"] = current_day
    $ adi_meter = 0
    
    scene expression Transform("images/bg_ekskul_koridor.jpg", size=(1920, 1080))
    "Kamu menemui Adi di depan perpustakaan. Ia sedang sibuk memeriksa catatan di ponselnya."
    ar "Sibuk banget kelihatannya, Di. Nyari apaan tuh?"
    adi "Eh, Aruna. Biasa, nyusun data buat artikel. Makin ke sini makin pusing."
    ar "Artikel jurnalistik? Gimana progresnya?"
    adi "Lumayan. Sebenarnya gue lagi ngulik latar belakang para kandidat. Termasuk elo."
    adi "Tapi ada satu hal menarik yang gue temuin soal kandidat lain. Cecillia, atau mungkin Fanya."
    
    menu:
        "Oh ya? Info macam apa tuh?":
            $ adi_meter += 1
            adi "Info yang cukup... sensitif. Kalau gue publish, kredibilitas mereka bisa anjlok."
            jump adi_pingpong_1
            
        "Hati-hati, Di. Jangan sampai jadi fitnah.":
            $ adi_meter += 2
            adi "Tenang, sumber gue valid. Cuma masalahnya, dampaknya bakal besar."
            jump adi_pingpong_1

label adi_pingpong_1:
    adi "Gue jujur aja, gue agak ragu. Kalau gue publish, ini bakal nguntungin posisi lo."
    adi "Tapi di sisi lain, gue gak pengen sekolah kita ribut karena berita ini."
    adi "Menurut lo, gue harus apain info ini? Publish atau simpan aja?"
    
    menu:
        "Publish aja. Publik berhak tahu kebenarannya.":
            $ adi_meter += 1
            adi "Berani juga lo. Lo gak takut kena getahnya kalau dituduh yang nyuruh gue?"
            jump adi_path_publish
            
        "Simpan aja. Gak usah main kotor.":
            $ adi_meter += 4
            adi "Gue respek sama jawaban lo. Kampanye bersih, ya?"
            jump adi_path_simpan
            
        "Gimana kalau infonya lo kasih ke gue aja?":
            $ adi_meter += 0
            adi "Hmm. Lo mau pake sendiri? Menarik... tapi berisiko."
            jump adi_path_sendiri

label adi_path_publish:
    ar "Gue gak peduli. Selama itu fakta, itu edukasi buat pemilih."
    adi "Gue ngerti. Tapi reputasi lo bisa dibilang 'menyerang' secara gak langsung."
    menu:
        "Biarin aja. Yang penting kompetisi ini transparan.":
            $ adi_meter += 1
            adi "Oke, kalau itu mau lo. Gue akan proses buat buletin besok."
            jump adi_ending
        "Kalau gitu, tulis anonim atau jangan sebut nama gue.":
            $ adi_meter -= 1
            adi "Ya pasti lah, ini kan artikel gue. Tapi tetep aja, baunya kecium."
            jump adi_ending

label adi_path_simpan:
    ar "Kita tanding secara fair aja. Gak usah jatuhin lawan pake cara gitu."
    adi "Gue seneng denger itu dari kandidat langsung. Banyak yang bakal ambil kesempatan ini."
    menu:
        "Kejujuran itu modal utama buat gue.":
            $ adi_meter += 2
            adi "Gue catet omongan lo. Lo beda dari yang lain."
            jump adi_ending
        "Bukan soal jujur, tapi gue gak mau ada masalah di belakang.":
            $ adi_meter += 1
            adi "Realistis. Gue juga gak mau repot kalau panitia protes."
            jump adi_ending

label adi_path_sendiri:
    ar "Daripada dibikin berita umum, biar gue yang urus secara personal ke orangnya."
    adi "Jadi lo mau konfrontasi langsung? Ini bisa jadi senjata atau boomerang."
    menu:
        "Percayain aja ke gue.":
            $ adi_meter += 0
            adi "Oke. Gue kirim filenya ntar malem. Jangan sampai nyebut nama gue."
            jump adi_ending
        "Cuma buat jaga-jaga kalau dia main kasar duluan.":
            $ adi_meter += 1
            adi "Buat kartu as? Cerdik. Oke, gue kasih infonya."
            jump adi_ending

label adi_ending:
    adi "Sip, obrolan yang mencerahkan. Makasih waktunya, Aruna."
    ar "Sama-sama, Di. Semangat nulisnya."
    
    $ complete_quest("adi", adi_meter)
    
    "Quest Adi selesai. Akumulasi meter: [adi_meter]. Kamu mendapatkan [npc_state['adi']['votes_banked']] vote."
    jump end_day_routine


# ============================================================
# QUEST ANGGUN
# ============================================================
label quest_anggun:
    $ npc_state["anggun"]["quest_status"] = "in_progress"
    $ npc_state["anggun"]["approached_day"] = current_day
    $ anggun_meter = 0
    
    scene expression Transform("images/bg_lapangan_ganti.jpg", size=(1920, 1080))
    "Kamu menemui Anggun di depan ruang ganti setelah latihan karate. Dia tampak mengusap keringat dengan kasar."
    ar "Latihan berat hari ini, Nggun?"
    ang "Biasa aja. Cuma situasinya yang bikin berat."
    ar "Situasi? Ada masalah apa di ekskul?"
    ang "Gue males ngomonginnya, tapi mumpung ada lo... lo kan kenal Lulu."
    
    menu:
        "Iya, kenapa sama Lulu?":
            $ anggun_meter += 1
            ang "Ada ribut internal soal siapa yang bakal gantiin dia jadi ketua tahun depan."
            jump anggun_pingpong_1
            
        "Ketua karate kalian itu? Kenapa, dia galak?":
            $ anggun_meter += 0
            ang "Bukan galaknya. Keputusannya yang bikin gue ngerasa dirugikan."
            jump anggun_pingpong_1

label anggun_pingpong_1:
    ang "Intinya gue ngerasa gak dilibatin padahal gue yang paling lama di sini."
    ang "Tapi gue gak enak mau ngomong langsung ke Lulu. Dia keras kepala."
    ang "Lo bisa bantu bilangin ke dia gak soal ini? Sebagai pihak ketiga?"
    
    menu:
        "Gue bakal bilang ke dia dan bela posisi lo.":
            $ anggun_meter += 4
            ang "Serius? Makasih banget, Aruna. Gue cuma butuh suara gue didengar."
            $ anggun_path_flag = "bela_anggun"
            jump anggun_ending
            
        "Gue coba ngomong, tapi secara netral ya. Biar gak makin panas.":
            $ anggun_meter += 2
            ang "Ya... boleh lah. Asal pesannya nyampe ke dia."
            $ anggun_path_flag = "netral"
            jump anggun_ending
            
        "Waduh, urusan internal karate gue gak berani ikut campur.":
            $ anggun_meter -= 2
            ang "Yah... padahal gue kira lo berani bantu. Yaudah deh gapapa."
            $ anggun_path_flag = "tolak"
            jump anggun_ending

label anggun_ending:
    if anggun_meter > 0:
        ang "Gue ngandelin lo ya, Aruna. Jangan sampai lupa."
        ar "Sip, serahin ke gue."
    else:
        ang "Gue balik duluan ya. Masih mau pendinginan."
        ar "Oke, istirahat yang cukup, Nggun."
        
    $ complete_quest("anggun", anggun_meter)
    
    "Quest Anggun selesai. Akumulasi meter: [anggun_meter]. Kamu mendapatkan [npc_state['anggun']['votes_banked']] vote."
    jump end_day_routine


# ============================================================
# QUEST LULU
# ============================================================
label quest_lulu:
    $ npc_state["lulu"]["quest_status"] = "in_progress"
    $ npc_state["lulu"]["approached_day"] = current_day
    $ lulu_meter = 0
    
    scene expression Transform("images/bg_lapangan_basket.jpg", size=(1920, 1080))
    "Kamu menjumpai Lulu di lapangan basket. Dia sedang meregangkan otot."
    ar "Hei Lu, rajin amat pemanasan di sini."
    lul "Eh, Aruna. Iya nih, sekalian cari udara segar. Di dalem sumpek."
    ar "Sumpek ruangannya atau suasananya?"
    lul "Hah, ketebak banget ya? Iya, suasana di ekskul lagi gak enak."
    
    menu:
        "Soal suksesi ketua tahun depan ya?":
            $ lulu_meter += 1
            lul "Kok lo tau? Pasti ada yang ngadu ke lo."
            jump lulu_pingpong_1
            
        "Kelihatan dari muka lo yang tegang.":
            $ lulu_meter += 0
            lul "Sebenernya ada ketidakpuasan internal. Terutama dari Anggun."
            jump lulu_pingpong_1

label lulu_pingpong_1:
    lul "Gue tau Anggun kecewa, tapi gue sebagai ketua harus milih yang terbaik buat ekskul."
    lul "Gue gak bisa bahas ini langsung ke dia karena takutnya emosi."
    lul "Gue butuh penengah yang gak punya kepentingan. Lo mau bantu?"
    
    menu:
        "Sebenernya gue setuju sama Anggun. Keputusan lo agak memberatkan dia.":
            # Cek ripple effect
            if anggun_path_flag == "bela_anggun":
                $ lulu_meter += 3
                $ npc_state["anggun"]["relationship_quality"] += 1
                lul "Lo belain dia? Berarti lo udah ngobrol... Okelah, gue hargai lo berani bilang langsung."
            else:
                $ lulu_meter += 2
                $ npc_state["anggun"]["relationship_quality"] -= 1
                lul "Lo memihak dia? Padahal lo gatau pertimbangan gue. Tapi gapapa, gue dengerin."
            jump lulu_ending
            
        "Gue bisa bantu cari solusi tengah. Biar kalian sama-sama enak.":
            $ lulu_meter += 2
            lul "Nah, itu yang gue butuh. Solusi win-win tanpa harus ada yang merasa kalah."
            jump lulu_path_netral
            
        "Sori Lu, urusan dapur ekskul orang, gue gak berani nyentuh.":
            $ lulu_meter -= 2
            lul "Sayang banget. Gue kira calon ketua OSIS berani nyelesaiin konflik."
            jump lulu_ending

label lulu_path_netral:
    lul "Kalau menurut lo, jalan tengahnya kayak apa?"
    menu:
        "Bikin uji kelayakan terbuka di depan semua anggota.":
            $ lulu_meter += 2
            lul "Ide bagus. Lebih objektif dan transparan."
            jump lulu_ending
        "Anggun dikasih jabatan lain yang setara di kepengurusan.":
            $ lulu_meter += 1
            lul "Bisa dicoba. Walau gue ragu dia bakal nerima."
            jump lulu_ending

label lulu_ending:
    lul "Makasih udah dengerin curhatan gue, Run. Ini ngurangin beban pikiran gue."
    ar "Sama-sama, Lu. Semoga masalahnya cepet kelar."
    
    $ complete_quest("lulu", lulu_meter)
    
    "Quest Lulu selesai. Akumulasi meter: [lulu_meter]. Kamu mendapatkan [npc_state['lulu']['votes_banked']] vote."
    jump end_day_routine


# ============================================================
# QUEST INEZ
# ============================================================
label quest_inez:
    $ npc_state["inez"]["quest_status"] = "in_progress"
    $ npc_state["inez"]["approached_day"] = current_day
    $ inez_meter = 0
    
    scene expression Transform("images/bg_ekskul_seni.jpg", size=(1920, 1080))
    "Kamu menemukan Inez duduk di pojok koridor sambil mencoret-coret sketchbook-nya dengan kasar."
    ar "Nez? Karya baru?"
    inz "Bukan. Ini karya yang baru aja ditolak sama panitia acara sekolah."
    ar "Ditolak? Kenapa? Gambar lo kan bagus-bagus."
    inz "Katanya 'kurang sesuai tema'. Padahal gue tau itu cuma alasan. Mereka emang gak suka selera gue."
    
    menu:
        "Masa sih? Emang temanya apa?":
            $ inez_meter += 1
            inz "Temanya soal 'Keberagaman', tapi gambar gue dibilang terlalu abstrak."
            jump inez_pingpong_1
            
        "Pasti ada unsur politik panitia tuh.":
            $ inez_meter += 2
            inz "Bener banget! Panitianya deket sama sirkelnya Flourine. Gue curiga ini sengaja."
            jump inez_pingpong_1

label inez_pingpong_1:
    inz "Gue ngerasa gak adil aja. Karya seni diukur dari kedekatan ke panitia."
    inz "Lo bisa tolong lobi mereka gak? Biar karya gue dipertimbangin ulang."
    
    menu:
        "Tentu. Gue bakal lobi mereka habis-habisan. Karya lo berhak mejeng!":
            $ inez_meter += 4
            inz "Wah, serius?! Lo emang the best, Aruna!"
            jump inez_path_lobi
            
        "Gimana kalau kita sedikit modif karyanya biar lebih nyambung ke tema mereka?":
            $ inez_meter += 2
            inz "Dimodif? Berarti gue ngalah sama selera mereka dong?"
            jump inez_path_revisi
            
        "Mending lo terima aja keputusannya, Nez. Daripada ribut panjang.":
            $ inez_meter -= 2
            inz "Kok lo malah nyerah? Kecewa gue."
            jump inez_ending

label inez_path_lobi:
    inz "Tapi lo hati-hati ya, mereka itu cukup ngaruh di OSIS."
    menu:
        "Tenang, gue tau cara ngomong sama mereka.":
            $ inez_meter += 1
            inz "Bagus deh. Gue harap lo gak kena masalah gara-gara gue."
            jump inez_ending
        "Risikonya gue ambil. Keadilan harus ditegakkan.":
            $ inez_meter += 2
            inz "Mantap. Ini baru calon pemimpin."
            jump inez_ending

label inez_path_revisi:
    inz "Tapi seni itu soal ekspresi diri, Run."
    menu:
        "Gue ngerti, tapi kadang kita butuh kompromi dikit buat masuk sistem.":
            $ inez_meter += 1
            inz "Huft... oke deh, ntar gue coba revisi dikit."
            jump inez_ending
        "Kalau lo masukin elemen mereka, setidaknya lo dapet panggungnya dulu.":
            $ inez_meter += 2
            inz "Ada benarnya juga sih. Biar karya gue bisa dilihat banyak orang."
            jump inez_ending

label inez_ending:
    inz "Gue lanjut coret-coret dulu ya. Thanks udah mampir, Run."
    ar "Sama-sama. Semangat terus, Nez."
    
    $ complete_quest("inez", inez_meter)
    
    "Quest Inez selesai. Akumulasi meter: [inez_meter]. Kamu mendapatkan [npc_state['inez']['votes_banked']] vote."
    jump end_day_routine


# ============================================================
# QUEST ANGGA
# ============================================================
label quest_angga:
    $ npc_state["angga"]["quest_status"] = "in_progress"
    $ npc_state["angga"]["approached_day"] = current_day
    $ angga_meter = 0
    
    scene expression Transform("images/bg_pramuka.jpg", size=(1920, 1080))
    "Di markas Pramuka, Angga terlihat sibuk memilah tenda dan perlengkapan outbond."
    ar "Wih, sibuk banget Ngga. Ada acara besar?"
    aga "Eh, Aruna! Iya nih, Persami gabungan bulan depan persiapannya harus dari sekarang."
    ar "Hebat, selalu terorganisir. Ada yang bisa gue bantu?"
    aga "Pas banget lo nanya. Gue lagi pusing soal koordinasi logistik."
    
    menu:
        "Boleh, lo butuh bantuan apa spesifiknya?":
            $ angga_meter += 1
            aga "Hari H acaranya ternyata bentrok sama jadwal kampanye akbar lo."
            jump angga_pingpong_1
            
        "Waduh, kalau urusan logistik berat gue pas deh.":
            $ angga_meter += 0
            aga "Bukan logistik fisiknya, tapi lebih ke koordinasi orang-orangnya pas hari H."
            jump angga_pingpong_1

label angga_pingpong_1:
    aga "Gue tau lo sibuk kampanye. Tapi gue beneran kekurangan kordinator yang bisa diandalkan buat nanganin divisi acara."
    aga "Gue butuh lo turun langsung bantu kita pas acara itu. Gimana?"
    
    menu:
        "Oke, gue bakal full bantu lo seharian. Kampanye bisa gue reschedule.":
            $ angga_meter += 5
            aga "Serius?! Wah, makasih banget Run! Pramuka utang budi besar sama lo."
            "Perhatian: Kamu telah mengorbankan 1 hari kampanye penuh!"
            # $ current_day += 1  # BIsa diadjust sesuai logika main loop
            jump angga_ending
            
        "Gue bantu setengah hari ya? Atau gue bantu dari jauh lewat hp.":
            $ angga_meter += 2
            aga "Setengah hari udah ngebantu banget kok. Sisanya gue yang cover."
            jump angga_ending
            
        "Sorry banget Ngga, hari itu krusial banget buat kampanye gue. Gue gak bisa.":
            $ angga_meter -= 3
            aga "Yah... gue ngerti sih. Emang gak bisa dipaksa."
            jump angga_ending

label angga_ending:
    if angga_meter > 0:
        aga "Gue lanjut nyiapin ini dulu ya. Makasih banyak, Aruna!"
    else:
        aga "Gue harus lanjut kerja nih. Sukses ya kampanyenya."
    ar "Sip, duluan ya Ngga."
    
    $ complete_quest("angga", angga_meter)
    
    "Quest Angga selesai. Akumulasi meter: [angga_meter]. Kamu mendapatkan [npc_state['angga']['votes_banked']] vote."
    jump end_day_routine


# ============================================================
# QUEST FERDI (ROBOTIKA)
# ============================================================
label quest_ferdi:
    $ npc_state["ferdi"]["quest_status"] = "in_progress"
    $ npc_state["ferdi"]["approached_day"] = current_day
    $ ferdi_meter = 0
    
    scene expression Transform("images/bg_lab_robotika.jpg", size=(1920, 1080))
    "Kamu masuk ke Lab Fisika yang disulap jadi markas ekskul Robotika. Ferdi, Juan, dan Faizal tampak mengelilingi robot mereka yang membongkar."
    ar "Halo semuanya! Lagi ngerakit apa nih?"
    fer "Aruna! Ini nih, lagi ngoprek robot line follower buat kompetisi regional bulan depan."
    ar "Keren! Tapi kok pada lemes gitu mukanya?"
    fer "Masalah klasik ekskul kita, Run. Budget."
    
    menu:
        "Kurang komponen ya?":
            $ ferdi_meter += 1
            fer "Bukan cuma kurang, tapi banyak sensor yang udah usang dan butuh diganti."
            jump ferdi_pingpong_1
            
        "Wah, gak dapet dana dari sekolah?":
            $ ferdi_meter += 2
            fer "Proposal udah masuk, tapi cairnya lama banget. Keburu deadline."
            jump ferdi_pingpong_1

label ferdi_pingpong_1:
    fer "Intinya kita butuh dana cair cepet. Lo kan banyak koneksi di OSIS atau mungkin tau celah ke pihak sekolah/sponsor?"
    fer "Bisa bantu nyariin jalan keluarnya gak?"
    
    menu:
        "Tenang, gue bakal pakai koneksi OSIS gue buat cari sponsor/dana kilat.":
            $ ferdi_meter += 4
            fer "Gila, ini yang kita tunggu dari calon ketua! Makasih banyak Run!"
            jump ferdi_path_dana
            
        "Gue gak bisa janjiin dana, tapi gue bisa bantu nyari pinjaman komponen ke lab lain.":
            $ ferdi_meter += 2
            fer "Boleh juga, setidaknya robot kita bisa jalan dulu buat trial."
            jump ferdi_ending
            
        "Aduh Fer, urusan dana agak susah. Gue lagi fokus kampanye nih, gak bisa bantu banyak.":
            $ ferdi_meter -= 2
            fer "Ya... wajar sih. Lo emang sibuk. Kita cari cara lain deh."
            jump ferdi_ending

label ferdi_path_dana:
    fer "Juan, Faizal, denger tuh! Kita dapet backup dari Aruna!"
    juan "Beneran nih? Gak cuma janji manis kampanye kan?"
    menu:
        "Gue kasih bukti, bukan janji.":
            $ ferdi_meter += 1
            juan "Oke, kita pegang omongan lo."
            jump ferdi_ending
        "Kalian bisa pantau progresnya tiap hari.":
            $ ferdi_meter += 2
            faizal "Sip, yang penting kita menang kompetisi ini."
            jump ferdi_ending

label ferdi_ending:
    fer "Makasih udah mampir dan ngobrol, Run. Kita mau lanjut debugging dulu."
    ar "Semangat ya! Semoga robotnya cepet beres."
    
    $ complete_quest("ferdi", ferdi_meter)
    $ complete_quest("juan", ferdi_meter)
    $ complete_quest("faizal", ferdi_meter)
    
    $ robotika_unique_quest_status = "available"
    
    "Quest Ferdi selesai. Akumulasi meter: [ferdi_meter]."
    "Efek berantai: Juan dan Faizal ikut terpengaruh oleh keputusanmu."
    "Kamu mendapatkan tambahan vote dari Ferdi, Juan, dan Faizal. Total vote saat ini: [total_votes]."
    jump end_day_routine
