'''
Created on 16 Jan 2017

@author: admin
'''


import json

d = json.load(open('game.json'))
              
print(d)



s = {'characterName': '', 'class': '', 'level': '', 'background': '', 'playerName': '', 'faction': '', 'race': 'race', 'alignment': '', 'experiencePoints': '', 'dciNumber': '', 'vitals': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'passiveWisdom': 0, 'otherProficiencies': [], 'armourClass': 0, 'initiative': 0, 'speed': 0, 'hitPoints': {'hitpointMax': 0, 'currentHitPoints': 0, 'temporaryHitPoints': 0}, 'savingThrows': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'skills': {'acrobatics': {'value': 0, 'enabled': False}, 'animalHandling': {'value': 0, 'enabled': False}, 'arcana': {'value': 0, 'enabled': False}, 'athletics': {'value': 0, 'enabled': False}, 'deception': {'value': 0, 'enabled': False}, 'history': {'value': 0, 'enabled': False}, 'insight': {'value': 0, 'enabled': False}, 'intimidation': {'value': 0, 'enabled': False}, 'investigation': {'value': 0, 'enabled': False}, 'medicine': {'value': 0, 'enabled': False}, 'nature': {'value': 0, 'enabled': False}, 'perception': {'value': 0, 'enabled': False}, 'performance': {'value': 0, 'enabled': False}, 'persuation': {'value': 0, 'enabled': False}, 'religion': {'value': 0, 'enabled': False}, 'slightOfHand': {'value': 0, 'enabled': False}, 'stealth': {'value': 0, 'enabled': False}, 'survival': {'value': 0, 'enabled': False}}, 'attacksSpellcasting': {'notes': '', 'attacks': [{'name': '', 'atkBonus': '', 'damageType': ''}]}, 'personalityTraits': '', 'ideals': '', 'bonds': '', 'flaws': '', 'featuresTraits': '', 'age': 0, 'height': '', 'weight': '', 'eyes': '', 'skin': '', 'hair': '', 'factionRank': '', 'additionalFeaturesTraits': '', 'Treasure': [], 'characterBackstory': ''}
