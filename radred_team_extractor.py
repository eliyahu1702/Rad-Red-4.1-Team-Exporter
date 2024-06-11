import struct
import pandas as pd
import streamlit as st
abilities = pd.read_csv("species_abilities.csv")
# Function to get the ability of a given species and ability type
def get_ability(species, ability_type):
    # Find the row for the given species
    species_row = abilities[abilities['Species'] == species]
    
    if species_row.empty:
        return "Species not found"
    
    # Get the ability based on the ability type
    if ability_type == '1':
        return species_row['Primary Ability'].values[0]
    elif ability_type == '2':
        return species_row['Secondary Ability'].values[0]
    elif ability_type == 'h':
        hidden_ability = species_row['Hidden Ability'].values[0]
        return hidden_ability if pd.notna(hidden_ability) else "No hidden ability"
    else:
        return "Invalid ability type"
def get_name_by_species(species_id):

    with open('Species.txt', 'r') as file:
    # Read lines from the file and store them in an array
        names_array = file.readlines()
    # Optional: Remove newline characters from each name
    names_array = [name.strip() for name in names_array]
    return names_array[species_id-1]
def get_Moves_by_Id(move_id):
    with open('Moves.txt', 'r') as file:
    # Read lines from the file and store them in an array
        move_array = file.readlines()
    # Optional: Remove newline characters from each name
    move_array = [move.strip() for move in move_array]
    return move_array[move_id-1]

def get_Item_by_id(item_id):
        with open('Items.txt', 'r') as file:
    # Read lines from the file and store them in an array
            item_array = file.readlines()
    # Optional: Remove newline characters from each name
            item_array = [item.strip() for item in item_array]
            if item_id == 0:
                return "None" 
            return item_array[item_id-1]
# Constants
SECTION_SIZE = 0x1000
NUM_SECTIONS = 14
SECTION_ID_OFFSET = 0x0FF4
SIGNATURE_OFFSET = 0x0FF8
SAVE_INDEX_OFFSET = 0x0FFC
SIGNATURE = 0x08012025
PARTY_OFFSET = 0x0038
POKEMON_ENTRY_SIZE = 100
POKEMON_PARTY_SIZE = 6
SAVE_FILE_SIZE = 128 * 1024  # 128KB
NATURES = {
0	:	'Hardy',
1	:	'Lonely',
2	:	'Brave',
3	:	'Adamant',
4	:	'Naughty',
5	:	'Bold',
6	:	'Docile',
7	:	'Relaxed',
8	:	'Impish',
9	:	'Lax',
10	:	'Timid',
11	:	'Hasty',
12	:	'Serious',
13	:	'Jolly',
14	:	'Naive',
15	:	'Modest',
16	:	'Mild',
17	:	'Quiet',
18	:	'Bashful',
19	:	'Rash',
20	:	'Calm',
21	:	'Gentle',
22	:	'Sassy',
23	:	'Careful',
24	:	'Quirky'
}
character_map = {
    0x00: ' ', 0x01: 'À', 0x02: 'Á', 0x03: 'Â', 0x04: 'Ç', 0x05: 'È', 0x06: 'É', 0x07: 'Ê', 0x08: 'Ë', 0x09: 'Ì', 0x0A: ' ', 0x0B: 'Î', 0x0C: 'Ï', 0x0D: 'Ò', 0x0E: 'Ó', 0x0F: 'Ô', 
    0x10: 'Œ', 0x11: 'Ù', 0x12: 'Ú', 0x13: 'Û', 0x14: 'Ñ', 0x15: 'ß', 0x16: 'à', 0x17: 'á', 0x18: ' ', 0x19: 'ç', 0x1A: 'é', 0x1B: 'ê', 0x1C: 'ë', 0x1D: 'ì', 0x1E: 'í', 0x1F: ' ', 
    0x20: 'ï', 0x21: 'ò', 0x22: 'ó', 0x23: 'ô', 0x24: 'œ', 0x25: 'ù', 0x26: 'ú', 0x27: 'û', 0x28: '', 0x29: 'ñ', 0x2A: 'ª', 0x2B: 'º', 0x2C: 'ᵉʳ', 0x2D: '&', 0x2E: '+', 0x2F: '=',  
    0x30: ';', 0x31: '¿', 0x32: '¡', 0x33: 'Pk', 0x34: 'Mn', 0x35: 'Po', 0x36: 'ké', 0x37: 'Í', 0x38: '%', 0x39: '(', 0x3A: ')', 0x3B: '▾', 0x3C: '▸', 0x3D: '▹', 0x3E: '♀', 0x3F: '♂',
    0x40: ' ', 0x41: ' ', 0x42: ' ', 0x43: ' ', 0x44: ' ', 0x45: ' ', 0x46: ' ', 0x47: ' ', 0x48: ' ', 0x49: ' ', 0x4A: ' ', 0x4B: ' ', 0x4C: ' ', 0x4D: ' ', 0x4E: ' ', 0x4F: ' ', 
    0x50: ' ', 0x51: ' ', 0x52: ' ', 0x53: ' ', 0x54: ' ', 0x55: ' ', 0x56: ' ', 0x57: ' ', 0x58: ' ', 0x59: ' ', 0x5A: ' ', 0x5B: ' ', 0x5C: ' ', 0x5D: ' ', 0x5E: ' ', 0x5F: ' ', 
    0x60: ' ', 0x61: ' ', 0x62: ' ', 0x63: ' ', 0x64: ' ', 0x65: ' ', 0x66: ' ', 0x67: ' ', 0x68: ' ', 0x69: ' ', 0x6A: ' ', 0x6B: ' ', 0x6C: ' ', 0x6D: ' ', 0x6E: ' ', 0x6F: ' ', 
    0x70: ' ', 0x71: ' ', 0x72: ' ', 0x73: ' ', 0x74: ' ', 0x75: ' ', 0x76: ' ', 0x77: ' ', 0x78: ' ', 0x79: ' ', 0x7A: ' ', 0x7B: ' ', 0x7C: ' ', 0x7D: ' ', 0x7E: ' ', 0x7F: ' ', 
    0x80: '0', 0x81: '1', 0x82: '2', 0x83: '3', 0x84: '4', 0x85: '5', 0x86: '6', 0x87: '7', 0x88: '8', 0x89: '9', 0x8A: '!', 0x8B: '?', 0x8C: '.', 0x8D: '-', 0x8E: '·', 0x8F: '…', 
    0x90: '“', 0x91: '”', 0x92: " ", 0x93: " ", 0x94: '♂', 0x95: '♀', 0x96: '$', 0x97: ',', 0x98: ' ', 0x99: '÷', 0x9A: ' ', 0x9B: ' ', 0x9C: ' ', 0x9D: ' ', 0x9E: ' ', 0x9F: ' ', 
    0xA0: 'ʳᵉ', 0xA1: '0', 0xA2: '1', 0xA3: '2', 0xA4: '3', 0xA5: '4', 0xA6: '5', 0xA7: '6', 0xA8: '7', 0xA9: '8', 0xAA: '9', 0xAB: '!', 0xAC: '?', 0xAD: '.', 0xAE: '-', 0xAF: '･', 
    0xB0: '‥', 0xB1: '“', 0xB2: '”', 0xB3: '‘', 0xB4: "'", 0xB5: '♂', 0xB6: '♀', 0xB7: '$', 0xB8: ',', 0xB9: '×', 0xBA: '/', 0xBB: 'A', 0xBC: 'B', 0xBD: 'C', 0xBE: 'D', 0xBF: 'E', 
    0xC0: 'F', 0xC1: 'G', 0xC2: 'H', 0xC3: 'I', 0xC4: 'J', 0xC5: 'K', 0xC6: 'L', 0xC7: 'M', 0xC8: 'N', 0xC9: 'O', 0xCA: 'P', 0xCB: 'Q', 0xCC: 'R', 0xCD: 'S', 0xCE: 'T', 0xCF: 'U', 
    0xD0: 'V', 0xD1: 'W', 0xD2: 'X', 0xD3: 'Y', 0xD4: 'Z', 0xD5: 'a', 0xD6: 'b', 0xD7: 'c', 0xD8: 'd', 0xD9: 'e', 0xDA: 'f', 0xDB: 'g', 0xDC: 'h', 0xDD: 'i', 0xDE: 'j', 0xDF: 'k', 
    0xE0: 'l', 0xE1: 'm', 0xE2: 'n', 0xE3: 'o', 0xE4: 'p', 0xE5: 'q', 0xE6: 'r', 0xE7: 's', 0xE8: 't', 0xE9: 'u', 0xEA: 'v', 0xEB: 'w', 0xEC: 'x', 0xED: 'y', 0xEE: 'z', 0xEF: '►', 
    0xF0: ':', 0xF1: 'Ä', 0xF2: 'Ö', 0xF3: 'Ü', 0xF4: 'ä', 0xF5: 'ö', 0xF6: 'ü', 0xF7: ' ', 0xF8: ' ', 0xF9: ' ', 0xFA: ' ', 0xFB: ' ', 0xFC: ' ', 0xFD: ' ', 0xFE: ' ', 0xFF: '',
}
def read_pokemon_party(sav_file_path):
    sav_data = sav_file_path.read()
    
    if len(sav_data) != SAVE_FILE_SIZE:
        raise ValueError("Invalid save file size")
    
    sections = []
    for save_block in range(2):
        for section_index in range(NUM_SECTIONS):
            offset = save_block * NUM_SECTIONS * SECTION_SIZE + section_index * SECTION_SIZE
            section = sav_data[offset:offset + SECTION_SIZE]
            section_id = struct.unpack('<H', section[SECTION_ID_OFFSET:SECTION_ID_OFFSET + 2])[0]
            signature = struct.unpack('<I', section[SIGNATURE_OFFSET:SIGNATURE_OFFSET + 4])[0]
            save_index = struct.unpack('<H', section[SAVE_INDEX_OFFSET:SAVE_INDEX_OFFSET + 2])[0]
            
            if section_id == 0x01 and signature == SIGNATURE:
                sections.append((save_index, section))
    
    if not sections:
        raise ValueError("No valid sections found")
    
    # Get the section with the largest save index
    _, latest_section = max(sections, key=lambda x: x[0])
    
    # Extract party data
    party_data = latest_section[PARTY_OFFSET:PARTY_OFFSET + POKEMON_ENTRY_SIZE * POKEMON_PARTY_SIZE]
    
    party = []
    for i in range(POKEMON_PARTY_SIZE):
        entry_data = party_data[i * POKEMON_ENTRY_SIZE:(i + 1) * POKEMON_ENTRY_SIZE]
        if entry_data[0] == 0:
            break  # No more Pokémon in party
        pokemon = parse_pokemon_entry(entry_data)
        party.append(pokemon)
    
    return party

def parse_pokemon_entry(entry_data):
    # Parse the binary data for a single Pokémon entry
    personal_id = struct.unpack('<I', entry_data[0:4])[0]
    species = get_name_by_species(struct.unpack('<H', entry_data[32:34])[0])
    #species = struct.unpack('<H', entry_data[32:34])
    level = entry_data[84]  # Assuming level is stored at offset 84
    held_item_id = get_Item_by_id(struct.unpack('<H', entry_data[34:36])[0])  # Held item at offset 0x08
    
    # Decode nickname using custom character encoding
    nickname_bytes = entry_data[8:18]
    nickname = ""
    for byte in nickname_bytes:
        nickname+= character_map[byte]
    nickname.rstrip(" ")
    
    evs = struct.unpack('6B', entry_data[56:56 + 6])
    ev_hp, ev_attack, ev_defense, ev_speed, ev_special_attack, ev_special_defense = evs

        # Extract IVs and additional flags
    ivs_data = struct.unpack('<I', entry_data[72:76])[0]
    iv_hp = ivs_data & 0x1F
    iv_attack = (ivs_data >> 5) & 0x1F
    iv_defense = (ivs_data >> 10) & 0x1F
    iv_speed = (ivs_data >> 15) & 0x1F
    iv_special_attack = (ivs_data >> 20) & 0x1F
    iv_special_defense = (ivs_data >> 25) & 0x1F
    is_egg = (ivs_data >> 30) & 0x01
    ability = (ivs_data >> 31) & 0x01

    if ability != 1:
        if personal_id%2 == 0:
            ability = "1"
        else:
            ability = "2"
    else:
        ability = "h"
    ability = get_ability(species, ability)
        
    
    moves = struct.unpack('<4H', entry_data[44:52])
    move1, move2, move3, move4 = moves
    move1 = get_Moves_by_Id(move1) 
    move2 = get_Moves_by_Id(move2)
    move3 = get_Moves_by_Id(move3)
    move4 = get_Moves_by_Id(move4)

    nature = NATURES[personal_id%25]

    return {
        'species': species,
        'level': level,
        'held_item_id': held_item_id,
        'nickname': nickname,
        'ev_hp': ev_hp,
        'ev_attack': ev_attack,
        'ev_defense': ev_defense,
        'ev_speed': ev_speed,
        'ev_special_attack': ev_special_attack,
        'ev_special_defense': ev_special_defense,
        'iv_hp': iv_hp,
        'iv_attack': iv_attack,
        'iv_defense': iv_defense,
        'iv_speed': iv_speed,
        'iv_special_attack': iv_special_attack,
        'iv_special_defense': iv_special_defense,
        'is_egg': is_egg,
        'ability': ability,
        'move1': move1,
        'move2': move2,
        'move3': move3,
        'move4': move4,
        'nature': nature
    }

def Print_Pokemon_Party(sav_file_path):
    # sav_file_path = input("enter file path ")
    pokemon_text= ''
    try:
        party = read_pokemon_party(sav_file_path)
        for i, pokemon in enumerate(party):
            if pokemon['held_item_id'] != "None":
                pokemon_text+= f"{pokemon['nickname']} ({pokemon['species']}) @ {pokemon['held_item_id']}\n"
            else:
                 pokemon_text+= f"{pokemon['nickname']} ({pokemon['species']})\n"
            pokemon_text+= f"Ability: {pokemon['ability']}\n"
            pokemon_text+= f"Level: {pokemon['level']}\n"
            pokemon_text+= f"EVs: {pokemon['ev_hp']} HP / {pokemon['ev_attack']} Atk / {pokemon['ev_defense']} Def / {pokemon['ev_speed']} Spe / {pokemon['ev_special_attack']} SpA / {pokemon['ev_special_defense']} SpD\n"
            pokemon_text+= f"{pokemon['nature']} Nature\n"
            pokemon_text+= f"IVs: {pokemon['iv_hp']} HP / {pokemon['iv_attack']} Atk / {pokemon['iv_defense']} Def / {pokemon['iv_speed']} Spe / {pokemon['iv_special_attack']} SpA / {pokemon['iv_special_defense']} SpD\n"
            pokemon_text+= f"- {pokemon['move1']}\n"
            pokemon_text+= f"- {pokemon['move2']}\n"
            pokemon_text+= f"- {pokemon['move3']}\n"
            pokemon_text+= f"- {pokemon['move4']}\n"
            pokemon_text+= "\n"
    except Exception as e:
        print(f"Error: {e}")
    return pokemon_text

def process_file_streamlit(file):
    file_content = file.read()
    hex_content = file_content.hex()
    formatted_hex_content = ' '.join(hex_content[i:i+2] for i in range(0, len(hex_content), 2))
    return formatted_hex_content
st.set_page_config(page_title="Radical Red Team Exporter",page_icon="radredicon.ico")
st.title("Radical Red Team Exporter")

# File upload
uploaded_file = st.file_uploader("Choose a radical red 4.1  .sav file", type="sav")

result = Print_Pokemon_Party(uploaded_file)
st.text_area("Pokemon Party", value=result, height=400)
if result:
    st.toast("file uploaded")
# Provide a button to copy text to clipboard (this is a placeholder since Streamlit can't directly access clipboard)
st.download_button(label="Download Processed Content", data=result, file_name="processed_content.txt")