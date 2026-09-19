default fanya_trust = 0
default fanya_dorongan_diketahui = False
default fanya_approach_style = None 
default fanya_resolved = None

default flourine_suspicion = 0
default flourine_trust = 0
default flourine_leverage_found = []
default flourine_comeback_active = False
default flourine_resolved = None

label rival_fanya_loop:
    if player_path is None:
        $ player_path = "rival"
    if fanya_resolved:
        "Urusanmu dengan Fanya sudah selesai. Kini tinggal menunggu hasil akhirnya."
        jump end_day_routine

    if fanya_stage == 0:
        "Hari pertama pengamatan. Fanya terlihat membagikan brosur kampanye dengan senyum yang dipaksakan."
        "Aruna memperhatikannya dari kejauhan, menganalisis bahasa tubuhnya."
        menu:
            "Dekati dan berikan pujian palsu":
                ar "Fanya, brosurnya bagus banget. Kamu kelihatan siap banget buat jadi ketua."
                fa "Ah, makasih Aruna... Iya, aku nyoba yang terbaik aja."
                "Senyumnya sedikit goyah. Ia membetulkan jepit rambutnya dengan canggung."
            "Perhatikan siapa yang membantunya":
                "Aruna menyipitkan mata. Hanya ada beberapa anak kelasnya yang ikut membagikan brosur."
                "Wajah mereka tampak bosan, tidak bersemangat. Dukungan untuknya tidak sebesar kelihatannya."
            "Langsung tembak dengan pertanyaan tajam":
                ar "Fan, jujur aja, kamu capek kan memaksakan diri begini?"
                fa "E-eh? Enggak kok! Kenapa nanya gitu?"
                "Fanya gelagapan, segera membuang muka. Tangannya gemetar pelan."
                $ fanya_trust -= 1
        
        "Aruna mencatat bahwa Fanya sangat tidak nyaman dengan posisinya sekarang."
        "Dia terus-menerus melirik ke arah anak-anak kelasnya seolah meminta persetujuan."
        menu:
            "Tawarkan bantuan kecil":
                ar "Sini aku bantu bagiin beberapa. Lagian kita saingan bukan berarti harus musuhan, kan?"
                fa "Serius? Makasih banget ya, Aruna. Kamu baik banget..."
                $ fanya_trust += 1
                "Mata Fanya berbinar. Dia benar-benar haus akan sedikit kebaikan di tengah tekanan ini."
            "Beri tekanan pasif":
                ar "Semoga sisa brosurnya cepat habis ya. Kasihan kalau terbuang sia-sia."
                fa "I-iya, pasti habis kok. Teman-temanku rajin membagikannya."
                "Nadanya terdengar sangat tidak yakin."
            "Abaikan dan pergi":
                "Aruna berlalu tanpa mengatakan apa-apa lagi."
                "Dari ekor matanya, ia bisa melihat bahu Fanya turun, seolah kehabisan napas."
        
        "Hari masih panjang. Aruna melihat Fanya duduk sendirian di kantin saat jam istirahat."
        "Ini kesempatan bagus untuk menekan atau merangkulnya lebih jauh."
        menu:
            "Temani dia makan":
                ar "Kosong kan? Boleh gabung?"
                fa "Tentu saja. Duduklah, Aruna."
                ar "Gimana rasanya jadi pusat perhatian akhir-akhir ini?"
                fa "Rasanya... lumayan berat. Aku gak biasa diliatin banyak orang."
                $ fanya_trust += 1
            "Sindir porsi makannya":
                ar "Makan dikit banget, pantes kelihatan lemas dari pagi."
                fa "Lagi nggak nafsu aja... perutku rasanya mual terus mikirin debat nanti."
                ar "Kalau mental nggak kuat, fisik juga bakal hancur loh."
                $ fanya_trust -= 1
            "Perhatikan dari meja lain":
                "Aruna hanya duduk dua meja darinya."
                "Ia menatap tajam ke arah Fanya sampai Fanya menyadarinya dan menunduk ketakutan."
        
        $ fanya_stage = 1
        jump end_day_routine

    elif fanya_stage == 1:
        "Aruna kembali mencecar Fanya hari ini. Ia harus tahu motivasi asli gadis itu."
        ar "Hai Fanya, masih sibuk kampanye ya?"
        fa "Eh, Aruna. Iya nih... lumayan capek. Sebenarnya... aku maju juga karena didorong anak-anak sih."
        menu:
            "Gali lebih dalam tentang siapa yang mendorongnya":
                ar "Oh ya? Didorong sama siapa emangnya? Emang bukan murni keinginan kamu?"
                fa "Ya gitu deh... beberapa guru dan anak kelasku merasa aku cocok karena aku sering jadi sekretaris."
                fa "Mereka bilang ini saatnya aku bersinar, tapi aku merasa buta."
                $ fanya_dorongan_diketahui = True
                "Kamu mencatat kelemahan ini. Fanya tidak sepenuhnya yakin dengan pencalonannya."
            "Pertanyakan kompetensinya":
                ar "Kalau cuma didorong orang, kamu yakin bisa mimpin OSIS dengan benar?"
                fa "Aku... aku akan belajar! Aku janji!"
                "Fanya tampak defensif namun matanya berkaca-kaca."
                $ fanya_trust -= 1
            "Tunjukkan empati palsu":
                ar "Wah, pasti berat banget ya nanggung ekspektasi banyak orang gitu."
                fa "B-benar! Kamu paham rasanya ya, Aruna? Kadang aku ngerasa pengap."
                $ fanya_trust += 1
        
        "Fanya menghela napas panjang, menatap kosong ke lantai."
        fa "Kadang aku mikir, apa aku ini cuma alat mereka aja supaya kelas kita kelihatan aktif..."
        menu:
            "Validasi ketakutannya":
                ar "Menurutku sih gitu. Kamu tahu kan, politik sekolah kadang sekejam itu."
                fa "Jadi... mereka nggak benar-benar peduli padaku?"
                ar "Hanya pada status yang bisa kamu bawa."
                $ fanya_approach_style = "agresif"
            "Beri semangat yang terasa hampa":
                ar "Jangan mikir gitu dong, pasti mereka percaya sama kemampuanmu."
                fa "Mungkin kamu benar... aku harus lebih positif."
                "Meski berkata begitu, wajahnya tetap muram."
            "Diamkan dan tatap matanya":
                "Aruna terdiam. Menatap langsung ke dalam mata Fanya yang panik."
                fa "K-kenapa diam aja? Ada yang salah di wajahku?"
                ar "Enggak. Aku cuma kasihan melihatmu."
        
        "Sebelum bel masuk berbunyi, Aruna memberikan satu pukulan mental terakhir."
        menu:
            "Ingatkan tentang debat":
                ar "Siap-siap aja buat debat besok. Jangan sampai menangis di depan mic."
                fa "A-aku nggak akan nangis!"
            "Tawarkan 'jalan keluar'":
                ar "Kalau kamu nggak sanggup, mundur itu bukan hal memalukan, Fan."
                fa "Mundur...? Tapi teman-temanku..."
                $ fanya_approach_style = "empatik"
            "Berikan senyuman dingin":
                "Aruna hanya tersenyum tipis, lalu berbalik tanpa sepatah kata pun."
                "Keheningan itu lebih mencekik daripada kata-kata."
        
        $ fanya_stage = 2
        jump end_day_routine

    elif fanya_stage == 2:
        "Ketegangan Fanya semakin memuncak. Lingkaran hitam mulai terlihat di bawah matanya."
        "Aruna mendekatinya saat ia sedang mengatur setumpuk dokumen."
        if fanya_dorongan_diketahui:
            ar "Fan, soal omonganmu kemarin... kamu gak apa-apa kan didorong maju gitu padahal mungkin kamu gak mau?"
            fa "Jujur, berat sih. Aku kadang merasa cuma jadi boneka aja."
            fa "Semua keputusan, sloganku, bahkan pidatoku... mereka yang buat."
            $ fanya_trust += 2
        else:
            ar "Gimana kampanyenya sejauh ini? Aman?"
            fa "Aman kok, walau lumayan melelahkan. Aku kurang tidur beberapa hari ini."
        
        menu:
            "Eksploitasi kata 'boneka'":
                ar "Boneka, ya? Pantas saja kamu terlihat kaku banget. Nggak ada jiwanya."
                fa "Itu jahat banget, Aruna! Tapi... mungkin kamu benar."
                $ fanya_trust -= 1
            "Jadilah pendengar yang baik":
                ar "Kamu harusnya bisa bilang tidak. Kamu punya hak atas dirimu sendiri."
                fa "Susah... mereka udah keluar banyak uang buat poster."
                $ fanya_trust += 1
            "Tawarkan bantuan radikal":
                ar "Biar aku yang ngomong ke mereka kalau kamu nggak berani."
                fa "JANGAN! M-maksudku, biar aku selesaikan sendiri..."
        
        "Tiba-tiba, seorang teman kelas Fanya datang dan menegurnya keras karena salah membagikan jadwal."
        "Teman: 'Fanya! Kan udah dibilang yang jadwal B itu buat besok! Kok dibagiin sekarang sih?!'"
        "Fanya menunduk dalam-dalam, meminta maaf berkali-kali. Temannya pergi dengan kesal."
        menu:
            "Tertawakan nasibnya":
                ar "Wow. Calon ketua OSIS dimarahi di depan umum. Menarik."
                fa "Tolong jangan lihat... memalukan..."
            "Bela dia di belakang temannya":
                ar "Temanmu itu keterlaluan. Dia pikir dia siapa?"
                fa "Dia ketua tim suksesku... Wajar dia marah, aku yang salah."
            "Bisikkan keraguan":
                ar "Lihat? Mereka tak menghormatimu. Mereka memperlakukanmu seperti babu."
                fa "..."
                "Fanya menggigit bibirnya keras hingga hampir berdarah."
                $ fanya_approach_style = "agresif"

        "Fanya terlihat hampir menangis. Ia memunguti sisa brosur dengan tangan gemetar."
        menu:
            "Bantu dia memungutnya":
                "Aruna membantunya dalam diam."
                fa "Terima kasih... kamu satu-satunya yang memperlakukanku seperti manusia hari ini."
                $ fanya_trust += 1
                $ fanya_approach_style = "empatik"
            "Injak salah satu brosur dengan pelan":
                "Secara tak sengaja (yang sangat disengaja), Aruna menginjak brosur bergambar wajah Fanya."
                fa "Oh... brosurnya kotor..."
                ar "Maaf. Tapi toh harganya nggak seberapa, kan?"
            "Tinggalkan dia dengan tatapan kasihan":
                "Aruna berlalu. Tatapan kasihan yang ditinggalkannya membuat Fanya semakin hancur."
        
        $ fanya_stage = 3
        jump end_day_routine

    elif fanya_stage == 3:
        "Ini saatnya menekan titik kritis Fanya."
        "Aruna menyudutkannya di perpustakaan saat sedang tak ada orang lain."
        ar "Fan. Kita perlu bicara serius. Berdua."
        fa "T-tentang apa? Aku harus segera rapat..."
        
        menu:
            "Yakinkan demi kebaikannya":
                ar "Fan, kalau ini memang bukan keinginanmu dan cuma bikin stres, kamu gak harus maksain diri loh."
                ar "Mundur bukan berarti kalah, tapi memilih apa yang terbaik buat mental dan fisikmu."
                fa "Tapi... ekspektasi mereka..."
                $ fanya_approach_style = "empatik"
            "Manfaatkan keraguannya secara agresif":
                ar "Kalau kamu sendiri gak yakin, gimana kamu bisa mimpin OSIS nanti?"
                ar "Mending kamu kasih posisi ini ke yang memang niat, daripada nanti berantakan. Berhenti jadi egois."
                fa "Egois?! Aku justru melakukan ini demi mereka!"
                $ fanya_approach_style = "agresif"
            "Manipulasi rasa bersalahnya":
                ar "Setiap hari kamu menderita, kinerjamu turun, dan kamu membohongi seluruh sekolah."
                ar "Apa ini ketua yang mereka inginkan? Seorang pembohong yang tertekan?"
                fa "Aku bukan pembohong!"
                $ fanya_approach_style = "agresif"

        "Fanya terdiam lama. Napasnya memburu, matanya membelalak mencari udara."
        fa "Kamu... kamu sengaja kan ngomong gini supaya sainganmu berkurang?!"
        menu:
            "Bantah dengan lembut":
                ar "Kalau aku cuma mau menang, aku biarkan saja kamu hancur di debat nanti."
                ar "Aku bicara begini karena peduli."
                $ fanya_trust += 1
            "Akui dengan bangga":
                ar "Tentu saja. Ini politik. Dan kamu kebetulan adalah mangsa paling lemah."
                $ fanya_trust -= 2
            "Alihkan pembicaraan ke dirinya":
                ar "Ini bukan tentang aku. Ini tentang kamu yang tidak bisa tidur berhari-hari karena takut gagal."
        
        "Fanya menutup wajahnya dengan kedua tangan, perlahan merosot ke lantai perpustakaan."
        fa "Aku capek... aku benar-benar capek, Aruna..."
        menu:
            "Peluk dia":
                "Aruna memeluknya perlahan."
                ar "Iya. Berhentilah sekarang."
                $ fanya_trust += 2
            "Tatap dengan dingin":
                ar "Maka berhentilah merengek dan mundur."
                $ fanya_trust -= 1
            "Tinggalkan dia dalam tangis":
                "Aruna pergi tanpa suara, membiarkan isak tangis Fanya menggema di perpustakaan sepi."

        $ fanya_stage = 4
        jump end_day_routine

    elif fanya_stage == 4:
        "Fanya terlihat sangat goyah hari ini. Ia tidak membagikan brosur, tidak juga menemui tim suksesnya."
        "Ia menghampiri Aruna di lorong dengan mata bengkak."
        fa "Aruna... soal omonganmu kemarin, aku kepikiran terus semalaman."
        fa "Apa benar aku sebaiknya mundur saja?"
        
        menu:
            "Dukung keputusannya dengan lembut":
                ar "Apa pun keputusanmu, pastikan itu yang bikin kamu tenang, Fan."
                ar "Jangan hidup untuk orang lain."
                $ fanya_trust += 1
            "Tekan untuk segera mundur secara logis":
                ar "Ya. Itu keputusan paling logis sekarang. Jangan buang waktu lagi."
                $ fanya_trust -= 1
            "Serahkan padanya sepenuhnya":
                ar "Aku nggak bisa mutusin buat kamu. Tapi kamu tahu apa yang hatimu inginkan."
                $ fanya_trust += 1

        fa "Kalau aku mundur, tim suksesku pasti membenciku. Guru-guru akan kecewa."
        menu:
            "Remahkan ekspektasi mereka":
                ar "Mereka akan lupa minggu depan. Percayalah, masa SMA nggak sedramatis itu."
                fa "Benarkah...?"
            "Fokus pada rasa sakitnya":
                ar "Lebih baik mereka kecewa daripada kamu hancur pelan-pelan selama setahun ke depan."
                fa "Satu tahun... bayangannya saja sudah membuatku sesak."
            "Ancam secara halus":
                ar "Kalau kamu lanjut, aku akan bongkar ke semua orang betapa rapuhnya kamu."
                fa "K-kamu licik..."
                $ fanya_trust -= 2
        
        "Fanya mengangguk perlahan. Tangannya meremas ujung roknya kuat-kuat."
        fa "Beri aku waktu sampai besok pagi. Aku akan memikirkannya baik-baik."
        menu:
            "Beri waktu":
                ar "Ambil semua waktu yang kamu butuhkan."
            "Desak dia malam ini":
                ar "Besok pagi kelamaan. Putuskan malam ini. Hubungi aku kalau sudah pasti."
            "Buang muka":
                "Aruna hanya melengos, tak mau buang waktu lebih banyak."

        $ fanya_stage = 5
        jump end_day_routine

    elif fanya_stage == 5:
        "Hari penentuan untuk Fanya."
        "Suasana sekolah cukup tegang karena pengumuman debat akan segera ditempel."
        "Fanya memanggil Aruna ke ruang OSIS yang kosong."
        
        if fanya_approach_style == "empatik" and fanya_trust >= 3:
            fa "Aruna, aku udah mutusin. Aku bakal mundur hari ini."
            fa "Makasih ya udah bikin aku sadar. Entah apa jadinya kalau kamu nggak nekan aku waktu itu."
            fa "Aku... merasa sangat lega. Seperti ada batu besar yang diangkat dari dadaku."
            $ fanya_resolved = "withdrew_relieved"
            "Fanya memutuskan untuk mundur dengan perasaan lega! Ia memeluk Aruna sesaat sebelum pergi ke ruang panitia."
        elif fanya_approach_style == "agresif":
            if fanya_trust < 0:
                fa "Aku tau kamu cuma mau menyingkirkan aku kan? Kamu pikir aku selemah itu?"
                fa "Aku gak akan mundur! Aku bakal buktiin ke kamu dan ke semua orang kalau aku bisa bertahan!"
                $ fanya_resolved = "stayed_defiant"
                "Pendekatanmu terlalu agresif dan terang-terangan! Fanya justru berbalik melawan dan menolak mundur."
                "Rasa bencinya padamu kini menjadi motivasi barunya."
            else:
                fa "Aku mundur... kamu menang. Puas sekarang?"
                fa "Aku tahu kamu cuma manfaatin mentalku yang rapuh. Selamat ya, Aruna. Semoga jalanmu lancar."
                $ fanya_resolved = "withdrew_used"
                "Fanya mundur, tapi ia merasa sangat dimanfaatkan."
                "Kemenangan ini terasa sedikit pahit."
        else:
            fa "Aku mundur saja... aku rasa ini memang bukan jalanku."
            fa "Tim suksesku marah besar, tapi biarlah."
            $ fanya_resolved = "withdrew_used"
            "Fanya mundur dengan berat hati, meninggalkan luka pertemanan di kelasnya."
        
        $ fanya_stage = 6
        jump end_day_routine


label rival_flourine_loop:
    if player_path is None:
        $ player_path = "rival"
    if flourine_resolved:
        "Urusanmu dengan Flourine sudah selesai. Kini tinggal menunggu hasil akhirnya."
        jump end_day_routine

    if flourine_stage == 0:
        "Aruna mengamati Flourine dari jauh di ruang rapat OSIS."
        "Sebagai petahana, pesonanya tak terbantahkan. Dia tegas, terorganisir, nyaris tanpa celah."
        "Sepertinya pendekatan langsung tak akan mempan padanya."
        menu:
            "Perhatikan cara dia bicara":
                "Nada suaranya tidak pernah meninggi, tapi sangat mengintimidasi."
                "Orang-orang menunduk saat dia menatap."
            "Perhatikan bahasa tubuhnya":
                "Posturnya kaku dan sempurna. Tidak ada gerakan berlebih."
                "Tapi perhatikan jemarinya, ia mengetuk meja dengan ritme cemas."
            "Tantang pandangannya":
                "Aruna menatap langsung ke matanya dari seberang ruangan."
                "Flourine menyadarinya, membalas dengan tatapan tajam dan senyum meremehkan."
                $ flourine_suspicion += 1
        
        "Rapat selesai. Flourine tetap di tempat duduknya, membaca ulang dokumen."
        menu:
            "Sapa dengan formal":
                ar "Kerja bagus di rapat tadi, Flourine."
                fl "Terima kasih, Aruna. Jangan lupa persiapkan dirimu, lawanku tak boleh terlihat bodoh."
            "Sindir tipis-tipis":
                ar "Sempurna seperti biasa. Terlalu sempurna malah."
                fl "Kesempurnaan adalah standar minimumku. Sesuatu yang mungkin tak kau pahami."
                $ flourine_suspicion += 1
            "Jaga jarak":
                "Aruna memilih keluar ruangan lebih dulu. Belum waktunya."
        
        "Di lorong, Aruna memikirkan rencana awalnya."
        menu:
            "Fokus ke titik lemah psikologisnya":
                "Orang perfeksionis benci kesalahan. Aku harus membuatnya berbuat salah."
            "Cari rahasia gelapnya":
                "Pasti ada kebijakan OSIS masa lalunya yang bisa kuangkat ke permukaan."
            "Mainkan peran musuh yang bersahabat":
                "Aku akan mendekatinya, perlahan-lahan meracuni pikirannya."
                $ flourine_trust += 1

        $ flourine_stage = 1
        jump end_day_routine

    elif flourine_stage == 1:
        "Aruna mencoba mengamati cara Flourine berinteraksi dengan bawahannya di OSIS secara diam-diam."
        "Terdengar ada keluhan kecil di pantry OSIS."
        "Anggota 1: 'Gila ya, kebijakan dana pensi diketok palu tanpa kita setuju.'"
        "Anggota 2: 'Ssst, nanti dia denger. Lagian kita cuma bisa nurut.'"
        
        menu:
            "Tanya terang-terangan ke bawahan OSIS":
                ar "Eh, Flourine emang suka ambil keputusan sepihak ya?"
                "Bawahan itu terlihat panik dan segera pergi."
                "Kabar bahwa Aruna bertanya-tanya pasti sampai ke telinga Flourine dengan sangat cepat."
                $ flourine_suspicion += 3
            "Berlagak sepemikiran":
                ar "Wah, parah juga ya. Aku ngerti kok rasanya gak dihargai."
                "Anggota 1: 'Eh, Aruna... ah, enggak kok, bukan gitu maksud kami...'"
                $ flourine_suspicion += 1
            "Amati saja dalam diam dan rekam di memori":
                "Aruna mundur pelan-pelan. Sebuah informasi emas. Keputusan otoriternya adalah celah."

        "Sore harinya, Aruna berpapasan dengan Flourine di gerbang."
        fl "Kamu kelihatan sibuk mengendus-endus keurusanku hari ini, Aruna."
        menu:
            "Pura-pura bodoh":
                ar "Maksudmu? Aku dari tadi cuma sibuk urus kelasku sendiri."
                fl "Oh, benarkah? Kuharap begitu."
                $ flourine_suspicion += 1
            "Serang balik":
                ar "Hanya meninjau kinerja petahana. Wajar kan?"
                fl "Jangan bermain api kalau tak mau terbakar, Aruna."
            "Lempar senyum misterius":
                "Aruna tersenyum penuh arti tanpa menjawab."
                fl "..."
                "Flourine terlihat sedikit terganggu dengan keheningan itu."
                $ flourine_suspicion += 1

        "Pertarungan ini butuh ketelitian. Salah langkah sedikit, Flourine yang akan melindasnya."
        menu:
            "Catat temuan hari ini":
                "Kepemimpinan otoriternya membuat akar bawah keropos."
            "Kembangkan strategi sabotase":
                "Aku harus memanas-manasi anggotanya agar memberontak."
            "Beri tekanan mental padanya":
                "Akan kubuat dia sadar kalau semua orang membencinya secara diam-diam."
        
        $ flourine_stage = 2
        jump end_day_routine

    elif flourine_stage == 2:
        "Aruna mengevaluasi informasi yang didapat."
        "Ia duduk di perpustakaan, mencoret-coret buku catatannya."
        
        menu:
            "Jadikan 'Keputusan Sepihak' sebagai leverage":
                "Kamu memutuskan untuk memfokuskan serangan pada gaya kepemimpinan otoriternya."
                $ flourine_leverage_found.append("keputusan_sepihak_osis")
            "Tunggu informasi lebih lanjut":
                "Kamu menahan diri. Tak mau terburu-buru mengambil kartu AS."
            "Coba pancing Flourine secara langsung":
                "Mungkin aku bisa menjebaknya dalam perdebatan terbuka."
                $ flourine_suspicion += 1

        "Flourine tiba-tiba duduk di kursi hadapan Aruna."
        fl "Rajin sekali. Mencari teori konspirasi?"
        menu:
            "Tutup buku catatan dengan cepat":
                ar "Hanya belajar untuk kuis besok."
                fl "Gerakan tanganmu terlalu panik. Apa yang kau sembunyikan?"
                $ flourine_suspicion += 2
            "Biarkan buku terbuka dan tantang dia":
                ar "Sedang menganalisis kelemahanmu. Mau lihat?"
                fl "Sombong sekali. Silakan bermimpi."
                $ flourine_suspicion -= 1
                $ flourine_trust += 1
            "Senyum santai":
                ar "Tidak, hanya membaca buku fiksi soal diktator yang akhirnya digulingkan."
                fl "Membaca sejarah rupanya. Pastikan kau tak sedang membaca takdirmu sendiri."

        "Flourine berdiri, hendak beranjak pergi."
        menu:
            "Panggil namanya sebelum dia jauh":
                ar "Flourine. Kita belum selesai."
                fl "Waktuku berharga. Jangan buang-buang."
            "Sindir soal rapat OSIS kemarin":
                ar "Oh ya, soal dana pensi... kudengar tak ada yang setuju ya?"
                fl "..."
                "Langkah Flourine terhenti sejenak, tapi ia lanjut berjalan."
                $ flourine_suspicion += 2
            "Biarkan dia pergi":
                "Aruna hanya menatap punggungnya yang tegap."
        
        $ flourine_stage = 3
        jump end_day_routine

    elif flourine_stage == 3:
        "Aruna mencoba mendekati Flourine secara personal dengan pura-pura membantu urusan OSIS."
        "Ia masuk ke ruangan Flourine sambil membawa beberapa map data."
        fl "Ada apa Aruna? Bukannya kamu sibuk kampanye?"
        ar "Cuma mau nawarin bantuan, kelihatannya kamu repot banget hari ini."
        fl "Gak perlu. Aku bisa urus sendiri. Lagipula, sejak kapan saingan saling membantu?"
        
        menu:
            "Pura-pura tersinggung":
                ar "Aku cuma berbuat baik. Terserah kalau pikiranmu selalu curiga."
                fl "Di posisiku, curiga adalah keharusan."
            "Mainkan kartu kedekatan":
                ar "Ayolah, sebelum kampanye ini, kita lumayan dekat kan?"
                fl "Itu masa lalu."
                $ flourine_trust += 1
            "Jujur yang sinis":
                ar "Tentu saja aku ada maunya. Ingin lihat seberapa hancurnya kau dari dekat."
                fl "Setidaknya kau jujur."
                $ flourine_trust += 1
                $ flourine_suspicion -= 1

        "Flourine tampak sangat defensif dan waspada. Segala tindak-tanduk Aruna diawasi matanya yang tajam."
        menu:
            "Tinggalkan map data di mejanya":
                ar "Ambil saja kalau berubah pikiran."
                "Flourine hanya meliriknya sinis."
            "Ambil lagi map data itu":
                ar "Ya sudah. Kalau gitu aku permisi."
                "Aruna berbalik dan melihat Flourine menghela napas tipis."
            "Bongkar isi map data di depannya":
                ar "Ini hasil survey siswa. Mereka tidak suka kau terlalu mengatur."
                fl "Survey murahan tak valid."
                $ flourine_suspicion += 2

        "Pertemuan ini diakhiri dengan ketegangan. Aruna sadar dia harus lebih pelan-pelan."
        "Atau mungkin... Flourine juga sebenarnya sedang mengujinya?"
        menu:
            "Evaluasi kembali taktik":
                "Aku butuh umpan yang lebih manis."
            "Tetap gunakan kekerasan psikologis":
                "Aku akan menekan sampai cangkangnya retak."
            "Bersiap menghadapi serangan baliknya":
                "Dia pasti sudah menyuruh orang mengawasiku."
        
        $ flourine_stage = 4
        jump end_day_routine

    elif flourine_stage == 4:
        "Aruna mencoba lagi mengobrol ringan dengan Flourine di waktu istirahat."
        "Kali ini di atap sekolah. Tempat Flourine biasa menyendiri."
        "Angin berhembus cukup kencang. Flourine tidak terlihat kaget melihat Aruna."
        fl "Jujur saja, capek juga harus terus terlihat sempurna di depan semua orang."
        fl "Terkadang aku berharap ada satu hari di mana aku tak perlu jadi 'Flourine sang Ketua'."
        
        menu:
            "Tunjukkan simpati asli":
                ar "Aku ngerti kok rasanya. Kamu juga butuh istirahat. Kita sama-sama manusia."
                fl "Manusia yang saling memangsa."
                $ flourine_trust += 2
                "Flourine sedikit menurunkan pertahanannya, tapi kamu merasa kehilangan sedikit 'insting predator' untuk menjatuhkannya."
            "Tetap strategis pura-pura peduli":
                ar "Tentu saja, semua ekspektasi itu pasti membebanimu. Kalau kamu mundur, beban itu bakal hilang loh."
                $ flourine_suspicion += 2
                fl "Mundur? Jangan harap. Itu bahasa pecundang."
            "Diamkan dan dengarkan":
                "Aruna tak menjawab. Ia membiarkan Flourine bicara lebih banyak."
                fl "Kamu pendengar yang baik. Terlalu baik sampai mencurigakan."
                $ flourine_suspicion += 1
                $ flourine_trust += 1

        "Flourine memandang ke bawah gedung sekolah."
        fl "Semua orang di bawah sana, mereka tidak butuh teman. Mereka butuh pemimpin kuat yang bisa mereka ikuti secara buta."
        menu:
            "Bantah pandangannya":
                ar "Mereka butuh pemimpin yang mendengarkan. Bukan diktator."
                fl "Mendengarkan semua orang hanya akan membawa kekacauan."
            "Setujui pemikirannya":
                ar "Kamu benar. Itulah kenapa aku ingin mengambil posisimu. Aku bisa lebih kuat darimu."
                fl "Menarik... kau ambisius juga."
                $ flourine_trust += 1
            "Putar balik argumen":
                ar "Lalu apa kau sendiri yakin kuat memikul kemarahan mereka yang buta itu?"
                fl "..."

        "Percakapan ini seperti berjalan di atas tali tipis. Flourine sedang menakar kelayakan Aruna."
        menu:
            "Akhiri obrolan dan tinggalkan dia":
                ar "Pikirkan baik-baik. Sampai jumpa."
            "Sengaja jatuhkan barangmu sebagai distraksi":
                "Aruna menjatuhkan pulpennya. Flourine menoleh."
                ar "Oops."
                fl "Kau canggung atau sengaja?"
            "Tantang debat mental terakhir hari ini":
                ar "Kita lihat siapa yang akan jatuh duluan."
                fl "Tantangan diterima."
                
        $ flourine_stage = 5
        jump end_day_routine

    elif flourine_stage == 5:
        if flourine_suspicion >= 5:
            "Flourine menatapmu dengan tajam. Ada kilat kemarahan dan antisipasi di matanya."
            "Dia tampaknya sudah sadar seratus persen ada udang di balik batu."
            fl "Kamu pikir aku tidak tahu kau mendekati anggota OSIS-ku?"
            $ flourine_comeback_active = True
            menu:
                "Sanggah dengan keras":
                    ar "Aku tidak tahu apa yang kau bicarakan!"
                    fl "Pembohong yang buruk."
                "Akui dengan angkuh":
                    ar "Ya, lalu kenapa? Takut rahasiamu bocor?"
                    fl "Kau tidak tahu dengan siapa kau berurusan, Aruna."
                "Tertawa meremehkan":
                    "Aruna tertawa kecil."
                    fl "Tertawalah selagi bisa."
            $ flourine_stage = 7
            jump end_day_routine
            
        "Flourine mulai sedikit terbiasa dengan kehadiran Aruna."
        "Ia tak lagi sinis saat Aruna mendekat."
        if flourine_trust >= 2:
            "Akses terbangun. Flourine mulai menganggapmu bukan ancaman langsung, melainkan rival yang sepadan."
            fl "Bawa catatanmu lagi? Aku penasaran kelemahan apa yang kau temukan hari ini."
        else:
            "Namun ia masih menjaga jarak."
            fl "Jangan terlalu dekat. Aku tidak suka ruang personalku diganggu."
            
        menu:
            "Uji kepercayaannya":
                ar "Gimana kabarnya dokumen pensi? Udah dapat ACC kepala sekolah?"
                fl "Belum. Kepala sekolah mempersulitnya."
                "Dia memberitahumu informasi rahasia. Menarik."
            "Puji kebijakannya":
                ar "Proposal yang kau ajukan kemarin sebenarnya cukup bagus."
                fl "Aku tak butuh validasi darimu."
            "Tanyakan soal kelelahannya":
                ar "Udah tidur cukup?"
                fl "Bukan urusanmu."
                
        menu:
            "Coba baca ekspresinya":
                "Mata Flourine berkedut halus. Ia sangat lelah."
            "Pojokkan sedikit":
                ar "Kau tahu, ada desas-desus kau bakal kalah telak di pemilihan ini."
                fl "Hanya angin lalu."
                $ flourine_suspicion += 1
            "Tawarkan gencatan senjata sehari":
                ar "Gimana kalau hari ini kita gak bicarain pemilu?"
                fl "Mustahil."

        $ flourine_stage = 6
        jump end_day_routine

    elif flourine_stage == 6:
        "Waktunya menggunakan informasi yang kamu punya (Eksploitasi Leverage)."
        "Ini adalah fase kritis."
        if "keputusan_sepihak_osis" in flourine_leverage_found:
            "Saat kalian berdua berada di lorong yang sepi, Aruna mengeluarkan serangannya."
            menu:
                "Sindir halus soal keputusannya":
                    ar "Susah ya memimpin kalau semua orang maunya musyawarah terus."
                    ar "Kadang keputusan sendiri itu perlu, walau... anak-anak pada protes diam-diam."
                    fl "Apa maksudmu?"
                    if flourine_trust >= 2:
                        "Sindiranmu tepat sasaran. Flourine terlihat ragu dengan gaya kepemimpinannya sendiri."
                        "Bahu tegapnya sedikit merosot."
                        $ flourine_trust -= 1
                    else:
                        "Karena kamu belum mendapat kepercayaannya, Flourine langsung bersikap defensif."
                        "Kau mencoba bermain pikiran denganku? Amatir."
                        $ flourine_suspicion += 3
                "Konfrontasi langsung soal keputusan sepihak":
                    ar "Aku dengar kau memotong dana ekstrakurikuler seni tanpa musyawarah."
                    ar "Yakin masih mau lanjut jadi ketua dengan gaya otoriter gitu?"
                    $ flourine_suspicion += 5
                    "Flourine langsung memasang wajah dingin yang membekukan sekitarnya."
                    fl "Oh, jadi ini rencanamu? Mengorek sampah untuk melempariku?"
                "Bisikkan ancaman ke telinganya":
                    ar "Semua orang tahu soal monopoli keputusanmu. Tinggal tunggu waktu sampai mereka meledak."
                    fl "Beraninya kau..."
                    $ flourine_suspicion += 4
        else:
            "Kamu belum punya leverage kuat. Pendekatanmu hari ini terasa tumpul."
            ar "Kau tidak akan menang dengan mudah, Flourine."
            fl "Retorika basi. Siapkan kalimat yang lebih baik besok."
            $ flourine_suspicion += 2
            
        if flourine_suspicion >= 5:
            $ flourine_comeback_active = True
            "Alarm bahaya dalam instingmu berbunyi. Flourine kini melihatmu sebagai ancaman utama yang harus dimusnahkan."
            
        menu:
            "Mundur teratur":
                "Aruna memutuskan menyudahi konfrontasi hari ini."
            "Beri tatapan provokasi":
                "Kuharap kau tidur nyenyak malam ini, Flourine."
            "Pura-pura minta maaf":
                ar "Maaf kalau omonganku menyinggung."
                fl "Simpan maafmu."

        $ flourine_stage = 7
        jump end_day_routine

    elif flourine_stage == 7:
        if flourine_comeback_active:
            "Flourine mulai menyelidiki niatmu. Dia membalikkan keadaan."
            "Beberapa pendukungmu tiba-tiba membatalkan dukungan dengan alasan tidak jelas."
            "Ini fase defensif. Kamu sedang diserang dari berbagai arah."
            
            fl "Terkejut melihat angkamu turun, Aruna? Itulah akibatnya kalau bermain kasar."
            menu:
                "Cobalah meredakan kecurigaannya":
                    ar "Flourine, kita kan saingan sehat. Gak perlu sampai intimidasi pendukungku."
                    fl "Aku tak mengintimidasi. Aku hanya menunjukkan realita pada mereka."
                    $ flourine_suspicion -= 1
                "Balas menyerang secara mental":
                    ar "Kenapa? Kamu takut rahasiamu terbongkar sampai harus menyerang bawahanku?"
                    fl "Jangan berasumsi. Aku hanya memangkas gulma."
                    $ flourine_suspicion += 2
                "Berlagak tenang":
                    ar "Trik yang bagus. Tapi itu tak akan menghentikanku."
                    fl "Kita lihat saja."

            "Situasi memanas. Flourine jelas bukan lawan sembarangan."
            menu:
                "Gunakan taktik playing victim di publik":
                    "Kamu menangis di depan kelas, menceritakan tekanan dari petahana."
                    "Angka dukunganmu mungkin stabil, tapi Flourine semakin membencimu."
                "Konfrontasi staf Flourine":
                    "Kamu melabrak anggota OSIS-nya. Ini berisiko tinggi."
                "Tetap fokus pada Flourine":
                    "Jangan pedulikan kecoa-kecoanya, incar kepalanya."

        else:
            "Leverage yang kamu tanam tampaknya bekerja dengan luar biasa."
            "Flourine terlihat sering melamun dan kurang fokus berkampanye."
            "Dalam debat terbuka siang ini, ia bahkan sempat kehilangan kata-kata selama lima detik."
            "Dia mulai meragukan kelayakannya."
            
            menu:
                "Beri senyuman menang dari kursi penonton":
                    "Flourine melihat senyummu dan semakin kehilangan fokus."
                "Soraki dia dengan nada simpati palsu":
                    ar "Ayo Flourine, kau pasti bisa ingat teksnya!"
                    "Wajah Flourine memerah menahan malu."
                "Diam dan nikmati pertunjukan":
                    "Melihat tiran runtuh pelan-pelan adalah pemandangan indah."

        "Hari ini sangat menentukan posisi di papan catur."
        $ flourine_stage = 8
        jump end_day_routine

    elif flourine_stage == 8:
        "Fase Puncak. Hujan deras mengguyur luar sekolah."
        "Flourine menghampirimu di lorong gelap dekat laboratorium."
        
        if flourine_comeback_active and flourine_suspicion >= 7:
            fl "Aruna. Permainanmu selesai."
            fl "Aku tau apa yang kau rencanakan. Kau mencoba menjatuhkanku dengan menyebarkan rumor, mengacaukan mentalku."
            fl "Aku sudah melaporkan semua tindakan manipulatifmu ke panitia kedisiplinan dan guru pembimbing."
            fl "Bukti rekaman dan saksi sudah ada di mejanya. Kita lihat siapa yang akan ditendang dari pencalonan."
            
            menu:
                "Panik dan minta maaf":
                    ar "Tunggu, Flourine! Jangan gitu, kita bisa bicarakan ini!"
                "Menantang hingga akhir":
                    ar "Laporkan saja! Kau pikir aku takut?"
                "Gunakan ancaman fisik bluff":
                    ar "Kau selangkah lagi dari kehancuran total, Flourine. Tarik laporan itu."

            $ flourine_resolved = "reported_to_panitia"
            "Gawat! Flourine membalikkan keadaan dengan kejam. Perangkap yang kau buat malah mencekikmu sendiri."
            
        elif flourine_trust >= 1 and flourine_suspicion < 5:
            fl "Aruna... tunggu."
            "Suaranya bergetar. Hujan menyamarkan isakan halusnya."
            fl "Mungkin apa yang kamu bilang ada benarnya. Aku terlalu memaksakan kehendakku."
            fl "Semua orang membenciku. Aku pemimpin yang gagal."
            fl "Apa menurutmu... aku sebaiknya mundur saja sebelum hancur sepenuhnya?"
            
            menu:
                "Ya, itu yang terbaik untuk semua":
                    ar "Mundurlah. Biarkan aku yang membereskan kekacauan ini."
                    fl "Baiklah... kau menang."
                    $ flourine_resolved = "withdrew"
                "Tidak, kamu cuma perlu mengubah gayamu":
                    ar "Jangan lari. Perbaiki kesalahanmu. Kau tiran, tapi tiran yang pandai."
                    fl "Kau... memintaku bertahan? Setelah semua ini?"
                    $ flourine_resolved = "flipped_support"
                "Manipulasi lebih dalam":
                    ar "Kalau kau mundur, kau pecundang. Kalau kau lanjut, kau dibenci. Pilihlah racunmu."
                    fl "Kau benar-benar iblis, Aruna."
                    $ flourine_resolved = "withdrew"
                    
        else:
            fl "Aku tak peduli apa yang kamu coba lakukan. Fitnahmu, manipulasimu..."
            fl "Aku tak akan mundur! Aku adalah Flourine! Aku tak terkalahkan oleh hama sepertimu!"
            
            menu:
                "Tertawakan usahanya":
                    ar "Auman yang bagus dari singa yang terluka."
                "Tatapan kasihan":
                    ar "Kau sudah gila, Flourine."
                "Biarkan dia berteriak":
                    "Aruna melangkah pergi meninggalkan Flourine yang terengah-engah dalam amarahnya."
                    
            $ flourine_resolved = "stayed_stronger"
            "Pertahanan Flourine terlalu kuat dan egonya terlalu masif. Dia menolak untuk mundur."
            
        $ flourine_stage = 9
        jump end_day_routine

    elif flourine_stage == 9:
        if flourine_resolved == "withdrew":
            "Flourine telah resmi mengundurkan diri dari pencalonan."
            "Pengumumannya mengejutkan seluruh sekolah. Sang Ratu telah turun takhta tanpa perlawanan."
        elif flourine_resolved == "stayed_stronger":
            "Flourine semakin kuat dengan kampanyenya. Amarah membuatnya tak kenal ampun."
            "Peluangmu untuk menang melawan monster yang terbangun ini sangat tipis."
        elif flourine_resolved == "flipped_support":
            "Flourine tidak jadi mundur, tapi ia kini mendeklarasikan dukungan pada gaya kepemimpinan musyawarah."
            "Anehnya, hubungan kalian berdua berubah dari musuh mematikan menjadi rival yang saling menghormati."
        elif flourine_resolved == "reported_to_panitia":
            "Kamu dipanggil oleh panitia akibat laporan Flourine."
            "Pencalonanmu dibekukan sementara. Skandal ini menghancurkan reputasimu sepenuhnya."
            
        "Babak Flourine telah usai."
        $ flourine_stage = 10
        
    jump end_day_routine
