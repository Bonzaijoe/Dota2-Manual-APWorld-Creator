import os
import zipfile

class HeroList:

    def __init__(self):
        self.heroes = [
            "Abaddon",
            "Alchemist",
            "Ancient Apparition",
            "Anti-Mage",
            "Arc Warden",
            "Axe",
            "Bane",
            "Batrider",
            "Beastmaster",
            "Bloodseeker",
            "Bounty Hunter",
            "Brewmaster",
            "Bristleback",
            "Broodmother",
            "Centaur Warrunner",
            "Chaos Knight",
            "Chen",
            "Clinkz",
            "Clockwork",
            "Crystal Maiden",
            "Dark Seer",
            "Dark Willow",
            "Dawnbreaker",
            "Dazzle",
            "Death Prophet",
            "Disruptor",
            "Doom",
            "Dragon Knight",
            "Drow Ranger",
            "Earth Spirit",
            "Earthshaker",
            "Elder Titan",
            "Ember Spirit",
            "Enchantress",
            "Enigma",
            "Faceless Void",
            "Grimstroke",
            "Gyrocopter",
            "Hoodwink",
            "Huskar",
            "Invoker",
            "IO",
            "Jakiro",
            "Juggernaut",
            "Keeper of the Light",
            "Kunkka",
            "Legion Commander",
            "Leshrac",
            "Lich",
            "Lifestealer",
            "Lina",
            "Lion",
            "Lone Druid",
            "Luna",
            "Lycan",
            "Magnus",
            "Marci",
            "Mars",
            "Medusa",
            "Meepo",
            "Mirana",
            "Monkey King",
            "Morphling",
            "Muerta",
            "Naga Siren",
            "Nature's Prophet",
            "Necrophos",
            "Night Stalker",
            "Nyx Assassin",
            "Ogre Magi",
            "Omniknight",
            "Oracle",
            "Outworld Devourer",
            "Pangolier",
            "Phantom Assassin",
            "Phantom Lancer",
            "Phoenix",
            "Primal Beast",
            "Puck",
            "Pudge",
            "Pugna",
            "Queen of Pain",
            "Razor",
            "Riki",
            "Ringmaster",
            "Rubick",
            "Sand King",
            "Shadow Demon",
            "Shadow Fiend",
            "Shadow Shaman",
            "Silencer",
            "Skywrath Mage",
            "Slardar",
            "Slark",
            "Snapfire",
            "Sniper",
            "Spectre",
            "Spirit Breaker",
            "Storm Spirit",
            "Sven",
            "Techies",
            "Templar Assassin",
            "Terrorblade",
            "Tidehunter",
            "Timbersaw",
            "Tinker",
            "Tiny",
            "Treant Protector",
            "Troll Warlord",
            "Tusk",
            "Underlord",
            "Undying",
            "Ursa",
            "Vengeful Spirit",
            "Venomancer",
            "Viper",
            "Visage",
            "Void Spirit",
            "Warlock",
            "Weaver",
            "Windranger",
            "Winter Wyvern",
            "Witch Doctor",
            "Wraith King",
            "Zeus"
        ]


class HeroList_Support:

    def __init__(self):
        self.heroes = [
            "Ancient Apparition",
            "Bane",
            "Batrider",
            "Chen",
            "Clockwork",
            "Crystal Maiden",
            "Dark Willow",
            "Dazzle",
            "Disruptor",
            "Earth Spirit",
            "Earthshaker",
            "Enchantress",
            "Enigma",
            "Grimstroke",
            "Gyrocopter",
            "Hoodwink",
            "IO",
            "Jakiro",
            "Keeper of the Light",
            "Lich",
            "Lion",
            "Marci",
            "Mirana",
            "Nyx Assassin",
            "Ogre Magi",
            "Omniknight",
            "Oracle",
            "Phoenix",
            "Pudge",
            "Pugna",
            "Ringmaster",
            "Rubick",
            "Shadow Demon",
            "Shadow Shaman",
            "Silencer",
            "Skywrath Mage",
            "Snapfire",
            "Spirit Breaker",
            "Techies",
            "Tiny",
            "Treant Protector",
            "Tusk",
            "Undying",
            "Vengeful Spirit",
            "Venomancer",
            "Warlock",
            "Winter Wyvern",
            "Witch Doctor"
        ]


if __name__ == '__main__':

    import random

    hero_list = HeroList()
    hero_list_support = HeroList_Support()
    print("Welcome to the Dota2 Manual AP World Creator!")
    num_heroes_to_include = int(input("How Many Heroes would you like included in the APWorld? "))
    num_starting_heroes = int(input("How Many Heroes would you like to start with? "))
    num_kills_required_attackers = input("How Many Kills should you get with Non-Support Heroes? ")
    num_assists_required_attackers = input("How Many Assists should you get with Non-Support Heroes? ")
    num_cs_required_attackers = input("How Many CS should you get with Non-Support Heroes? ")
    num_kills_required_supports = input("How Many Kills should you get with Support Heroes? ")
    num_assists_required_supports = input("How Many Assists should you get with Support Heroes? ")
    num_denies_required_supports = input("How Many Denies should you get with Support Heroes? ")

    randomized_hero_list = random.sample(hero_list.heroes, num_heroes_to_include)
    starter_hero_list = random.sample(randomized_hero_list, num_starting_heroes)
    checks_list = []
    for hero in randomized_hero_list:

        if hero in hero_list_support.heroes:
            checks_list.append(hero + " - Get " + num_kills_required_supports + " Kills")
            checks_list.append(hero + " - Get " + num_assists_required_supports + " Assists")
            checks_list.append(hero + " - Get " + num_denies_required_supports + " Denies")
        else:
            checks_list.append(hero + " - Get " + num_kills_required_attackers + " Kills")
            checks_list.append(hero + " - Get " + num_assists_required_attackers + " Assists")
            checks_list.append(hero + " - Get " + num_cs_required_attackers + " Last Hits")

        checks_list.append(hero + " - Assist Detroying Tower")
        checks_list.append(hero + " - Assist Destroying Barracks")
        checks_list.append(hero + " - Assist Killing Roshan")
        checks_list.append(hero + " - Complete A Game")

    # Now that the lists of Heroes you can receive + Starting Heroes + Checks are created, now create the json files
    # for the APWorld

    # Create Game JSON
    game_json = '''{
    "game": "dota2",
    "creator": "bonzaijoe",
    "filler_item_name": "gl hf",
    "starting_items": [
        {
          "items": ['''
    for hero in starter_hero_list:
        game_json += f'"{hero}",'
    game_json = game_json[:-1]
    game_json += ''']
        }
    ]
}'''

    # Create Items JSON
    items_json = '''[
    '''
    for hero in randomized_hero_list:
        items_json += '''{
        "count":1,
        "name": "''' + hero + '''",
        "category": [],
        "progression": true
    },
    '''
    items_json = items_json[:-6]
    items_json += '''
]'''

    # Create Locations JSON
    count = 0
    current_hero_num = 0
    hero_required = ""

    locations_json = '''[
    '''
    for check in checks_list:
        hero_required = randomized_hero_list[current_hero_num]
        locations_json += '''{
        "name": "''' + check + '''",
        "category": [],
        "requires": "|''' + hero_required + '''|"
    },
    '''
        count += 1
        if count == 7:
            current_hero_num += 1
            count = 0
    locations_json += '''{
    "name": "One Game Completed with Every Included Character",
    "victory": true,
    "requires": [
        '''
    for hero in randomized_hero_list:
        locations_json += f'''"{hero}",
        '''
    locations_json = locations_json[:-10]
    locations_json += '''
        ]
    }
]'''

    # Write 3 JSONs to data folder inside manual_dota2_bonzaijoe
    with open('manual_dota2_bonzaijoe/data/game.json', 'w') as file:
        file.writelines(game_json)
    with open('manual_dota2_bonzaijoe/data/items.json', 'w') as file:
        file.writelines(items_json)
    with open('manual_dota2_bonzaijoe/data/locations.json', 'w') as file:
        file.writelines(locations_json)

    # Zip manual_dota2_bonzaijoe folder as APWorld and Save
    zf = zipfile.ZipFile("manual_dota2_bonzaijoe.apworld", "w")
    for dirname, subdirs, files in os.walk("manual_dota2_bonzaijoe"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
