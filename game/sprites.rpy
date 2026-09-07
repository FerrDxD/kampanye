## Automatic Sprite System - Kampanye

# 1. Image Declarations
image aruna = "images/aruna.png"
image fanya = "images/fanya.png"
image flourine = "images/flourine.png"

# 2. Smooth ATL Transforms with Fade / Dimming
transform sprite_left(target_alpha=1.0):
    xalign 0.15
    yalign 1.0
    yanchor 1.0
    easein 0.25 alpha target_alpha

transform sprite_right(target_alpha=1.0):
    xalign 0.85
    yalign 1.0
    yanchor 1.0
    easein 0.25 alpha target_alpha

# 3. Python Callback Logic (init -1 to load before character defines)
init -1 python:
    # Managed sprite characters and their screen side
    SPRITE_POSITIONS = {
        "aruna": "left",
        "fanya": "right",
        "flourine": "right"
    }

    def update_character_sprites(speaker_tag):
        """Highlights speaking character (alpha 1.0) and dims non-speaking active characters (alpha 0.6)."""
        if speaker_tag not in SPRITE_POSITIONS:
            return

        for tag, side in SPRITE_POSITIONS.items():
            if tag == speaker_tag:
                # Active speaker -> Full brightness (alpha 1.0)
                trans = sprite_left(1.0) if side == "left" else sprite_right(1.0)
                renpy.show(tag, at_list=[trans])
            elif renpy.showing(tag):
                # Non-speaking active sprite -> Dimmed (alpha 0.6)
                trans = sprite_left(0.6) if side == "left" else sprite_right(0.6)
                renpy.show(tag, at_list=[trans])

    def make_sprite_cb(speaker_tag):
        def cb(event, interact=True, **kwargs):
            if event == "begin":
                update_character_sprites(speaker_tag)
        return cb
