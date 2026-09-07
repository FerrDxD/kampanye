## Automatic Sprite System - Kampanye

# 1. Image Declarations
image aruna = "images/aruna.png"
image fanya = "images/fanya.png"
image flourine = "images/flourine.png"

# 2. Smooth ATL Transforms with Zoom, Alignment, Anchor, Fade-In, and Dimming
transform sprite_left_appear:
    xalign 0.18
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    alpha 0.0
    easein 0.35 alpha 1.0

transform sprite_left_highlight:
    xalign 0.18
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    easein 0.2 alpha 1.0

transform sprite_left_dim:
    xalign 0.18
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    easein 0.2 alpha 0.5

transform sprite_right_appear:
    xalign 0.82
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    alpha 0.0
    easein 0.35 alpha 1.0

transform sprite_right_highlight:
    xalign 0.82
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    easein 0.2 alpha 1.0

transform sprite_right_dim:
    xalign 0.82
    xanchor 0.5
    yalign 1.0
    yanchor 1.0
    zoom 0.58
    easein 0.2 alpha 0.5

# 3. Python Callback Logic
init -1 python:
    SPRITE_POSITIONS = {
        "aruna": "left",
        "fanya": "right",
        "flourine": "right"
    }

    def update_character_sprites(speaker_tag):
        """Manages fade-in appearance, highlighting for speaker, and dimming for listeners."""
        if speaker_tag not in SPRITE_POSITIONS:
            return

        for tag, side in SPRITE_POSITIONS.items():
            is_showing = renpy.showing(tag)
            
            if tag == speaker_tag:
                if not is_showing:
                    # New entry -> Fade in from alpha 0.0 to 1.0
                    trans = sprite_left_appear if side == "left" else sprite_right_appear
                else:
                    # Already on screen -> Highlight to alpha 1.0
                    trans = sprite_left_highlight if side == "left" else sprite_right_highlight
                renpy.show(tag, at_list=[trans])
            elif is_showing:
                # Non-speaking character on screen -> Dim to alpha 0.5
                trans = sprite_left_dim if side == "left" else sprite_right_dim
                renpy.show(tag, at_list=[trans])

    def make_sprite_cb(speaker_tag):
        def cb(event, interact=True, **kwargs):
            if event == "begin":
                update_character_sprites(speaker_tag)
                if interact:
                    renpy.restart_interaction()
        return cb
