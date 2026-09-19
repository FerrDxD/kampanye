screen npc_choice(items):
    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#09090be6") # Zinc-950 semi-transparent
        padding (50, 50)
        
        vbox:
            spacing 40
            xalign 0.5
            
            # Subtle section title
            text "SELECT DESTINATION" size 20 color "#a1a1aa" kerning 2.0 xalign 0.5 bold True
            
            hbox:
                box_wrap True
                box_wrap_spacing 20
                spacing 20
                xalign 0.5
                xmaximum 1100
                
                for i in items:
                    textbutton i.caption:
                        action i.action
                        text_size 24
                        text_color "#fafafa" # Zinc-50
                        text_hover_color "#ffffff"
                        text_align 0.5
                        background Solid("#18181b") # Zinc-900
                        hover_background Solid("#27272a") # Zinc-800
                        padding (20, 20)
                        xsize 500
                        ysize 80

screen school_map():
    add Transform("bg_school_map.jpg", size=(1920, 1080))
    
    # Title overlay
    frame:
        xalign 0.5 ypos 20
        background Solid("#000000aa")
        padding (20, 10)
        text "PETA SEKOLAH - Pilih Lokasi" size 40 color "#ffffff" bold True

    # Floating location buttons
    textbutton "Gerbang Depan":
        action Return("loc_gerbang")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#2c3e50cc")
        padding (15, 10)
        xpos 100 ypos 800

    textbutton "Lapangan Olahraga":
        action Return("loc_lapangan")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#27ae60cc")
        padding (15, 10)
        xpos 350 ypos 300

    textbutton "Laboratorium":
        action Return("loc_lab")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#2980b9cc")
        padding (15, 10)
        xpos 1400 ypos 550

    textbutton "Perpustakaan":
        action Return("loc_perpus")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#d35400cc")
        padding (15, 10)
        xpos 1500 ypos 300

    textbutton "Ruang OSIS":
        action Return("loc_osis")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#c0392bcc")
        padding (15, 10)
        xpos 900 ypos 300

    textbutton "Koridor Ekskul":
        action Return("loc_ekskul")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#8e44adcc")
        padding (15, 10)
        xpos 250 ypos 600

    textbutton "Aula Utama":
        action Return("loc_aula")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#f39c12cc")
        padding (15, 10)
        xpos 100 ypos 350

    textbutton "UKS":
        action Return("loc_uks")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#16a085cc")
        padding (15, 10)
        xpos 800 ypos 550

    textbutton "Markas Pramuka":
        action Return("loc_pramuka")
        text_size 25 text_color "#ffffff" text_bold True text_align 0.5
        background Solid("#7f8c8dcc")
        padding (15, 10)
        xpos 1100 ypos 700

    # System Buttons (Bottom Right)
    vbox:
        xalign 0.95 yalign 0.95
        spacing 15
        
        if robotika_unique_quest_status in ["available", "pending"]:
            textbutton "MISI ROBOTIKA (Malam)":
                action Return("heist")
                text_size 25 text_color "#ffffff" text_bold True
                background Solid("#e74c3ccc")
                padding (20, 15)

        textbutton "Pulang ke Rumah":
            action Return("pulang")
            text_size 25 text_color "#ffffff" text_bold True
            background Solid("#34495ecc")
            padding (20, 15)
            
        textbutton "Mundur (Menyerah)":
            action Return("mundur")
            text_size 25 text_color "#ffffff" text_bold True
            background Solid("#c0392bcc")
            padding (20, 15)


label loc_gerbang:
    scene expression Transform("images/bg_gerbang.jpg", size=(1920, 1080))
    "Aruna berdiri di dekat gerbang depan sekolah."
    "Suasana di sini cukup sepi, hanya ada beberapa siswa yang baru datang atau bersiap pulang."
    menu (screen="npc_choice"):
        "Tunggu, sepertinya tidak ada siapa-siapa di sini yang bisa diajak bicara soal kampanye."
        "Kembali ke Peta":
            jump map_navigation

label loc_lapangan:
    scene expression Transform("images/bg_lapangan.jpg", size=(1920, 1080))
    "Suasana lapangan sangat ramai. Matahari bersinar terik, dan beberapa ekskul olahraga terlihat sedang berlatih keras."
    "Suara peluit dan teriakan semangat terdengar bersahut-sahutan."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Lapangan?"
        
        "Anggun (Anggota Karate)" if npc_state["anggun"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_anggun
            
        "Lulu (Ketua Karate)" if npc_state["lulu"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_lulu
            
        "Cecillia (Ketua Badminton)" if npc_state["cecillia"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_cecillia
            
        "Aulia (Ketua Paskibra)" if npc_state["aulia"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_aulia

        "Kembali ke Peta":
            jump map_navigation


label loc_ekskul:
    scene expression Transform("images/bg_ekskul.jpg", size=(1920, 1080))
    "Lorong ruang ekskul terasa hidup. Kamu bisa mendengar alunan alat musik dari ruang akustik, serta bunyi ketikan keyboard dari ruang jurnalistik."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Ruang Ekskul?"

        "Adam (Ketua Jurnalistik)" if npc_state["adam"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_adam
            
        "Adi (Anggota Jurnalistik)" if npc_state["adi"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_adi

        "Yura (Anggota Jurnalistik)" if npc_state["yura"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_yura

        "Ami (Anggota Jurnalistik)" if npc_state["ami"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_ami

        "Inez (Anggota Seni)" if npc_state["inez"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_inez

        "Nayra (Ketua Akustik)" if npc_state["nayra"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_nayra

        "Kembali ke Peta":
            jump map_navigation


label loc_lab:
    scene expression Transform("images/bg_lab.jpg", size=(1920, 1080))
    "Area laboratorium sains dan teknologi. Suasananya lebih tenang dan dipenuhi siswa yang sedang fokus pada eksperimen mereka."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Laboratorium?"

        "Ferdi (Ketua Robotika)" if npc_state["ferdi"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_ferdi

        "Juan (Anggota Robotika)" if npc_state["juan"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_juan

        "Faizal (Anggota Robotika)" if npc_state["faizal"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_faizal

        "Lukman (Ketua Zoologi)" if npc_state["lukman"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_lukman

        "Kembali ke Peta":
            jump map_navigation


label loc_perpus:
    scene expression Transform("images/bg_perpus.jpg", size=(1920, 1080))
    "Perpustakaan sekolah yang hening. Aroma buku tua dan kertas mendominasi ruangan ini."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Perpustakaan?"

        "Ellisa (Anggota Math Club)" if npc_state["ellisa"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_ellisa

        "Bagus (Pustakawan)" if npc_state["bagus"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_bagus

        "Kembali ke Peta":
            jump map_navigation


label loc_osis:
    scene expression Transform("images/bg_osis.jpg", size=(1920, 1080))
    "Selasar di depan Ruang OSIS. Pusat pemerintahan sekolah di mana segala keputusan krusial diambil. Para kandidat dan anggota inti sering berkumpul di sini."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Ruang OSIS?"
        
        "Fanya (Kandidat OSIS)" if player_path == None or player_path == "rival":
            if player_path == None:
                $ player_path = "rival"
            jump rival_fanya_loop
            
        "Flourine (Ketua OSIS Petahana)" if player_path == None or player_path == "rival":
            if player_path == None:
                $ player_path = "rival"
            jump rival_flourine_loop

        "Kembali ke Peta":
            jump map_navigation


label loc_uks:
    scene expression Transform("images/bg_uks.jpg", size=(1920, 1080))
    "Unit Kesehatan Sekolah (UKS). Beberapa siswa terlihat sedang beristirahat, sementara petugas piket sibuk merapikan obat-obatan."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di UKS?"

        "Desti (Ketua PMR)" if npc_state["desti"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_desti

        "Kembali ke Peta":
            jump map_navigation


label loc_aula:
    scene expression Transform("images/bg_aula.jpg", size=(1920, 1080))
    "Aula Utama sekolah. Sering digunakan untuk seminar, forum, dan acara besar. Saat ini sedang ada perkumpulan kecil di sudut ruangan."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Aula?"

        "Ayya (Ketua FPSH)" if npc_state["ayya"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_ayya

        "Kembali ke Peta":
            jump map_navigation


label loc_pramuka:
    scene expression Transform("images/bg_pramuka.jpg", size=(1920, 1080))
    "Markas Pramuka (Dewan Ambalan). Penuh dengan peralatan kemah, tali temali, dan papan tulis yang penuh dengan jadwal kegiatan."
    menu (screen="npc_choice"):
        "Siapa yang ingin kamu temui di Markas Pramuka?"

        "Angga (Dewan Ambalan)" if npc_state["angga"]["quest_status"] in ["not_started", "in_progress"] and (player_path == None or player_path == "support"):
            if player_path == None:
                $ player_path = "support"
            jump quest_angga

        "Kembali ke Peta":
            jump map_navigation
