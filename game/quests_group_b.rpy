# Quests Group B - Juan, Faizal, Nayra, Aulia, Ellisa, Desti

label quest_juan:
    $ start_quest("juan")
    $ juan_meter = 0
    
    scene expression Transform("images/bg_lab_robotika.jpg", size=(1920, 1080))
    "Kamu menemukan Juan di sudut lab, sedang mengotak-atik sebuah papan sirkuit kecil dengan solder di tangannya."
    "Asap tipis mengepul dari meja kerjanya. Dia terlihat sangat fokus sampai tidak menyadari kehadiranmu."
    
    ar "Sibuk banget, Juan? Awas kena tangan tuh solder."
    "Juan terkejut sedikit, lalu menaruh soldernya dan melepas kacamata pelindungnya."
    
    juan "Oh, Aruna. Ngagetin aja lo. Untung tangan gue stabil."
    juan "Lagi nyoba benerin modul sensor yang kebakar pas uji coba kemaren."
    
    menu:
        "Keliatannya susah. Sering rusak ya alatnya?":
            $ juan_meter += 1
            juan "Bukan sering rusak, tapi emang umurnya udah tua. Kita pake barang seadanya."
            jump juan_talk_2
            
        "Gue kira Robotika selalu dapet alat baru tiap tahun.":
            $ juan_meter -= 1
            juan "Hah? Lo bercanda? Ekskul kita tuh anak tiri buat urusan anggaran."
            jump juan_talk_2
            
        "Semangat ya. Gue nggak ngerti ginian sih, tapi keliatan keren.":
            $ juan_meter += 0
            juan "Keren sih keren, pusingnya itu loh."
            jump juan_talk_2

label juan_talk_2:
    juan "Lagian, tumben banget kandidat Ketua OSIS main ke bengkel kotor kayak gini."
    juan "Biasanya petinggi OSIS kalau ke sini cuma buat marah-marah karena tagihan listrik kita bengkak."
    
    ar "Gue ke sini murni mau liat keadaan kalian kok."
    
    juan "Ya... kadang kerasa ekskul kita ini gak dianggap penting sama OSIS. Cuma dituntut menang lomba, tapi pas minta ganti alat dipersulit."
    juan "Lo beda gak dari mereka, Aruna?"
    
    menu:
        "Tentu aja gue beda. Gue bakal pastiin anggaran kalian cair.":
            $ juan_meter += 3
            juan "Cair? Ngomong sih gampang. Flourine juga dulu janjinya gitu pas kampanye."
            jump juan_core
            
        "Gue ngerti frustrasi lo. Gue janji bakal lebih sering dengerin keluhan kalian.":
            $ juan_meter += 1
            juan "Dengerin doang mah percuma kalau nggak ada aksi nyatanya, Aruna."
            jump juan_core
            
        "Kalau kalian bisa buktiin prestasi, OSIS pasti bakal perhatiin kok.":
            $ juan_meter -= 2
            juan "Lah? Buktiin prestasi gimana kalau alatnya aja nggak support? Logika lo kebalik."
            jump juan_core

label juan_core:
    juan "Gini ya, gue butuh kepastian. Kalau lo kepilih, lo berani nggak kasih jaminan hitam di atas putih buat nambah kuota anggaran kita?"
    
    menu:
        "Gue janji. Gue bakal masukin itu ke program kerja 100 hari pertama gue.":
            $ juan_meter += 4
            juan "Serius lo? Kalau sampe bohong, gue bakal bawa anak-anak demo ke ruang OSIS loh."
            ar "Silakan. Gue pegang janji gue."
            jump juan_ending
            
        "Gue bakal berusaha keras buat bantu, tapi gue nggak bisa janji langsung cair. Ada birokrasinya.":
            $ juan_meter += 2
            juan "Setidaknya lo jujur. Ya udah, gue hargai itu."
            jump juan_ending
            
        "Fokus aja dulu menangin lomba yang sekarang. Nanti gue usahain dari sisa dana yang ada.":
            $ juan_meter -= 2
            juan "Sisa dana? Lo pikir ekskul kita ini cuma pantes dapet sisa-sisa? Wah, parah lo."
            jump juan_ending

label juan_ending:
    if juan_meter >= 6:
        juan "Oke, lo beda. Gue pegang kata-kata lo. Anak Robotika bakal tau soal obrolan kita hari ini."
        "Juan tersenyum sambil kembali mengambil soldernya."
    elif juan_meter >= 3:
        juan "Yah... kita liat aja nanti. Gue harap lo beneran beda dari yang lain."
    else:
        juan "Sama aja lo kayak yang lain. Cuma manis di mulut pas butuh suara."
        "Juan membuang muka dan fokus lagi ke pekerjaannya."
        
    $ complete_quest("juan", juan_meter)
    "Quest Juan selesai. Kamu mendapatkan [npc_state['juan']['votes_banked']] vote."
    jump end_day_routine


label quest_faizal:
    $ start_quest("faizal")
    $ faizal_meter = 0
    
    scene expression Transform("images/bg_lab_robotika.jpg", size=(1920, 1080))
    "Kamu melihat Faizal sedang sibuk mengetik barisan kode di laptopnya, duduk di pojok koridor dekat lab komputer."
    "Wajahnya terlihat tegang, dan ada dua gelas kopi instan yang sudah kosong di sebelahnya."
    
    ar "Zal? Jangan bilang lo nginep di sekolah buat ngerjain itu."
    
    faizal "Hah? Eh, Aruna."
    faizal "Nggak nginep, tapi dari subuh gue udah di mari. Lusa deadline submit kodingan buat robot kita, dan masih ada bug di sistem navigasinya."
    
    menu:
        "Istirahat bentar, Zal. Kesehatan lo lebih penting.":
            $ faizal_meter += 1
            faizal "Kalau gue istirahat, tim gue kalah. Gue nggak bisa egois."
            jump faizal_talk_2
            
        "Mau gue beliin kopi lagi? Kayaknya lo butuh asupan kafein.":
            $ faizal_meter += 2
            faizal "Boleh banget kalau lo maksa. Tapi entar aja, tanggung ini."
            jump faizal_talk_2
            
        "Kodingan apaan tuh? Keliatannya rumit banget.":
            $ faizal_meter += 0
            faizal "Algoritma pathfinding. Lo nggak bakal paham, pusing."
            jump faizal_talk_2

label faizal_talk_2:
    faizal "Lo ke sini pasti ada maunya kan? Kampanye?"
    faizal "Gue to the point aja, Na. Gue gak peduli sama janji-janji manis soal 'perhatian ke ekskul' atau apalah."
    faizal "Gue cuma mau tim ini menang. Tapi server sekolah buat jalanin simulasi kita sering down."
    
    ar "Terus, lo mau gue ngapain?"
    
    faizal "Lo bisa bantu apa yang nyata? Atau cuma bisa kasih semangat doang kayak suporter bola?"
    
    menu:
        "Gue punya akses ke server lab bahasa yang jarang dipake. Gue bisa mintain izin ke guru buat lo pake simulasinya.":
            $ faizal_meter += 4
            faizal "Serius lo bisa dapet izinnya hari ini? Gila, kalau beneran bisa, lo penyelamat kita."
            jump faizal_core
            
        "Gue akan dukung lo dan tim 100 persen. Kalian pasti bisa ngelewatin ini.":
            $ faizal_meter -= 1
            faizal "Dukungan moral. Hhh... thanks, tapi sayangnya itu nggak bisa nge-compile kode gue."
            jump faizal_core
            
        "Gue nggak ngerti IT, Zal. Kayaknya gue nggak bisa bantu banyak soal itu.":
            $ faizal_meter -= 2
            faizal "Ya udah kalau gitu. Jangan ganggu gue, gue lagi fokus."
            jump faizal_core

label faizal_core:
    if faizal_meter >= 3:
        faizal "Kalau lo beneran bisa kasih gue akses server itu, seisi lab Robotika bakal vote lo. Gue jamin."
    else:
        faizal "Kalau lo mau suara kita, lo harus buktiin lo ngerti kebutuhan kita, Na."

    faizal "Satu lagi. Misal lo kepilih, lo berani nggak motong dana acara seni tahunan buat dialihin ke kompetisi sains?"
    
    menu:
        "Pasti. Prestasi akademi dan sains jauh lebih penting buat nama sekolah.":
            $ faizal_meter += 3
            faizal "Jawaban berani. Anak seni bakal ngamuk, tapi gue suka gaya lo."
            jump faizal_ending
            
        "Gue bakal cari sponsor dari luar buat kalian, tanpa motong dana ekskul lain.":
            $ faizal_meter += 2
            faizal "Ide bagus, meski prakteknya susah. Tapi gue hargain effort lo."
            jump faizal_ending
            
        "Seni dan sains harus seimbang. Gue nggak bisa milih kasih.":
            $ faizal_meter -= 2
            faizal "Klasik. Jawaban politisi banget. Selalu mau nengahin tapi ujungnya nggak nyelesein masalah."
            jump faizal_ending

label faizal_ending:
    if faizal_meter >= 7:
        faizal "Oke, Na. Lo dapet suara gue. Buruan urus izin servernya, gue tunggu!"
        "Faizal kembali mengetik dengan semangat."
    elif faizal_meter >= 3:
        faizal "Gue bakal pertimbangin. Lo lebih baik dari yang gue kira."
    else:
        faizal "Udahlah, lo mending cari suara ke anak ekskul lain aja. Gue sibuk."
        "Faizal mengabaikanmu sepenuhnya."
        
    $ complete_quest("faizal", faizal_meter)
    "Quest Faizal selesai. Kamu mendapatkan [npc_state['faizal']['votes_banked']] vote."
    jump end_day_routine


label quest_nayra:
    $ start_quest("nayra")
    $ nayra_meter = 0
    
    scene expression Transform("images/bg_ekskul_musik.jpg", size=(1920, 1080))
    "Kamu berjalan melewati ruang musik dan mendengar petikan gitar yang indah namun tiba-tiba berhenti dengan nada sumbang."
    "Di dalam, Nayra sedang duduk di lantai, mengacak-acak rambutnya frustrasi."
    
    ar "Loh, Nay? Kenapa berhenti? Tadi bagus banget loh."
    
    nayra "Bagus apanya? Fals gitu."
    nayra "Ah, Aruna. Sori, gue lagi pusing."
    nayra "Kita mau manggung minggu depan, tapi jadwal latihan kita selalu bentrok."
    
    menu:
        "Bentrok sama siapa?":
            $ nayra_meter += 1
            nayra "Sama ekskul Tari Tradisional. Mereka kan juga mau ada pentas."
            jump nayra_talk_2
            
        "Jangan dipaksain, ntar malah stres.":
            $ nayra_meter += 0
            nayra "Kalo nggak dipaksain, kita mau mainin apa pas manggung? Bisu di atas panggung?"
            jump nayra_talk_2
            
        "Pantesan tadi mainnya agak kasar. Lo lagi emosi ya?":
            $ nayra_meter -= 1
            nayra "Makasih kritiknya. Gue emang lagi nggak mood."
            jump nayra_talk_2

label nayra_talk_2:
    nayra "Masalahnya tuh di ruangannya. Ruang seni cuma satu, sedangkan yang mau pake banyak."
    nayra "Gue udah ajuin permohonan buat pake aula kalau sore, tapi Pak Yanto (wakasek kesiswaan) bilangnya aula cuma buat rapat penting."
    
    ar "Terus rencana lo sekarang gimana?"
    
    nayra "Gue pengen minta tolong lo, Na."
    nayra "Lo kan lumayan deket sama guru-guru. Bisa bantu gue dapetin izin tempat latihan yang lebih pasti nggak?"
    
    menu:
        "Gue bakal maju ke Pak Yanto dan ngotot minta izin aula buat kalian sampai tuntas.":
            $ nayra_meter += 4
            nayra "Wah... beneran? Pak Yanto tuh galak banget loh. Lo berani adu argumen sama dia?"
            ar "Demi kalian, gue berani."
            jump nayra_core
            
        "Gue kenal penjaga gedung serbaguna kelurahan deket sini. Kalian bisa pake itu sementara.":
            $ nayra_meter += 2
            nayra "Kelurahan? Lumayan sih daripada nggak ada... tapi repot mindahin alatnya."
            jump nayra_core
            
        "Duh, gue nggak berani kalau harus lawan Pak Yanto. Gimana kalau kalian latihan di luar sekolah aja?":
            $ nayra_meter -= 2
            nayra "Di luar sekolah nyewa studionya mahal, Na. Ya udahlah, emang gue nggak bisa ngandelin lo."
            jump nayra_core

label nayra_core:
    nayra "Kadang gue ngerasa sekolah ini terlalu nganakemasin ekskul akademik. Giliran seni, dipersulit terus."
    nayra "Kalau lo jadi ketua, apa lo beneran peduli sama ekskul seni?"
    
    menu:
        "Pasti. Seni itu jiwa sekolah kita. Gue bakal usahain dana lebih buat kalian.":
            $ nayra_meter += 3
            nayra "Gue seneng dengernya. Semoga itu bukan janji kampanye doang."
            jump nayra_ending
            
        "Gue peduli, tapi gue juga harus adil ke semua ekskul, Nay. Nggak bisa berat sebelah.":
            $ nayra_meter -= 1
            nayra "Adil itu bukan berarti ngasih porsi yang sama persis, Na. Tapi sesuai kebutuhan."
            jump nayra_ending
            
        "Gue bakal bikin festival gede biar ekskul seni bisa unjuk gigi maksimal.":
            $ nayra_meter += 2
            nayra "Bagus juga idenya! Jadi kita punya panggung sendiri."
            jump nayra_ending

label nayra_ending:
    if nayra_meter >= 6:
        nayra "Makasih banyak, Na! Gue tunggu kabar baik soal izinnya. Kalau beres, lo pasti dapet vote gue dan anak akustik!"
        "Wajah Nayra kembali ceria dan ia mulai memetik gitarnya lagi."
    elif nayra_meter >= 3:
        nayra "Oke, kita liat aja nanti. Makasih udah dengerin keluhan gue."
    else:
        nayra "Kayaknya lo sama aja kayak yang lain. Nggak ngerti betapa pentingnya ini buat kita."
        "Nayra membereskan gitarnya dan pergi."
        
    $ complete_quest("nayra", nayra_meter)
    "Quest Nayra selesai. Kamu mendapatkan [npc_state['nayra']['votes_banked']] vote."
    jump end_day_routine


label quest_aulia:
    $ start_quest("aulia")
    $ aulia_meter = 0
    
    scene expression Transform("images/bg_lapangan_paskibra.jpg", size=(1920, 1080))
    "Kamu menemui Aulia, Ketua Paskibra, di pinggir lapangan."
    "Posturnya tegak seperti biasa, tapi wajahnya menunjukkan ketegangan yang amat sangat."
    "Dia sedang memegang sebuah kotak rokok kecil."
    
    ar "Aul? Lo merokok?!"
    
    aulia "Hush! Pelan-pelan!"
    aulia "Bukan! Ini bukan punya gue. Ini punya salah satu junior gue yang ketahuan nongkrong di gudang belakang."
    
    menu:
        "Wah, parah. Siapa orangnya?":
            $ aulia_meter += 1
            aulia "Gue nggak bisa sebut nama. Ini masalah internal."
            jump aulia_talk_2
            
        "Laporin ke guru BK langsung, Aul. Bahaya kalau ketahuan.":
            $ aulia_meter -= 2
            aulia "Nggak segampang itu, Aruna. Lo nggak ngerti dinamika Paskibra."
            jump aulia_talk_2
            
        "Terus lo mau apain barang buktinya?":
            $ aulia_meter += 2
            aulia "Itu yang lagi gue pikirin dari tadi."
            jump aulia_talk_2

label aulia_talk_2:
    aulia "Masalahnya, kalau ini bocor ke pihak sekolah, reputasi seluruh pleton Paskibra bakal hancur."
    aulia "Kita bisa-bisa di-skors dan batal ikut lomba tingkat provinsi bulan depan."
    aulia "Gue sebagai ketua nggak mau anak-anak lain kena getahnya gara-rata satu orang bodoh."
    
    ar "Jadi lo mau lindungin dia?"
    
    aulia "Gue mau hukum dia dengan cara gue sendiri. Internal Paskibra."
    aulia "Gue butuh bantuan lo. Gue butuh ini diselesaikan diam-diam. Lo bisa jaga rahasia ini?"
    
    menu:
        "Gue akan tutup mulut. Kita selesain ini diam-diam biar Paskibra aman.":
            $ aulia_meter += 4
            aulia "Gue tahu gue bisa percaya sama lo. Makasih, Na."
            jump aulia_core
            
        "Gue saranin lo tetep lapor ke BK, tapi gue bakal dampingi lo buat belain pleton biar nggak kena imbas.":
            $ aulia_meter += 1
            aulia "Itu berisiko tinggi. Kalau kepsek nggak mau denger penjelasan kita gimana?"
            jump aulia_core
            
        "Gue nggak mau terlibat, Aul. Ini pelanggaran berat, gue nggak berani nutup-nutupin.":
            $ aulia_meter -= 3
            aulia "Kecewa gue sama lo. Gue kira lo punya nyali buat ngelindungin teman sendiri."
            jump aulia_core

label aulia_core:
    if aulia_meter >= 3:
        aulia "Kalau lo bisa bantu gue melewati krisis ini tanpa ada yang tahu, lo punya kesetiaan anak Paskibra."
    else:
        aulia "Kayaknya gue emang sendirian ngadepin ini."
        
    aulia "Sebagai calon ketua OSIS, kadang lo bakal dihadapkan sama pilihan antara aturan tertulis dan melindungi anggota lo sendiri. Mana yang bakal lo pilih?"
    
    menu:
        "Gue akan pilih melindungi orang-orang gue, apapun risikonya. Aturan bisa diakali, tapi kepercayaan nggak bisa dibeli.":
            $ aulia_meter += 3
            aulia "Sikap seorang pemimpin sejati. Walau gelap, tapi nyata."
            jump aulia_ending
            
        "Aturan itu dibuat untuk dipatuhi. Kalau kita longgar, ke depannya bakal makin hancur.":
            $ aulia_meter -= 2
            aulia "Idealis. Sangat kaku. Lo nggak akan bertahan lama kalau selalu lurus."
            jump aulia_ending
            
        "Tergantung situasinya. Kita harus lihat case by case.":
            $ aulia_meter += 1
            aulia "Jawaban abu-abu. Sangat politis."
            jump aulia_ending

label aulia_ending:
    if aulia_meter >= 6:
        aulia "Gue lega bisa cerita sama lo. Rahasia ini aman berdua. Dan lo dapet dukungan dari gue."
        "Aulia menyembunyikan kotak itu di sakunya dengan senyum tipis."
    elif aulia_meter >= 3:
        aulia "Semoga pilihan lo tepat, Na. Gue hargai pendapat lo."
    else:
        aulia "Mending lo pergi dari sini. Lupakan apa yang lo liat barusan."
        "Aulia membuang muka, terlihat kesal dan kecewa."
        
    $ complete_quest("aulia", aulia_meter)
    "Quest Aulia selesai. Kamu mendapatkan [npc_state['aulia']['votes_banked']] vote."
    jump end_day_routine


label quest_ellisa:
    $ start_quest("ellisa")
    $ ellisa_meter = 0
    
    scene expression Transform("images/bg_perpus_sudut.jpg", size=(1920, 1080))
    "Kamu melihat Ellisa dari kejauhan, duduk sendirian di taman sekolah sambil memeluk kedua lututnya."
    "Wajahnya merah, sepertinya ia baru saja menangis."
    
    ar "Ellisa? Kamu kenapa?"
    
    ellisa "Eh? Kak Aruna..."
    ellisa "Gue... gue dituduh curang, Kak."
    
    menu:
        "Curang? Lomba matematika internal kemarin?":
            $ ellisa_meter += 2
            ellisa "Iya. Pak Rudi nemuin contekan rumus di bawah laci meja gue."
            jump ellisa_talk_2
            
        "Astaga! Lo beneran nggak ngelakuin itu kan?":
            $ ellisa_meter -= 1
            ellisa "Ya ampun Kak, masa Kakak juga nggak percaya sama gue?"
            jump ellisa_talk_2
            
        "Sabar dulu, coba ceritain pelan-pelan. Siapa yang nuduh?":
            $ ellisa_meter += 1
            ellisa "Pak Rudi, pembina Math Club. Dia nemuin kertas di laci gue."
            jump ellisa_talk_2

label ellisa_talk_2:
    ellisa "Gue berani sumpah itu bukan tulisan gue! Ada yang sengaja taruh kertas itu di sana buat ngejatuhin gue!"
    ellisa "Tapi Pak Rudi nggak mau denger. Dia bilang gue bakal didiskualifikasi dari tim olimpiade sekolah."
    
    ar "Ini masalah serius, El."
    
    ellisa "Makanya, Kak! Lo bisa bantu gue nggak? Tolong klarifikasi ini ke pihak yang nuduh. Lo kan disegani sama guru-guru."
    
    menu:
        "Gue bakal kumpulin bukti tulisan tangan asli lo dan buktiin ke Pak Rudi kalau itu konspirasi.":
            $ ellisa_meter += 4
            ellisa "Kak Aruna... makasih banget! Lo bener-bener pahlawan gue!"
            jump ellisa_core
            
        "Gue temenin lo nemuin Pak Rudi, tapi lo harus berani ngomong dan bela diri lo sendiri.":
            $ ellisa_meter += 2
            ellisa "Aduh, gue takut banget ngomong sama beliau... tapi kalau ada Kakak, gue coba deh."
            jump ellisa_core
            
        "Mungkin lo biarin aja dulu, biar reda. Kadang melawan guru malah bikin makin runyam.":
            $ ellisa_meter -= 4
            ellisa "Biarin aja?! Ini soal harga diri dan kejujuran gue, Kak! Gue kecewa banget sama lo."
            jump ellisa_core

label ellisa_core:
    if ellisa_meter >= 2:
        ellisa "Gue pengen nanya satu hal, Kak."
        ellisa "Kenapa orang-orang jahat suka pake cara kotor buat menang? Kenapa nggak bersaing sehat aja?"
        
        menu:
            "Karena mereka takut kalah kalau pakai cara jujur. Itu tanda kelemahan mereka.":
                $ ellisa_meter += 3
                ellisa "Kakak bener... berarti orang yang naruh contekan itu aslinya minder sama kemampuan gue."
                jump ellisa_ending
                
            "Karena dunia ini emang kejam, El. Lo harus siap ngadepin hal-hal kayak gini.":
                $ ellisa_meter -= 1
                ellisa "Gue nggak mau dunia yang kayak gitu, Kak."
                jump ellisa_ending
                
            "Kadang mereka halalkan segala cara demi ambisi. Lo jangan sampai kayak gitu ya.":
                $ ellisa_meter += 2
                ellisa "Pasti, Kak! Gue nggak akan pernah curang."
                jump ellisa_ending

label ellisa_ending:
    if ellisa_meter >= 6:
        ellisa "Gue ngerasa jauh lebih tenang sekarang. Makasih ya, Kak Aruna. Dukung gue, dan gue bakal dukung Kakak!"
        "Mata Ellisa kembali berbinar penuh harap."
    elif ellisa_meter >= 3:
        ellisa "Makasih masukannya, Kak. Gue harap semuanya bisa kelar."
    else:
        ellisa "Kakak nggak ngerti perasaan gue. Maaf, gue mau sendirian aja."
        "Ellisa kembali membenamkan wajahnya di lututnya."
        
    $ complete_quest("ellisa", ellisa_meter)
    "Quest Ellisa selesai. Kamu mendapatkan [npc_state['ellisa']['votes_banked']] vote."
    jump end_day_routine


label quest_desti:
    $ start_quest("desti")
    $ desti_meter = 0
    
    scene expression Transform("images/bg_uks_kasur.jpg", size=(1920, 1080))
    "Kamu menjenguk UKS. Desti, Ketua PMR, sedang mengatur kotak P3K sambil menghela napas panjang."
    "Ada dua siswa yang sedang tidur di ranjang UKS dengan wajah pucat."
    
    ar "Sibuk banget, Des? Banyak yang sakit ya?"
    
    desti "Ah, Aruna. Iya nih, gila banget belakangan ini."
    desti "Bulan ini aja udah lebih dari dua puluh anak tumbang karena kelelahan."
    
    menu:
        "Musim hujan gini emang gampang sakit sih.":
            $ desti_meter -= 1
            desti "Bukan karena cuaca, Na. Ini karena sistem sekolah."
            jump desti_talk_2
            
        "Kelelahan? Kegiatannya lagi padet banget emangnya?":
            $ desti_meter += 1
            desti "Sangat! Lo nggak nyadar ya gara-gara sibuk kampanye?"
            jump desti_talk_2
            
        "Kasihan banget. Lo pasti juga capek ngurusin mereka.":
            $ desti_meter += 2
            desti "Gue capek sih, tapi lebih kasihan liat mereka."
            jump desti_talk_2

label desti_talk_2:
    desti "Guru-guru pada ngebut ngasih tugas karena mau masuk musim ujian."
    desti "Ditambah lagi panitia pemilihan OSIS narik banyak anak buat bantu-bantu. Anak-anak diforsir abis-abisan."
    desti "Gue resah, Na. Keliatannya nggak ada yang berani angkat isu ini secara resmi ke pihak sekolah."
    
    ar "Jadi menurut lo, harus ada yang ngomong langsung ke kepala sekolah?"
    
    desti "Iya. Dan gue pengen ada yang mau denger & bantu suarakan ini, bukan cuma gue sendiri dari PMR."
    desti "Sebagai kandidat ketua, lo mau merespons isu ini gimana?"
    
    menu:
        "Gue bakal jadiin isu kesejahteraan mental dan fisik siswa ini sebagai janji kampanye utama gue. Gue angkat ke publik!":
            $ desti_meter += 4
            desti "Beneran?! Wah, itu bakal jadi terobosan banget, Na! Anak-anak butuh sosok yang berani nyuarain ini."
            jump desti_core
            
        "Gue paham. Gue bakal bantu lobi guru-guru secara personal biar nggak terlalu ngasih tugas, tapi pelan-pelan ya.":
            $ desti_meter += 2
            desti "Pendekatan halus ya? Oke, itu masuk akal juga. Yang penting ada langkah nyata."
            jump desti_core
            
        "Gue setuju sih kasihan, tapi jujur aja, fokus gue sekarang ke pemenangan dulu. Isu ini mungkin ntar setelah gue menjabat.":
            $ desti_meter -= 3
            desti "Kecewa gue. Kalo gitu lo sama aja kayak politisi di TV, mikirin kursi doang."
            jump desti_core

label desti_core:
    desti "Isu kesehatan mental tuh sering diremehin di sekolah kita. Dianggapnya kita cuma males."
    desti "Menurut lo, apa yang paling bikin stres anak-anak jaman sekarang?"
    
    menu:
        "Tekanan ekspektasi dari guru dan orang tua yang nggak realistis.":
            $ desti_meter += 3
            desti "Seratus persen bener! Itu yang bikin mereka burn out."
            jump desti_ending
            
        "Kurangnya manajemen waktu. Mereka terlalu sering begadang buat main atau nongkrong.":
            $ desti_meter -= 2
            desti "Itu victim blaming, Na. Nggak semua anak sakit karena main game."
            jump desti_ending
            
        "Persaingan antar teman yang terlalu toksik.":
            $ desti_meter += 1
            desti "Bisa jadi, tapi akar masalahnya tetep di sistem beban tugasnya."
            jump desti_ending

label desti_ending:
    if desti_meter >= 6:
        desti "Makasih, Aruna. Lo satu-satunya kandidat yang ngerti urgensi masalah ini. Gue dan anak-anak PMR ada di belakang lo!"
        "Desti tersenyum lega, merasa beban di pundaknya sedikit terangkat."
    elif desti_meter >= 3:
        desti "Gue harap omongan lo bisa dipegang. Kita butuh perubahan."
    else:
        desti "Udahlah, Na. Lo kampanye sana aja. Gue masih banyak kerjaan ngurusin anak-anak sakit."
        "Desti membalikkan badan dan kembali sibuk mengecek kotak P3K."
        
    $ complete_quest("desti", desti_meter)
    "Quest Desti selesai. Kamu mendapatkan [npc_state['desti']['votes_banked']] vote."
    jump end_day_routine

