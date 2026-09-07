## Automatic Sprite System - Kampanye
## Visual Novel Industry Standards Applied (Full Body Sprites):
## - Left position: xalign 0.3 (30% from left - natural character placement)
## - Right position: xalign 0.7 (70% from left - natural character placement)
## - Zoom: 0.95 (increased for full body sprites to show mid-thigh up)
## - Vertical: yalign 0.85 with yanchor 1.0 (crops bottom ~15% for full body sprites)
## - Transitions: 0.2-0.35s for smooth character appearances
## - Full body sprites are cropped to show from mid-thigh upward

# 1. Image Declarations
image aruna = "images/aruna.png"
image fanya = "images/fanya.png"
image flourine = "images/flourine.png"

# 2. Smooth ATL Transforms with Zoom, Alignment, Anchor, Fade-In, and Dimming
transform sprite_left_appear:
    xalign 0.3
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    alpha 0.0
    ease 0.6 alpha 1.0

transform sprite_left_highlight:
    xalign 0.3
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 1.0

transform sprite_left_dim:
    xalign 0.3
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 0.4

transform sprite_right_appear:
    xalign 0.7
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    alpha 0.0
    ease 0.6 alpha 1.0

transform sprite_right_highlight:
    xalign 0.7
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 1.0

transform sprite_right_dim:
    xalign 0.7
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 0.4

# Center position for focus scenes or single character
transform sprite_center_appear:
    xalign 0.5
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    alpha 0.0
    ease 0.6 alpha 1.0

transform sprite_center_highlight:
    xalign 0.5
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 1.0

transform sprite_center_dim:
    xalign 0.5
    xanchor 0.5
    yalign 1.5
    yanchor 1.0
    zoom 0.95
    linear 0.25 alpha 0.4

# 3. Python Callback Logic
init -1 python:
    SPRITE_POSITIONS = {
        "aruna": "left",
        "fanya": "right",
        "flourine": "right"
    }

    def get_transform(side, state):
        """Returns appropriate transform based on position side and state."""
        if side == "left":
            if state == "appear":
                return sprite_left_appear
            elif state == "highlight":
                return sprite_left_highlight
            else:  # dim
                return sprite_left_dim
        elif side == "right":
            if state == "appear":
                return sprite_right_appear
            elif state == "highlight":
                return sprite_right_highlight
            else:  # dim
                return sprite_right_dim
        else:  # center
            if state == "appear":
                return sprite_center_appear
            elif state == "highlight":
                return sprite_center_highlight
            else:  # dim
                return sprite_center_dim

    def update_character_sprites(speaker_tag):
        """Manages fade-in appearance, highlighting for speaker, and dimming for listeners."""
        if speaker_tag not in SPRITE_POSITIONS:
            return

        for tag, side in SPRITE_POSITIONS.items():
            if not renpy.showing(tag):
                # Character not yet on screen -> only the speaker enters with fade-in
                if tag == speaker_tag:
                    trans = get_transform(side, "appear")
                    renpy.show(tag, at_list=[trans])
            else:
                # Character is already on screen; update transparency smoothly
                if tag == speaker_tag:
                    # Speaking -> fully visible
                    trans = get_transform(side, "highlight")
                    renpy.show(tag, at_list=[trans])
                else:
                    # Listening -> dimmed but still visible
                    trans = get_transform(side, "dim")
                    renpy.show(tag, at_list=[trans])

    def make_sprite_cb(speaker_tag):
        def cb(event, interact=True, **kwargs):
            if event == "begin":
                update_character_sprites(speaker_tag)
            elif event == "say":
                # Ensure speaker highlight persists across dialogue lines
                update_character_sprites(speaker_tag)
        return cb
