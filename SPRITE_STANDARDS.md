# Sprite Character Standards - Kampanye Visual Novel

## Industry Standards Applied (Full Body Sprites)

Based on research from visual novel industry best practices and Ren'Py documentation, the following standards have been implemented for character sprite positioning and sizing.

**Important**: This project uses **full body sprites** that are cropped to show from mid-thigh upward, which requires different positioning parameters than standard mid-thigh sprites.

## Positioning Standards

### Horizontal Positioning (xalign)
- **Left Position**: `xalign 0.3` (30% from left edge)
- **Right Position**: `xalign 0.7` (70% from left edge)  
- **Center Position**: `xalign 0.5` (50% from left edge - for focus scenes)

These values follow industry conventions where characters are naturally positioned at ~30% and ~70% of screen width, leaving space for dialogue boxes and avoiding edge crowding.

### Vertical Positioning (yalign)
- **Base**: `yalign 1.5` with `yanchor 1.0` (bottom-cropped positioning for full body sprites on 1080p canvas)
- Characters are anchored at their bottom edge and positioned below the screen baseline so the lower portion (feet/legs) is hidden outside the visible area
- Only upper body and mid-torso remain visible within the 1920x1080 canvas
- Adjusted for 1024x1536 full body sprites on a 1920x1080 Ren'Py canvas

### Size/Zoom Standards
- **Zoom Factor**: `0.95` (95% of original size)
- Increased to make the figure more prominent on screen; combined with a deeper yalign placement below the baseline, the enlarged sprite still keeps the feet hidden and the visible figure remains cleanly framed within the 1080p canvas

## Transform States

Each position has three states for smooth character transitions:

### 1. Appear (Fade-in)
- **Initial State**: `alpha 0.0` (invisible)
- **Transition**: `ease 0.6 alpha 1.0` (gentler 0.6s fade-in)
- Used when a character first enters the scene

### 2. Highlight (Speaking)
- **State**: `alpha 1.0` (fully visible)
- **Transition**: `linear 0.25 alpha 1.0` (smooth 0.25s settle to full visibility)
- Used when character is currently speaking

### 3. Dim (Listening)
- **State**: `alpha 0.4` (40% opacity)
- **Transition**: `linear 0.25 alpha 0.4` (smooth 0.25s settle to dimmed visibility)
- Used when character is on screen but not speaking

## Implementation Details

### Current Character Positions
```python
SPRITE_POSITIONS = {
    "aruna": "left",
    "fanya": "right", 
    "flourine": "right"
}
```

### Available Transforms
- `sprite_left_appear`, `sprite_left_highlight`, `sprite_left_dim`
- `sprite_right_appear`, `sprite_right_highlight`, `sprite_right_dim`
- `sprite_center_appear`, `sprite_center_highlight`, `sprite_center_dim`

### Usage Pattern
When adding new characters:
1. Add image declaration: `image character_name = "images/character_name.png"`
2. Define position in `SPRITE_POSITIONS` dictionary: `"character_name": "left"/"right"/"center"`
3. Character callback will automatically handle positioning and state transitions

## Guidelines for New Sprites

### Image Resolution Recommendations
- **Base Resolution**: Minimum 1200x1800 pixels for full body sprites
- **Aspect Ratio**: 2:3 (width:height) for full body character art
- **Canvas Size**: Draw at 2x final display size for crispness
- **Transparency**: PNG format with transparent background
- **Focus Area**: Character details should be concentrated in upper 70% of sprite (will be visible when cropped)

### Composition Guidelines
- Draw full body characters but frame them so the important details are in the upper 70%
- When cropped to show mid-thigh upward, ensure character head stays within top 10% of screen
- Maintain consistent eye level across characters for scene cohesion
- Silhouette test: Character should be recognizable in silhouette form
- Important character details (face, upper body) should be clearly visible in the cropped view

### Adding New Characters
```python
# In characters.rpy
define char_name = Character('Character Name', color="#hexcode", callback=make_sprite_cb("char_name"))

# In sprites.rpy
image char_name = "images/char_name.png"

# In SPRITE_POSITIONS dictionary
SPRITE_POSITIONS = {
    # ... existing characters
    "char_name": "left"  # or "right" or "center"
}
```

## Technical Notes

- **Anchor Point**: All sprites use `xanchor 0.5` (horizontal center) and `yanchor 1.0` (bottom)
- **Vertical Positioning**: `yalign 1.5` with `yanchor 1.0` places the bottom of the sprite well below the visible baseline so the enlarged figure still keeps feet/legs hidden; the visible figure ends around upper torso region
- **Zoom Factor**: `0.95` provides a larger, more prominent full body figure while the deeper yalign keeps the sprite within vertical bounds
- **Performance**: Minimal impact as transforms are cached by Ren'Py
- **Compatibility**: Standards work with existing callback system without breaking changes
- **Extensibility**: New positions can be added following the same pattern
- **Bug Fix**: Callback logic guards against sprite disappearing during dialogue by only entering a character on first appearance and otherwise only adjusting transparency; `renpy.restart_interaction()` is no longer called on every `begin` event to avoid flickering

## References

Based on industry standards from:
- VN Paths: Visual Novel Sprite Creation Guide
- Crystal Game Works: Sprite Setup Best Practices  
- Lemma Soft Forums: Ren'Py Sprite Dimensions Discussion
- Ren'Py Documentation: Transform Properties
