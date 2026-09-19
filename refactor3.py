import os

map_path = r'C:\kampanye\game\map_system.rpy'
with open(map_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('player_path == None or player_path == "support"', 'player_path != "rival"')
content = content.replace('player_path == None or player_path == "rival"', 'player_path != "support"')

with open(map_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
