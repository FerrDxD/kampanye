import os
import re

game_dir = r'C:\kampanye\game'

# 1. Update map_system.rpy
map_path = os.path.join(game_dir, 'map_system.rpy')
with open(map_path, 'r', encoding='utf-8') as f:
    map_content = f.read()

# Remove the inline player_path setting in menus
pattern_map = r'            if player_path == None:\n                \$ player_path = "(support|rival)"\n'
map_content = re.sub(pattern_map, '', map_content)

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(map_content)

# 2. Add start_quest in script.rpy
script_path = os.path.join(game_dir, 'script.rpy')
with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()

new_complete = r'''    def complete_quest(npc, meter):'''
start_quest_code = r'''    def start_quest(npc):
        if store.player_path is None:
            store.player_path = "support"
        npc_state[npc]["quest_status"] = "in_progress"
        npc_state[npc]["approached_day"] = store.current_day

    def complete_quest(npc, meter):'''
script_content = script_content.replace(new_complete, start_quest_code)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

# 3. Update quests_group_*.rpy
for group in ['a', 'b', 'c']:
    quest_path = os.path.join(game_dir, f'quests_group_{group}.rpy')
    if os.path.exists(quest_path):
        with open(quest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the manual status setting with start_quest
        pattern = r'    \$ npc_state\["([a-z]+)"\]\["quest_status"\] = "in_progress"\n    \$ npc_state\["\1"\]\["approached_day"\] = current_day\n'
        replacement = r'    $ start_quest("\1")\n'
        content = re.sub(pattern, replacement, content)
        
        with open(quest_path, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. Update rival_path.rpy
rival_path = os.path.join(game_dir, 'rival_path.rpy')
with open(rival_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('label rival_fanya_loop:', 'label rival_fanya_loop:\n    if player_path is None:\n        $ player_path = "rival"')
content = content.replace('label rival_flourine_loop:', 'label rival_flourine_loop:\n    if player_path is None:\n        $ player_path = "rival"')

with open(rival_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
