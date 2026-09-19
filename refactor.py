import os
import re

game_dir = r'C:\kampanye\game'

# 1. Update script.rpy
script_path = os.path.join(game_dir, 'script.rpy')
with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()

# Replace npc_state
old_npc_state = r'''default npc_state = {
    "adam": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "adi": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "anggun": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "lulu": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "inez": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "angga": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ferdi": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "juan": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "faizal": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "nayra": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "aulia": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ellisa": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "desti": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "lukman": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "bagus": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "yura": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ayya": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "ami": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None},
    "cecillia": {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None}
}'''

new_npc_state = '''default npc_state = {name: {"quest_status": "not_started", "relationship_quality": 0, "votes_banked": 0, "approached_day": None} for name in ["adam", "adi", "anggun", "lulu", "inez", "angga", "ferdi", "juan", "faizal", "nayra", "aulia", "ellisa", "desti", "lukman", "bagus", "yura", "ayya", "ami", "cecillia"]}'''
script_content = script_content.replace(old_npc_state, new_npc_state)

# Replace calc_total_votes and inject complete_quest
old_calc = r'''    def calc_total_votes():
        base = 0
        for key in npc_state:
            base += npc_state[key]["votes_banked"]
        return base + passive_votes'''
new_calc = r'''    def calc_total_votes():
        return sum(npc["votes_banked"] for npc in npc_state.values()) + passive_votes

    def complete_quest(npc, meter):
        npc_state[npc]["relationship_quality"] += meter
        npc_state[npc]["quest_status"] = "completed"
        npc_state[npc]["votes_banked"] = get_votes_from_relationship(npc_state[npc]["relationship_quality"])
        store.total_votes = calc_total_votes()'''
script_content = script_content.replace(old_calc, new_calc)

# Replace map navigation
old_map = r'''        call screen school_map
        $ current_location = _return
        
        if current_location == "gerbang":
            jump loc_gerbang
        elif current_location == "lapangan":
            jump loc_lapangan
        elif current_location == "ekskul":
            jump loc_ekskul
        elif current_location == "lab":
            jump loc_lab
        elif current_location == "perpus":
            jump loc_perpus
        elif current_location == "osis":
            jump loc_osis
        elif current_location == "uks":
            jump loc_uks
        elif current_location == "aula":
            jump loc_aula
        elif current_location == "pramuka":
            jump loc_pramuka
        elif current_location == "heist":
            jump robotika_heist
        elif current_location == "pulang":
            "Aruna memutuskan untuk mengakhiri harinya dan pulang ke rumah."
            jump end_day_routine
        elif current_location == "mundur":'''

new_map = r'''        call screen school_map
        $ current_location = _return
        
        if current_location == "heist":
            jump robotika_heist
        elif current_location == "pulang":
            "Aruna memutuskan untuk mengakhiri harinya dan pulang ke rumah."
            jump end_day_routine
        elif current_location != "mundur":
            $ renpy.jump(current_location)
            
        if current_location == "mundur":'''
script_content = script_content.replace(old_map, new_map)

# Replace adam quest ending since adam is in script.rpy
script_content = re.sub(
    r'    \$ npc_state\["adam"\]\["relationship_quality"\] \+= adam_meter\n    \$ npc_state\["adam"\]\["quest_status"\] = "completed"\n    \$ npc_state\["adam"\]\["votes_banked"\] = get_votes_from_relationship\(npc_state\["adam"\]\["relationship_quality"\]\)\n    \$ total_votes = calc_total_votes\(\)',
    r'    $ complete_quest("adam", adam_meter)',
    script_content
)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

# 2. Update map_system.rpy
map_path = os.path.join(game_dir, 'map_system.rpy')
with open(map_path, 'r', encoding='utf-8') as f:
    map_content = f.read()
    
map_content = map_content.replace('Return("gerbang")', 'Return("loc_gerbang")')
map_content = map_content.replace('Return("lapangan")', 'Return("loc_lapangan")')
map_content = map_content.replace('Return("ekskul")', 'Return("loc_ekskul")')
map_content = map_content.replace('Return("lab")', 'Return("loc_lab")')
map_content = map_content.replace('Return("perpus")', 'Return("loc_perpus")')
map_content = map_content.replace('Return("osis")', 'Return("loc_osis")')
map_content = map_content.replace('Return("uks")', 'Return("loc_uks")')
map_content = map_content.replace('Return("aula")', 'Return("loc_aula")')
map_content = map_content.replace('Return("pramuka")', 'Return("loc_pramuka")')

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(map_content)

# 3. Update quests_group_*.rpy
for group in ['a', 'b', 'c']:
    quest_path = os.path.join(game_dir, f'quests_group_{group}.rpy')
    if os.path.exists(quest_path):
        with open(quest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the 4-line update pattern and replace it
        pattern = r'    \$ npc_state\["([a-z]+)"\]\["relationship_quality"\] \+= ([a-z_]+_meter)\n    \$ npc_state\["\1"\]\["quest_status"\] = "completed"\n    \$ npc_state\["\1"\]\["votes_banked"\] = get_votes_from_relationship\(npc_state\["\1"\]\["relationship_quality"\]\)\n    \$ total_votes = calc_total_votes\(\)'
        replacement = r'    $ complete_quest("\1", \2)'
        
        new_content = re.sub(pattern, replacement, content)
        with open(quest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print('Done')
