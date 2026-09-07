################################################################################
## Inisialisasi
################################################################################

init offset = -1


################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Layar In-game
################################################################################


## Layar Say ###################################################################
##
## Layar say di gunakan untuk menampilkan dialog kepada pemain. Ini menggunakan
## dua parameter, who dan what, yang merupakan nama karakter yang berbicara dan
## text yang akan di tampilkan, masing-masing. (Kedua parameter dapat berisi
## None jika tidak ada nama yang di berikan.
##
## Layar ini harus membuat text yang dapat di tampilkan dengan id "what", yang
## di mana Ren'Py menggunakan ini untuk mengatur tampilan text. Ini juga dapat
## membuat sesuatu yang dapat di tampilkan dengan id "who" dan id "window" untuk
## mengaplikasikan properti gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jika ada gambar di sisi, tampilkan di atas text. Jangan tampilkan di
    ## versi HP[Handphone)(Android) - Karena tidak ada ruang.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Solid("#09090be6") # Zinc-950 semi-transparent

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Solid("#18181b") # Zinc-900
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    color "#fafafa" # Zinc-50

style say_dialogue:
    properties gui.text_properties("dialogue")
    color "#d4d4d8" # Zinc-300

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Layar masukkan/input ########################################################
##
## Layar ini di gunakan untuk menampilkan renpy.input. Parameter prompt
## digunakan untuk meneruskan text yang di prompt/minta.
##
## Layar ini harus membuat input yang dapat di tampilkan dengan id "input" untuk
## menerima berbagai parameter masukan.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Layar Pilihan ###############################################################
##
## Layar ini digunakan untuk menampilkan pilihan dalam game yang disajikan oleh
## menu statement. Satu parameter, item, adalah daftar objek, masing-masing
## dengan bidang keterangan dan tindakan.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Solid("#18181be6") # Zinc-900
    hover_background Solid("#27272ae6") # Zinc-800
    padding (20, 15)
    margin (0, 5)

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    color "#a1a1aa" # Zinc-400
    hover_color "#fafafa" # Zinc-50
    size 24


## Layar Menu Cepat/Quick Menu #################################################
##
## Menu cepat ditampilkan dalam game untuk memudahkan akses ke menu di luar
## game.

screen quick_menu():

    ## Memastikan ini muncul di atas layar yang lain.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Kembali") action Rollback()
            textbutton _("Riwayat") action ShowMenu('history')
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Simpan") action ShowMenu('save')
            textbutton _("Simpan.C") action QuickSave()
            textbutton _("Muat.C") action QuickLoad()
            textbutton _("Setting") action ShowMenu('preferences')


## Kode ini memastikan layar quick_menu di tampilkan di dalam permainan,
## kapanpun player tidak secaralangsung menyembunyikan antarmuka.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Layar Menu Utama dan Menu Permainan
################################################################################

## Layar navigasi ##############################################################
##
## Layar ini di ikutsertakan di menu utama dan permainan, dan menyediakan
## navigasi ke menu lainnya, dan untuk memulai permainan.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Mulai") action Start()

        else:

            textbutton _("Riwayat") action ShowMenu("history")

            textbutton _("Simpan") action ShowMenu("save")

        textbutton _("Muat") action ShowMenu("load")

        textbutton _("Setting") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Akhiri Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu Utama") action MainMenu()

        textbutton _("Tentang") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Bantuan tidak perlu atau relevan dengan perangkat mobile.
            textbutton _("Bantuan") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Tombol keluar dilarang di iOS dan tidak diperlukan di Android dan
            ## Web.
            textbutton _("Keluar") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Layar Menu Utama - Cinematic Full-Screen ####################################
##
## Desain cinematic: full-screen background, gradient overlay,
## judul besar, navigasi minimalis di kiri bawah.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    tag menu

    ## Background full-screen
    add gui.main_menu_background

    ## Gradient overlay - gelap keseluruhan untuk kedalaman cinematic
    add Solid("#00000099")

    ## Gelapkan bagian bawah untuk depth
    add Solid("#000000aa")

    ## Navigasi - kiri bawah, layout vertikal
    vbox:
        style "main_menu_nav"

        textbutton _("Mulai"):
            action Start()
            style "main_menu_nav_button"

        textbutton _("Muat"):
            action ShowMenu("load")
            style "main_menu_nav_button"

        textbutton _("Setting"):
            action ShowMenu("preferences")
            style "main_menu_nav_button"

        textbutton _("Tentang"):
            action ShowMenu("about")
            style "main_menu_nav_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Bantuan"):
                action ShowMenu("help")
                style "main_menu_nav_button"

        if renpy.variant("pc"):
            textbutton _("Keluar"):
                action Quit(confirm=True)
                style "main_menu_nav_button"

    ## Title block - kanan bawah
    if gui.show_name:
        vbox:
            style "main_menu_title_block"

            text "[config.name!t]":
                style "main_menu_title"

            text "Visual Novel":
                style "main_menu_subtitle"

            text "[config.version]":
                style "main_menu_version"


## Style definitions - Cinematic Main Menu

style main_menu_nav is vbox:
    xpos 60
    yalign 1.0
    yoffset -50
    spacing 4

style main_menu_nav_button is gui_button:
    xsize 220
    ysize 52
    background Solid("#18181b")  # Zinc-900
    hover_background Solid("#27272a")  # Zinc-800
    selected_background Solid("#3f3f46")  # Zinc-700
    padding (24, 12, 24, 12)

style main_menu_nav_button_text is gui_button_text:
    font gui.interface_text_font
    size 22
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50
    selected_color "#ffffff"
    insensitive_color "#52525b"  # Zinc-600
    xalign 0.0

style main_menu_title_block is vbox:
    xalign 1.0
    yalign 1.0
    xoffset -60
    yoffset -50
    xmaximum 800
    spacing 6

style main_menu_title is gui_text:
    font gui.interface_text_font
    size 72
    color "#fafafa"  # Zinc-50
    bold True
    xalign 1.0
    outlines [(2, "#00000066", 0, 0)]

style main_menu_subtitle is gui_text:
    font gui.interface_text_font
    size 22
    color "#71717a"  # Zinc-500
    xalign 1.0

style main_menu_version is gui_text:
    font gui.interface_text_font
    size 16
    color "#52525b"  # Zinc-600
    xalign 1.0


## layar Menu Permainan ########################################################
##
## Ini menjalaskan struktur dasar yang paling sering di gunakan di layar menu
## permainan, ini ditampilkan beserta layar judul, dan menampilkan latar
## belakang,judul,dan navigasi.
##
## Parameter scroll dapat berisi 'None', atau "viewport" dan "vpgrid". Layar
## ini di maksudkan untuk di gunakan dengan cabang satu atau lebih, yang di
## tempatkan di dalamnya.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    tag menu

    ## Background full-screen
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    ## Gradient overlay - gelap keseluruhan untuk kedalaman cinematic
    add Solid("#00000099")

    ## Gelapkan bagian bawah untuk depth
    add Solid("#000000aa")

    ## Content area - tengah kanan
    frame:
        style "game_menu_content_container"

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    spacing spacing
                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                spacing spacing

                transclude

        else:

            transclude

    ## Navigasi - kiri bawah, layout vertikal
    vbox:
        style "game_menu_nav"

        if main_menu:
            textbutton _("Mulai"):
                action Start()
                style "game_menu_nav_button"
        else:
            textbutton _("Riwayat"):
                action ShowMenu("history")
                style "game_menu_nav_button"

            textbutton _("Simpan"):
                action ShowMenu("save")
                style "game_menu_nav_button"

        textbutton _("Muat"):
            action ShowMenu("load")
            style "game_menu_nav_button"

        textbutton _("Setting"):
            action ShowMenu("preferences")
            style "game_menu_nav_button"

        if _in_replay:
            textbutton _("Akhiri Replay"):
                action EndReplay(confirm=True)
                style "game_menu_nav_button"
        elif not main_menu:
            textbutton _("Menu Utama"):
                action MainMenu()
                style "game_menu_nav_button"

        textbutton _("Tentang"):
            action ShowMenu("about")
            style "game_menu_nav_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Bantuan"):
                action ShowMenu("help")
                style "game_menu_nav_button"

        if renpy.variant("pc"):
            textbutton _("Keluar"):
                action Quit(confirm=not main_menu)
                style "game_menu_nav_button"

    ## Title block - kanan atas
    if main_menu:
        vbox:
            style "game_menu_title_block"

            text "[config.name!t]":
                style "game_menu_title"

            text "Visual Novel":
                style "game_menu_subtitle"

            text "[config.version]":
                style "game_menu_version"
    else:
        ## Title untuk game menu (preferences, dll)
        text title:
            style "game_menu_page_title"

    ## Tombol kembali - hanya untuk game menu (bukan main menu)
    if not main_menu:
        textbutton _("Kembali"):
            style "game_menu_return_button"
            action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


## Style definitions - Cinematic Game Menu

style game_menu_content_container is frame:
    xalign 1.0
    yalign 0.5
    xoffset -120
    xsize 1400
    ysize 800
    background None

style game_menu_nav is vbox:
    xpos 60
    yalign 1.0
    yoffset -50
    spacing 4

style game_menu_nav_button is gui_button:
    xsize 220
    ysize 52
    background Solid("#18181b")  # Zinc-900
    hover_background Solid("#27272a")  # Zinc-800
    selected_background Solid("#3f3f46")  # Zinc-700
    padding (24, 12, 24, 12)

style game_menu_nav_button_text is gui_button_text:
    font gui.interface_text_font
    size 22
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50
    selected_color "#ffffff"
    insensitive_color "#52525b"  # Zinc-600
    xalign 0.0

style game_menu_title_block is vbox:
    xalign 1.0
    yalign 1.0
    xoffset -60
    yoffset -50
    xmaximum 800
    spacing 6

style game_menu_title is gui_text:
    font gui.interface_text_font
    size 72
    color "#fafafa"  # Zinc-50
    bold True
    xalign 1.0
    outlines [(2, "#00000066", 0, 0)]

style game_menu_subtitle is gui_text:
    font gui.interface_text_font
    size 22
    color "#71717a"  # Zinc-500
    xalign 1.0

style game_menu_version is gui_text:
    font gui.interface_text_font
    size 16
    color "#52525b"  # Zinc-600
    xalign 1.0

style game_menu_page_title is gui_text:
    font gui.interface_text_font
    size 64
    color "#fafafa"  # Zinc-50
    bold True
    xalign 0.0
    yalign 0.0
    outlines [(2, "#00000066", 0, 0)]

style game_menu_return_button is gui_button:
    xsize 220
    ysize 52
    background Solid("#27272a")  # Zinc-800
    hover_background Solid("#3f3f46")  # Zinc-700
    padding (24, 12, 24, 12)
    xpos 60
    yalign 1.0
    yoffset -120

style game_menu_return_button_text is gui_button_text:
    font gui.interface_text_font
    size 22
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50
    xalign 0.0


## Layar About - Kampanye Custom ###############################################
##
## Menampilkan informasi tentang game, deskripsi, dan kredit.

screen about():

    tag menu

    use game_menu(_("Tentang"), scroll="viewport"):

        frame:
            style "about_content_frame"

            vbox:
                spacing 25

                ## Judul game
                text "[config.name!t]":
                    style "about_title"

                ## Subtitle
                text "Visual Novel - Pemilihan OSIS":
                    style "about_subtitle"

                null height 15

                ## Deskripsi game
                if gui.about:
                    text "[gui.about!t]":
                        style "about_description"

                null height 25

                ## Garis pemisah
                add Solid("#27272a") xsize 800 ysize 1

                null height 15

                ## Info teknis
                text _("Versi [config.version!t]"):
                    style "about_info"

                null height 8

                ## Kredit engine
                text _("Dibuat dengan {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]"):
                    style "about_engine"

                null height 25

                ## Kredit tambahan
                text "Kampanye - Visual Novel tentang politik sekolah dan pemilihan OSIS.":
                    style "about_credit"


style about_content_frame is frame:
    background Solid("#18181b33")  # Zinc-900 dengan transparansi
    padding (40, 35, 40, 35)
    xsize 1300

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_title:
    font gui.interface_text_font
    size 56
    color "#fafafa"
    bold True
    outlines [(2, "#00000066", 0, 0)]

style about_subtitle:
    font gui.interface_text_font
    size 26
    color "#71717a"

style about_description:
    font gui.interface_text_font
    size 24
    color "#d4d4d8"  # Zinc-300
    line_spacing 8
    xmaximum 1200

style about_info:
    font gui.interface_text_font
    size 20
    color "#a1a1aa"  # Zinc-400

style about_engine:
    font gui.interface_text_font
    size 20
    color "#a1a1aa"  # Zinc-400

style about_credit:
    font gui.interface_text_font
    size 20
    color "#a1a1aa"  # Zinc-400
    xmaximum 1200


## Layar Load and Save #########################################################
##
## Layar ini bertanggungjawab untuk mengijinkan pemain menyimpan dan
## meload lagi. Semenjak mereke hampir memiliki hal yang sama, keduanya di
## implementasinan di percabangan layar ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Simpan"))


screen load():

    tag menu

    use file_slots(_("Muat"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Otomatis save"), quick=_("Save cepat"))

    use game_menu(title):

        fixed:

            ## Ini memastikan input akan mendapat event masuk sebelum tombol
            ## lainnya.
            order_reverse True

            ## Nama halaman, yang dapat di edit dengan mengklik tombol.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Kolom slot file.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Slot Kosong")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Tombol untuk mengakses halaman lain.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}O") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}C") action FilePage("quick")

                    ## antara(1,10) beri nomor antara 1 sampai 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Sinkronisasi Unggah"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Unduh Sinkronisasi"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    color "#71717a"  # Zinc-500

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50

style slot_button:
    properties gui.button_properties("slot_button")
    background Solid("#18181b")  # Zinc-900
    hover_background Solid("#27272a")  # Zinc-800
    padding (15, 15, 15, 15)

style slot_button_text:
    properties gui.text_properties("slot_button")
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50


## Layar preferensi/opsi #######################################################
##
## Layar preferensi mengijinkan pemain untuk mengkonfigurasi permainan untuk
## menyesuaikan gaya bermain masing masing individu.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Setting"), scroll="viewport"):

        vbox:
            spacing 30

            ## Section 1: Display & Skip Settings
            frame:
                style "pref_section_frame"

                vbox:
                    spacing 20

                    text _("Tampilan & Gameplay"):
                        style "pref_section_title"

                    hbox:
                        box_wrap True
                        spacing 40

                        if renpy.variant("pc") or renpy.variant("web"):
                            vbox:
                                style_prefix "radio"
                                spacing 12
                                label _("Tampilan")
                                textbutton _("Jendela") action Preference("display", "window")
                                textbutton _("Layar Penuh") action Preference("display", "fullscreen")

                        vbox:
                            style_prefix "check"
                            spacing 12
                            label _("Lompati")
                            textbutton _("Belum Terlihat") action Preference("skip", "toggle")
                            textbutton _("Setelah Pilihan") action Preference("after choices", "toggle")
                            textbutton _("Transisi") action InvertSelected(Preference("transitions", "toggle"))

            ## Section 2: Text & Audio Settings
            frame:
                style "pref_section_frame"

                vbox:
                    spacing 20

                    text _("Kecepatan & Audio"):
                        style "pref_section_title"

                    hbox:
                        box_wrap True
                        spacing 40

                        vbox:
                            spacing 20

                            label _("Kecepatan Text")
                            bar value Preference("text speed") style "pref_slider"

                            label _("Waktu Otomatis-Maju")
                            bar value Preference("auto-forward time") style "pref_slider"

                        vbox:
                            spacing 20

                            if config.has_music:
                                label _("Volume Musik")
                                bar value Preference("music volume") style "pref_slider"

                            if config.has_sound:
                                label _("Volume Suara")
                                hbox:
                                    bar value Preference("sound volume") style "pref_slider"
                                    if config.sample_sound:
                                        textbutton _("Tes") action Play("sound", config.sample_sound) style "pref_test_button"

                            if config.has_voice:
                                label _("Volume Vokal")
                                hbox:
                                    bar value Preference("voice volume") style "pref_slider"
                                    if config.sample_voice:
                                        textbutton _("Tes") action Play("voice", config.sample_voice) style "pref_test_button"

                            if config.has_music or config.has_sound or config.has_voice:
                                null height 20
                                textbutton _("Senyapkan Semua"):
                                    action Preference("all mute", "toggle")
                                    style "pref_mute_button"


## Style definitions - Cinematic Preferences

style pref_section_frame is frame:
    background Solid("#18181b33")  # Zinc-900 dengan transparansi
    padding (30, 25, 30, 25)
    xsize 1300

style pref_section_title is gui_text:
    font gui.interface_text_font
    size 32
    color "#fafafa"  # Zinc-50
    bold True
    xalign 0.0
    bottom_margin 15

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style pref_slider is gui_slider
style pref_test_button is gui_button
style pref_test_button_text is gui_button_text
style pref_mute_button is gui_button
style pref_mute_button_text is gui_button_text

style pref_label:
    top_margin 10
    bottom_margin 8

style pref_label_text:
    yalign 1.0
    color "#d4d4d8"  # Zinc-300
    size 22

style pref_vbox:
    xsize 400

style radio_vbox:
    spacing 8

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    background Solid("#27272a")  # Zinc-800
    hover_background Solid("#3f3f46")  # Zinc-700
    selected_background Solid("#52525b")  # Zinc-600
    padding (18, 10, 18, 10)
    xsize 380

style radio_button_text:
    properties gui.text_properties("radio_button")
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50
    selected_color "#ffffff"
    size 20

style check_vbox:
    spacing 8

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    background Solid("#27272a")  # Zinc-800
    hover_background Solid("#3f3f46")  # Zinc-700
    selected_background Solid("#52525b")  # Zinc-600
    padding (18, 10, 18, 10)
    xsize 380

style check_button_text:
    properties gui.text_properties("check_button")
    color "#a1a1aa"  # Zinc-400
    hover_color "#fafafa"  # Zinc-50
    selected_color "#ffffff"
    size 20

style pref_slider:
    ysize 40
    xsize 350
    base_bar Solid("#27272a")  # Zinc-800
    hover_base_bar Solid("#3f3f46")  # Zinc-700
    thumb Solid("#0099cc")  # Accent color
    hover_thumb Solid("#66c1e0")  # Hover accent

style pref_test_button:
    background Solid("#0099cc")  # Accent color
    hover_background Solid("#66c1e0")  # Hover accent
    padding (15, 8, 15, 8)
    xsize 80
    ysize 35

style pref_test_button_text:
    color "#000000"
    hover_color "#000000"
    size 18
    bold True

style pref_mute_button:
    background Solid("#ef4444")  # Red-500
    hover_background Solid("#f87171")  # Red-400
    padding (20, 12, 20, 12)
    xsize 200
    ysize 45

style pref_mute_button_text:
    color "#ffffff"
    hover_color "#ffffff"
    size 20
    bold True
    selected_color "#ffffff"

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Layar Riwayat ###############################################################
##
## Layar yang menampilkan History dialog kepada pemain. Semenjak tidak ada yang
## spesial tentang layar ini, ini memiliki akses ke history dialog yang di
## simpan di _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Hindari mempredisi layar ini, ini dapat berukuran sangat besar.
    predict False

    use game_menu(_("Riwayat"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Ini menampilkan layar secara semestinya jika history_height
                ## memiliki value None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Mengambil warna dari text 'who' dari karakter, jika
                        ## di set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Riwayat dialog kosong.")


## Ini menentukan tag apa yang diizinkan ditampilkan di layar sejarah/catatan.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Layar Bantuan - Kampanye Custom #############################################
##
## Layar bantuan yang disederhanakan untuk konteks visual novel.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Bantuan"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 20

            ## Judul section
            text "Panduan Kontrol":
                style "help_section_title"

            null height 5

            hbox:
                spacing 40

                ## Keyboard
                vbox:
                    spacing 8
                    text "Keyboard":
                        style "help_device_label"

                    hbox:
                        label _("Enter/Spasi")
                        text _("Lanjutkan dialog")

                    hbox:
                        label _("Escape")
                        text _("Buka menu permainan")

                    hbox:
                        label _("Tombol Panah")
                        text _("Navigasi antarmuka")

                    hbox:
                        label _("Ctrl")
                        text _("Tahan untuk lompati dialog")

                    hbox:
                        label _("Tab")
                        text _("Nyalakan/matikan skip")

                    hbox:
                        label _("Page Up")
                        text _("Kembali ke dialog sebelumnya")

                    hbox:
                        label _("Page Down")
                        text _("Maju ke dialog berikutnya")

                ## Mouse
                vbox:
                    spacing 8
                    text "Tetikus":
                        style "help_device_label"

                    hbox:
                        label _("Klik Kiri")
                        text _("Lanjutkan dialog")

                    hbox:
                        label _("Klik Kanan")
                        text _("Buka menu permainan")

                    hbox:
                        label _("Scroll Atas")
                        text _("Kembali ke dialog sebelumnya")

                    hbox:
                        label _("Scroll Bawah")
                        text _("Maju ke dialog berikutnya")


style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_section_title:
    font gui.interface_text_font
    size 32
    color "#fafafa"
    bold True

style help_device_label:
    font gui.interface_text_font
    size 20
    color "#71717a"
    bold True
    xsize 160

style help_label:
    xsize 250
    right_padding 30

style help_label_text:
    size 20
    color "#d4d4d8"  # Zinc-300
    text_align 1.0
    xalign 1.0

style help_text:
    size 20
    color "#a1a1aa"  # Zinc-400


style help_button is gui_button
style help_button_text is gui_button_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Layar Tambahan
################################################################################


## Layar konfirmasi ############################################################
##
## Layar konfirmasi di panggil ketika Ren'Py mau menanyakan ke pemain pertanyaan
## ya atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Memastikan layar lain tidak mendapatkan input ketika layar ini di
    ## panggil.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ya") action yes_action
                textbutton _("Tidak") action no_action

    ## Klik kanan dan jawaban escape "Tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Lompati indikator layar #####################################################
##
## layar skip_indicator di tampilkan untuk mengindikasian proses skipping sedang
## dalam proses.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melompati")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## transform digunakan untuk mengkedipkan panah setelah yang lain.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami harus menggunakan font yang mempunyai glyph BLACK RIGHT-POINTING
    ## SMALL TRIANGLE didalamnya.
    font "DejaVuSans.ttf"


## Layar pemberitahuan #########################################################
##
## layar notify digunakan untuk menampilkan pesan kepada pemain. (Seperti,
## ketika game di simpan cepat atau screenshot di ambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Layar NVL ###################################################################
##
## Layar ini digunakan untuk dialog dan menu mode-NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Menampilkan dialog pada vpgrid atau vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Menampilkan menu, jika diberikan. Menu dapat ditampilkan dengan tidak
        ## benar jika config.narrator_menu diatur ke True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengendalikan angka maksimum entri mode-NVL yang dapat di tampilkan
## sekaligus.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Layar gelembung #############################################################
##
## Layar gelembung digunakan untuk menampilkan dialog kepada pemain saat
## menggunakan gelembung ucapan. Layar gelembung mengambil parameter yang sama
## dengan layar ucapkan, harus membuat tampilan dengan id "apa", dan dapat
## membuat tampilan dengan id "kotak nama", "siapa", dan "jendela".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Versi Mobile(HP/Handphone/Android)
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Semenjak mouse tidak ada, kami mengganti menu cepat dengan yang menggunakan
## tombol yang lebih besar dan sedikit, yang memudahkan untuk di sentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Kembali") action Rollback()
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
