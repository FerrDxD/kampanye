# Characters Group C
define lk = Character('Lukman', color="#a29bfe")
define bg = Character('Bagus', color="#00cec9")
define yr = Character('Yura', color="#ffeaa7")
define ay = Character('Ayya', color="#fab1a0")
define am = Character('Ami', color="#ff7675")
define cc = Character('Cecillia', color="#fd79a8")
define ar = Character('Aruna', color="#3498db") # In case not carried over

# -------------------------------------------------------------
# QUEST LUKMAN (Zoologi)
# -------------------------------------------------------------
label quest_lukman:
    $ npc_state["lukman"]["quest_status"] = "in_progress"
    $ npc_state["lukman"]["approached_day"] = current_day
    $ lukman_meter = 0
    
    scene expression Transform("images/bg_lab_biologi.jpg", size=(1920, 1080))
    "Kamu berjalan menuju area belakang sekolah tempat lab Zoologi berada."
    "Lukman, sang ketua ekskul, terlihat sedang jongkok mengamati sebuah kandang terrarium besar sambil mencatat sesuatu."
    "Kamu mendekat pelan-pelan agar tidak mengagetkannya."
    
    ar "Sibuk banget, Man? Lagi ngamatin apaan tuh?"
    lk "Eh, Aruna. Ini, iguana kita lagi masa adaptasi suhu baru."
    lk "Udah dua hari gue pusing ngurusin setelan lampunya biar pas."
    ar "Oh pantes, dari kemarin gue liat muka lo agak kusut. Udah mendingan sekarang iguananya?"
    lk "Lumayan sih. Seenggaknya udah mau makan."
    lk "Ngomong-ngomong, ada angin apa calon ketua OSIS mampir ke kandang belakang gini? Pasti bukan cuma mau nanyain iguana kan?"
    
    menu:
        "Tentu aja mau nanyain kabar lo dong.":
            $ lukman_meter += 1
            lk "Haha, bisa aja lo. Tapi gue tau lo lagi sibuk kampanye."
            jump lukman_basa_basi
            
        "Gue lagi keliling nyari dukungan. Dan lo salah satu incaran gue.":
            $ lukman_meter += 2
            lk "Jujur banget. Gue apresiasi itu."
            jump lukman_basa_basi
            
        "Capek gue ngurus kampanye, mending liatin iguana.":
            $ lukman_meter += 1
            lk "Gue paham rasanya. Kadang hewan lebih gampang diurus daripada manusia."
            jump lukman_basa_basi

label lukman_basa_basi:
    lk "Tapi mumpung lo di sini, gue sebenarnya lagi ada masalah yang lumayan bikin pusing."
    lk "Bukan soal iguana, tapi soal birokrasi sekolah."
    ar "Birokrasi gimana maksudnya?"
    lk "Gini, ekskul Zoologi lagi ada proyek observasi besar bulan depan."
    lk "Kita butuh akses khusus ke lab biologi lanjutan di lantai tiga, dan butuh izin bawa beberapa spesimen keluar sekolah buat dipamerin."
    lk "Masalahnya, wakil kepala sekolah bagian sarpras ribet banget mintanya. Harus ada tanda tangan ini itu, persetujuan pembina yang lagi cuti, dan surat rekomendasi OSIS."
    lk "Gue udah bolak-balik ruang guru tiga kali minggu ini dan cuma di-ping-pong."
    
    menu:
        "Gila, ribet banget. Emang birokrasi sekolah kita kadang nggak ngotak.":
            $ lukman_meter += 1
            lk "Nah itu dia! Mereka mikirnya ekskul kita cuma mainan peliharaan doang."
            jump lukman_inti_1
            
        "Mungkin karena resikonya gede bawa spesimen keluar?":
            $ lukman_meter -= 1
            lk "Ya emang ada resiko, tapi kita kan udah ada SOP-nya!"
            jump lukman_inti_1
            
        "Terus, lo mau gue bantu apain?":
            $ lukman_meter += 0
            lk "To the point ya."
            jump lukman_inti_1

label lukman_inti_1:
    lk "Gue tau lo punya koneksi bagus ke beberapa guru, dan lo juga pengurus OSIS."
    lk "Bisa nggak lo bantu gue buka jalur birokrasi ini? Minimal bantuin gue dapetin surat rekomendasi OSIS dan lobi Pak Sarpras biar izinnya keluar minggu ini."
    
    menu:
        "Gue bakal urus penuh sampai izin dan fasilitas lo dapet semua.":
            $ lukman_meter += 3
            lk "Serius? Wah, kalau lo bisa lakuin itu, ekskul Zoologi bakal ngutang budi besar sama lo."
            jump lukman_full_bantu
            
        "Gue bisa kasih saran dan template suratnya, tapi lo tetep harus maju sendiri.":
            $ lukman_meter += 1
            lk "Hm, gue butuhnya lebih dari sekadar saran sih sebenernya..."
            jump lukman_setengah_bantu
            
        "Maaf Man, urusan birokrasi lagi sensitif sekarang. Gue nggak bisa bantu.":
            $ lukman_meter -= 2
            lk "Yah, sayang banget."
            jump lukman_nolak

label lukman_full_bantu:
    ar "Gue bakal temenin lo ke ruang guru, dan gue yang bakal ngomong sama Wakasek Sarpras."
    ar "Gue juga bakal teken surat rekomendasi OSIS-nya pake wewenang gue sekarang."
    lk "Gila, lo berani ngambil resiko itu? Kalau Wakasek tau lo pake ini buat kampanye, lo bisa kena tegur loh."
    
    menu:
        "Ini bukan buat kampanye, ini karena gue peduli sama ekskul sekolah.":
            $ lukman_meter += 2
            lk "Kata-kata manis seorang politisi. Tapi gue pegang janji lo."
            jump lukman_end
            
        "Resiko itu urusan belakangan. Yang penting pameran lo jalan.":
            $ lukman_meter += 3
            lk "Gue bener-bener gak nyangka lo senekat ini buat bantu. Thanks, Aruna."
            jump lukman_end
            
        "Biarin aja. Kalau gue kepilih jadi ketua, masalah ginian bakal gue pangkas habis.":
            $ lukman_meter += 2
            lk "Wah, janji kampanye nih? Boleh juga."
            jump lukman_end

label lukman_setengah_bantu:
    ar "Gue bisa bantu siapin draf surat rekomendasi yang dijamin tembus, dan ngasih tau lo celah ngomong ke Pak Sarpras."
    ar "Tapi lo harus tetep ngadep beliau sendiri."
    lk "Gitu ya... Gue sebenernya agak ciut kalau disuruh ngadep beliau sendirian lagi."
    
    menu:
        "Lo harus berani, Man. Lo kan ketuanya.":
            $ lukman_meter += 1
            lk "Iya sih. Lo bener. Gue ketua, gue harus berani tanggung jawab."
            jump lukman_end
            
        "Gue bakal temenin di luar ruangan, jadi lo tenang aja.":
            $ lukman_meter += 2
            lk "Oke deh. Kalau ada lo di luar seenggaknya gue gak grogi-grogi amat."
            jump lukman_end
            
        "Gue jamin draft dari gue bakal langsung ditanda tangan.":
            $ lukman_meter += 0
            lk "Semoga aja ya."
            jump lukman_end

label lukman_nolak:
    ar "Kalau gue maksa masuk sekarang, nanti disangka gue mainin kekuasaan OSIS buat nyari suara doang."
    lk "Ya gue ngerti sih posisi lo. Cuma agak kecewa aja."
    lk "Berarti gue harus mikir cara lain."
    jump lukman_end

label lukman_end:
    "Obrolan kalian pun berakhir setelah menyepakati langkah selanjutnya."
    $ npc_state["lukman"]["relationship_quality"] += lukman_meter
    $ npc_state["lukman"]["quest_status"] = "completed"
    $ npc_state["lukman"]["votes_banked"] = get_votes_from_relationship(npc_state["lukman"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Lukman selesai. Kamu mendapatkan [npc_state['lukman']['votes_banked']] vote."
    jump end_day_routine


# -------------------------------------------------------------
# QUEST BAGUS (Pustakawan)
# -------------------------------------------------------------
label quest_bagus:
    $ npc_state["bagus"]["quest_status"] = "in_progress"
    $ npc_state["bagus"]["approached_day"] = current_day
    $ bagus_meter = 0
    
    scene expression Transform("images/bg_perpus_meja.jpg", size=(1920, 1080))
    "Suasana perpustakaan selalu sepi setelah jam pelajaran selesai."
    "Hanya ada suara ketikan keyboard yang sayup-sayup terdengar dari meja penjaga perpustakaan."
    "Bagus sedang merapikan setumpuk arsip sekolah yang sudah mulai menguning."
    
    ar "Sore, Gus. Belum balik lo?"
    bg "Oh, Aruna. Belum. Masih ada sisa inventaris arsip tahun lalu yang belum masuk database."
    ar "Rajin banget. Perpus emang gak ada lo bisa berantakan kali ya."
    bg "Bisa aja lo. Duduk sini, nafas dulu. Lo keliatan capek banget habis keliling nyari suara."
    
    menu:
        "Emang capek banget, Gus. Politik sekolah tuh nguras energi.":
            $ bagus_meter += 2
            bg "Gue paham. Lo harus senyum ke semua orang tiap hari."
            jump bagus_basa_basi
            
        "Biasa aja sih, masih semangat 45!":
            $ bagus_meter += 1
            bg "Haha, semangat yang bagus buat calon pemimpin."
            jump bagus_basa_basi
            
        "Kelihatan banget ya muka gue kucel?":
            $ bagus_meter += 1
            bg "Gak kucel sih, cuma kayak orang kurang tidur aja tiga hari."
            jump bagus_basa_basi

label bagus_basa_basi:
    bg "Gue ngamatin kampanye lo akhir-akhir ini."
    bg "Lo narik banyak perhatian, tapi saingan lo, Flourine dan Fanya, juga gak main-main."
    bg "Gue kepikiran satu hal."
    ar "Apa tuh?"
    bg "Gue pustakawan di sini udah dua tahun. Gue punya akses ke arsip lama sekolah..."
    bg "...termasuk riwayat organisasi, laporan pertanggungjawaban yang nggak pernah dipublish, dan catatan pelanggaran disiplin."
    bg "Beberapa dari dokumen itu ngandung info sensitif soal kandidat-kandidat lain, dan sejarah kampanye mereka."
    
    menu:
        "Tunggu, lo punya data rahasia kandidat lain?":
            $ bagus_meter += 1
            bg "Bukan rahasia kalau lo tau di mana nyarinya."
            jump bagus_inti_1
            
        "Lo mau nawarin gue buat make data itu?":
            $ bagus_meter += 2
            bg "Ketebak banget ya arah pembicaraan gue?"
            jump bagus_inti_1
            
        "Gue rasa gue tau arah pembicaraan ini, dan gue kurang suka.":
            $ bagus_meter -= 1
            bg "Dengerin dulu aja."
            jump bagus_inti_1

label bagus_inti_1:
    bg "Gue mau nawarin bantuan. Lo mau gue carikan referensi atau preseden dari pemilihan sebelumnya?"
    bg "Mungkin ada skandal lama yang ditutupi, atau celah di laporan mereka yang bisa lo pakai buat 'amunisi'."
    bg "Gue tau lo main bersih sejauh ini, tapi di dunia politik, informasi adalah senjata terkuat."
    
    menu:
        "Gue terima. Tolong cariin data itu buat gue.":
            $ bagus_meter += 4
            bg "Pilihan yang realistis."
            jump bagus_terima_strategis
            
        "Gue mau liat datanya, tapi murni cuma buat wawasan gue aja.":
            $ bagus_meter += 2
            bg "Cuma buat wawasan? Lo yakin bisa nahan diri buat gak makai itu pas lagi kepepet?"
            jump bagus_terima_wawasan
            
        "Gue gak butuh cara kotor kayak gitu. Simpen aja arsipnya.":
            $ bagus_meter += 0
            bg "Integritas. Menarik."
            jump bagus_tolak

label bagus_terima_strategis:
    ar "Kalau gue mau menang, gue harus siap dengan segala amunisi. Kalau mereka main kotor duluan, gue udah punya kartu as."
    bg "Gue suka cara berpikir lo. Gak naif."
    bg "Gue udah tandain beberapa dokumen yang berkaitan sama Flourine. Kasus dana acara tahun lalu yang lenyap tanpa jejak."
    
    menu:
        "Wow. Ini bisa langsung ngancurin reputasi dia.":
            $ bagus_meter += 1
            bg "Gunakan dengan bijak, Aruna."
            jump bagus_end
            
        "Gue bakal simpen ini. Kita keluarin saat momennya tepat.":
            $ bagus_meter += 2
            bg "Timing adalah segalanya. Gue tunggu aksi lo."
            jump bagus_end
            
        "Jangan cuma Flourine, cari juga buat Fanya.":
            $ bagus_meter += 2
            bg "Gue udah duga lo bakal minta itu. Gue lagi nyari celahnya Fanya sekarang."
            jump bagus_end

label bagus_terima_wawasan:
    ar "Gue mau tau apa yang sebenernya terjadi di OSIS tahun-tahun lalu, supaya gue gak ngulangin kesalahan yang sama."
    ar "Tapi gue janji, gue gak akan make info personal buat nyerang mereka di publik."
    bg "Itu komitmen yang berat, Aruna."
    
    menu:
        "Gue komitmen. Gue pengen menang terhormat.":
            $ bagus_meter += 1
            bg "Baiklah. Gue harap lo beneran bisa nepatin omongan lo."
            jump bagus_end
            
        "Kalau mereka nyerang gue duluan, mungkin janji itu batal.":
            $ bagus_meter += 1
            bg "Haha. Fleksibel ya. Oke, gue ngerti."
            jump bagus_end
            
        "Pokoknya lo kumpulin aja dulu datanya.":
            $ bagus_meter += 0
            bg "Sip. Besok gue kasih ringkasannya."
            jump bagus_end

label bagus_tolak:
    ar "Gue gak mau menang dengan cara ngejatuhin orang lain pakai aib mereka."
    ar "Kalau kampanye gue kuat, gue gak perlu taktik kotor."
    bg "Gue hargai pilihan lo, Aruna. Lo punya prinsip yang kuat."
    bg "Meski jujur, menurut gue lo lagi ngilangin kesempatan besar."
    jump bagus_end

label bagus_end:
    "Kamu dan Bagus menghabiskan sisa sore itu mendiskusikan sejarah organisasi di sekolah."
    $ npc_state["bagus"]["relationship_quality"] += bagus_meter
    $ npc_state["bagus"]["quest_status"] = "completed"
    $ npc_state["bagus"]["votes_banked"] = get_votes_from_relationship(npc_state["bagus"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Bagus selesai. Kamu mendapatkan [npc_state['bagus']['votes_banked']] vote."
    jump end_day_routine


# -------------------------------------------------------------
# QUEST YURA (Jurnalistik)
# -------------------------------------------------------------
label quest_yura:
    $ npc_state["yura"]["quest_status"] = "in_progress"
    $ npc_state["yura"]["approached_day"] = current_day
    $ yura_meter = 0
    
    scene expression Transform("images/bg_ekskul_jurnalistik.jpg", size=(1920, 1080))
    "Kamu melihat Yura sedang duduk di taman belakang sekolah, mencoret-coret bukunya dengan gelisah."
    "Sebagai anggota ekskul Jurnalistik, biasanya dia lebih sibuk keliling dengan kameranya."
    
    ar "Yura? Ngelamun aja. Ada masalah apa?"
    yr "Eh, Kak Aruna. Enggak, ini... lagi mikirin draft liputan doang."
    ar "Liputan soal pemilihan OSIS?"
    yr "Iya... Adam sama Ami lagi semangat banget ngulik profil kandidat, tapi gue kedapet jatah nulis opini redaksi."
    
    menu:
        "Opini redaksi tuh keren. Suara lo bisa didenger seluruh sekolah.":
            $ yura_meter += 2
            yr "Masalahnya itu kak, suaranya mungkin terlalu... kenceng."
            jump yura_basa_basi
            
        "Pasti berat ya nulis opini pas lagi musim kampanye gini?":
            $ yura_meter += 2
            yr "Banget, kak. Penuh tekanan dari sana-sini."
            jump yura_basa_basi
            
        "Mau gue bantu ngasih ide?":
            $ yura_meter += 1
            yr "Bukan masalah ide, kak. Idenya udah ada, cuma..."
            jump yura_basa_basi

label yura_basa_basi:
    yr "Gue punya ide liputan soal 'Fasilitas VIP di Sekolah'."
    yr "Banyak kandidat—termasuk petahana—sering pakai fasilitas sekolah yang gak bisa dipakai siswa biasa untuk kepentingan kelompok mereka sendiri."
    yr "Ini isu yang udah lama jadi rahasia umum, tapi gak ada yang berani nulis."
    yr "Gue ngerasa ini penting banget buat diangkat, biar semua siswa tau kenyataannya sebelum milih."
    yr "Tapi jujur... gue takut. Isu ini terlalu kontroversial."
    
    menu:
        "Kalau lo tulis ini, bakal banyak pihak atas yang marah ke Jurnalistik.":
            $ yura_meter += 0
            yr "Itu yang gue takutin..."
            jump yura_inti_1
            
        "Ini berita besar, Yur. Lo bisa ngebuka mata semua orang!":
            $ yura_meter += 2
            yr "Iya kan? Tapi resikonya juga besar banget buat gue personal."
            jump yura_inti_1
            
        "Kenapa lo ragu?":
            $ yura_meter += 1
            yr "Gue ragu soalnya dampaknya bisa ngerembet ke mana-mana."
            jump yura_inti_1

label yura_inti_1:
    yr "Menurut lo gimana, Kak Aruna?"
    yr "Sebagai salah satu kandidat... apa menurut lo gue harus tetep angkat isu ini walau berisiko? Atau mending gue cari isu yang main aman aja?"
    
    menu:
        "Lo harus berani angkat isu itu. Suarakan kebenarannya.":
            $ yura_meter += 4
            yr "Lo serius dukung gue? Padahal ini bisa aja nyerang reputasi orang-orang di sekitar lo juga."
            jump yura_dorong_berani
            
        "Mending lo pake pendekatan yang lebih hati-hati. Jangan langsung nge-gas.":
            $ yura_meter += 2
            yr "Pendekatan hati-hati? Maksudnya bahas dari kulit luarnya aja gitu?"
            jump yura_hati_hati
            
        "Gak usah diangkat, Yur. Resikonya gak sepadan. Main aman aja.":
            $ yura_meter -= 2
            yr "Gitu ya... Jadi ide gue emang mending dibuang ke tong sampah."
            jump yura_aman

label yura_dorong_berani:
    ar "Pers sekolah itu pilar transparansi. Kalau kalian gak berani, siapa lagi yang bakal negur mereka?"
    ar "Gue bakal back-up tulisan lo. Kalau ada yang berani intimidasi ekskul lo, sebut nama gue."
    yr "Wah... Kak Aruna bener-bener beda dari bayangan gue."
    
    menu:
        "Gue serius. Kita butuh perubahan radikal di sekolah ini.":
            $ yura_meter += 2
            yr "Oke! Gue bakal ketik draftnya malam ini juga!"
            jump yura_end
            
        "Tapi inget, lo harus siap sama segala serangannya nanti.":
            $ yura_meter += 2
            yr "Gue siap, Kak. Selama ada yang dukung di belakang."
            jump yura_end
            
        "Sebenernya gue cuma pengen liat mereka panik sih.":
            $ yura_meter -= 1
            yr "Haha, jahat juga ya. Tapi makasih dorongannya."
            jump yura_end

label yura_hati_hati:
    ar "Lo bisa angkat isunya, tapi jangan sebut nama atau nunjuk hidung."
    ar "Bahas soal pentingnya kesetaraan fasilitas secara umum. Biar siswa yang mikir sendiri."
    yr "Jadi semacam sindiran halus ya? Gak akan bikin meledak, tapi tetap ngasih pesan."
    
    menu:
        "Tepat. Kritik yang baik adalah kritik yang bisa bikin orang mikir.":
            $ yura_meter += 2
            yr "Gue ngerti sekarang. Ini jauh lebih aman."
            jump yura_end
            
        "Yang penting lo gak kena masalah sama petinggi sekolah.":
            $ yura_meter += 1
            yr "Iya, gue setuju. Gue gak mau Jurnalistik kena bredel."
            jump yura_end
            
        "Lebih elegan gitu, daripada kesannya kayak akun gosip.":
            $ yura_meter += 1
            yr "Bener juga. Sip deh, gue bakal revisi arah tulisannya."
            jump yura_end

label yura_aman:
    ar "Mending cari isu soal visi misi biasa aja. Lo gak perlu nyari musuh pas masa kritis gini."
    yr "Gue paham maksud Kak Aruna... Ya udahlah, mungkin emang belum saatnya pahlawan-pahlawanan."
    jump yura_end

label yura_end:
    "Yura menutup bukunya dan mengangguk pelan padamu."
    $ npc_state["yura"]["relationship_quality"] += yura_meter
    $ npc_state["yura"]["quest_status"] = "completed"
    $ npc_state["yura"]["votes_banked"] = get_votes_from_relationship(npc_state["yura"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Yura selesai. Kamu mendapatkan [npc_state['yura']['votes_banked']] vote."
    jump end_day_routine


# -------------------------------------------------------------
# QUEST AYYA (FPSH)
# -------------------------------------------------------------
label quest_ayya:
    $ npc_state["ayya"]["quest_status"] = "in_progress"
    $ npc_state["ayya"]["approached_day"] = current_day
    $ ayya_meter = 0
    
    scene expression Transform("images/bg_aula.jpg", size=(1920, 1080))
    "Di sebuah ruang kelas yang kosong, Ayya, sang ketua Forum Pemuda Sadar Hukum (FPSH) sekolah, tampak serius membaca setumpuk kertas fotokopian."
    "Itu adalah buku panduan tata tertib dan AD/ART OSIS sekolah."
    
    ar "Rajin banget, Ay. Nyari celah hukum buat ngehukum siapa nih hari ini?"
    ay "Aruna. Kebetulan banget lo ke sini. Sini duduk."
    ay "Gue bukan mau ngehukum orang, gue lagi meriksa legalitas proses pemilihan OSIS tahun ini."
    
    menu:
        "Legalitas? Emang ada yang salah sama pemilihannya?":
            $ ayya_meter += 1
            ay "Banyak yang salah, dan gue baru sadar setelah gue baca detail aturannya."
            jump ayya_basa_basi
            
        "Kayaknya lo mikir terlalu jauh deh. Ini cuma OSIS, bukan pemilu negara.":
            $ ayya_meter -= 2
            ay "Cuma OSIS? Justru karena dari kecil kita biarin hal 'kecil' cacat aturan, gedenya pada korup."
            jump ayya_basa_basi
            
        "Gue tertarik. Cacat di bagian mana?":
            $ ayya_meter += 2
            ay "Bagus lo nanya gitu. Gue jelasin."
            jump ayya_basa_basi

label ayya_basa_basi:
    ay "Liat pasal 14 ayat 2 di sini. 'Kandidat petahana tidak wajib melepaskan jabatan kepanitiaan selama masa kampanye'."
    ay "Ini jelas-jelas konflik kepentingan! Flourine masih pegang kendali soal alokasi dana acara besar bulan ini, sementara dia juga kampanye."
    ay "Ini ngasih dia panggung dan privilege yang gak dimiliki kandidat lain kayak lo atau Fanya."
    ay "Aturan ini dibuat jaman baheula dan panitia sekarang sengaja tutup mata karena nguntungin golongan mereka."
    
    menu:
        "Gila, pantesan gerakan Flourine mulus banget.":
            $ ayya_meter += 2
            ay "Tepat! Mereka main licik di balik aturan yang cacat."
            jump ayya_inti_1
            
        "Tapi kalau aturannya emang gitu dari dulu, ya mau gimana lagi?":
            $ ayya_meter -= 1
            ay "Aturan yang salah itu harus diubah, bukan dimaklumi, Aruna!"
            jump ayya_inti_1
            
        "Gue juga ngerasa ada yang aneh sama struktur kepanitiaan kampanye tahun ini.":
            $ ayya_meter += 2
            ay "Makanya gue pengen bertindak."
            jump ayya_inti_1

label ayya_inti_1:
    ay "Gue mau ngajuin nota keberatan resmi dari FPSH ke MPK dan Pembina OSIS buat ninjau ulang aturan ini."
    ay "Tapi gue butuh dukungan dari pihak yang berkepentingan langsung. Lo, sebagai kandidat."
    ay "Gue butuh lo ikut tanda tangan dan bawa ini ke permukaan."
    ay "Lo mau bantu gue tinjau ulang aturannya, dan nuntut pemilihan yang fair, atau lo milih diem dan nurut sama sistem yang rusak ini?"
    
    menu:
        "Gue dukung penuh. Kita protes aturan ini dan tuntut transparansi!":
            $ ayya_meter += 4
            ay "Gue tau gue bisa ngandelin keberanian lo!"
            jump ayya_dukung_penuh
            
        "Gue setuju prinsipnya, tapi jangan sampai bikin heboh atau berantem sama panitia.":
            $ ayya_meter += 2
            ay "Setuju prinsip tapi takut eksekusi? Yaudah, kita main lebih smooth."
            jump ayya_dukung_terbatas
            
        "Maaf Ay, gue gak mau nyari ribut sama panitia. Gue mending fokus nyari suara aja.":
            $ ayya_meter -= 2
            ay "Gue kecewa banget denger itu dari mulut calon ketua OSIS."
            jump ayya_tolak

label ayya_dukung_penuh:
    ar "Gue gak cuma bakal tanda tangan. Gue bakal bawa isu keadilan aturan ini sebagai materi kampanye gue ke depan."
    ar "Biar semua siswa tau kalau ada yang dimanipulasi dari atas."
    ay "Ini baru namanya reformasi! Kita bakal guncang sistemnya."
    
    menu:
        "Flourine pasti bakal kaget dan panik.":
            $ ayya_meter += 2
            ay "Biarin dia panik. Kebenaran harus ditegakkan."
            jump ayya_end
            
        "Semoga guru-guru memihak kita.":
            $ ayya_meter += 1
            ay "Kalau pake dasar hukum yang kuat, mereka gak bisa ngelak."
            jump ayya_end
            
        "Gue serahin draft hukumnya ke lo ya, lo ahlinya.":
            $ ayya_meter += 1
            ay "Beres. Malam ini draft protesnya bakal kelar."
            jump ayya_end

label ayya_dukung_terbatas:
    ar "Gue bakal tanda tangan sebagai dukungan tertutup."
    ar "Lo serahin suratnya ke pembina, tapi jangan bikin ini jadi keributan massa."
    ay "Lebih lambat efeknya, tapi seenggaknya secara legal kita punya pijakan."
    
    menu:
        "Kita tunggu respon dari pembina aja.":
            $ ayya_meter += 1
            ay "Ya, gue harap mereka ngasih respon positif secepatnya."
            jump ayya_end
            
        "Gue gak mau dianggap kandidat tukang protes yang cari alasan doang.":
            $ ayya_meter += 0
            ay "Gue paham kekhawatiran lo soal image kampanye."
            jump ayya_end
            
        "Semoga aja Flourine gak dapet celah baru buat ngeles.":
            $ ayya_meter += 1
            ay "Gue bakal awasin dia dengan ketat."
            jump ayya_end

label ayya_tolak:
    ar "Kalau gue protes sekarang, kesannya gue nyalah-nyalahin aturan karena takut kalah saing."
    ay "Lo lebih mikirin ego kampanye lo daripada sistem yang jujur? Terserah deh."
    jump ayya_end

label ayya_end:
    "Ayya kembali menatap kertas-kertasnya, kali ini dengan ekspresi yang berbeda."
    $ npc_state["ayya"]["relationship_quality"] += ayya_meter
    $ npc_state["ayya"]["quest_status"] = "completed"
    $ npc_state["ayya"]["votes_banked"] = get_votes_from_relationship(npc_state["ayya"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Ayya selesai. Kamu mendapatkan [npc_state['ayya']['votes_banked']] vote."
    jump end_day_routine


# -------------------------------------------------------------
# QUEST AMI (Jurnalistik)
# -------------------------------------------------------------
label quest_ami:
    $ npc_state["ami"]["quest_status"] = "in_progress"
    $ npc_state["ami"]["approached_day"] = current_day
    $ ami_meter = 0
    
    scene expression Transform("images/bg_ekskul_jurnalistik.jpg", size=(1920, 1080))
    "Kamu menemui Ami di sudut koridor lantai dua yang sepi."
    "Dia sedang membawa buku catatan kecil dengan stiker bunga-bunga, memegang pulpen warna-warni."
    
    ar "Hai Ami, sibuk nyatet apaan tuh?"
    am "Oh, Aruna! Kebetulan banget ketemu. Aku emang lagi nyari kamu."
    ar "Nyari aku? Ada tugas jurnalistik lagi?"
    am "Iya bener. Tapi ini bukan wawancara tegang kayak yang dibikin Adam kok, tenang aja."
    
    menu:
        "Syukurlah. Wawancara sama Adam bikin gue serasa diinterogasi FBI.":
            $ ami_meter += 2
            am "Hahaha, Adam emang gitu! Kaku banget orangnya."
            jump ami_basa_basi
            
        "Mau gaya apa aja gue siap kok. Apa pertanyaannya?":
            $ ami_meter += 1
            am "Semangat banget ya! Santai aja, kita ngobrol ringan."
            jump ami_basa_basi
            
        "Bagus deh. Gue butuh break dari obrolan berat soal visi-misi.":
            $ ami_meter += 2
            am "Nah, pas banget kalau gitu!"
            jump ami_basa_basi

label ami_basa_basi:
    am "Jadi gini, kolom buletin bulan ini bakal nampilin rubrik 'Sisi Lain Sang Kandidat'."
    am "Aku ditugasin nulis profil personal kalian."
    am "Aku gak peduli soal janji kerja kalian, soal kas OSIS, atau soal aturan sekolah."
    am "Aku mau tau... siapa sih Aruna Wirasena Wisnu di luar embel-embel OSIS?"
    
    menu:
        "Aruna di luar OSIS? Orang yang hobi rebahan sambil dengerin musik.":
            $ ami_meter += 2
            am "Nah, yang kayak gini yang aku mau denger!"
            jump ami_inti_1
            
        "Gue tetep orang yang berdedikasi tinggi buat sekolah, kapanpun dimanapun.":
            $ ami_meter -= 2
            am "Yah... jawaban template politisi lagi."
            jump ami_inti_1
            
        "Susah juga jawabnya. Kadang gue ngerasa gue ini gabungan dari ekspektasi orang-orang.":
            $ ami_meter += 3
            am "Wow, dalem banget. Ayo ceritain lebih lanjut."
            jump ami_inti_1

label ami_inti_1:
    am "Aku mau tanya satu pertanyaan yang agak personal."
    am "Di tengah semua tekanan kampanye ini, pernah gak sih kamu ngerasa pengen nyerah aja? Pengen jadi siswa biasa yang pulang sekolah langsung main?"
    am "Gue janji ini cuma buat profil empati, bukan buat nunjukin kelemahan kamu."
    am "Kamu mau cerita jujur, atau mau tetep pake topeng 'kandidat kuat'?"
    
    menu:
        "Gue bakal cerita sejujurnya.":
            $ ami_meter += 3
            am "Makasih udah mau terbuka sama aku, Aruna."
            jump ami_jujur
            
        "Gue ceritain seadanya aja ya, gue tetep harus jaga wibawa dikit.":
            $ ami_meter += 1
            am "Ngerti kok. Nggak gampang buat nunjukin sisi rentan."
            jump ami_seadanya
            
        "Maaf Mi, gue harus tetep profesional. Kandidat gak boleh keliatan lemah.":
            $ ami_meter -= 2
            am "Oh... sayang banget. Padahal pembaca lebih suka orang yang realistis lho."
            jump ami_tolak

label ami_jujur:
    ar "Sejujurnya... tiap malem gue mikir. Buat apa gue ngelakuin ini semua?"
    ar "Gue kehilangan waktu main, waktu istirahat, bahkan temen-temen lama gue ngerasa gue berubah."
    ar "Kadang gue ngerasa kesepian di tengah keramaian pendukung gue sendiri."
    am "Itu... sedih banget dengernya, Aruna."
    
    menu:
        "Tapi gue udah mulai melangkah, gue gak bisa mundur.":
            $ ami_meter += 2
            am "Kamu bener-bener punya tekad yang luar biasa."
            jump ami_end
            
        "Makanya, ngobrol santai kayak gini berharga banget buat gue.":
            $ ami_meter += 3
            am "Awww, aku seneng bisa jadi temen ngobrol kamu."
            jump ami_end
            
        "Semoga artikel lo bisa nunjukin kalau gue juga manusia biasa.":
            $ ami_meter += 2
            am "Pasti! Aku jamin artikel ini bakal menyentuh hati banyak orang."
            jump ami_end

label ami_seadanya:
    ar "Terkadang capek sih, wajar. Tugas numpuk, rapat sana-sini."
    ar "Tapi itu udah jadi konsekuensi dari pilihan gue maju nyalon."
    am "Jadi kamu ngerasa ini semacam pengorbanan yang emang harus dilakuin ya?"
    
    menu:
        "Bisa dibilang gitu.":
            $ ami_meter += 1
            am "Okelah, ini cukup buat ngasih gambaran soal keteguhan hati kamu."
            jump ami_end
            
        "Ya, gue harap hasilnya sepadan.":
            $ ami_meter += 1
            am "Pasti ada hasilnya kok, apapun itu."
            jump ami_end
            
        "Namanya juga hidup, nikmatin aja prosesnya.":
            $ ami_meter += 1
            am "Mindset yang bagus!"
            jump ami_end

label ami_tolak:
    ar "Gue gak pernah mikir buat nyerah. Kalau udah komitmen, ya harus jalan terus."
    am "O-oke... Cukup diplomatis. Makasih ya atas waktunya."
    jump ami_end

label ami_end:
    "Ami tersenyum hangat setelah mencatat beberapa kalimat darimu."
    $ npc_state["ami"]["relationship_quality"] += ami_meter
    $ npc_state["ami"]["quest_status"] = "completed"
    $ npc_state["ami"]["votes_banked"] = get_votes_from_relationship(npc_state["ami"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Ami selesai. Kamu mendapatkan [npc_state['ami']['votes_banked']] vote."
    jump end_day_routine


# -------------------------------------------------------------
# QUEST CECILLIA (Badminton)
# -------------------------------------------------------------
label quest_cecillia:
    $ npc_state["cecillia"]["quest_status"] = "in_progress"
    $ npc_state["cecillia"]["approached_day"] = current_day
    $ cecillia_meter = 0
    
    scene expression Transform("images/bg_lapangan_badminton.jpg", size=(1920, 1080))
    "Gema pukulan shuttlecock terdengar nyaring di GOR sekolah."
    "Cecillia sedang berlatih sendirian. Dia melompat dan melakukan smash keras ke sisi lapangan yang kosong."
    "Dia terlihat lelah dan sedikit frustrasi."
    
    ar "Woi, Cecillia! Lawan angin doang nih dari tadi?"
    cc "Eh, Aruna. Iya nih, anginnya jago banget nangkis smash gue."
    cc "Lagi rehat kampanye lo? Tumben nyasar ke GOR."
    
    menu:
        "Sengaja nyari lo. Liat lo sendirian gini bikin kasihan.":
            $ cecillia_meter += 1
            cc "Enak aja kasihan. Gue lagi ngelatih footwork mandiri tau!"
            jump cecillia_basa_basi
            
        "Iya, butuh refreshing dikit liat orang olahraga.":
            $ cecillia_meter += 2
            cc "Refreshing sekalian nyari keringet mendingan lo ikut main sini."
            jump cecillia_basa_basi
            
        "Anak-anak badminton pada ke mana emang?":
            $ cecillia_meter += 1
            cc "Nah, itu dia masalahnya."
            jump cecillia_basa_basi

label cecillia_basa_basi:
    cc "Gue lagi agak pusing nih, Run."
    cc "Sebulan lagi kita ada kejuaraan antar-sekolah."
    cc "Tapi karena sekarang lagi musim kampanye OSIS dan banyak acara beruntun, anak-anak pada sibuk di kepanitiaan."
    cc "Latihan rutin jadi sepi banget. Banyak yang izin."
    cc "Gue ngerti sih mereka sibuk, tapi sebagai kapten, gue harus jaga semangat dan keutuhan tim."
    
    menu:
        "Susah juga ya kalau jadwalnya pada bentrok gini.":
            $ cecillia_meter += 1
            cc "Iya banget. Kepala gue sampe nyut-nyutan mikirin jadwal doang."
            jump cecillia_inti_1
            
        "Mereka harusnya tetep prioritasin ekskul dong kalau mau turnamen!":
            $ cecillia_meter += 2
            cc "Gue juga maunya gitu, tapi gue gak mau egois maksain mereka."
            jump cecillia_inti_1
            
        "Terus lo rencananya mau ngapain sekarang?":
            $ cecillia_meter += 1
            cc "Gue butuh bantuan."
            jump cecillia_inti_1

label cecillia_inti_1:
    cc "Gue butuh seseorang buat bantu balikin semangat latihan anak-anak minggu ini."
    cc "Lo bisa bantu hadir dan ikut ngeramein latihan kita besok sore? Kehadiran calon ketua OSIS lumayan bisa ngasih suntikan moral."
    cc "Atau seenggaknya, lo bisa bantu koordinasiin jadwal panitia dari sisi OSIS biar gak bentrok banget sama jadwal GOR?"
    
    menu:
        "Gue bakal hadir besok sore. Bawa raket, kita main bareng!":
            $ cecillia_meter += 4
            cc "Serius lo mau ikutan main? Wah, ini baru yang namanya aksi nyata!"
            jump cecillia_hadir
            
        "Gue bantu dari balik layar aja ya. Gue omongin jadwalnya sama anak panitia.":
            $ cecillia_meter += 2
            cc "Boleh banget, itu juga udah sangat ngebantu urusan logistik gue."
            jump cecillia_koordinasi
            
        "Aduh Cil, maaf banget gue jadwalnya full buat kampanye minggu ini.":
            $ cecillia_meter -= 2
            cc "Yah... gapapa sih, gue paham kok posisi lo."
            jump cecillia_tolak

label cecillia_hadir:
    ar "Gue udah lama gak nyari keringet. Besok gue bawa air mineral se-kardus buat anak-anak sekalian."
    cc "Wah! Makasih banyak Aruna! Lo beneran penyelamat di tengah kegalauan gue."
    
    menu:
        "Tapi lo jangan smash gue kenceng-kenceng ya besok.":
            $ cecillia_meter += 2
            cc "Hahaha, gak janji ya! Siap-siap aja encok."
            jump cecillia_end
            
        "Ini hitung-hitung refreshing juga buat pikiran gue.":
            $ cecillia_meter += 1
            cc "Cocok banget! Olahraga bisa ngilangin stres politik."
            jump cecillia_end
            
        "Tapi anak badminton pada harus milih gue ya nanti!":
            $ cecillia_meter -= 1
            cc "Yee, pamrih nih ceritanya? Tapi oke lah, gue bakal promosiin elo entar."
            jump cecillia_end

label cecillia_koordinasi:
    ar "Gue bakal usahain lobi panitia acara lain supaya rapat-rapat gede gak dibikin barengan sama jadwal latihan kalian."
    cc "Itu ngebantu banget Run, seenggaknya anak-anak gak dilema kalau disuruh milih antara ekskul atau kepanitiaan."
    
    menu:
        "Semoga aja bisa diatur, gue bakal ngomong baik-baik sama koordinatornya.":
            $ cecillia_meter += 1
            cc "Sip, makasih ya atas bantuannya."
            jump cecillia_end
            
        "Kalau mereka ngeyel, biar gue yang paksa rubah jadwalnya.":
            $ cecillia_meter += 0
            cc "Eh jangan keras-keras juga, nanti malah ribut. Yang smooth aja ya."
            jump cecillia_end
            
        "Sukses ya buat persiapan turnamennya!":
            $ cecillia_meter += 1
            cc "Amin! Doain kita bawa pulang piala lagi tahun ini."
            jump cecillia_end

label cecillia_tolak:
    ar "Gue pengen banget bantu, tapi sisa waktu kampanye ini bener-bener kritis buat gue."
    cc "Gak masalah kok Run, profesional aja. Kampanye lo emang lagi penting-pentingnya."
    jump cecillia_end

label cecillia_end:
    "Kamu dan Cecillia saling melempar senyum sebelum kamu pamit meninggalkan GOR."
    $ npc_state["cecillia"]["relationship_quality"] += cecillia_meter
    $ npc_state["cecillia"]["quest_status"] = "completed"
    $ npc_state["cecillia"]["votes_banked"] = get_votes_from_relationship(npc_state["cecillia"]["relationship_quality"])
    $ total_votes = calc_total_votes()
    "Quest Cecillia selesai. Kamu mendapatkan [npc_state['cecillia']['votes_banked']] vote."
    jump end_day_routine
