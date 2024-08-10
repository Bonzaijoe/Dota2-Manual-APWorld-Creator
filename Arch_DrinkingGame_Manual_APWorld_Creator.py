import os
import zipfile


if __name__ == '__main__':

    print("Welcome to the Archipelago Drinking Game Manual AP World Creator!")
    num_group_sips = int(input("How many 'Whole Group Takes a Sip' Checks should there be? "))
    num_group_shots = int(input("How many 'Whole Group Takes a Shot' Checks should there be? "))
    num_group_drinks = int(input("How many 'Whole Group Finishes their Drink' Checks should there be? "))
    num_take_sips = int(input("How many 'Finder Take a Sip' Checks should there be? "))
    num_take_shots = int(input("How many 'Finder Takes a Shot' Checks should there be? "))
    num_take_drinks = int(input("How many 'Finder Finishes their Drink' Checks should there be? "))
    num_give_sips = int(input("How many 'Give another player a Sip' Checks should there be? "))
    num_give_shots = int(input("How many 'Give another player a Shot' Checks should there be? "))
    num_give_drinks = int(input("How many 'Make another player finish their Drink' Checks should there be? "))

    total = (num_group_sips + num_group_shots + num_group_drinks + num_take_sips + num_take_shots + num_take_drinks +
             num_give_sips + num_give_shots + num_give_drinks)
    checks_list = []
    locations_list = []
    for x in range(num_group_sips):
        checks_list.append("Whole Group Took a Sip")
        locations_list.append("Whole Group Takes a Sip")

    for x in range(num_group_shots):
        checks_list.append("Whole Group Took a Shot")
        locations_list.append("Whole Group Takes a Shot")

    for x in range(num_group_drinks):
        checks_list.append("Whole Group Finished their Drink")
        locations_list.append("Whole Group Finishes their Drink")

    for x in range(num_take_sips):
        checks_list.append("Finder Took a Sip")
        locations_list.append("Finder Takes a Sip")

    for x in range(num_take_shots):
        checks_list.append("Finder took a Shot")
        locations_list.append("Finder Takes a Shot")

    for x in range(num_take_drinks):
        checks_list.append("Finder finished their Drink")
        locations_list.append("Finder finishes their Drink")

    for x in range(num_give_sips):
        checks_list.append("Victim Took a Sip")
        locations_list.append("Finder gives another player a Sip")

    for x in range(num_give_shots):
        checks_list.append("Victim took a Shot")
        locations_list.append("Finder gives another player a Shot")

    for x in range(num_give_drinks):
        checks_list.append("Victim finished their Drink")
        locations_list.append("Finder tells another player to finish their Drink")

    # create the json files for the APWorld

    # Create Game JSON
    game_json = '''{
    "game": "drinking",
    "creator": "bonzaijoe",
    "filler_item_name": "party on",
    "starting_items": [
        {
          "items": []
        }
    ]
}'''

    # Create Items JSON
    items_json = '''[
    '''
    for location in locations_list:
        items_json += '''{
        "count":1,
        "name": "''' + location + '''",
        "category": [],
        "progression": true
    },
    '''
    items_json = items_json[:-6]
    items_json += '''
]'''

    # Create Locations JSON
    locations_json = '''[
    '''
    for check in checks_list:
        locations_json += '''{
        "name": "''' + check + '''",
        "category": [],
        "requires": "||"
    },
    '''

    locations_json += '''{
    "name": "Have Fun & Get Drunk!",
    "victory": true,
    "requires": []
    }
]'''

    # Write 3 JSONs to data folder inside manual_drinking_bonzaijoe
    with open('manual_drinking_bonzaijoe/data/game.json', 'w') as file:
        file.writelines(game_json)
    with open('manual_drinking_bonzaijoe/data/items.json', 'w') as file:
        file.writelines(items_json)
    with open('manual_drinking_bonzaijoe/data/locations.json', 'w') as file:
        file.writelines(locations_json)

    # Zip manual_drinking_bonzaijoe folder as APWorld and Save
    zf = zipfile.ZipFile("manual_drinking_bonzaijoe.apworld", "w")
    for dirname, subdirs, files in os.walk("manual_drinking_bonzaijoe"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
